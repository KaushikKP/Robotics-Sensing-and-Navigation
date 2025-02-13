#!/usr/bin/env python
# -*- coding: utf-8 -*-
# for GPS

import sys
import lcm
import time
import serial
from exlcm import gps_message
#import seabed_lcm


class Gps(object):
    def __init__(self, port_name):
        self.port = serial.Serial(port_name, 4800, timeout=1.)  # 9600-N-8-1
        self.lcm = lcm.LCM("udpm://?ttl=12")
        self.packet = gps_message()
        #while True:
        print 'GPS: Initialization'


    def readloop(self):
        while True:
            line = self.port.readline()

            gpsval = line.split(',')
            if gpsval[0]=="$GPGGA":
                  print gpsval
                  self.packet.time = gpsval[1]
                  if len(gpsval)>2:
                    self.packet.latitude = gpsval[2]
                  if len(gpsval)>3:
                    self.packet.lat_direction = gpsval[3]
                  if len(gpsval)>4:
                    self.packet.longitude = gpsval[4]
                  if len(gpsval)>5:
                    self.packet.long_direction = gpsval[5]
                  if len(gpsval)>6:
                    self.packet.altitude = gpsval[6]
                  self.lcm.publish("GPS", self.packet.encode())

 
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s <serial_port>\n" % sys.argv[0]
        sys.exit(0)
    mygps = Gps(sys.argv[1])
    mygps.readloop()
