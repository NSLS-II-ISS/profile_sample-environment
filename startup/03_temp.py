

import numpy as np
import time as ttime
from ophyd import Component as Cpt, Device, EpicsSignal, Kind


temp1 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B2:5}InCh0:Data-I', name='temp1')
temp2 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B2:5}InCh1:Data-I', name='temp2')


temp1_sp = EpicsSignal('XF:08IDB-CT{DIODE-HTR:1}T-SP', name='temp1_sp')
temp2_sp = EpicsSignal('XF:08IDB-CT{DIODE-HTR:2}T-SP', name='temp2_sp')
temps = [temp1, temp1_sp, temp2, temp2_sp]



for pv in temps:
    arch_iss.pvs.update({pv.name: pv.pvname})

heater1_curr_output = EpicsSignal('XF:08IDB-CT{DIODE-HTR:1}CURR:1-SP', name='curr_override')
heater2_volt_output = EpicsSignal('XF:08IDB-CT{DIODE-HTR:2}VOLT:1-SP', name='volt_override')

class Ramper(Device):
    pv_sp = Cpt(EpicsSignal, 'pv_sp', name='pv_sp')
    pv_sp_rate = Cpt(EpicsSignal, 'pv_sp_rate', name='pv_sp_rate') # pv setpoint change rate in pv units per minute
    go = Cpt(EpicsSignal, 'go', name='go')
    pv_pause = EpicsSignal('XF:08IDB-Ramping:pause', name='pv_pause')

    tprog = Cpt(EpicsSignal, 'tprog', name='tprog')
    pvprog = Cpt(EpicsSignal, 'pvprog', name='pvprog')

    step = Cpt(EpicsSignal, 'step', name='step')
    dwell = Cpt(EpicsSignal, 'dwell', name='dwell')
    safety_thresh = Cpt(EpicsSignal, 'safety_thresh', name='safety_thresh')
    safety_timer = Cpt(EpicsSignal, 'safety_timer', name='safety_timer')
    pid_enable_name = Cpt(EpicsSignal, 'pid_enable_name', name='pid_enable_name')
    pid_output_name = Cpt(EpicsSignal, 'pid_output_name', name='pid_output_name')

    def __init__(self, aux_pv_sp=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aux_pv_sp = aux_pv_sp
        self._subscribe_aux_pv_sp()
        self.subscribe_safety_timer_upd()

    def _subscribe_aux_pv_sp(self):
        if self.aux_pv_sp is not None:

            def subscription(value, **kwargs):
                setpoint = value
                self.aux_pv_sp.put(setpoint)
                return

            self.pv_sp.subscribe(subscription)

    def subscribe_safety_timer_upd(self):
        def subscription(value, **kwargs):
            if value>5:
                self.safety_timer.put(0)

        self.safety_timer.subscribe(subscription)


    def enable(self):
        self.pv_pause.put(0)
        self.go.put(1)

    def pause(self):
        self.pv_pause.put(1)

    def depause(self):
        self.pv_pause.put(0)

    def disable(self, pv_sp_value=25):
        self.go.put(0)
        self.pv_pause.put(0)
        ttime.sleep(0.3)
        if pv_sp_value is not None:
            self.pv_sp.put(pv_sp_value)


try:
    ramper = Ramper(aux_pv_sp=temp2_sp ,prefix='XF:08IDB-Ramping:', name='ramper')
    ramper.go.get() # to see if it is accessible
except:
    print('ramper PV is not initialized')
    ramper = None




class SamplePID(Device):
    pv = Cpt(EpicsSignal, '.CVAL', name='pv')
    pv_sp = Cpt(EpicsSignal, '.VAL', name='pv_sp')
    enabled = Cpt(EpicsSignal, ':on')
    KP = Cpt(EpicsSignal, '.KP')
    KI = Cpt(EpicsSignal, '.KI')
    KD = Cpt(EpicsSignal, '.KD')
    I = Cpt(EpicsSignal, '.I')
    pid_pv_outout_str = Cpt(EpicsSignal, ':out.OUTN')

    def __init__(self, human_name, pv_name, pv_units,
                 kp=0.025, ki=0.02, kd=0.00,
                 pv_output=None,
                 pv_output_name='',
                 pv_output_units='',
                 ramper=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.process_program = None
        self.human_name = human_name
        self.pv_name = pv_name
        self.pv_units = pv_units
        self.pv_output = pv_output
        self.pv_output_name = pv_output_name
        self.pv_output_units = pv_output_units
        self.ramper = ramper
        self._subscribe_to_ramper()
        self._check_pid_values(kp, ki, kd)

    def _subscribe_to_ramper(self):
        if self.ramper is not None:

            def subscription(value, **kwargs):
                setpoint = value
                self.pv_sp.put(setpoint)
                return

            self.ramper.pv_sp.subscribe(subscription)
            self.ramper.pid_enable_name.put(self.enabled.pvname)
            self.ramper.pid_output_name.put(self.pv_output.pvname)

            def _handle_gas_flow_program(value, old_value, **kwargs):
                if value != old_value:
                    self.handle_gas_flow_program(value, old_value, **kwargs)

            self.ramper.step.subscribe(_handle_gas_flow_program)

    def handle_gas_flow_program(self, value, old_value, **kwargs):
        # print(f'step subscription: {value=}, {old_value=}, {kwargs=}')
        if self.process_program is not None:
            print('Checkpoint 1')
            for i in range(1, 6): # number of gases is hardcoded to 5!
                print('Checkpoint 2')
                gas, channel, program = self.process_program[f'flowgas{i}'], self.process_program[f'flowchannel{i}'], self.process_program[f'flowprog{i}']
                if (gas is not None) and (gas != -1) and (gas != '') and (gas != 'None'):
                    print('Checkpoint 3')
                    flow_rate = program[value]
                    print(f'Program step {value}: Setting {gas} flow to {flow_rate}')
                    flow(gas, channel=channel, flow_rate=flow_rate)

    def enable(self):
        self.pid_pv_outout_str.put(self.pv_output.pvname)
        self.enabled.put(1)

    def disable(self):
        self.enabled.put(0)

    def _check_pid_values(self, kp, ki, kd):
        if ((not np.isclose(self.KP.get(), kp, 1e-3)) or
            (not np.isclose(self.KI.get(), ki, 1e-3)) or
            (not np.isclose(self.KD.get(), kd, 1e-3))):
            print(f'Warning: Sample PID loop for {self.human_name} was initialized with non-standard values !!!!')

    def current_pv_reading(self, offset=0.5):
        return (self.pv.get() - offset)

    def ramp_start(self, process_program):
        self.ramper.step.put(0)
        self.process_program = process_program.copy()
        self.I.put(0, wait=True)
        self.ramper.disable(pv_sp_value=None)
        self.ramper.tprog.put(process_program['times'])
        self.ramper.pvprog.put(process_program['setpoints'])
        self.enable()
        self.ramper.enable()

    def ramp_pause(self):
        self.ramper.pause()

    def ramp_continue(self):
        self.ramper.depause()

    def ramp_stop(self):
        self.disable()
        self.ramper.disable()
        self.process_program = None
        # self.ramper.step = 0







heater_spiral = SamplePID(human_name='Spiral Heater', pv_name='Temperature', pv_units='C deg',
                          kp=0.05, ki=0.02, kd=0.00,
                          pv_output=heater2_volt_output,
                          pv_output_name='Voltage',
                          pv_output_units='V',
                          ramper=ramper,
                          prefix='XF:08IDB-CT{FbPid:01}PID', name='heater_spiral')

heater_ir = SamplePID(human_name='Cartridge Heater', pv_name='Temperature', pv_units='C deg',
                          kp=0.01, ki=0.00, kd=0.00,
                          pv_output=heater1_curr_output,
                          pv_output_name='Current',
                          pv_output_units='mA',
                          ramper=ramper,
                          prefix='XF:08IDB-CT{FbPid:02}PID', name='heater_cartridge')

sample_envs_dict = {'Spiral Heater' : heater_spiral,
                    'IR Heater': heater_ir}


def disable_all_envs():
    for key in sample_envs_dict.keys():
        sample_envs_dict[key].ramp_stop()


