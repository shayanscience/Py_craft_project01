# This file is called 'updater.py' and contains the logical behind determining if an update is available and if so update
import file_utils as fu
import config
import time
import importlib
import sys
import loader

def is_update_available():
    if (fu.file_exists(config.mission_control)):   #only checks existence, not whether the remote file is actually newer than the local one.
        print("IDLE -> REMOTE_AVAILABLE")
        config.state="REMOTE_AVAILABLE"
        time.sleep(1)
    elif (fu.file_exists(config.craft_directory+"\missionControl.py") and not config.executed_flag):
        print("IDLE->LOCAL_AVAILABLE")
        time.sleep(1)
        config.state="LOCAL_AVAILABLE"
    else:
        print("No update available!")
        time.sleep(2)
        config.state="IDLE"

def roll_back():
    fu.copy_file("missionControl_backup.py", "missionControl.py")
    print("Rolled back to previous version")
    # if "missionControl" in sys.module:
    # if config.missionControl:
    #     importlib.reload(config.missionControl)
    #     config.missionControl = sys.modules["missionControl"]
    # else:
    config.missionControl = loader.load_mission_control("missionControl.py")