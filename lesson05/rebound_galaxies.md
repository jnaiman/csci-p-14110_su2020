---
layout: lesson
visible: false
---

# Rebound Galaxies

**Note: this example has less documentation and therefore might be a tougher problem.**

First install with pip: add ```!pip install rebound``` in your jupyter notebook. Then you should be able to do ```import rebound``` in your notebook to import this package. See this website for more info about installing and testing rebound.

Begin by going through the solar system example as a warm up: <a href="https://rebound.readthedocs.io/en/latest/ipython/Horizons.html">NASA Horizon interface</a> and the <a href="https://rebound.readthedocs.io/en/latest/ipython/Starman.html">Starman</a> example.  This pings the NASA Horizon telescope to get the current positions of all the planets.

Once you have a feel for the ```Rebound``` solver, translate the galaxy initial conditions found on the [Lesson 4 page](../lesson04/index.html) into units that ```Rebound``` expects.  For hints you can check out some [old code right here](http://www.astroblend.com/ba2016/code/day4/rebound_galaxyMerger_jill.py).

EXTENSION: Download and use [PyICs](http://jakobherpich.github.io/pyICs/) to generate your own initial galaxy particle positions.
