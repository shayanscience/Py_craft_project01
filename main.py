# This is the main firmware
# Release date 11/10/2025
# Author: Shayan Sheikhrezaei
# Email: Shayan_rezaei@cus.fullerton.edu
# Firmware 1.0.0


# Libraries
import time


# testing
print("Hello World!")


# Firmware Greeting - executes once
print("**** Craft Oblivious ****")
execution_date = time.localtime()
formatted = time.strftime("%Y-%m-%d", execution_date)
print(f"**** Date: {formatted} ****")

# print(time.asctime()[0])
