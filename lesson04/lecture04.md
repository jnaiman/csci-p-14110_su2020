---
title: Lecture 4 - Intro to Data Viz
layout: lecture
visible_lec: true
visible_n: true
---
<!-- .slide: class="titleslide" -->

# Intro to Programming & Data Viz

<div style="height: 6.0em;"></div>

## Jill P. Naiman
## Summer 2020
## Lecture 4

---

## Announcements!

 * HW2/HW3 - weekend fun!
 * Lecture/Coding/Choose your own adventure
 * Things to let me know over the weekend
    * test imports 6
	* test imports 7

---

## Last time

* functions
* data storage & operations 
* reading in data in general
* reading in data with Pandas

notes:
Last time we sort of finished covering our intro to programming and we'll start using these skills to do 
some actual coding!  Huzzah!

---

## This time

* What is data viz?
* What do we have to consider when we do data viz?
* Conceptual overview of topics in data viz
* Practice more with Python

notes:
today we'll loop back into some of the ideas covered in day 1 about what data viz IS

then we'll get lots of practice in Python doing what we need to do get data viz working for us!

---

<br />
<br />
<br />

# Data Viz

notes:
just a reminder of things we covered on day 1

---

### Why any data viz course will feel a little weird


<img src="https://thumbnails-visually.netdna-ssl.com/what-is-data-visualization_50290b9240bd8_w1500.png" width='700px'>

notes:

so I showed a similar diagram from my semester long grad class, but here's another way to look at all of the overlapping areas of data viz!

there is a *huge* overlay of topics that cover data viz - from the neurology of how your prefrontal cortex process information, to how humans process storytelling, to data analytics, and color theory and the list goes on!

---

## Start thinking about

 * What is a visualization?
 * Why do we visualize?
 * What types of data do we visualize?
 * How do we visualize?

![](../lesson01/images/pie.jpg)


notes:
We're going to start out at a very high-level, discussing why we choose to
visualize versus other types of representation, what types of data, and how we
might do it.

---

## What is a visualization anyway?

"Computer-based *visualization* systems provide visual representations of datasets designed to help people carry out tasks more effectively."

   * Visualization Analysis & Design, Tamara Munzner

notes:
I really like this definition because it gives us a sense of purpose - i.e. that our visualization must help a human with a task that has to do with data.

---

## What is a visualization anyway?

"Computer-based *visualization* systems provide visual representations of datasets designed to help people carry out tasks more effectively."

   * Visualization Analysis & Design, Tamara Munzner

Data Viz is task oriented:

<img src="https://www.savalli.us/BIO370/Anatomy/AnatomyImages/TyrannosaurusSkeletonLabel.jpg">


notes:
here for example, we might want to know the labels of bones or how they fit together

---

## What is a visualization anyway?

"Computer-based *visualization* systems provide visual representations of datasets designed to help people carry out tasks more effectively."

   * Visualization Analysis & Design, Tamara Munzner

... versus artistic representations used to convey emotions:

<img src="https://i.etsystatic.com/5150206/r/il/fe175b/1823842266/il_570xN.1823842266_b9y3.jpg" height='400px'>

---

## What is a visualization anyway?

"Computer-based *visualization* systems provide visual representations of datasets designed to help people carry out tasks more effectively."

   * Visualization Analysis & Design, Tamara Munzner

... versus movies, comics, or other cinematic representations used to tell stories:

<img src="http://www.dinopit.com/wp-content/uploads/2012/08/funny-dinosaur.jpg" height='300px'>


---

# Even so, the visual cortex is great for information transfer

Your visual cortex is processing information from different parts of this page AT THE SAME TIME which means it can do impressive things very quickly.

notes: 
recall last time we compared our "parallel processing" cababilities through visualization vs. sound


---

Can you spot the differences?

<img src="https://www.rd.com/wp-content/uploads/2018/01/Can-You-Spot-the-10-Differences-in-This-Picture-_585659516-Ksenya-Savva.jpg" height='400px'>

notes:
compare this to how long it would take to spot differences in 2 songs - you'd have to listen to both songs (probably more than once) and compare after!  This would be sequential rather than parallel data transfer!

---

Can you spot the differences?

