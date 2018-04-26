#######################################################################
# David Ardy
# Locker #14, Combo 18-28-10
#######################################################################

def get_diddled():
    print('')


get_diddled()

left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

assert left_motor.connected
assert right_motor.connected
left_motor.run_forever(speed_sp=speed+8, stop_ation=stop_action)
