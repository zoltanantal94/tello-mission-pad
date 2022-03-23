#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fly1, fly2, fly3, fly4, fly5, fly6, fly7, fly8

# pad distance in cm
import fly8

pad_dist = 140
# distance resolution
res = 6
# wait after command second
wait = 0.01
# fly speed in cm/s [10...100]
speed = 100
# fly altitude in cm [30...120]
alt = 100
# specify ip if Tello connected to WiFi router, else comment out
ip = ''  # '192.168.1.158'


def main():
    fly8.fly(pad_dist, alt, speed, wait, res, ip)


if __name__ == '__main__':
    main()
