import numpy as np
from ..vector import vector, norm
import pupy as units

from .einstein_radius import einstein_radius

import matplotlib.pyplot as plt

def deflection_position(sources             : vector, 
						lens                : vector,
						mass_lens           : float  = units.Mbh,
						observer_distance   : float  = units.R0):

	# Ensure input is iterable
	if not isinstance(sources, list):
		sources = [sources]  

	p_images = []
	s_images = []
	e_radius = []


	#Observer vector
	observer = vector([0,0,observer_distance])
 	
	for source in sources:
		
		# Check if lens is closer to the observer
		rl = lens - observer
		rs = source - observer

		Dl = rl.norm()
		Ds = rs.norm()

		#If in front of lensing plane, no lensing happens
		if Ds < Dl:

			#No lensing
			sky_pos_source = np.array([-rs.x/rs.z, -rs.y/rs.z]) * units.rad_to_as * 1e3
			sky_pos_lens   = np.array([-rl.x/rl.z, -rl.y/rl.z]) * units.rad_to_as * 1e3
			
			p_images.append(sky_pos_source)
			s_images.append(sky_pos_source)
			e_radius.append(0.0)
			
			continue

		# Get sky positions of source and lens
		sky_pos_source = np.array([-rs.x/rs.z, -rs.y/rs.z]) * units.rad_to_as * 1e3
		sky_pos_lens   = np.array([-rl.x/rl.z, -rl.y/rl.z]) * units.rad_to_as * 1e3

		# Calculate angular distance vector
		bvec = sky_pos_source - sky_pos_lens
		beta = np.sqrt(np.sum(np.square(bvec)))
		n_vector = bvec / beta

		# Calculate deflection
		Rg = units.G * mass_lens / units.c**2
		Etheta = einstein_radius(Dl, (Ds - Dl), Rg=Rg, units='mas')
		
		Delta = np.sqrt(beta**2 + 4 * Etheta**2)

		theta_plus = 0.5 * (beta + Delta)
		theta_minus = 0.5 * (beta - Delta)

		p_image = sky_pos_lens + n_vector * theta_plus
		s_image = sky_pos_lens + n_vector * theta_minus

		p_images.append(p_image)
		s_images.append(s_image)
		e_radius.append(Etheta)

	return np.array(p_images), np.array(s_images), np.array(e_radius)
