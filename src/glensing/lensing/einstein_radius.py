import numpy as np
import pupy as units

def einstein_radius(
		D_l,
		D_ls,
		Rg = units.Rg,
		units = 'mas'):
	"""Returns the value of the einstein radius in the specified units

	Args:
		D_l (_float_): Distance from observer to lens in meters
		D_ls (_float_): Distance from lens to emitter in meters
		Rg (_float_, optional): Gravvitational radius of lens in meters. Defaults to units.Rg.
		units(_str_,optional): Units in which to return the radius. Defaults to mas.
	Returns:
		_float_: Einstein radius in mas
	"""
	

	if units == 'mas':
		return np.sqrt( (D_ls/(D_l*(D_l+D_ls))) * 4*Rg  )*(180/np.pi)*3600*1e3
	elif units == 'deg':
		return np.sqrt( (D_ls/(D_l*(D_l+D_ls))) * 4*Rg  )*(180/np.pi)
	elif units == 'as':
		return np.sqrt( (D_ls/(D_l*(D_l+D_ls))) * 4*Rg  )*(180/np.pi)*3600
	elif units == 'microas':
		return np.sqrt( (D_ls/(D_l*(D_l+D_ls))) * 4*Rg  )*(180/np.pi)*3600*1e6
	else:
		raise KeyError(
			f"{units} is not a valid argument units. It must be in ['deg','as','mas','microas']"
		)
	