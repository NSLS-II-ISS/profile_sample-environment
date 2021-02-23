

p_values = np.arange(40, 55, 5)
i_values = np.arange(10, 11)

T1 = 100
T2 = 150
time_window = 3*60


from simple_pid import PID
import h5py

def pid_testing(max_time=60, p=0.01, i=0.01, d=0.001, setpoint=40, plotting=True):

    time, temp_rb, volt_out = [], [], []

    pid = PID(p, i, d, setpoint=setpoint)
    pid.sample_time = 0.01
    pid.output_limits = (0, 3.5)

    RE(bps.mv(volt_override, 0))
    RE(bps.mv(heater_enable2, 1))
    RE(bps.mv(heater_override2, 1))
    time_start = ttime.time()
    while True:
        current_value = temp2.value
        output = pid(current_value)
        time.append(ttime.time() - time_start)
        temp_rb.append(current_value)
        volt_out.append(output)
        RE(bps.mv(volt_override, output))


        if ttime.time() - time_start > max_time:
            break
        # ttime.sleep(0.1)

    RE(bps.mv(volt_override, 0))
    RE(bps.mv(heater_enable2, 0))
    RE(bps.mv(heater_override2, 0))
    if plotting:
        fig, ax = plt.subplots(1)
        ax2 = ax.twinx()
        ax.plot(time, temp_rb, 'r.-')
        ax2.plot(time, volt_out, 'k.-')
        ax.hlines(setpoint, time[0], time[-1], colors='g')

    return np.array(time[::5]), np.array(temp_rb[::5]), np.array(volt_out[::5])


def pid_scanning(sleep_time=5*60, exec_time=10*60, setpoint=300):
    hf = h5py.File(r'/nsls2/xf08id/Sandbox/pid_temp_data/2020_12_29_data_high_temp.h5', 'w')

    p_grid = 10**np.linspace(-2.7, -1.9, 5)
    i_grid = 10**np.linspace(-3.25, -3.75, 5)
    n = p_grid.size * i_grid.size
    idx = 1
    for _p in p_grid:
        for _i in i_grid:
            print(f'checking p={_p}, i={_i} | progress = {round(idx/n*100)}')
            _t, _T, _V = pid_testing(max_time=exec_time, p=_p, i=_i, d=0, setpoint=setpoint, plotting=False)
            R = np.sum(((_T[_t > 0.33*exec_time] - setpoint) / setpoint)**2)

            g = hf.create_group(str(idx))
            g.create_dataset('t', data=_t)
            g.create_dataset('T', data=_T)
            g.create_dataset('V', data=_V)
            g.create_dataset('P', data=_p)
            g.create_dataset('I', data=_i)
            g.create_dataset('R', data=R)
            idx += 1
            ttime.sleep(sleep_time)

    hf.close()


def pid_ramping(t_ramp=3*60, T=400, max_time=5*60, p=0.01, i=0.01, d=0.001):
    time, temp_rb, volt_out = [], [], []
    T_init =  temp2.value
    pid = PID(p, i, d, setpoint=T_init)
    pid.sample_time = 0.01
    pid.output_limits = (0, 3.5)

    RE(bps.mv(volt_override, 0))
    RE(bps.mv(heater_enable2, 1))
    RE(bps.mv(heater_override2, 1))
    time_start = ttime.time()
    ramp_rate = (T - T_init) / t_ramp
    while True:
        dt = ttime.time() - time_start
        if dt < t_ramp:
            pid.setpoint = ramp_rate * dt + T_init
        else:
            pid.setpoint = T
        print(pid.setpoint)
        current_value = temp2.value
        output = pid(current_value)
        time.append(dt)
        temp_rb.append(current_value)
        volt_out.append(output)
        RE(bps.mv(volt_override, output))

        if dt > max_time:
            break
        # ttime.sleep(0.1)

    RE(bps.mv(volt_override, 0))
    RE(bps.mv(heater_enable2, 0))
    RE(bps.mv(heater_override2, 0))



# hf =  h5py.File(r'/nsls2/xf08id/Sandbox/pid_temp_data/2020_12_23_data.h5', 'r')

def plot_pid_scanning_data():
    hf = h5py.File('/nsls2/xf08id/Sandbox/pid_temp_data/2020_12_29_data.h5', 'r')
    P = []
    I = []
    t = []
    T = []
    V = []
    R = []
    for item in hf.items():
        P.append(hf[item[0]]['P'][()])
        I.append(hf[item[0]]['I'][()])
        t.append(hf[item[0]]['t'][()])
        T.append(hf[item[0]]['T'][()])
        V.append(hf[item[0]]['V'][()])
        R.append(hf[item[0]]['R'][()])

    P = np.array(P)
    I = np.array(I)
    t = np.array(t)
    T = np.array(T)
    V = np.array(V)
    R = np.array(R)
    idx_best = np.argmin(R)

    plt.figure(1)
    plt.clf()

    for i in range(P.size):
        if i == idx_best:
            label = 'P = ' + str(P[idx_best]) + ', I = ' + str(I[idx_best])
            plt.plot(t[i], T[i], 'r', alpha=1.0, label=label, lw=2)
        else:
            plt.plot(t[i], T[i], 'k', alpha=0.5)
    plt.plot([t[0][0], t[0][-1]], [50, 50], 'g-', label='setpoint')
    plt.legend()
    plt.xlabel('time, s')
    plt.ylabel('Temperature RB')
    # plt.plot(t, T)
    return P, I, R






def pid_test():

    for p in p_values:
        for i in i_values:
            print(f'testing values p={p} and i={i}')
            now = ttime.time()
            print(f'Time is {ttime.ctime(now)}')
            RE(bps.mv(pid_p1, p))
            RE(bps.mv(pid_i1, i))
            RE(bps.mv(temp_sp1, T2))

            RE(bps.mv(heater_enable1, 1))
            while True:
                RE(bps.sleep(1))
                if temp1.get() > T2:
                    RE(bps.sleep(60 * 5))
                    break

            RE(bps.mv(heater_enable1, 0))
            while True:
                RE(bps.sleep(60 * 1))
                if np.abs(temp1.get() - T1)<1:
                    break


def stabilize_temperature(T, t=60, thresh=1):
    t = int(t)
    RE(bps.mv(temp_sp1, T))
    RE(bps.mv(heater_enable1, 1))
    print('waiting until intitial temperature is stabilized')
    T_history = [temp1.get()]
    while True:
        RE(bps.sleep(1))
        T_history.append(temp1.get())
        if len(T_history)>t:
            delta_set = T_history[-1] - T
            delta_hist = T_history[-1] - T_history[-t]
            print(f'error wrt set: {delta_set} \t error wrt {t} s ago: {delta_hist}')
            if ((np.abs(delta_set) < thresh) and
                (np.abs(delta_hist) < thresh)):
                break


def temp_ramp(T1, T2, t, n=100):
    dt = t/n
    dT = (T2 - T1)/n
    RE(bps.mv(temp_sp1, T1))
    RE(bps.mv(heater_enable1, 1))
    # wait until stabilize
    print('waiting until intitial temperature is stabilized')
    while True:
        RE(bps.sleep(1))
        if np.abs(temp1.get() - T1)<1:
            break

    print('starting ramping the temperature')
    # ramping
    for i in range(n):
        T_set = T1 + (i+1)*dT
        now = ttime.time()
        print(f'Set temperature: {T_set} \t Time : {ttime.ctime(now)}')
        RE(bps.mv(temp_sp1, T_set))
        RE(bps.sleep(dt))





# pid_p1
# pid_i1
# pid_d1
# curr_rb
#
# temp_sp1