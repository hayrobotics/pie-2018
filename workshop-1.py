LEFT_MOTOR = "47244718417202768690407"
RIGHT_MOTOR = "47246956744893298830406"
RFID = "51978179310080419449587"
# NOTICE: LEFT MOTOR BACKWARDS. USE NEGATIVE PULSE VALUES.
    
def autonomous_setup():
    print("Going auto!")

async def autonomous_actions():
    # Sensor logic in async:
    if not Robot.get_value(RFID, "tag_detect"): # If RFID sensor detects a tag:
        print("A tag was detected!")
        await Actions.sleep(5.0)

def autonomous_main():
    Robot.run(autonomous_actions) # Run async actions to infinity and beyond!
    

def teleop_setup():
    print("Going telly!") # Cause 

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
    else:
        Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0.0)
        
    
    
    # --- FORCE STOP LOGIC  ---
    if Gamepad.get_value("l_trigger") and Gamepad.get_value("r_trigger"): # If you pull both triggers:
        Robot.set_value(LEFT_MOTOR, "duty_cycle", 0.0)
        Robot.set_value(RIGHT_MOTOR, "duty_cycle", 0.0)
        # Force both motors to stop. 
        
    '''
    IN ORDER TO DRIVE:
    Push/pull both in same direction to drive forward/backwards
    Push/pull in opposite directions to turn on axis 
    Squeeze both triggers to force stop 
    '''

def teleop_main(): # Subscribe to @InfiniteLoops
    Robot.run(teleop_actions) # Controller logic runs in an async function 