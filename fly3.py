import math

from djitellopy import Tello
import time

def fly(pad_dist, alt, speed, wait, res, ip):
    # Camera preparation
    if 'ip' in locals() and ip != '':
        tello = Tello(ip, 3)
    else:
        tello = Tello()
    tello.connect()

    battery = tello.get_battery()
    print("                    BATTERY: ", battery, "%")

    tello.enable_mission_pads()
    tello.set_mission_pad_detection_direction(0)
    time.sleep(1)

    tello.takeoff()

    pad = tello.get_mission_pad_id()
    print("pad: ", pad)

    for i in range(3):
        tello.go_xyz_speed_mid(0, 0, alt, speed, 1)
        time.sleep(3)
        tello.move_back(25)
        tello.move_left(25)
        tello.move_forward(50)
        tello.move_right(50)
        tello.move_back(50)
        tello.move_left(25)
        tello.move_forward(25)
        tello.go_xyz_speed_mid(0, 0, alt, speed, 1)

    tello.disable_mission_pads()
    tello.land()
    tello.turn_motor_on()
    time.sleep(7)
    tello.turn_motor_off()
    tello.end()