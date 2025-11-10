# This is the main firmware
# Release date 11/10/2025
# Author: Shayan Sheikhrezaei
# Email: Shayan_rezaei@cus.fullerton.edu
# Firmware 1.1.0

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



#Messages Flag
update_flag = True
file_execution_flag = False

#directories
mission_control = r"C:\Users\ShayanSheikhrezaei\OneDrive - Orca Technologies\Personal\Projects\Programming\Py_mission_control_project01\missionControl.py"
craft_directory = r"C:\Users\ShayanSheikhrezaei\OneDrive - Orca Technologies\Personal\Projects\Programming\Py_craft_project01"
craft_update = r"C:\Users\ShayanSheikhrezaei\OneDrive - Orca Technologies\Personal\Projects\Programming\Py_craft_project01\missionControl.py"



# Firmware Greeting - executes once
print("**** Craft Oblivious ****")                      # Craft name
execution_date = time.localtime()                       # Get the local time
formatted = time.strftime("%Y-%m-%d", execution_date)   # Convert time to formatted time (interested in date)
print(f"**** Date: {formatted} ****")


"""
    Here is what function below does:
        - Define the global flags to the 'execute_update()'.
        - Look into the mission control directory, check if updates available.
            - If update exists, set the 'update_flag'.
                - Check if similar file name exists on the craft.
                    - If it exists remove it first.
                - If the similar file doesn't exists or removed, then move the existing available update
                    from the mission control into the craft.
                - Checks if the update has ever been executed, if not, it proceeds.
                - Sets the 'file_execution_flag' and executes the 'update01()', respectively. 
        - If there is no update available, it prints the appropriate message that no update is available.
"""

#executables
def execute_update():
    global update_flag, file_execution_flag
    if (os.path.exists(mission_control)):               #Mission control directory check
        update_flag = True
        if(os.path.exists(craft_update)):               #Craft directory check
            os.remove(craft_update)
        shutil.move(mission_control, craft_directory)
        if(file_execution_flag==False):
            import missionControl
            file_execution_flag = True
            print("There is an update available!")
            time.sleep(1)
            print("Fetching the file...")
            time.sleep(3)
            missionControl.update01()
    else:
        if(update_flag):
            print("No update available!")
            print("Continouing previous instructions")
            update_flag = False



while True:
    execute_update()

    # Following script is just for the testing purposes demonstrating something is occuring
    execution_date = time.localtime() 
    test_formatted = time.strftime("%H:%M:%S", execution_date)  
    print("Time: ", test_formatted)
    time.sleep(5)

