import atexit


def full_stop_for_sample_envs():
    print('IPYTHON SESSION CLOSED')
    print('DISABLING ALL SAMPLE ENVIRONMENTS')
    print()
    print()
    disable_all_envs() # from /03_temp.py
    kill_pid_ioc() # from /00_startup.py


atexit.register(full_stop_for_sample_envs)


def quit_without_sample_env_shutdown():
    atexit.unregister(full_stop_for_sample_envs)
    print('IPYTHON SESSION CLOSED')
    print('ALL SAMPLE ENVIRONMENTS ARE STILL ENABLED AND IOCs ARE RUNNING')
    quit()


