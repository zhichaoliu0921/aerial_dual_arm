import time
from open_close import open_close_gripper


def reach_retrieve_arm(shoulderServo, middleServo, rotServo, wristServo, gripperServo, cmd):
    """
    Move the arm horizontally
    :param shoulderServo: name of the shoulder servo
    :param middleServo: name of the middle servo
    :param rotServo: name of the rotation horizontally servo
    :param wristServo: name of the wrist servo
    :param gripperServo: name of the gripper servo, and some related angle information
    :param cmd: command for the robot arm and the gripper
    :return: motion of two servos to move horizontally
    """

    # get the name of all motors
    wristMotor    = wristServo["name"]
    shoulderMotor = shoulderServo["name"]
    gripperMotor  = gripperServo["name"]
    middleMotor   = middleServo["name"]
    rotHMotor     = rotServo["name"]

    # get the needed angles and command
    wristAngleStart = wristServo["angle"][0]
    wristAngleEnd   = wristServo["angle"][1]
    angleGripper    = gripperServo["angle"]
    cmdGripper      = gripperServo["cmd"]
    shoulderReach   = shoulderServo["angleReach"]
    shoulderRetri   = shoulderServo["angleRetrieve"]
    midReach        = middleServo["angleReach"]
    midRetri        = middleServo["angleRetrieve"]
    rotReach        = rotServo["angleReach"]
    rotRetri        = rotServo["angleRetrieve"]

    if cmd == "reach":

        # move the wrist servo to its start posture
        wristMotor.move(angle=wristAngleStart, time=300)
        time.sleep(0.5)

        # move the shoulder servo to reaching posture
        shoulderMotor[0].move(angle=shoulderReach, time=1200)
        shoulderMotor[1].move(angle=shoulderReach, time=1200)
        time.sleep(0.5)

        # move the middle servo to reaching posture
        middleMotor.move(angle=midReach-30, time=1200)
        time.sleep(0.5)

        # move the rotation-horizontally servo to reaching posture
        rotHMotor.move(angle=rotReach, time=1200)
        time.sleep(0.5)

        # operate the gripper
        # open the gripper
        open_close_gripper(gripperMotor, angleGripper, cmdGripper["openCMD"])
        time.sleep(2)

        # close the gripper
        open_close_gripper(gripperMotor, angleGripper, cmdGripper["closeCMD"])
        time.sleep(1)

        # rotate the wrist for certain degrees
        wristMotor.move(angle=wristAngleEnd, time=300)
        time.sleep(0.5)

    elif cmd == "retrieve":
        # retrieving the arm and close the gripper
        # move the shoulder servo to retrieving posture
        shoulderMotor[0].move(angle=shoulderRetri, time=1200)
        shoulderMotor[1].move(angle=shoulderRetri, time=1200)
        time.sleep(0.5)

        # move the middle servo to retrieving posture
        middleMotor.move(angle=midRetri, time=1200)
        time.sleep(2)

        # move the rotation-horizontally servo to retrieving posture
        rotHMotor.move(angle=rotRetri, time=1200)
        time.sleep(1)
