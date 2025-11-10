# This is the main firmware
# Release date 11/10/2025
# Author: Shayan Sheikhrezaei
# Email: Shayan_rezaei@cus.fullerton.edu
# Firmware 1.0.0


# Libraries
import time
import sys
sys.path.append("C:/Users/ShayanSheikhrezaei/OneDrive - Orca Technologies/Personal/Projects/Programming/Py_mission_control_project01")
from missionControl import update01
import os


#Messages Flag
update_flag = True
file_execution_flag = False

#directories
mission_control = r"C:\Users\ShayanSheikhrezaei\OneDrive - Orca Technologies\Personal\Projects\Programming\Py_mission_control_project01\missionControl.py"

# testing
print("Hello World!")


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
                - Checks if the update has ever been executed, if not, it proceeds.
                - Sets the 'file_execution_flag' and executes the 'update01()', respectively. 
        - If there is no update available, it prints the appropriate message that no update is available.
"""
#executables
def execute_update():
    global update_flag, file_execution_flag
    if (os.path.exists(mission_control)):
        update_flag = True
        if(file_execution_flag==False):
            file_execution_flag = True
            print("There is an update available!")
            time.sleep(1)
            print("Fetching the file...")
            time.sleep(3)
            update01()
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

