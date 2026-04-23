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

observations = [
      {"name": "sirius", "alt": 30.0, "ra":6.752, "dec": -16.716},
      {"name": "betelgeuse", "alt": 45.0, "ra": 5.9195, "dec": 7.407}
]

#===

#initialization

ts = load.timescale()
t = ts.utc (year, month, day, hour, minute, second)
planets = load(' de421.bsp ')
earth = planets[' earth ']

#calculate error functions

def compute_alt (lat, lon, star)

def error_function (params)


#solve your position
initial_guess = [0, 0]
result = minimize (error_function, initial_guess, method = ' Nelder-Mead ')
lat, lon = result.x

#output

print