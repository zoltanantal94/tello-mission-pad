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

    tello.turn_motor_on()
    time.sleep(13)
    tello.turn_motor_off()

    tello.enable_mission_pads()
    tello.set_mission_pad_detection_direction(0)
    time.sleep(1)

    tello.takeoff()

    pad = tello.get_mission_pad_id()
    print("pad: ", pad)

    # noinspection PyUnreachableCode
    if not True:
        id = 1
        wait = 0.001
        tello.go_xyz_speed_mid(x=50, y=0, z=alt, speed=speed, mid=id)
        time.sleep(1)
        flycircle(tello, alt, speed, wait, id)
        tello.go_xyz_speed_mid(x=150, y=0, z=alt, speed=speed, mid=1)
        time.sleep(6)
        tello.go_xyz_speed_mid(x=50, y=0, z=alt, speed=speed, mid=2)
        time.sleep(1)
        id = 2
        flycircle(tello, alt, speed, wait, id)
        tello.go_xyz_speed_mid(x=-150, y=0, z=alt, speed=speed, mid=2)
        time.sleep(2)
        tello.go_xyz_speed_mid(x=0, y=0, z=alt, speed=speed, mid=1)
    else:
        for i in range(31):
           tello.go_xyz_speed_mid(x = i*5, y = 0, z = alt, speed = speed, mid = 1)
           pad = tello.get_mission_pad_id()
           print("pad: ", pad)
           if pad == 2:
               break
           #time.sleep(0.2)
        for i in range(31):
           tello.go_xyz_speed_mid(x = i*5, y = 0, z = alt, speed = speed, mid = 2)
           pad = tello.get_mission_pad_id()
           print("pad: ", pad)
           #time.sleep(0.2)

    tello.disable_mission_pads()
    tello.land()
    tello.turn_motor_on()
    time.sleep(7)
    tello.turn_motor_off()
    battery = tello.get_battery()
    print("                    BATTERY: ", battery, "%")
    tello.end()


def flycircle(tello, alt, speed, wait, idm):
    tello.go_xyz_speed_mid(x=50, y=0, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=48, y=13, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=43, y=25, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=35, y=35, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=25, y=43, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=13, y=48, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=0, y=50, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-13, y=48, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-25, y=43, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-35, y=35, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-43, y=25, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-48, y=13, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-50, y=0, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-48, y=-13, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-43, y=-25, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-35, y=-35, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-25, y=-43, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=-13, y=-48, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=0, y=-50, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=13, y=-48, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=25, y=-43, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=35, y=-35, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=43, y=-25, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=48, y=-13, z=alt, speed=speed, mid=idm)
    tello.go_xyz_speed_mid(x=50, y=0, z=alt, speed=speed, mid=idm)