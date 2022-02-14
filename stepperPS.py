from RpiMotorLib import RpiMotorLib
directionbase= 18 # Direction (DIR) GPIO Pin
stepbase = 15 # Step GPIO Pin

directionshoulder= 24 # Direction (DIR) GPIO Pin
stepshoulder = 23 # Step GPIO Pin

directionend= 8 # Direction (DIR) GPIO Pin
stepend = 25 # Step GPIO Pin

EN_pin = 14 # enable pin (LOW to enable)

GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

# Declare a instance of class pass GPIO pins numbers and the motor type
motorbase = RpiMotorLib.A4988Nema(directionbase, stepbase, (21,21,21), "DRV8825")
motorshoulder = RpiMotorLib.A4988Nema(directionshoulder, stepshoulder, (21,21,21), "DRV8825")
motorend = RpiMotorLib.A4988Nema(directionend, stepend, (21,21,21), "DRV8825")
motorend = RpiMotorLib.A4988Nema(directionend, stepend, (21,21,21), "DRV8825")