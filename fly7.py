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

    # code here

    # mission end
    tello.disable_mission_pads()
    tello.land()
    tello.turn_motor_on()
    time.sleep(7)
    tello.turn_motor_off()
    battery = tello.get_battery()
    print("                    BATTERY: ", battery, "%")
    tello.end()


def glob2loc_coord(global_coordinate, pad_id):
    pad_coordinates = [[3, 2], [3, 2], [3, 2], [3, 2], [3, 2], [3, 2]]
    if pad_id == -1:
        return -1
    else:
        x = global_coordinate[0] - pad_coordinates[pad_id - 1][0]
        y = global_coordinate[1] - pad_coordinates[pad_id - 1][1]
    return [x, y]
