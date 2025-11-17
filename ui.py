# This file takes care of the UI (User Interface) functions

import time


def show_fetching_animation():
    print("Fetching the file", end="", flush=True)      # the ' end="" ' wouldn't allow to go to the next line so that you can continue printing on the same line
    for i in range(3):                                  # Animation Starts
        if i<2:
            print(".", end="", flush=True)
        else:
            print(".", flush=True)
        time.sleep(1)

def show_erasing():
    print("Ereasing local firmware...")
    time.sleep(1)

def show_updating():
    print("Update available!")
    time.sleep(1)

def show_local_available():
    print("LOCAL_AVAILABLE") 

def show_executing():
    print("EXECUTING")
    time.sleep(1)

def show_update_failure(err_msg):
    print(f"update failed: {err_msg}")


def show_rolling_back():
    print("Rolling back...")
    time.sleep(1)