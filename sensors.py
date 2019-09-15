import RPi.GPIO as GPIO
import time
import props
import firebase

GPIO.setmode(GPIO.BOARD)

def setupPin(PIN):
    PIN_TRIGGER = PIN["trigger"]
    PIN_ECHO = PIN["echo"]

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

def getDistance(PIN):
    PIN_TRIGGER = PIN["trigger"]
    PIN_ECHO = PIN["echo"]

    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    time.sleep(2)

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print(distance)
    return distance

def updateHistory(PIN, newDistance):
    x = PIN["history"].pop(0)
    PIN["history"].append(newDistance)

def validateOccupation(PIN):
    history = PIN["history"]
    similarityIndex = 0
    errorMargin = 2.5
    for i in history:
        if i < history[0] + errorMargin and i > history[0] - errorMargin:
            similarityIndex += 1
    if similarityIndex == len(history):
        if history[0] < 220:
            print(str(PIN["trigger"]) + " is occupied.")
            return True
        else:
            return False
    else:
        return False

def initPins():
    setupPin(ps1)
    setupPin(ps2)

def updateStatus(PIN, PIN_PARENT):
    distance = getDistance(PIN)
    updateHistory(PIN, distance)

    if validateOccupation(PIN):
        PIN_PARENT["occupied"] = True
        if PIN_PARENT["start-time"] == 0:
            PIN_PARENT["start-time"] = time.time()
            PIN_PARENT["user-parked-for"] = 0
    else:
        PIN_PARENT["occupied"] = False
        if PIN_PARENT["start-time"] != 0:
            parkedFor = round((time.time() - PIN_PARENT["start-time"]), 2)
            PIN_PARENT["user-parked-for"] = parkedFor
            PIN_PARENT["start-time"] = 0

    return PIN_PARENT


def updateAllPins():
    parkingSpace1_DataOLD = props.parkingSpace1_Data
    parkingSpace2_DataOLD = props.parkingSpace2_Data

    props.parkingSpace1_Data = updateStatus(ps1, props.parkingSpace1_Data)
    props.parkingSpace2_Data = updateStatus(ps2, props.parkingSpace2_Data)
    
    # print(parkingSpace1_DataOLD != props.parkingSpace1_Data)
    # print(parkingSpace2_DataOLD != props.parkingSpace2_Data)    

    firebase.syncToDatabase()

# pins for parking space 1
ps1 = {
    "trigger": props.parkingSpace1_Setup['tracking_pin'],
    "echo": props.parkingSpace1_Setup['echo_pin'],
    "history": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# pins for parking space 2
ps2 = {
    "trigger": props.parkingSpace2_Setup['tracking_pin'],
    "echo": props.parkingSpace2_Setup['echo_pin'],
    "history": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
