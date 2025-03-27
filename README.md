# Glensing

Glensing is a python package for fitting gravitational lensing events.

## Installation

To use Glensing, clone the git repository to your local machine or server using
```bash
git clone https://github.com/diogoribeiro98/GravityPy.git
```
and, from within the downloaded folder, install it with pip
```bash
pip install .
```
We advise the use of a virtual environment manager such as [conda](https://conda.io).

## Usage

The core function of the pakcage is the `deflection_position` function that has the signature

```python
p_image, s_image, e_radius = deflection_position(sources, lens, mass_lens, observer_distance)
```

where `sources` represents the position of your lensed source, `lens` that of the lensing object and `mass_lens` its mass. Similarly, one need to specify the distance to the observer. All quantities need to be provided in SI units. The `source` argument can also be a list of positions.

> **NOTE**  
> The observer is always placed in the positive z-direction

All positions need to be provided as a `vector` class on which the the function is based. As an example, say we want to specify the position in astronomical units:

```python
from glensing.vector import vector

au = 149597870700
position = vector([10,10,-10])*au
```
Here is a complete working example, calculating the deflection angle of a star by a solar mass object at 1 kiloparsec from the observer:

```python
from glensing import deflection_position
from glensing.vector import vector

#Scales
au = 149597870700
parsec = 206264*au
solar_mass = 2e30
distance_to_observer = 1e4*parsec

#Place lens at origin
lens = vector([0,0,0])

#Define source position with respect to lens
src =  vector([10,10,-10])*au

#Calculate the primary and secondary images
p_image, s_image, e_radius = deflection_position(
sources = src,
lens   = vector([0.,0.,0.]),
mass_lens=solar_mass,
observer_distance= distance_to_observer
)

print(f'RA:  {p_image[0,0]} mas')
print(f'Dec: {p_image[0,1]} mas')
```