---
title: Lecture 3, Part 1 - Kepler's Laws, Ellipses and Orbital Motion
layout: lecture
visible_lec: true
visible_n: true
---

# To Python for ellipse drawing practice!

We did this.

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

notes: this one, law #2, tells us something about how fast the planet moves at different parts of its orbit - near its perihelon (near the sun) it goes really fast, and at the furthest part of its orbit, apehelion (a=away) it goes very slow

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

$$ r(\theta) = \frac{a (1-e^2)}{1 + e cos(\theta)} $$

$$ e = \sqrt{1 - \frac{b^2}{a^2}} $$

Note the limits on $e$:
 * if $b = 0$, $e = 1$ $\rightarrow$ this is a parabola
 * if $a = b$, $e = 0$ $\rightarrow$ this is a perfect circle
 
Beware: $r(\theta)$ is trivial, but $r(t)$ and $\theta(t)$ are not easy to calculate and require numerical methods!

PS: if $e > 1$ $\rightarrow$ this is a hyperbola


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
