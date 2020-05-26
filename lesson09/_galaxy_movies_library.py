import numpy as np

# unit conversions
MassOfSun = 2e33 # g
MassOfJupiter = 1.898e30 # g
AUinCM = 1.496e13 # cm
kmincm = 1e5 # cm/km
G = 6.674e-8 # gravitational constant in cm^3 g^-1 s^-2

# NOTE: this is nearly the same as that for reading the planet data
def read_in_galaxy_data(save_file):
    inarr = np.genfromtxt(save_file, delimiter=',')
    # first, lets figure out what "N" (the number of planets) is
    N = (inarr.shape[1]-2)/(3+3+1) # the "6" = x/y/z + vx/vy/vz + part_type entries, 2 because: time, energy
    N = int(N)

    # create position, velocity, time and energy arrays
    r_res = np.zeros( [N, 3, inarr.shape[0]] )
    v_res = np.zeros( [N, 3, inarr.shape[0]] )
    t_h = np.zeros( [inarr.shape[0]] )
    e_h = np.zeros( [inarr.shape[0]] )
    part_type = np.zeros( [N, inarr.shape[0]] )

    # now fill
    for ti in range(0,len(t_h)):
        t_h[int(ti)] = inarr[int(ti),0]
        # fill position
        for j in range(0, N):
            r_res[j,0,int(ti)] = inarr[int(ti),1+j*3]
            r_res[j,1,int(ti)] = inarr[int(ti),1+j*3+1]
            r_res[j,2,int(ti)] = inarr[int(ti),1+j*3+2]
        # fill velocities
        for j in range(0, N):
            v_res[j,0,int(ti)] = inarr[int(ti),N*3+1+j*3]
            v_res[j,1,int(ti)] = inarr[int(ti),N*3+1+j*3+1]
            v_res[j,2,int(ti)] = inarr[int(ti),N*3+1+j*3+2]
            part_type[j,int(ti)] = inarr[int(ti), N*3*2+1+j]
        # finally, fill energy
        e_h[int(ti)] = inarr[int(ti), inarr.shape[1]-1]


    # for plotting also create the "average radius"
    l = 0.0
    for i in range(0,N):
        l += np.sqrt( r_res[i,0,:].max()**2 + r_res[i,1,:].max()**2 + r_res[i,2,:].max()**2 )

    # l = average distance
    l /= N

    return t_h, r_res, v_res, e_h, N, part_type
