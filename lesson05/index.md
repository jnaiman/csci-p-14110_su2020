---
layout: lesson
visible: true
---

# Lesson 5 - Kepler's Planets, Orbits in 3D & Other Python Solvers: Choose your own adventure

## Main Lecture Materials

Today we'll continue our simulations in 2D and we'll start thinking in 3D as well.  There are links to other solvers as well, but they are not required if you like the ```Hermite``` one!

Motivation: [Online 3D solar system interactive animation - https://theskylive.com/3dsolarsystem](https://theskylive.com/3dsolarsystem)

### Notes:

* [Part1_programming_readWriteData_keplersData_lesson05.pdf](Part1_programming_readWriteData_keplersData_lesson05.pdf)
* [Part2_planetsIn3D_lesson05.pdf](Part2_planetsIn3D_lesson05.pdf)


### Python Libraries

**Note: put these in the same directory as your .pynb notebooks.**

* <a href="hermite_library.py" download>hermite_library.py</a>
* <a href="convert_kepler_data.py" download>convert_kepler_data.py</a>
* <a href="convert_galaxy_data.py" download>convert_galaxy_data.py</a>

### Data

 * <a href="kepler11data.txt" download>Kepler 11 System Data</a>
 * <a href="kepler101data.txt" download>Kepler 101 System Data</a>

#### Galaxy snapshot files - different resolutions

* <a href="galaxySnaps/snap_001_fac1n3.txt" download>low res - galaxySnaps/snap_001_fac1n3.txt</a>
* <a href="galaxySnaps/snap_001_fac1n2.txt" download>mid res - galaxySnaps/snap_001_fac1n2.txt</a>
* <a href="galaxySnaps/snap_001_fac1n1.txt" download>high res - galaxySnaps/snap_001_fac1n1.txt</a>

### Reading

* [This paper by Piet Hut](hutspaper.pdf) talks about the evolution of numerical simulations in science.


## Other Python Solvers

You can check out these other solvers either now or come back to later in your life.  Order is in order of decreasing documentation/increasing difficulty.

### Rebound

[Rebound](https://rebound.readthedocs.io/en/latest/index.html) has both C and Python implementations to solve N-body equations with a variety of solvers.  There are other examples that include comments on the [Rebound examples page](https://rebound.readthedocs.io/en/latest/examples.html) if you find something of interest to explore there (make sure you use only the Python ones).

* The [Rebound Solar System Project](rebound_solar_system.html): uses the ```Rebound``` Python package to calculate up-to-date orbits of our own solar system.  Extension question deals with adding more planets.  

* The [Rebound Galaxies Project](rebound_galaxies.html): uses ```Rebound``` to integrate the motion of the galaxies presented in [Lesson 4](../lesson04/index.html).  Extensions include generating your own initial conditions with [pyICs](http://jakobherpich.github.io/pyICs/).

### SciPy

[SciPy](https://www.scipy.org/) is a package that does all kinds of neat scientific calculation stuffs.  Check out [this example](https://www.marksmath.org/classes/Spring2018NumericalAnalysis/code/nBody.html) of how to use it to make your own 2D N-body integrator.  How would you extend this to 3D?

### Others

There are many [GitHub repos for N-body Solvers in Python and other languages](https://github.com/topics/nbody) that you may want to check out.
