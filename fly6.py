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

    while pad == -1:

        while tello.get_height() <= 95:
            tello.send_rc_control(0, 0, 10, 0)

        pad = tello.get_mission_pad_id()

        tello.send_rc_control(0, 0, 0, 0)

    x_data = tello.get_mission_pad_distance_x()
    y_data = tello.get_mission_pad_distance_y()
    z_data = tello.get_mission_pad_distance_z()
    _list = [x_data, y_data, z_data]
    print("Result: ", _list)

    # mission end
    tello.disable_mission_pads()
    tello.land()
    tello.turn_motor_on()
    time.sleep(7)
    tello.turn_motor_off()
    battery = tello.get_battery()
    print("                    BATTERY: ", battery, "%")

    f = open('result.txt', 'a')
    f.write('A megtett távolság: {}\n'.format(_list))
    f.close()

    tello.end()
