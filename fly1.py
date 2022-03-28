import math
from djitellopy import Tello
import time


def fly(pad_dist, alt, speed, wait, res, ip):
    # Camera preparation
    print(globals())
    if 'ip' in locals() and ip != '':
        tello = Tello(ip, 3)
    else:
        tello = Tello()
    tello.connect()
    # ip: 192.168.10.2 - PC     <--> 192.168.10.1 - Tello
    # tello.connect_to_wifi('SSID','password')
    # exit(0)
    battery = tello.get_battery()
    print("                    BATTERY: ", battery, "%")

    tello.enable_mission_pads()
    tello.set_mission_pad_detection_direction(0)
    time.sleep(1)

    tello.takeoff()
    # print("press any key")
    # input()

    pad = tello.get_mission_pad_id()
    print("pad: ", pad)

    # print("press any key")
    # input()
    i = 0

    for pad_id in range(1, 5):
        for set_y_pos in reversed(
                range(math.floor(-pad_dist / 2), math.floor(pad_dist / 2), math.floor(pad_dist / res))):
            try:
                while pad != pad_id:
                    pad = tello.get_mission_pad_id()
                tello.go_xyz_speed_mid(0, int(set_y_pos), alt, speed, pad_id)
            except tello.TelloException:
                print("No valid IMU")
                continue
            time.sleep(wait)
            pad = tello.get_mission_pad_id()
            x = tello.get_mission_pad_distance_x()
            y = tello.get_mission_pad_distance_y()
            z = tello.get_mission_pad_distance_z()
            battery = tello.get_battery()
            print('pad: ', pad, ', x:', x, ', y:', y, ', z:', z, ', bat: ', battery, '%')
        if pad_id < 4:
            tello.go_xyz_speed_yaw_mid(0, 0, alt, speed, 0, pad_id, pad_id + 1)

    # print("press any key for END")
    # input()

    tello.disable_mission_pads()
    tello.land()
    tello.turn_motor_on()
    time.sleep(7)
    tello.turn_motor_off()
    tello.end()
