import numpy as np

#Constants of nature
c = 3e8
G = 6.67e-11

#prefixes
deci  = 1e-1
centi = 1e-2
mili  = 1e-3
micro = 1e-6
nano  = 1e-9

kilo = 1e3
mega = 1e6
giga = 1e9

#Time quantities
minute  = 60
hour    = 60*minute
day     = 24*hour 
week    = 7*day
month   = 30*day
year    = 365*day

#Lenght units
kilometer           = 1e4

parsec              = 3.086e16
kiloparsec          = kilo*parsec
megaparsec          = mega*parsec

astronomical_unit   = 1.496e11

#Mass units
solar_mass = 2e30

#Angular conversion factors
rad_to_as = (180/np.pi)*60*60
as_to_rad = 1/rad_to_as
deg_to_rad = np.pi/180
rad_to_deg = 1/deg_to_rad

#galactic center units
Mbh = 4.297017427e6*solar_mass
R0  = 8277.09055*parsec
Rg  = G*Mbh/c**2 