RIGHT_MOTOR = "47246956744893298830406"
LEFT_MOTOR = "47244718417202768690407"
ELEVATOR_WINCH = "BLAH"
TRAP_WINCH = "BLAH"

async def turn_cw(seconds): # Or, "turn right"
    Robot.set_value(LEFT_MOTOR, "duty_cycle", -0.5)
    Robot.set_value(RIGHT_MOTOR, "duty_cycle", -0.5)
    await Actions.sleep(seconds)
    Robot.set_value(LEFT_MOTOR, "duty_cycle", 0)
    Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0)
    
async def turn_ccw(seconds): # Or, "turn left"
    Robot.set_value(LEFT_MOTOR, "duty_cycle", 0.5)
    Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0.5)
    await Actions.sleep(seconds)
    Robot.set_value(LEFT_MOTOR, "duty_cycle", 0)
    Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0)

async def drive(seconds): # Or, "move forward"
    Robot.set_value(LEFT_MOTOR, "duty_cycle", -0.5)
    Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0.5)
    await Actions.sleep(seconds)
    Robot.set_value(LEFT_MOTOR, "duty_cycle", 0)
    Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0)
    
async def reverse(seconds): # Or, "move backwards"
    Robot.set_value(LEFT_MOTOR, "duty_cycle", 0.5)
    Robot.set_value(RIGHT_MOTOR, "duty_cycle", -0.5)
    await Actions.sleep(seconds)
    Robot.set_value(LEFT_MOTOR, "duty_cycle", 0)
    Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0)

async def turbine_procedure(speed):
    Robot.set_value(turbine, "duty_cycle", speed)
    await Actions.sleep(2.0) 
    Robot.set_value(turbine, "duty_cycle", 0)
    
async def lift_procedure(speed):
    await Actions.sleep(5.0) # Give the turbine some time to sweep up balls..
    
    # Then, to trap balls:
    
    # Activate trap motor
    Robot.set_value(TRAP_WINCH, "duty_cycle", speed)    
    # Wait half a second
    await Actions.sleep(0.5)
    # Stop trap motor
    Robot.set_value(TRAP_WINCH)
    await Actions.sleep(1.0)

    
    # Activate elevator winch!
    Robot.set_value(ELEVATOR_WINCH, "duty_cycle", 0.75)
    await Actions.sleep(2.0)
    # Stop the winch.
    Robot.set_value(ELEVATOR_WINCH, "duty_cycle", 0)

async def drop_procedure():
    # Re-open the trap...
    Robot.set_value(trap_servo, "servo0", 0.0)
    # Activate elevator winch, w/ negative voltage.
    Robot.set_value(ELEVATOR_WINCH, "duty_cycle", -0.75)
    await Actions.sleep(2.0)
    # Stop the winch.
    Robot.set_value(ELEVATOR_WINCH, "duty_cycle", 0)
    
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

async def teleop_actions():  # Async function for controller logic.
    # --- LEFT MOTOR LOGIC ---
    if Gamepad.get_value("joystick_left_y") != 0.0: # If left joystick moves up or down: 
        Robot.set_value(LEFT_MOTOR, "duty_cycle", Gamepad.get_value("joystick_left_y"))
        # The left motor will move proportionally to the push of the joystick.
        # To go faster, push harder. 
        # To go backwards, pull joystick.
        
    else: # If the left joystick is centered:
        Robot.set_value(LEFT_MOTOR, "duty_cycle", 0.0)
        # Stop the left motor.
    
    # --- RIGHT MOTOR LOGIC --- 
    # Same principle w/ right side instead of left...
    if Gamepad.get_value("joystick_right_y") != 0.0:
        Robot.set_value(RIGHT_MOTOR, "duty_cycle", -1 * Gamepad.get_value("joystick_right_y"))
        print("ye")
    else:
        Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0.0)
        
    '''
    IN ORDER TO DRIVE:
    Push/pull both in same direction to drive forward/backwards
    Push/pull in opposite directions to turn on axis 
    '''
    
    # ACTIVATE TURBINE - SLOW MODE
    if Gamepad.get_value("button_b"): 
        Robot.run(turbine_procedure, 0.25)
        
    # ACTIVATE TURBINE - FAST MODE  
    if Gamepad.get_value("button_b"):
        Robot.run(turbine_procedure, 0.75)
        
    # ELEVATOR LOGIC
    '''
    if Gamepad.get_value("l_bumper"):
        Robot.set_value(ELEVATOR_WINCH, "duty_cycle", 0.5)
    
    if Gamepad.get_value("r_bumper"):
        if Gamepad.get_value("r_trigger"):
            Robot.set_value(TRAP_WINCH, "duty_cycle", 0.75)
            Robot.set_value(ELEVATOR_WINCH, "duty_cycle", 0.5)
        else:
            Robot.set_value(ELEVATOR_WINCH, "duty_cycle", 0.5)
    
    if Gamepad.get_value("l_bumper"):
        Robot.set_value(TRAP_WINCH, "duty_cycle", 0.25)
        
    if Gamepad.get_value("r_trigger") and not Gamepad.get_value("r_button"):
        Robot.set_value(TRAP_WINCH, "duty_cycle", 0.25)
        
    if Gamepad.get_value("r_bumper") and Gamepad.get_value("r_trigger"):
        
        
    
    '''
        
    '''
    
    BUMPER: Moves elevator winch up and "dpad_down"
    TRIGGERS: Makes elevator open and close
    '''
def teleop_setup():
    print("Tele-op mode has started!")
    
def teleop_main(): # Subscribe to @InfiniteLoops
    Robot.run(teleop_actions) # Controller logic runs in an async function 