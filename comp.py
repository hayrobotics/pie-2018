async def turn_cw(seconds): # Or, "turn right"
    Robot.set_value(left_motor, "duty_cycle", -0.5)
    Robot.set_value(right_motor, "duty_cycle", -0.5)
    await Actions.sleep(seconds)
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)
    
async def turn_ccw(seconds): # Or, "turn left"
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", 0.5)
    await Actions.sleep(seconds)
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)

async def drive(seconds): # Or, "move forward"
    Robot.set_value(left_motor, "duty_cycle", -0.5)
    Robot.set_value(right_motor, "duty_cycle", 0.5)
    await Actions.sleep(seconds)
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)
    
async def reverse(seconds): # Or, "move backwards"
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", -0.5)
    await Actions.sleep(seconds)
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)

async def turbine_procedure(speed):
    Robot.set_value(turbine, "duty_cycle", speed)
    await Actions.sleep(2.0)
    Robot.set_value(turbine, "duty_cycle", 0)
    
async def lift_procedure():
    await Actions.sleep(5.0) # Give the turbine some time to sweep up balls...
    # Then close.
    Robot.set_value(trap_servo, "servo0", 0.5)
    await Actions.sleep(1.0)
    # Activate elevator winch!
    Robot.set_value(winch_motor, "duty_cycle", 0.75)
    await Actions.sleep(2.0)
    Robot.set_value(winch_motor, "duty_cycle", 0)

def autonomous_setup():
    # Set up servo
    Robot.set_value(trap_servo, "servo0", 0)
    # Move out of start box, to balls
    Robot.run(drive, '''''')
    # Activate turbines on slow, briefly, then stop!
    Robot.run(turbine_procedure, -0.25)
    # Turn right (clockwise)
    Robot.run(turn_cw, '''''')
    # Move forward a little
    Robot.run(drive, '''''')
    # Turn left (counterclockwise)
    Robot.run(turn_ccw, '''''')
    # Back into goal
    Robot.run(reverse, '''''')
    # Activate turbines on fast to shoot balls!
    Robot.run(turbine_procedure, -0.75)
    
def autonomous_main():
    pass