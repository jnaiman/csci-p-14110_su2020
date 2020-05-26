---
title: Lecture 1, Part 4 - Kepler's Laws, Ellipses and Orbital Motion
layout: lecture
visible_lec: true
visible_n: true
---

## Euler's Method with Gravity

To summarize, we used Euler's Method to derive:

$v\_{i} = \frac{\Delta y\_i}{\Delta t} = \frac{y\_{i+1} - y\_{i}}{\Delta t} $

$a\_i = \frac{\Delta v\_i}{\Delta t} = \frac{v\_{i+1} - v\_i}{\Delta t}$

---

## Euler's Method with Gravity

To summarize, we used Euler's Method to derive:

$v\_{i} = \frac{\Delta y\_i}{\Delta t} = \frac{y\_{i+1} - y\_{i}}{\Delta t} $

$a\_i = \frac{\Delta v\_i}{\Delta t} = \frac{v\_{i+1} - v\_i}{\Delta t}$

we can swap these:

$y\_{i+1} = y\_i + v\_i \Delta t$

$v\_{i+1} = v\_i + a\_i \Delta t$

---

## Euler's Method with Gravity

To summarize, we used Euler's Method to derive:

$v\_{i} = \frac{\Delta y\_i}{\Delta t} = \frac{y\_{i+1} - y\_{i}}{\Delta t} $

$a\_i = \frac{\Delta v\_i}{\Delta t} = \frac{v\_{i+1} - v\_i}{\Delta t}$

we can swap these:

$y\_{i+1} = y\_i + v\_i \Delta t$

$v\_{i+1} = v\_i + a\_i \Delta t$

If we are at the surface of the Earth:

$a\_i = g = 9.8 \, m/s^2$

---

## Euler's Method with Gravity

If we use the 3D position vector, $\vec{r}$, as the vector from the Star to the Planet to generalize:

$\vec{r}\_{i+1} = \vec{r}\_i + \vec{v}\_i \Delta t$

$\vec{v}\_{i+1} = \vec{v}\_i + \vec{a}\_i \Delta t$

---

## Euler's Method with Gravity

If we use the 3D position vector, $\vec{r}$, as the vector from the Star to the Planet to generalize:

$\vec{r}\_{i+1} = \vec{r}\_i + \vec{v}\_i \Delta t$

$\vec{v}\_{i+1} = \vec{v}\_i + \vec{a}\_i \Delta t$

If we are at the surface of the Earth:

$\vec{a}\_i = g = 9.8 \, m/s^2$ pointed toward the center of the Earth

---

## Euler's Method with Gravity

If we use the 3D position vector, $\vec{r}$, as the vector from the Star to the Planet to generalize:

$\vec{r}\_{i+1} = \vec{r}\_i + \vec{v}\_i \Delta t$

$\vec{v}\_{i+1} = \vec{v}\_i + \vec{a}\_i \Delta t$

If we are at the surface of the Earth:

$\vec{a}\_i = g = 9.8 \, m/s^2$ pointed toward the center of the Earth

For planets around stars we can use $\vec{F} = m\_{planet} \vec{a}$ and Newton's law of gravitation to derive:

$\vec{a} = - \frac{G M\_{star}}{| \vec{r} |^2}$

---

## Euler's Method with Gravity

If we use the 3D position vector, $\vec{r}$, as the vector from the Star to the Planet to generalize:

$\vec{r}\_{i+1} = \vec{r}\_i + \vec{v}\_i \Delta t$

$\vec{v}\_{i+1} = \vec{v}\_i + \vec{a}\_i \Delta t$

If we are at the surface of the Earth:

$\vec{a}\_i = g = 9.8 \, m/s^2$ pointed toward the center of the Earth

For planets around stars we can use $\vec{F} = m\_{planet} \vec{a}$ and Newton's law of gravitation to derive:

$\vec{a} = - \frac{G M\_{star}}{| \vec{r} |^2}$ or, discretized $\vec{a}\_{i} = - \frac{G M\_{star}}{| \vec{r\_{i}} |^2}$


---

## Euler's Method with Gravity

If we use the 3D position vector, $\vec{r}$, as the vector from the Star to the Planet to generalize:

$\vec{r}\_{i+1} = \vec{r}\_i + \vec{v}\_i \Delta t$

