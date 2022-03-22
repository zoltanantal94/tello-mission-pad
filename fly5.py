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
    i = 0
    while not False:
        pad = tello.get_mission_pad_id()
        if pad != -1:
            tello.go_xyz_speed_mid(x=i, y=0, z=alt, speed=speed, mid=1)
            i += 1
        else:
            print("Result: ", i)
            break

    # mission end
    tello.disable_mission_pads()
    tello.land()
    tello.turn_motor_on()
    time.sleep(7)
    tello.turn_motor_off()
    battery = tello.get_battery()
    print("                    BATTERY: ", battery, "%")
    tello.end()
