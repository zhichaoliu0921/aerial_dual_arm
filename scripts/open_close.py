# this function is to open or close the gripper

def open_close_gripper(servoName, motorBound, cmd):
    """
    Used to open the gripper or close the gripper
    :param servoName: the name of the servo
    :param motorBound: the angle range to close the gripper
    :param cmd: the cmd string to open and close the motor
    :return: nothing
    """
    if cmd == 'open':
        servoName.move(angle=motorBound[0], time=400)
    elif cmd == 'close':
        servoName.move(angle=motorBound[1], time=400)