$\vec{v}\_{i+1} = \vec{v}\_i + \vec{a}\_i \Delta t$

If we are at the surface of the Earth:

$\vec{a}\_i = g = 9.8 \, m/s^2$ pointed toward the center of the Earth

For planets around stars we can use $\vec{F} = m\_{planet} \vec{a}$ and Newton's law of gravitation to derive:

$\vec{a} = - \frac{G M\_{star}}{| \vec{r} |^2}$ or, discretized $\vec{a}\_{i} = - \frac{G M\_{star}}{| \vec{r\_{i}} |^2}$

**We can go ahead and use Python to calculate orbits, but how do we know they are correct?**

notes: we need to use a few more law's called "Kepler's Laws" to help us generate analytical orbits that we can check our simulations against


---

## Kepler's Laws

<img src="http://slideplayer.com/slide/2878322/10/images/1/JOHANNES+KEPLER+BORN+IN+WEIL+DER+STADT+NEAR+PRESENT+DAY+STUTTGART.+HE+WAS+BORN+PREMATURELY+AND+WAS+PHYSICALLY+WEAK..jpg" width="800" />

notes: now we'll chat about Kepler's laws, kepler was another "big deal" in Astronomy - and along with Tycho Brahe did a lot of work on orbital motion

---

## Kepler's Laws

**Kepler's Law #1**: All planets move about the Sun in elliptical orbits, having the Sun as one of the foci.

<img src="http://en.es-static.us/upl/2016/12/kepler-1st-law.gif" width="500" />

notes: so we've been talking a lot about circular motion and how gravity might allow for objects to move around objects like the earth in a circular fashion

Now we're going to start thinking about orbits in reality - it turns out these are actually ellipses, not circles. Why is this?

---

## A Quick Physics Crash Course: Angular Motion, cont

<img src="https://s3-us-west-2.amazonaws.com/courses-images-archive-read-only/wp-content/uploads/sites/222/2014/12/20103410/Figure_11_01_03a.jpg" width="500" />

notes: lets think back to this here - before we were thinking of uniform motion - i.e. constant angular veloctiy

But what happens if we add a little bit of tangential acceleration - for example if we have a rocket we turn on its booster tangential to the motion?

Elliptical motion!  The orbit can still be *bound* i.e. it won't fly off into infinity, but now your orbit is no longular circular

---

## A Quick Physics Crash Course: Angular Motion, cont

Fun aside: Non-uniform orbital motion can be used to transfer between to circular orbits

<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Animation_of_InSight_trajectory.gif/440px-Animation_of_InSight_trajectory.gif" width="400">

Legend:
 * Inner orbit = Earth
 * Outer orbit = Mars
 * Red dot = Insight 


