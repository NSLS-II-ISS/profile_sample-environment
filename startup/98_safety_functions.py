import atexit
import time as ttime


print('this is ran!!')

def full_stop_for_sample_envs():
    import time as ttime
    print('IPYTHON SESSION CLOSED')
    print('DISABLING ALL SAMPLE ENVIRONMENTS')
    print()
    print()
    # disable_all_envs()  # from /03_temp.py
    try:
        disable_all_envs() # from /03_temp.py
    except Exception as e:
        print(e)
        print('COULD NOT DISABLE SAMPLE ENVIRONMENTS: IOCs NOT FOUND')
    ttime.sleep(0.5)
    # kill_pid_ioc()  # from /00_startup.py
    try:
        kill_pid_ioc() # from /00_startup.py
    except Exception as e:
        print(e)
        print('COULD NOT KILL IOCs: PROCESS NOT FOUND')


atexit.register(full_stop_for_sample_envs)


def quit_without_sample_env_shutdown():
    atexit.unregister(full_stop_for_sample_envs)
    print('IPYTHON SESSION CLOSED')
    print('ALL SAMPLE ENVIRONMENTS ARE STILL ENABLED AND IOCs ARE RUNNING')
    quit()


