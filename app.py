import RPI.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(7) == GPIO.HIGH:
        print("Button Pressed")

    