---
title: Lecture 2, Part 2 - stuff
layout: lecture
visible_lec: true
visible_n: true
---

## Recall: One Star + Planetary System

1. Gravitational Force - Newton's Laws
1. Circular motion
1. Kepler's Laws - elliptical orbits

---

## Recall: One Star + Planetary System

For one massive star at the center of the system, orbits can be written as:

$ r(\theta) = \frac{a (1-e^2)}{1 + e cos(\theta)} $, $ e = \sqrt{1 - \frac{b^2}{a^2}} $

Recall:

$\vec{r}\_{i+1} = \vec{r}\_i + \vec{v}\_i \Delta t$

$\vec{v}\_{i+1} = \vec{v}\_i + \vec{a}\_i \Delta t$ = $\vec{v}\_i - \frac{G M\_{star}}{| \vec{r\_{i}} |^2} \Delta t$

$ e = \frac{ r\_p v\_p^2 }{G (m\_{planet} + M\_{star} )} - 1 \approx \frac{ r\_p v\_p^2 }{G M\_{star} } - 1 $, $ a = \frac{r\_p}{1 - e} $

notes: here, I'm using shorthand $| \vec{r}\_p | = r\_p$

---

## Two Body Motion for any masses

What if $M\_{star} \approx M\_{planet}$ - i.e. we have two stars orbiting each other.

Planetary orbits:

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Orbit4.gif" width="400"/>

notes: in detail, we've been basically assuming the star's mass is so much bigger than the planet's mass so we can assume there is no motion of the star

in reality even in planet-star systems, the star gets a little "wiggle" from more massive planets

this is actually how we can discover exoplanets!

---

## Two Body Motion for any masses

<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Orbit4.gif" width="400"/>

<img align="left" src="https://upload.wikimedia.org/wikipedia/commons/7/73/Orbit1.gif" width="400" />

notes: if we have two similar mass things, they actually orbit their common **center of mass**

---

## Two Body Motion for any masses

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0e/Orbit5.gif" width="600" />

$$ R\_{CM} = \frac{1}{M\_1 + M\_2} (M\_1 \vec{r\_1} + M\_2 \vec{r\_2} ) $$

notes: in most binary systems, there is actually ellptical motion, but around the common center of mass!

---

## Two Body Motion for any masses

**Kepler's Law #1**: Elliptical motion around center of mass

<img src="http://hosting.astro.cornell.edu/academics/courses/astro201/images/mbin1.gif" width="500" />

---

## Two Body Motion for any masses

**Kepler's Law #2**: Equal areas in equal times - for each star

<img src="http://hosting.astro.cornell.edu/academics/courses/astro201/images/mbin2.gif" width="500" />

<img src="http://hosting.astro.cornell.edu/academics/courses/astro201/images/mbin3.gif" width="500" />

---

## Two Body Motion for any masses

**Kepler's Law #3**: Period semi-major axis relationships are *almost* the same

$$ T^2 = \frac{4 \pi^2 a^3}{G (M\_1 + M\_2)} $$

where $a$ is now the mean seperation between the two masses.

<!--$$ T^2 = \frac{4 \pi ^2}{\mu\_1}a\_1^3, \, \, \, T^2 = \frac{4 \pi^2}{\mu\_2} a\_2^3 $$

where

$$ \mu\_1 = \frac{G M\_2^3}{(M\_1 + M\_2)^2}, \, \, \,  \mu\_2 = \frac{G M\_1^3}{(M\_1 + M\_2)^2} $$-->

---

## Two Body Motion for any masses

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0e/Orbit5.gif" width="600" />

How can we check our work?
 * analytical solutions - gets a little more complicated
 * **conserved quantities**
 
notes: we can certainly use an analytical solution again, the math gets slightly more complicated, but it is doable

but we should probably develop other methods - when we move to more than 2 bodys, there are no analytical solutions!

we'll look at some things called conserved quantities - these are things that should stay the same during the entire motion

---

## Conserved Quantities: Energy and Momentum

For a two body system:

**Energy**

$$ E = \frac{1}{2} ( M\_1 v\_1^2 + M\_2 v\_2^2 ) - \frac{G M\_1 M\_2}{ | \vec{r}\_1 - \vec{r}\_2 | } $$

**Angular Momentum**

$$ | \vec{L} | = | M\_1 \vec{r}\_1 \times \vec{v}\_1 + M\_2 \vec{r}\_2 \times \vec{v}\_2 | $$

*Energy and angular momentum cannot be created or destroyed.*

---

## Conserved Quantities: Energy and Momentum

These are constants of motion:

**Energy**

$$ E = \frac{1}{2} ( M\_1 v\_1^2 + M\_2 v\_2^2 ) - \frac{G M\_1 M\_2}{ | \vec{r}\_1 - \vec{r}\_2 | } = -\frac{G M\_1 M\_2}{2 a}$$

**Angular Momentum**

$$ | \vec{L} | = | M\_1 \vec{r}\_1 \times \vec{v}\_1 + M\_2 \vec{r}\_2 \times \vec{v}\_2 | = \mu r\_p v\_p$$

*Energy and angular momentum cannot be created or destroyed.*

notes: here $\mu$ is the reduced mass

these are submitted without proof - I'll link to some resources for the curious on the webpage, but this is something you have seen or will see more of in your physics classes

---

# Two-body motion in Python once again!

---


* Other solvers - 4th order by hand

Day 3
* why we can't solve the multibody problem analtyically
* multibody problem in 2D
* Kepler's planets

Day 4
* multibody problem in 3D
* galaxies

Day 5
* Other solvers - python packages? 
* We can skip this day if we run out of time
