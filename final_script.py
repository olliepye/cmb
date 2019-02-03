# ----------------------------------------------------------------
# This was produced in paraview by:
# Oliver Pye (n9703977)
# o.pye@connect.qut.edu.au
# Queensland University of Technology
# November 2018
# ----------------------------------------------------------------

from astropy.io 
import fits
import matplotlib.pyplot as plt
import numpy as np
import healpy as hpy
from pylab import figure
import math as m
from mpl_toolkits.mplot3d import Axes3D
from astropy_healpix import HEALPix
from astropy.coordinates import Galactic

# Set the coordinate system
hp = HEALPix(nside=2048, order='nested', frame=Galactic())

# open the cmb dataset (obtained from the ESA Planck Legacy Archive)
data = fits.open('COM_CMB_IQU-commander-field-Int_2048_R2.01_full.fits')
print data[1].header


# plot the cmb
map1 = hpy.read_map('COM_CMB_IQU-commander-field-Int_2048_R2.01_full.fits', nest = False)

# set the nside resolution
nside = 2048

# store the cmb data in a ring structure
cmb_map = hpy.pixelfunc.ud_grade(map1, nside, order_in = 'RING', order_out = 'RING')

##### Convert to Coordinates #####

# initialise and pre allocate arrays for speed
x = np.zeros(len(cmb_map))
y = np.zeros(len(cmb_map))
z = np.zeros(len(cmb_map))
temp = cmb_map
coords = []
xf = np.zeros(len(cmb_map))
yf = np.zeros(len(cmb_map))
zf = np.zeros(len(cmb_map))

# get celestial coordinates
coords = hp.healpix_to_skycoord(np.arange(len(cmb_map)))
print coords

# store cartesian coordinates of each data point
# This is for a plain sphere with no height attribute
for i in range(0,len(cmb_map)):
    x[i], y[i], z[i] = hpy.pix2vec(nside, i, nest = False)
    r = 30
    theta = m.acos(z[i]/m.sqrt(m.pow(x[i],2)+m.pow(y[i],2)+m.pow(z[i],2)))
    phi = m.atan2(y[i],x[i])
    xf[i] = (r*m.sin(theta)*m.cos(phi))
    yf[i] = (r*m.sin(theta)*m.sin(phi))
    zf[i] = (r*m.cos(theta))

# open file to write data
file = open('plaindata.txt', 'w')
file.write('x y z temp\n')

# write the geometry
for i in range(0, len(cmb_map)):
    file.write('{} {} {} {}\n'.format(xf[i], yf[i], zf[i], cmb_map[i]))


# scale radius of spherical data to temperature values
# This is for the height map
temp_scaled = temp*10000
for i in range(0, len(cmb_map)):
    r = 30 + temp_scaled[i]
    theta = m.acos(z[i]/m.sqrt(m.pow(x[i],2)+m.pow(y[i],2)+m.pow(z[i],2)))
    phi = m.atan2(y[i],x[i])
    x[i] = r*m.sin(theta)*m.cos(phi)
    y[i] = r*m.sin(theta)*m.sin(phi)
    z[i] = r*m.cos(theta)

# export data to a txt file
file = open('height_data.txt', 'w')
file.write('x y z temp\n')

# write the geometry
for i in range(0, len(cmb_map)):
    file.write('{} {} {} {}\n'.format(x[i], y[i], z[i], temp[i]))
