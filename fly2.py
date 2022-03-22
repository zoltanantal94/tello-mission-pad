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

    tello.go_xyz_speed_mid(0, 0, 100, 50, 4)
    time.sleep(5)
    tello.go_xyz_speed_yaw_mid(90, 0, 100, 30, 0, 4, 1)
    time.sleep(8)
    tello.go_xyz_speed_yaw_mid(90, 0, 100, 30, 0, 1, 2)
    time.sleep(8)
    tello.go_xyz_speed_yaw_mid(90, 0, 100, 30, 0, 2, 3)
    time.sleep(8)
    tello.go_xyz_speed_yaw_mid(90, 0, 100, 30, 0, 3, 4)
    time.sleep(8)

    tello.disable_mission_pads()
    tello.land()
    tello.turn_motor_on()
    time.sleep(7)
    tello.turn_motor_off()
    tello.end()