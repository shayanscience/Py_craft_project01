# This is the main firmware
# Release date 11/10/2025
# Author: Shayan Sheikhrezaei
# Email: Shayan_rezaei@cus.fullerton.edu
# Firmware 1.2.1

''' In Firmware 1.0.0 what we tried to acheive was to continuesly check if there is any update available. If so, we would go ahead
        and executes it. Later, I came up with the idea of what if we only connect to the mission control once and loose our connection
        later, how are we going to execute a file given no connection.
    I thought that it would be handy to download the update from the mission control to the craft and then execute the local file instead.
    
    What happens in the program is that, it checks if the similar name exists on the local drive, if so it removes it and immediately download
        the file from mission control, somewhat like replacing it.
        
    I ran this program and works fine. There are certain concerns such as what if the update is corrupted or is not working good. what is
        the solution. I may dive into this section for later revision
'''



# Libraries
import time
import os
import shutil
import importlib
import importlib.util
import sys



#Messages Flag
updateAvailable_flag = False
fileExecuted_flag = False
localFirmwareAvailable_flag = False     # This flag is added to indicate if firmware is available on craft local drive

#directories
mission_control = r"C:\Users\ShayanSheikhrezaei\OneDrive - Orca Technologies\Personal\Projects\Programming\Py_mission_control_project01\missionControl.py"
craft_directory = r"C:\Users\ShayanSheikhrezaei\OneDrive - Orca Technologies\Personal\Projects\Programming\Py_craft_project01"
# craft_update = r"C:\Users\ShayanSheikhrezaei\OneDrive - Orca Technologies\Personal\Projects\Programming\Py_craft_project01\missionControl.py"
backup_file = "missionControl_backup.py"


# Firmware Greeting - executes once
print("**** Craft Oblivious ****")                      # Craft name
execution_date = time.localtime()                       # Get the local time
formatted = time.strftime("%Y-%m-%d", execution_date)   # Convert time to formatted time (interested in date)
print(f"**** Date: {formatted} ****")




def load_mission_control(path="missionControl.py"):
    if os.path.exists(path):
        spec = importlib.util.spec_from_file_location("missionControl", path)
        missionControl = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(missionControl)

        """ In following 'If/Else' statement we attempt to see if our firmware 'missionControl' exists within 'sys.module'
            if not we add it.
            The purpose is to execute the firmware/library once in the main program so that the content can be used whenever needed."""
        if "missionControl" in sys.modules:                     
            return missionControl
        else:
            sys.modules["missionControl"] = missionControl

        return missionControl
    return None

"""
    Here is what function below does:
        - Define the global flags.
        - Look into the mission control directory, check if any updates available.
            - If update exists: 
                - Set the 'updateAvailable_flag'.
                - Reset the 'fileExecuted_flag' -> This ensures the update executes once.
                - Check if similar file name exists on the craft local drive before downloading it.
                    - If it exists remove it first.
                - If it doesn't exist or is removed, download the update from the mission control into the craft local drive.
                    * Animation tag indicates the message and a small animation for having a better user experience.
                - Now we attempt to import the firmware (python file) using 'load_mission_control()'.
                - Checks if the update has ever been executed, if not, it proceeds.
                - Sets the 'fileExecuted_flag' and executes the 'update01()', respectively. 
        - If there is no update available, it prints the appropriate message that no update is available.
"""

#executables
def execute_update():
    global updateAvailable_flag, fileExecuted_flag, localFirmwareAvailable_flag, missionControl
    if (os.path.exists(mission_control)):               #Mission control directory check
        updateAvailable_flag = True
        fileExecuted_flag = False 
        if(os.path.exists("missionControl.py")):               #Craft directory check
            os.remove("missionControl.py")
        else:    
            print("Update available!")
            time.sleep(1)
            print("Fetching the file", end="", flush=True)      # the ' end="" ' wouldn't allow to go to the next line so that you can continue printing on the same line
            for i in range(3):                                  # Animation Starts
                if i<2:
                    print(".", end="", flush=True)
                else:
                    print(".", flush=True)
                time.sleep(1)                                   # Animation Ends
            shutil.move(mission_control, craft_directory)
            missionControl = load_mission_control("missionControl.py")
    
    elif(os.path.exists("missioncontrol.py") & ~updateAvailable_flag & ~localFirmwareAvailable_flag):
        localFirmwareAvailable_flag = True
        fileExecuted_flag = False
        missionControl = load_mission_control("missionControl.py")

    else:
        if(fileExecuted_flag==False):
            fileExecuted_flag = True
            if missionControl:
                try:
                    missionControl.update01()
                    updateAvailable_flag = False
                except Exception as e:
                    print(f"update failed: {e}")
                    shutil.copyfile("missionControl_backup.py", "missionControl.py")
                    print("Rolled back to previous version")
                    importlib.reload(missionControl)
                    fileExecuted_flag = False             #Resets the system (Treating as if the file has not been executed) since the update was bugged now we are going to run old firmware.
                    updateAvailable_flag = True


while True:
    execute_update()

    # Following script is just for the testing purposes demonstrating something is occuring
    execution_date = time.localtime() 
    test_formatted = time.strftime("%H:%M:%S", execution_date)  
    print("Time: ", test_formatted)
    time.sleep(1)

