#!/usr/bin/env python

from math import *

import xml.etree.ElementTree as ET
import dateutil.parser
import datetime
import time

prevlat = None
prevlon = None
totaldist = 0.0
prevgarmindist = None

tree = ET.parse("activity.tcx")

nodes = tree.findall(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Trackpoint")

print "#time,lat,lon,hleg,htotal,gleg,gtotal,legdiff,totdiff"
for n in nodes:
    timeelem = n.find(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Time")
    distelem = n.find(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}DistanceMeters")
    poselem = n.find(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Position")
    if poselem is not None:
        latelem = poselem.find(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}LatitudeDegrees")
        lonelem = poselem.find(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}LongitudeDegrees")
        latd = float(latelem.text)
        lond = float(lonelem.text)
        lat = radians(latd)
        lon = radians(lond)
        garmindist = (float(distelem.text)) / 1000.0

        if prevlat is not None and prevlon is not None:
            dlat = lat - prevlat
            dlon = lon - prevlon
            a = sin(dlat/2)**2 + cos(prevlat) * cos(lat) * sin(dlon/2)**2
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            leglen = 6371 * c
            totaldist = totaldist + leglen
            garminleg = garmindist - prevgarmindist
            garminlegdelta = ((garminleg-leglen)/leglen) * 100.0
            garmintotaldelta = ((garmindist-totaldist)/totaldist) * 100.0
            timeobj = dateutil.parser.parse(timeelem.text)
            timestamp = time.mktime(timeobj.timetuple())
            print "%d,%f,%f,%f,%f,%f,%f,%f,%f" % \
                (timestamp, latd, lond, leglen, totaldist, garminleg,
                 garmindist, garminlegdelta, garmintotaldelta)
        prevlat = lat
        prevlon = lon
        prevgarmindist = garmindist
