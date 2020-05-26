---
title: Optional - Galaxy Multibody Motion in 3D
layout: lecture
visible_lec: true
visible_n: true
---


## Three dimensional simulations

Options:
* add 3D component to planets
* galaxy simulations

notes: so, we will have a few options now - you can stick with planetary systems, if that is your jam, and start to move your simulations into 3d

we'll talk about other solvers for systems like Rebound that will do the solar system for us, but for now you can start adding these things *by hand*

---

## Three dimensional simulations - Galaxies

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/NGC_4414_%28NASA-med%29.jpg" width="800" />

notes: another natural type of 3D object is a galaxy

seen here is a "spiral" galaxy which is actually a relatively flat object - sort of like a disk in space

---

## Three dimensional simulations - Galaxies

<img src="http://en.es-static.us/upl/2019/01/galaxy-merger-mice-e1547088077596.jpg" width="800" />

notes: however, an important part of galaxy evolution are *galaxy mergers* which are very 3-dimensional events

---

## Three dimensional simulations - Galaxies

<img src="http://www2.iap.fr/users/volonter/m2.jpg" width="800" />

notes: its *these* sorts of things your every day computational physicist wants to be able to model

we won't get the types of galaxies we see today in the universe without them!

---

## Three dimensional simulations - Galaxies

<img src="https://milkyway.cs.rpi.edu/download/images/MW_cartoon.png" width="700" />

notes: galaxies are actually make up of a few different components - here the "bulge" which sits in the middle is greatly aggerated, as is the size of the sun

this is a cartoon of our own Milky Way galaxy and you can see some features - there are some "dwarf galaxies" around our Milky way, and there is a "stream" of material that has been stripped from one called Saggatarius Dwarf is it has collided with our Milky Way and is likely in the process of merging with our Milky Way

the "SDSS Data Wedge" just refers to the observational window of a particular mission that got to look at one of these "streams"

outside this there is a dark matter halo

---

## Three dimensional simulations - Galaxies

<img src="https://mcdonaldobservatory.org/sites/default/files/images/news/gallery/PIE-CHART.jpg" width="800" />

notes: this dark matter stuff is actually the dominate form of matter in the Universe

the stuff that makes up you and I comes from what we call "baryons" and is only roughly 4% of the Universe

There is also this stuff called "dark energy" that we are going to ignore for now, but its even more mysterious than dark matter!

---

## Three dimensional simulations - Galaxies

<img src="https://mk0astronomynow9oh6g.kinstacdn.com/wp-content/uploads/2015/11/Triangulum_II_620x400.jpg" width="600"/>

Dark matter is *dark* in the sense that we can't see it with light rays, but we can only *deduce* its existance from its gravitational effects on galaxies.

notes: dark matter gets its name because we cannot see it!

if we did it would look like the dominant form of matter in a galaxy as you can see from this image

we know it exists because of how it changes the rotation of stars in our galaxy - so we have to be sure to include it in our simulations!

---

## Three dimensional simulations - Galaxies

<iframe width="800" height="450" src="https://www.youtube.com/embed/RH7S_ajUniM?rel=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

notes: in reality, we need to include extra things like gas with which stars form, feedback from black holes, supernovae explosions, etc for a realistic simulation of a galaxy

here is an example from the group I've worked with called IllustrisTNG that modeled a big swath of the Universe to make a whole bunch of galaxies

*point out stuffs*

---

# Optional: Three dimensional simulations Galaxy in Python

notes: I'll go through a notebook that uses our Hermite solver to do some stuff, but I'll leave it up to the reader to actually change it to do the actual simulation.