This is called a [Hohmann transfer orbit](https://en.wikipedia.org/wiki/Hohmann_transfer_orbit) and it is pretty cool.

notes: a Hohmann transfer actually uses the "alightnment" of the 2 larger bodies - in this case earth and mars to use the lowest amount of rocket fuel possible

you can see for a period of time that Insight actually has an ellpitical instead of circular orbit

---

## Kepler's Laws

**Kepler's Law #1**: All planets move about ~~the Sun~~ their host star in elliptical orbits, having the ~~Sun~~ host star as one of the foci.

<img src="http://en.es-static.us/upl/2016/12/kepler-1st-law.gif" width="500" />

notes: this brings us back to Kepler's first law which should really be updated for the fact that we now have found so many exoplanets outside our solar system!


---

## Kepler's Laws $\rightarrow$ Ellipses and Conic Sections

**Kepler's Law #1**: All planets move about ~~the Sun~~ their host star in elliptical orbits, having the ~~Sun~~ host star as one of the foci.

<img src="http://en.es-static.us/upl/2016/12/kepler-1st-law.gif" width="500" />

Ok, but what is an ellipse?

notes: this brings us back to Kepler's first law which should really be updated for the fact that we now have found so many exoplanets outside our solar system!

---

## Ellipses

Planetary orbits follow **elliptical** paths.

What is an ellipse?

<img src="https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/896/2016/11/03202213/CNX_Precalc_Figure_10_01_0032.jpg" width="400"/>

notes: the first way we can think of an ellipse is how we can draw one by hand: if you take 2 tacks and a length of string, you can draw an ellipse by placing a pencil in the string and drawing around the tacks

think about - how does it look if the tacks are very close together?  What about far apart?

---

## Ellipses

There is a lot of other terminology you might run into with ellipses.

<img src="https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/896/2016/11/03202215/CNX_Precalc_Figure_10_01_0042.jpg" width="600"/>

notes: for example, we call the largest axis of this object the "major" axis and the smaller axis the "minor" axis

"major" is usually denoted with an "a" and "minor" with a "b" but you should always double check this

There are 2 focuses or "foci" that are basically where we would put the tacks if we were drawing this by hand

---

## Ellipses

There are many ways to write this ellipse shape as a formula.  In cartesian, or rectangular coordinates:

$$ \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

<img src="https://www.mathsisfun.com/geometry/images/ellipse-axes.svg" width="600"/>

notes: these are for ellipses that are centered at the origin

How does this equation change if the center of the ellipse is at a different position?  Lets say x0 and y0?

---

## Ellipses

Non-centered ellipse:

$$ \frac{(x-x\_0)^2}{a^2} + \frac{(y-y\_0)^2}{b^2} = 1$$

---

## Ellipses

Non-centered ellipse:

$$ \frac{(x-x\_0)^2}{a^2} + \frac{(y-y\_0)^2}{b^2} = 1$$

Area of an ellipse:

$$ A= \pi a b $$

---

## Ellipses as conic sections

<img src="https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/896/2016/11/03202211/CNX_Precalc_Figure_10_01_0022.jpg" width="800"/>

notes: ellipses are actually part of a family of geometrical objects called "conic sections" that can be created by taking different sorts of slices through 3D cones. 

The other 2 objects are parabolas and hyperbolas.  There are some orbits that follow these trajectories instead of ellipses.  These represent "unbound orbits" because, as you can see, they are paths that never return to were they started - only ellipses represent orbits that actually, well, orbit, instead of slingshoting off somewhere.

More on this idea a bit later.

---

# To Python for ellipse drawing practice!

---

## Kepler's Laws $\rightarrow$ Ellipses and Conic Sections

**Kepler's Law #1**: All planets move about ~~the Sun~~ their host star in elliptical orbits, having the ~~Sun~~ host star as one of the foci.

<img src="http://en.es-static.us/upl/2016/12/kepler-1st-law.gif" width="500" />

Ok, but what is an ellipse? Now we know!

notes: now that we know a bit more about what ellipses are, lets go back to looking at Kepler's laws

---

## Kepler's Laws $\rightarrow$ Ellipses and Conic Sections

**Kepler's Law #2**: A line that connects a planet to the sun sweeps out equal areas in equal times.

<img src="https://github.com/katiebreivik/Keplers_Laws/raw/b0418d7c75582692b7cb0e03d7cab687c5b1ae4c/KeplersSecondLaw.jpg" width="500" />

notes: there are two other of Kepler's laws 

---

## Kepler's Laws $\rightarrow$ Ellipses and Conic Sections

**Kepler's Law #2**: A line that connects a planet to the sun sweeps out equal areas in equal times.

<img src="http://ffden-2.phys.uaf.edu/webproj/211_fall_2016/Mikayla_Grunin/mikayla_grunin/Photo3.html.gif" width="500" />

notes: this one, law #2, tells us something about how fast the planet moves at different parts of its orbit - near its aphelion (near the sun) it goes really fast, and at the furthest part of its orbit, perhelion it goes very slow

---

## Kepler's Laws $\rightarrow$ Ellipses and Conic Sections

**Kepler's Law #3**: The square of the period of any planet is proportional to the cube of the semimajor axis of its orbit.

<img src="https://github.com/katiebreivik/Keplers_Laws/raw/b0418d7c75582692b7cb0e03d7cab687c5b1ae4c/KeplersThirdLaw.gif" width="800" />

notes: there are two other of Kepler's laws

---

## Kepler's Laws for Multi-body systems?

<img src="https://i.stack.imgur.com/bY8GT.gif" width="600" />

notes: while these laws don't hold for multi-body system, when there is a planetary system with a large sun, and the rest of the planets have masses much smaller than this sun

in this case, as a first brush, we can assume that each planet is orbiting a central star and figure out orbits that way

Later, we can use this to compare solutions we generate using Euler's method to what we find here

---

## Kepler's Laws for Multi-body systems?

For one massive star at the center of the system, orbits can be written as:

$$ r(\theta) = \frac{a (1-e^2)}{1 + e cos(\theta)} $$

$$ e = \sqrt{1 - \frac{b^2}{a^2}} $$

---

## Kepler's Laws for Multi-body systems?

For one massive star at the center of the system, orbits can be written as:

$$ r(\theta) = \frac{a (1-e^2)}{1 + e cos(\theta)} $$

$$ e = \sqrt{1 - \frac{b^2}{a^2}} $$

Note the limits on $e$:
 * if $b = 0$, $e = 1$ $\rightarrow$ this is a parabola
 * if $a = b$, $e = 0$ $\rightarrow$ this is a perfect circle

---

## Kepler's Laws for Multi-body systems?

For one massive star at the center of the system, orbits can be written as:

$$ r(\theta) = \frac{a (1-e^2)}{1 + e cos(\theta)} $$

$$ e = \sqrt{1 - \frac{b^2}{a^2}} $$

Note the limits on $e$:
 * if $b = 0$, $e = 1$ $\rightarrow$ this is a parabola
 * if $a = b$, $e = 0$ $\rightarrow$ this is a perfect circle
 
Beware: $r(\theta)$ is trivial, but $r(t)$ and $\theta(t)$ are not easy to calculate and require numerical methods!

---

## Kepler's Laws for Multi-body systems?

For one massive star at the center of the system, orbits can be written as:

$ r(\theta) = \frac{a (1-e^2)}{1 + e cos(\theta)} $, $ e = \sqrt{1 - \frac{b^2}{a^2}} $

---

## Kepler's Laws for Multi-body systems?

For one massive star at the center of the system, orbits can be written as:

$ r(\theta) = \frac{a (1-e^2)}{1 + e cos(\theta)} $, $ e = \sqrt{1 - \frac{b^2}{a^2}} $

Recall:

$\vec{r}\_{i+1} = \vec{r}\_i + \vec{v}\_i \Delta t$

$\vec{v}\_{i+1} = \vec{v}\_i + \vec{a}\_i \Delta t$ = $\vec{v}\_i - \frac{G M\_{star}}{| \vec{r\_{i}} |^2} \Delta t$


---

## Kepler's Laws for Multi-body systems?

For one massive star at the center of the system, orbits can be written as:

$ r(\theta) = \frac{a (1-e^2)}{1 + e cos(\theta)} $, $ e = \sqrt{1 - \frac{b^2}{a^2}} $

Recall:

$\vec{r}\_{i+1} = \vec{r}\_i + \vec{v}\_i \Delta t$

$\vec{v}\_{i+1} = \vec{v}\_i + \vec{a}\_i \Delta t$ = $\vec{v}\_i - \frac{G M\_{star}}{| \vec{r\_{i}} |^2} \Delta t$

So we need initial $\vec{r}\_0$ and $\vec{v}\_0$ to solve these equations.

---

## Kepler's Laws for Multi-body systems?

So we need initial $\vec{r}\_0$ and $\vec{v}\_0$ to solve these equations.  We'll use $\vec{r}\_0 = \vec{r}\_p$ and $\vec{v}\_0 = \vec{v}\_p$.

<img src="http://ffden-2.phys.uaf.edu/webproj/211_fall_2016/Mikayla_Grunin/mikayla_grunin/Photo3.html.gif" width="500" />


---

## Kepler's Laws for Multi-body systems?

So we need initial $\vec{r}\_0$ and $\vec{v}\_0$ to solve these equations.  We'll use $\vec{r}\_0 = \vec{r}\_p$ and $\vec{v}\_0 = \vec{v}\_p$.

<img src="http://ffden-2.phys.uaf.edu/webproj/211_fall_2016/Mikayla_Grunin/mikayla_grunin/Photo3.html.gif" width="500" />

We can use a few more relations for $e$ and position and velocity at perihelion, $r\_p$ and $v\_p$:

$ e = \frac{ r\_p v\_p^2 }{G (m\_{planet} + M\_{star} )} - 1 \approx \frac{ r\_p v\_p^2 }{G M\_{star} } - 1 $, $ a = \frac{r\_p}{1 - e} $

notes: here, I'm using shorthand $| \vec{r}\_p | = r\_p$

---

# By their powers combined:
## Orbital motion solutions with Python (finally)
