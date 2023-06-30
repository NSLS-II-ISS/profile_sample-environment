import atexit
import time as ttime


print('this is ran!!')



def full_stop_for_sample_envs():
    import time as ttime
    def disable_all_envs():
        from ophyd import EpicsSignal
        for i in range(1, 5):
            pid_on = EpicsSignal('XF:08IDB-CT{FbPid:0' + str(i) + '}PID:on', name='pid_on')
            pid_on.put(0, wait=True)
        ramper_go = EpicsSignal('XF:08IDB-Ramping:go', name='ramper_go')
        ramper_pause = EpicsSignal('XF:08IDB-Ramping:pause', name='ramper_pause')
        ramper_go.put(0, wait=True)
        ramper_pause.put(0, wait=True)

    def kill_pid_ioc():
        import shlex, subprocess
        import os
        ioc_args = shlex.split(
            'gnome-terminal -- python /nsls2/data/iss/shared/config/bluesky/profile_sample-environment/iocs/ioc_ramping.py')
        proc_id = list(map(int, subprocess.check_output(['pidof'] + ioc_args).split()))[0]
        os.kill(proc_id, 9)
    print('IPYTHON SESSION CLOSED')
    print('DISABLING ALL SAMPLE ENVIRONMENTS')
    print()
    print()
    # disable_all_envs()  # from /03_temp.py
    try:
        disable_all_envs() # from /03_temp.py
    except Exception as e:
        print(f'ERROR DISABLING SAMPLE ENVIRONMENTS: {e}')
    ttime.sleep(0.5)
    # kill_pid_ioc()  # from /00_startup.py
    try:
        kill_pid_ioc() # from /00_startup.py
    except Exception as e:
        print(e)
        print(f'ERROR DISABLING IOCs: {e}')


atexit.register(full_stop_for_sample_envs)


def quit_without_sample_env_shutdown():
    atexit.unregister(full_stop_for_sample_envs)
    print('IPYTHON SESSION CLOSED')
    print('ALL SAMPLE ENVIRONMENTS ARE STILL ENABLED AND IOCs ARE RUNNING')
    quit()


