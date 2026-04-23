#celestical_nav.py
from skyfield.api import load, Star, Topos
from scripy.optimize import minimize
import numpyas np

#===
#input

#UTC time
year, month, day = 2026,4, 22  #yy,mm, dd
hour, minute, second = 12,0, 0  #hh, mm, ss

#observation datas
