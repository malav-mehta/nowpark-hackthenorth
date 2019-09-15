import RPi.GPIO as GPIO
import sensors

if __name__ == "__main__":
    try:
        sensors.initPins()
        while True:
            sensors.updateAllPins()
    finally:
        GPIO.cleanup()
        print("Application closed by users.")
