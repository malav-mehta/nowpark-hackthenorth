# This file sets up the variables in main.py
import time

# Only the *_Data variables are to be modified
parkingLot_Data = u'hack-the-north'

parkingSpace1_Data = {
    "id": "C86",
    "location": "43.473813, -80.540458",
    "occupied": False,
    "start-time": 0,
    "user-parked-for": 0,
    "last-update": time.time()
}

parkingSpace2_Data = {
    "id": "B86",
    "location": "43.473871, -80.540503",
    "occupied": False,
    "start-time": 0,
    "user-parked-for": 0,
    "last-update": time.time()
}

# Variables that will not be modified
parkingSpace1_Setup = {
    "tracking_pin": 7,
    "echo_pin": 11
}

parkingSpace2_Setup = {
    "tracking_pin": 13,
    "echo_pin": 15
}