* [Moonlight Sonota, 1](https://soundcloud.com/redreapergrell/beethoven-moonlight-sonata)
* [Moonlight Sonota, 2](https://soundcloud.com/user-37232775/sets/beethoven-moonlight-sonata)

Try doing the same thing with these on your own!

notes:
recall it was harder to find differences!

ask: how long did this take you?  How many differences were there?
I spotted tempo as one (but you can cheat by looking at the timer on the bottom!)

Also, you can look at how different each of the sound-bars are on each link and see how different the music looks visually!

---

# Visualization augments human data analysis capabilities

 * enhances our ability to pattern find
 * allows us to summarize data quickly
 * allows us to search our data quickly

---

## Anscombe's Quartet

This famous example show's 4 datasets with the exact same mean, varience and correlation coefficient.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Anscombe%27s_quartet_3.svg/1280px-Anscombe%27s_quartet_3.svg.png" height='500px'>

Statistics can be useful, but visualization generated context!

---

## Same thing but with a dinosaur

<img src="https://miro.medium.com/max/600/1*W--cGoA3_n2ZlU6Xs4o2iQ.gif" width="600px">

Statistics can be useful, but visualization generated context!

---

<br />
<br />
<br />

# A few final considerations.

---

# Who are you visualizing for?

* For yourself?
* For a peer?
* For someone else?

notes:
*Whenever* you build a visualization you need to think about the context that
you can assume on the part of your viewer.

We will talk about how your viz changes with audience in this course.

---

# Tenet 1:

"Visualizing data" is not a strict subset of "making an image."

 * Collection of the data
 * Organization of that data
 * Representation of that data

notes:
We will approach visualization as encompassing several different stages in the
collection, organization and representation of data.

---

# Tenet 2:

We tell lies to visualize, but we _must_ be honest.

 * No representation is going to convey the entire complexity of a dataset.
 * Some representations are better than others.

---

### "The Principle of Proportional Ink" - callingbull****.org
![](../lesson01/images/proportionalInk.png)

notes:
In the reading you learned about the "principle of proportional ink" which is one good "rule" to follow when making data viz

---

### "Spurious Correlations" - tylervigen.com
<img src="../lesson01/images/spurious.png" alt="drawing" width="800">

notes:
We talked about some pretty serious issues of bad data-viz last time, but here is a fun one

you can have a lot of absurd fun with data - but when data is presented in a visualization, people often believe the authority of it even if it's outlandish. 

This guy has some good ideas of where to find sample datasets for upcoming homework assignments too!

This one isn't related to proportional ink, its just plotting dangerously!

---

<!-- .slide: data-background-image="../lesson01/images/hearts_battery.svg" data-background-size="contain" -->

notes:
here are a few more representations of data that you've probably run into!

---

<!-- .slide: data-background-image="../lesson01/images/battery.svg" data-background-size="contain" -->

<div style="height: 10em;"></div>

 1. Sensors read the current "fill" of the battery
    * Analog / digital conversion
    * Normalized with respect to expected "full"
 1. This is then scaled to a percentage
 1. The battery image is filled from left to right
 1. The image is then rasterized and displayed

notes: what goes into this representation

---

<!-- .slide: data-background-image="../lesson01/images/hearts_bw.svg" data-background-size="contain" -->

 * Some fixed maximum amount of damage
 * Each time damage is taken, decrement
 * Each time damage is reversed, increment
 * Display number of hearts as appropriate

---

2 out of 3 "points"

<!-- .slide: data-background-image="../lesson01/images/hearts_color.svg" data-background-size="contain" -->

---

<!-- .slide: data-background-image="../lesson01/images/hearts_color.svg" data-background-size="contain" -->

![](images/doom_status.png)

---

<!-- .slide: data-background-image="../lesson01/images/stitch_bg.png" data-background-size="contain"-->

notes:
This is a screenshot from the movie "Lilo and Stitch" where the little girl Lilo is graphing how much evil is in the alien Stitch. It borrows from a familiar visual - the thermometer. But how could this visualization be misinterpreted? How is it different from a thermometer?

---

<!-- .slide: data-background-image="../lesson01/images/stitch_nobg.png" data-background-size="contain"-->

notes:
The angle can be misleading. So can the relative width of the head vs the feet. The surface area is not consistent from top to bottom. Also there are empty areas in the mouth and eyes!

---

<!-- .slide: data-background-image="../lesson01/images/stitch_nobg_tilted.png" data-background-size="contain"-->

notes:
If we rotate the image so that the red liquid is level, do we get a different impression for how much bad is in Stitch?

---

<iframe width="1024" height="576"
src="https://www.youtube.com/embed/D-uBv6jB7r0?rel=0" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>

notes:
How could this visualization be misleading? What about the camera move? What about the colors used? Are there actually several distinct layers of shells or is this a continuous volume?

---

## Honesty

Our choices must be:

 * Deliberate
 * Informed
 * Motivated
 * Justifiable

---

## Election Maps

Mark Newman of the University of Michigan has created visualizations of the
election maps from several of the most recent elections.  For more information
and context, see his page http://www-personal.umich.edu/~mejn/election/2008/ .

 * [Map 1](http://www-personal.umich.edu/~mejn/election/2008/statemapredbluer1024.png)
 * [Map 2](http://www-personal.umich.edu/~mejn/election/2008/statepopredblue1024.png)
 * [Map 3](http://www-personal.umich.edu/~mejn/election/2008/countymapredbluer1024.png)
 * [Map 4](http://www-personal.umich.edu/~mejn/election/2008/countymappurpler1024.png)
 * [Map 5](http://www-personal.umich.edu/~mejn/election/2008/countycartpurple1024.png)

notes:

Each of these maps "lies" in some way and they each tell a different story.

These are great, but some criticisms might be that the color red is more apparent to the human eye than the color blue. And in the population-to-area adjusted maps, it's difficult to read for people used to geographic accuracy.

Map1 - this is just a geographical map of red and blue

Map2 - cartogram weighted by population (note, NOT by electoral college population)

Map3 - election results by county

Map4 - percentage of votes by county

Map5 - percentage of votes by county, weighted by population
