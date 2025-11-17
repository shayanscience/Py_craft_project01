# This is the main firmware
# Release date 11/10/2025
# Author: Shayan Sheikhrezaei
# Email: Shayan_rezaei@cus.fullerton.edu
# Firmware 2.1.0

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
import config
import file_utils as fu
import loader
import updater
import ui
import time



# Firmware Greeting - executes once
print("**** Craft Oblivious ****")                      # Craft name
execution_date = time.localtime()                       # Get the local time
formatted = time.strftime("%Y-%m-%d", execution_date)   # Convert time to formatted time (interested in date)
print(f"**** Date: {formatted} ****")


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
def execute_update():
    if config.state=="IDLE":
        config.timer += 1
        if config.timer==5:
            config.state="CHECK_FOR_UPDATE"
            config.timer=0


    elif config.state=="CHECK_FOR_UPDATE":
        updater.is_update_available()

    elif config.state=="REMOTE_AVAILABLE":
        if(fu.file_exists("missionControl.py")):               #Craft directory check
            ui.show_erasing()
            fu.delete_file("missionControl.py")
        else:    
            ui.show_updating()
            ui.show_fetching_animation()                         # Animation Ends
            fu.move_file(config.mission_control, config.craft_directory)
            config.missionControl = loader.load_mission_control("missionControl.py")
            config.state="EXECUTING"
            config.executed_flag = False

    elif config.state=="LOCAL_AVAILABLE":
        ui.show_local_available()
        config.missionControl = loader.load_mission_control("missionControl.py")
        config.state="EXECUTING"
        

    elif config.state=="EXECUTING":
        ui.show_executing()
        if config.missionControl:
            try:
                config.missionControl.update01()
                config.state="IDLE"
                config.executed_flag = True
            except Exception as e:
                ui.show_update_failure(e)
                config.state="ROLLED_BACK"

    elif config.state=="ROLLED_BACK":
        ui.show_rolling_back()
        updater.roll_back()
        config.state="EXECUTING"
        config.executed_flag = False

    else:
        config.state = "IDLE"


while True:
    execute_update()

    # Following script is just for the testing purposes demonstrating something is occuring
    execution_date = time.localtime() 
    test_formatted = time.strftime("%H:%M:%S", execution_date)  
    print("Time: ", test_formatted)
    time.sleep(1)