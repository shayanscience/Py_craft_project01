# This is the main firmware
# Release date 11/10/2025
# Author: Shayan Sheikhrezaei
# Email: Shayan_rezaei@cus.fullerton.edu
# Firmware 1.0.0


# Libraries
import time
import sys
sys.path.append("C:/Users/ShayanSheikhrezaei/OneDrive - Orca Technologies/Personal/Projects/Programming/Py_mission_control_project01")
import missionControl
import os


#Messages Flag
update_flag = True
file_execution_flag = False

#directories
mission_control = r"C:\Users\ShayanSheikhrezaei\OneDrive - Orca Technologies\Personal\Projects\Programming\Py_mission_control_project01\missionControl.py"

# testing
print("Hello World!")


# Firmware Greeting - executes once
print("**** Craft Oblivious ****")
execution_date = time.localtime()                       # Get the local time
formatted = time.strftime("%Y-%m-%d", execution_date)   # Convert time to formatted time (interested in date)
print(f"**** Date: {formatted} ****")


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
            missionControl.update01()
    else:
        if(update_flag):
            print("No update available!")
            print("Continouing previous instructions")
            update_flag = False

# test_formatted = time.strftime("%H:%M:%S", execution_date)
while True:
    execute_update()

    execution_date = time.localtime() 
    test_formatted = time.strftime("%H:%M:%S", execution_date)  
    print("Time: ", test_formatted)
    time.sleep(5)

