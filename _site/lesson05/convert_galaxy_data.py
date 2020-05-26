import numpy as np

MassOfSun = 2e33 # g


def convert_galaxy_data(galaxy_data):
    # some notes on the galaxy files
    # Mass units:
    #m1 = 0.00104634 X 1e10 Msun
    #m2 = 0.00023252 X 1e10 Msun
    #coords are in kpc
    #velocities are in km/s
    
    galaxy_data['Ptype'][galaxy_data['Ptype']==1] = 0.00104634*1e10*MassOfSun # Msun
    galaxy_data['Ptype'][galaxy_data['Ptype']==2] = 0.00023252*1e10*MassOfSun # Msun
    
    # position: kpc -> AU
    galaxy_data['x'] *= 2.063e+8
    galaxy_data['y'] *= 2.063e+8
    galaxy_data['z'] *= 2.063e+8


    # to format expected by hermite solver
    masses = galaxy_data['Ptype']

    pos = np.zeros([len(galaxy_data),3])
    pos[:,0] = galaxy_data['x']
    pos[:,1] = galaxy_data['y']
    pos[:,2] = galaxy_data['z']
    
    vel = np.zeros([len(galaxy_data),3])
    vel[:,0] = galaxy_data['vx']
    vel[:,1] = galaxy_data['vy']
    vel[:,2] = galaxy_data['vz']

    return masses, pos, vel
