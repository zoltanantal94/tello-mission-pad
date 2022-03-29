from djitellopy import Tello
import time
import math

path = [
    [3.25000000000000, 1.50000000000000],
    [3.21592582628907, 1.75881904510252],
    [3.11602540378444, 2],
    [2.95710678118655, 2.20710678118655],
    [2.75000000000000, 2.36602540378444],
    [2.50881904510252, 2.46592582628907],
    [2.25000000000000, 2.50000000000000],
    [1.99118095489748, 2.46592582628907],
    [1.75000000000000, 2.36602540378444],
    [1.54289321881345, 2.20710678118655],
    [1.38397459621556, 2.00000000000000],
    [1.28407417371093, 1.75881904510252],
    [1.25000000000000, 1.50000000000000],
    [1.28407417371093, 1.24118095489748],
    [1.38397459621556, 1.00000000000000],
    [1.54289321881345, 0.792893218813453],
    [1.75000000000000, 0.633974596215561],
    [1.99118095489748, 0.534074173710932],
    [2.25000000000000, 0.500000000000000],
    [2.50881904510252, 0.534074173710932],
    [2.75000000000000, 0.633974596215561],
    [2.95710678118655, 0.792893218813452],
    [3.11602540378444, 1.00000000000000],
    [3.21592582628907, 1.24118095489748],
    [3.25000000000000, 1.50000000000000]
]


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

    # code here
    pad = tello.get_mission_pad_id()
    while pad == -1:
        print("pad: ", pad)
        tello.send_rc_control(0, 10, 0, 0)
        pad = tello.get_mission_pad_id()
    tello.send_rc_control(0, 0, 0, 0)

    pad = current_pad = tello.get_mission_pad_id()

    for pos in path:
        pad = tello.get_mission_pad_id()
        if pad == -1:
            pad = current_pad
        else:
            current_pad = pad
        target = glob2loc_coord([pos[0], pos[1]], pad)
        # print(target)
        tello.go_xyz_speed_mid(int(target[0] * 100), int(target[1] * 100), alt, speed, pad)
        # print(pos)

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
    """ Convert global coordinates to local coordinate
        Arguments:
            global_coordinate: [x,y] in meter
            pad_id: 1~8
    """

    land = [1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8]
    local_delta_min = 100
    k_min = 0
    j = 0

    global_x = global_coordinate[0]
    global_y = global_coordinate[1]
    pad_coordinates = [
        [0.30, 1.50],  # 1.1,  1
        [0.90, 1.50],  # 1.2   2
        [1.50, 1.50],  # 1.3   3
        [2.10, 1.50],  # 1.4   4
        [0.30, 0.90],  # 2.1   3
        [0.90, 0.90],  # 2.2   4
        [1.50, 0.90],  # 2.3   5
        [2.10, 0.90],  # 2.4   6
        [0.30, 0.30],  # 3.1   5
        [0.90, 0.30],  # 3.2   6
        [1.50, 0.30],  # 3.3   7
        [2.10, 0.30]   # 3.4   8

    ]
    if pad_id == -1:
        raise Exception("pad_id must be greater than zero.")
    else:
        # same pad id, but different location

        land_pos = land
        possible_pads = land_pos.count(pad_id)

        for j in range(possible_pads):

            k = land_pos.index(pad_id)

            local_x1 = global_x - pad_coordinates[k][0]
            local_y1 = global_y - pad_coordinates[k][1]

            local_delta = math.sqrt((local_x1 ** 2) + (local_y1 ** 2))

            if local_delta < local_delta_min:
                local_delta_min = local_delta
                k_min = k

            land_pos[k] += 1

        local_x = global_x - pad_coordinates[k_min][0]
        local_y = global_y - pad_coordinates[k_min][1]

    return [local_x, local_y]


def glob2loc_coord_alt(global_coordinate, pad_id):
    """ Convert global coordinates to local coordinate
        Arguments:
            global_coordinate: [x,y] in meter
            pad_id: 1~8
    """
    global_x = global_coordinate[0]
    global_y = global_coordinate[1]
    pad_coordinates = [
        [[0.30, 1.50], 1],  # 1.1,  1
        [[0.90, 1.50], 2],  # 1.2   2
        [[1.50, 1.50], 3],  # 1.3   3
        [[2.10, 1.50], 4],  # 1.4   4
        [[0.30, 0.90], 3],  # 2.1   3
        [[0.90, 0.90], 4],  # 2.2   4
        [[1.50, 0.90], 5],  # 2.3   5
        [[2.10, 0.90], 6],  # 2.4   6
        [[0.30, 0.30], 5],  # 3.1   5
        [[0.90, 0.30], 6],  # 3.2   6
        [[1.50, 0.30], 7],  # 3.3   7
        [[2.10, 0.30], 8]   # 3.4   8
    ]
    if pad_id == -1:
        raise Exception("pad_id must be greater than zero.")
    else:
        possible_pads = []
        # select pads by id
        for p in pad_coordinates:
            if p[1] == pad_id:
                possible_pads.append(p[0])
        # calculate distances
        for p in possible_pads:
            p.append(
                math.sqrt(
                    (global_x - p[0]) ** 2 + (global_y - p[1]) ** 2
                )
            )
        # sort array by 3rd column, and return first row
        selected_pad = sorted(possible_pads, key=lambda x: x[2])[0]
        local_x = global_x - selected_pad[0]
        local_y = global_y - selected_pad[1]

    return [local_x, local_y]
