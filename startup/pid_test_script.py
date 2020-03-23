

p_values = np.arange(40, 55, 5)
i_values = np.arange(10, 11)

T1 = 100
T2 = 150
time_window = 3*60

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