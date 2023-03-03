import pylunar
from datetime import datetime
# import ephem
import geopy
from geopy.geocoders import Nominatim
from math import degrees as deg
# from skyfield.api import load, Topos
# from skyfield.trigonometry import position_angle_of

LOCATION_NAME = "Hooke Park, UK"
YEAR = 2023
MONTH = 3
DAY = 6
HOUR = 22
MIN = 59

geolocator = Nominatim(user_agent="moon_sim")
location = geolocator.geocode(LOCATION_NAME)

time_t = datetime(YEAR, MONTH, DAY, HOUR, MIN)
print(time_t)

format = "%Y-%m-%d %H:%M"

def deg_to_dms(deg, pretty_print=None, ndp=4):
    """Convert from decimal degrees to degrees, minutes, seconds."""

    m, s = divmod(abs(deg)*3600, 60)
    d, m = divmod(m, 60)
    if deg < 0:
        d = -d
    d, m = int(d), int(m)

    if pretty_print:
        if pretty_print=='latitude':
            hemi = 'N' if d>=0 else 'S'
        elif pretty_print=='longitude':
            hemi = 'E' if d>=0 else 'W'
        else:
            hemi = '?'
        return '{d:d}° {m:d}′ {s:.{ndp:d}f}″ {hemi:1s}'.format(
                    d=abs(d), m=m, s=s, hemi=hemi, ndp=ndp)
    return d, m, s

if location:
   print(location.address)
   print((location.latitude, location.longitude))
   lat = deg_to_dms(location.latitude)
   lon = deg_to_dms(location.longitude)
   print(lat, lon)

   mi = pylunar.MoonInfo(lat, lon)
   mi.update((YEAR, MONTH, DAY, HOUR, MIN, 0))
   print(mi.age())
   print(mi.fractional_phase())
   print(mi.phase_name())
   print(mi.azimuth(), mi.altitude())
   print(mi.earth_distance())
   print(mi.magnitude())
   print(mi.next_four_phases())
   #print(dir(mi))
   #lc = pylunar.LunarFeatureContainer("Lunar")
   #lc.load()
   #print(len(lc))
   #lc.load(mi)
   #print(len(lc))
   #for feature in lc:
   #  print(feature)









# from __future__ import print_function, division
# import datetime
# from PyAstronomy import pyasl
# import numpy as np

# # Convert calendar date to JD
# # using the datetime package
# jd = datetime.datetime(2023, 3, 7)
# jd = pyasl.jdcnv(jd)
# jd = np.arange(jd, jd + 20, 1)
# # Calculate Moon positions
# res = pyasl.moonpos(jd)

# print("%15s  %8s  %8s  %11s  %8s  %8s" %
#       ("JD", "RA", "DEC", "DIST", "GEOLON", "GEOLAT"))
# print("%15s  %8s  %8s  %11s  %8s  %8s" %
#       ("[d]", "[deg]", "[deg]", "[km]", "[deg]", "[deg]"))
# for i in range(jd.size):
#     print("%15.4f  %8.4f  %8.4f  %11.4f  %8.4f  %8.4f" %
#           (jd[i], res[0][i], res[1][i], res[2][i], res[3][i], res[4][i]))