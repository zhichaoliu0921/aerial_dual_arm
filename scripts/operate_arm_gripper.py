import time
from lx16a import *
from arm_reaching import reach_retrieve_arm

if __name__ == '__main__':
    # Initialize the lx16A motor
    LX16A.initialize('COM3') # leave it for now

    # Set the name of the motor

    # gripper arm (already assigned)
    grippMotor = LX16A(5)
    wristMotor = LX16A(4)
    rotHoMotor = LX16A(3)
    middlMotor = LX16A(2)
    shouMotor1 = LX16A(1)
    shouMotor2 = LX16A(0)

    # set the command for gripper motor to perform
    cmdGripper = {"openCMD": "open", "closeCMD": "close"}

    # pack information for wrist motor, gripper motor, shoulder motor, middle motor and rotation horizontally motor
    shoServo = {"name": [shouMotor1, shouMotor2], "angleReach": 135, "angleRetrieve": 205}
    midServo = {"name": middlMotor, "angleReach": 105, "angleRetrieve": 30}
    rotServo = {"name": rotHoMotor, "angleReach": 90, "angleRetrieve": 120}
    wriServo = {"angle": [35, 135], "name": wristMotor}
    griServo = {"angle": [500 / 1000 * 240, 580 / 1000 * 240], "cmd": cmdGripper, "name": grippMotor}

    t = 0

    while True:
        # operate the reaching and retrieving
        if t % 2 == 0:
            # opertate retrieving
            reach_retrieve_arm(shoServo, midServo, rotServo, wriServo, griServo, "retrieve")
        elif t % 2 == 1:
            # operate reaching
            reach_retrieve_arm(shoServo, midServo, rotServo, wriServo, griServo, "reach")

        # sleep for certain sec
        time.sleep(5)

        t = t + 1
