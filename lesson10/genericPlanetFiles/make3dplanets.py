# this is the library containing the making 3D planets stuff

# units
MassOfSun = 2e33 # g
MassOfJupiter = 1.898e30 # g
AUinCM = 1.496e13 # cm
kmincm = 1e5 # cm/km
G = 6.674e-8 # gravitational constant in cm^3 g^-1 s^-2

import os, shutil


import numpy as np
# I feel like maaaaayyyybeeee this started with: http://tf3dm.com/3d-model/photorealistic-earth-98256.html ?
# but I feel like it was even less licensed then this... anyway, from the larger website

def make3dplanets(SystemName, r_h, PlanetRadiusIn, output_planet_dir,  
                  generic_dir, colors = None, textures_dir = 'textureMaps/', 
                  texture_file=None, fnum = None, DistanceUnits=AUinCM, 
                 radii_units = 'Jupiter', distance_units = 'AU', verbose=True,
                  planet_radius_format = 'hermite', Nplot = 0, noVN = True):# , mass_units = 'Jupiter'): 
    # units for the origional generic file
    #Re = 6.371e8 # radius of earth in cm
    #Rarb = 100.0 # to look good on sketchfab, use this to scale things
    
    # have you linked to the right generic planet dir?
    if not os.path.isdir(generic_dir):
        print(generic_dir, ' is not a directory, check you have pointed to the correct generic planet directory!')
        import sys
        sys.exit()
        
    # texture maps
    if textures_dir == 'textureMaps/':
        textures_dir = generic_dir + 'textureMaps/'
        
        
    # check for highlevel output planet directory
    if not os.path.isdir(output_planet_dir):
        if verbose: print('making directory: ', output_planet_dir)
        os.makedirs(output_planet_dir)

    # wipe files if already files in a directory
    if os.path.isdir(output_planet_dir + SystemName + '/'):
        if verbose: print('Going to overwrite files in ', output_planet_dir + SystemName + '/')
        for filename in os.listdir(output_planet_dir + SystemName + '/'):
            file_path = os.path.join(output_planet_dir + SystemName + '/', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    
    # check units
    if (radii_units == 'Jupiter') and (distance_units == 'AU') :
        if verbose: print('Assuming radii are in Jupiter units except for the last particle which should have solar units, distances in AU... if not things are going to look weird!')
        
    # check planet formatting
    if planet_radius_format == 'hermite':
        PlanetLocation = np.zeros([len(PlanetRadiusIn), 3]) # initialize format
        # fill PlanetLocation with positions from r_h, our simulation data at timestep Nplot
        for p in range(0,len(PlanetRadiusIn)): # loop over each planet
            PlanetLocation[p,2] = r_h[p, 0, Nplot] # swapping z & x, and converting to cm
            PlanetLocation[p,0] = r_h[p, 1, Nplot] # swapping x & y, converting
            PlanetLocation[p,1] = r_h[p, 2, Nplot] # swapping y & z, converting
    else:
        PlanetLocation = r_h.copy()

        
    # rescale units
    PlanetLocation *= AUinCM # in cm
    PlanetRadius = np.array(PlanetRadiusIn).copy()
    PlanetRadius[:-1] = PlanetRadiusIn[:-1]*7.1492e7*100 # in cm
    PlanetRadius[-1] = PlanetRadiusIn[-1]*6.95700e8*100 # in cm

    # do some checking
    if (colors is None) and (texture_file is None):
        if verbose: print('no colors/textures specified -- generating random colors!')
        # generate random colors
        red,green,blue = np.random.random(len(PlanetRadius)), np.random.random(len(PlanetRadius)), np.random.random(len(PlanetRadius))
        # format properly
        colors = []
        for r,g,b in zip(red,green,blue):
            colors.append( (r,g,b) )
                 
        #print('Need to input list of colors or textures!!!  Exiting...')
        #import sys
        #sys.exit()
    

    # now, read in the generic obj file and read it in
    gobj_file = generic_dir + 'generic.obj'
    f = open(gobj_file)
    x = f.readlines()
    f.close()

    # find location and radius of generic file's planet
    v = []
    # also, count verticies, texture verticies, normal verticies
    v_count = 0
    vt_count = 0
    vn_count = 0
    for i in range(0, len(x)):
        l = x[i]
        #print(l)
        # search for verticies
        if l.find('v ') != -1:
            s = l.split(" ")
            #print(s)
            # convert
            if len(s) == 5:
                v.append( [float(s[2]), float(s[3]), float(s[4])] )
            elif len(s) == 4:
                v.append( [float(s[1]), float(s[2]), float(s[3])] )
            else:
                print('An unexpected format for verticies!')
            v_count += 1
        elif l.find('vt ') != -1:
            vt_count += 1
        elif l.find('vn ') != -1:
            vn_count += 1

    v = np.array(v)
    # now, get x/y/z min and max -> 1/2 of these is center
    gloc = np.array( [0.5*(v[0].max()-v[0].min())+v[0].min(),
                      0.5*(v[1].max()-v[1].min())+v[1].min(),
                      0.5*(v[2].max()-v[2].min())+v[2].min()] )

    # get radii -> an estimate there of since its not 100% spherical... for some reason :P
    gradius = np.mean( [v[0].max()-v[0].min(), v[1].max()-v[1].min(), v[2].max()-v[2].min()] )

    # now, we have to add in values for *each* planet
    y = []
    for p in range(0, len(PlanetLocation)):

        # first, write a little intro for each planet
        y.append('#\n')
        y.append('# object Sphere' + str(p).zfill(3) + '\n')
        y.append('#\n')

        # now, output a copy of the file
        # now loop and resize and then replace verticies
        for i in range(0, len(x)):
            l = x[i]
            # look for the call to the material file - only first loop!
            if l.find('mtllib') != -1:
                if p == 0:
                    #if fnum is None:
                    y.append('mtllib ' + SystemName + '.mtl\n')
                    #else:
                    #    y.append('mtllib ' + SystemName + str(fnum).zfill(4) + '.mtl\n')
            # search for verticies
            if l.find('v ') != -1:
                s = l.split(" ")
                # convert
                if len(s) == 5:
                    vert = [float(s[2]), float(s[3]), float(s[4])]
                elif len(s) == 4:
                    vert = [float(s[1]), float(s[2]), float(s[3])] 
                else:
                    print('An unexpected format for verticies!')
                #vert = [float(s[2]), float(s[3]), float(s[4])]
                # shift to zero
                vert[0] -= gloc[0]
                vert[1] -= gloc[1]
                vert[2] -= gloc[2]
                # now, scale... I think this does it right now?
                #vert[0] *= PlanetRadius[p]/(gradius*Re)#*Rarb
                #vert[1] *= PlanetRadius[p]/(gradius*Re)#*Rarb
                #vert[2] *= PlanetRadius[p]/(gradius*Re)#*Rarb
                vert[0] *= PlanetRadius[p]/gradius/DistanceUnits
                vert[1] *= PlanetRadius[p]/gradius/DistanceUnits
                vert[2] *= PlanetRadius[p]/gradius/DistanceUnits
                # now translate to new location, again, I think the units are ok?...
                #vert[0] += PlanetLocation[p,0]*DistanceFac#/(Re)*Rarb*DistanceFac
                #vert[1] += PlanetLocation[p,1]*DistanceFac#/(Re)*Rarb*DistanceFac
                #vert[2] += PlanetLocation[p,2]*DistanceFac#/(Re)*Rarb*DistanceFac
                vert[0] += PlanetLocation[p,0]/DistanceUnits
                vert[1] += PlanetLocation[p,1]/DistanceUnits
                vert[2] += PlanetLocation[p,2]/DistanceUnits
                y.append('v ' + str(vert[0]) + ' ' + str(vert[1]) + ' ' + str(vert[2]) + '\n')
            elif l.find('g ') != -1: # rename the group
                y.append('g Sphere' + str(p).zfill(3) + '\n')
            elif l.find('usemtl ') != -1: # say which material to use
                if p < 10:
                    y.append('usemtl ' + str(p).zfill(2) + '___Default\n')
                else:
                    y.append('usemtl ' + str(p).zfill(3) + '___Default\n')
            elif l.find('vt ') != -1: # only do vt for models with textures
                if texture_file is not None:
                    y.append(x[i])
                    #print('YO')
            elif l.find('f ') != -1: # we've found a face, and we gotta do fancy stuff
                s = l.split(" ")
                #if p == 0:
                #    print(s)
                sout = 'f '
                for k in range(0,len(s)):
                    if s[k].find('/') != -1:
                        ss = s[k].split('/')
                        if texture_file is not None:
                            sout += str( int(ss[0])+(p*v_count) ) + '/' + str( int(ss[1])+(p*vt_count) ) + '/' + str( int(ss[2])+(p*vn_count) ) + ' '
                        else:
                            sout += str( int(ss[0])+(p*v_count) ) + '//' + str( int(ss[2])+(p*vn_count) ) + ' '
                    #print(ss)
                #print(l)
                #print(sout)
                sout += '\n'
                y.append(sout)
            #elif l.find('s ') != -1: # so I don't think this actually makes a difference?
            #    y.append('s ' + str(p+1) + '\n')
            else:
                if (l.find('mtllib') == -1) and (l.find('#') == -1):
                    y.append(x[i])

    # now, write zee file
    # ok, first, look for planet directory and create if it does not
    outname = output_planet_dir + SystemName + '/'
    if not os.path.exists(outname):
        os.makedirs(outname)

    # write obj file
    if fnum is None:
        fname = SystemName + '.obj'
    else:
        fname = SystemName + str(fnum).zfill(4) + '.obj'
        
    f = open(outname+fname, 'w')
    for i in range(0,len(y)):
        if noVN:
            if 'vn ' not in y[i]:
                f.write(y[i].replace('\r\n', os.linesep))
        else:
            f.write(y[i].replace('\r\n', os.linesep))

    f.close()


    #xx = vv

    # now, lets write the material file and point to the new texture, copy new texture to
    # planet directory
    #
    # copy textures, if we have them
    if texture_file is not None:
        from shutil import copyfile
        for i in range(0,len(texture_file)):
            copyfile(textures_dir+texture_file[i], outname+texture_file[i])

    # now modify generic mtl file for our purposes
    f = open(generic_dir + 'generic.mtl')
    x = f.readlines()
    f.close()
    #y = x.copy()

    y = []
    for p in range(0, len(PlanetRadius)):
        for i in range(0, len(x)):
            l = x[i]
            if (l.find('map_Ka') != -1):
                if texture_file is not None:
                    y.append('	map_Ka ' + texture_file[p] + '\n')
            elif (l.find('map_Kd') != -1):
                if texture_file is not None:
                    y.append('	map_Kd ' + texture_file[p] + '\n')
            # use colors instead
            elif l.find('Kd ') != -1:
                if texture_file is None:
                    y.append('	Kd ' + str( colors[p][0] ) + ' ' + str( colors[p][1] ) + ' ' + str(colors[p][2]) + '\n')
            elif (l.find('newmtl ') != -1):
                if p < 10:
                    y.append('newmtl ' + str(p).zfill(2) + '___Default\n')
                else:
                    y.append('newmtl ' + str(p).zfill(3) + '___Default\n')
            else:
                y.append(x[i])


    # write mtl file
    #if fnum is None:
    f = open(outname + SystemName + '.mtl', 'w')
    #else:
    #    f = open(outname + SystemName + str(fnum).zfill(4) + '.mtl', 'w')
    for i in range(0,len(y)):
        f.write(y[i].replace('\r\n', os.linesep))

    f.close()
    return fname
