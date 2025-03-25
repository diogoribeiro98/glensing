from setuptools import setup, find_packages

setup(name='glensing',
      version='0.0',
      author='Diogo Ribeiro',
      description='Gravitational Lensing Modelling',
        url='https://github.com/diogoribeiro98/glensing',
      python_requires='>=3.7',
      packages=['glensing'],
      package_dir={'':'src'},
      include_package_data=False,
      install_requires=[
        'matplotlib',
        'numpy',
        'emcee',
        'lmfit'    
		]
)

