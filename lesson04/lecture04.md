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

## Last Time

 * reading and writing data in Python
 * basic plots with data
 
---

## This Time

 * (re)intro to data viz
 * more complex plotting
 
---

<br />
<br />
<br />

# A re-intro to Data Viz

notes:
we'll cover more on this after we've got some programming under our belt, but let's think a bit about these concepts now

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

![](images/pie.jpg)


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

# Why?

(Or rather, why _wouldn't_ we visualize?)

notes:
Not everything suits itself to visualization -- and part of the reason for that
is the necessary reductionism that visualization can require.

---

# We can't visualize everything

Peg + Cat:
https://www.youtube.com/embed/In72QAQJ1tY?rel=0

notes:
"There are lots of thing you can compare on a graph / Like who is the shortest
or the tallest giraffe / You can chart how much you walk / How much that you
laugh / There are lots of things you can compare on a graph"

"But the one thing you can't chart / Is how you feel in your heart"

---

# We can't visualize everything

Peg + Cat:
https://www.youtube.com/embed/In72QAQJ1tY?rel=0

<img src="images/peg_cat1.png" alt="drawing" height="400"/>

"There are lots of thing you can compare on a graph / Like who is the shortest
or the tallest giraffe..."

notes:
"There are lots of thing you can compare on a graph / Like who is the shortest
or the tallest giraffe / You can chart how much you walk / How much that you
laugh / There are lots of things you can compare on a graph"

"But the one thing you can't chart / Is how you feel in your heart"

---

# We can't visualize everything

Peg + Cat:
https://www.youtube.com/embed/In72QAQJ1tY?rel=0

<img src="images/peg_cat2.png" alt="drawing" height="400"/>

"But the one thing you can't chart / Is how you feel in your heart"

notes:
"There are lots of thing you can compare on a graph / Like who is the shortest
or the tallest giraffe / You can chart how much you walk / How much that you
laugh / There are lots of things you can compare on a graph"

"But the one thing you can't chart / Is how you feel in your heart"

---

# We can't visualize everything

<img src="images/traesApp.png" alt="drawing" height="500"/>

notes:
for example, here is a haptic, or touch based "visualization" for the blind & visually impaired

---

# We can't visualize everything

<img src="images/traesApp2.png" alt="drawing" height="500"/>

notes:
you should check it out, because its a thing we are also not going to cover!

---

<!-- .slide: data-background-image="images/fov.svg" data-background-size="contain" -->

notes:
Visual information is communicated through our eyes, where it is processed.  At
the most basic level, we can see a range of about 210 degrees horizontally with
one or both eyes.  The region that is covered by both ("binocular") is about
114 degrees in extent.

You can only cram so much information into the human eye.

---

![](https://upload.wikimedia.org/wikipedia/commons/2/27/AcuityHumanEye.svg)

By Vanessa Ezekowitz [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0), via Wikimedia Commons

notes:
When we think about visual communication of information, we *must* think about
how human physiology interacts with that communication.

Also, fair warning: I'm not a medical doctor.

This diagram shows the visual acuity of a "standard" human eye, as a function
of angular distance from the fovea.  We have to think about this in
*conjunction* with our field of view.

---

# Your brain does interpolation

<img src="images/dotsillusion.jpg_large" alt="drawing" width="500"/>

There are 12 dots, can you count them all at the same time?

---

# Your brain does interpolation

<img src="images/blindspotcross.png" alt="drawing" width="500"/>

Step 1: Look at the cross

Step 2: Close left eye, keep looking at the cross

Step 3: Slowly move your head toward & away from screen until dot disappears

---

# Your brain does interpolation

<img src="images/blindspotcross.png" alt="drawing" width="500"/>

Step 1: Look at the cross

Step 2: Close left eye, keep looking at the cross

Step 3: Slowly move your head toward & away from screen until dot disappears

# ... and sometimes it gets it wrong!

---

# Even so, the visual cortex is great for information transfer

Your visual cortex is processing information from different parts of this page AT THE SAME TIME which means it can do impressive things very quickly.


---

Can you spot the differences?

<img src="https://www.rd.com/wp-content/uploads/2018/01/Can-You-Spot-the-10-Differences-in-This-Picture-_585659516-Ksenya-Savva.jpg" height='400px'>

notes:
compare this to how long it would take to spot differences in 2 songs - you'd have to listen to both songs (probably more than once) and compare after!  This would be sequential rather than parallel data transfer!

---

Can you spot the differences?

<!-- [Moonlight Sonota, 1](https://www.youtube.com/watch?v=4591dCHe_sE) -->
<!-- [Moonlight Sonota, 2](https://www.youtube.com/watch?v=4Tr0otuiQuU) -->

* [Moonlight Sonota, 1](https://soundcloud.com/redreapergrell/beethoven-moonlight-sonata)
* [Moonlight Sonota, 2](https://soundcloud.com/user-37232775/sets/beethoven-moonlight-sonata)

Try doing the same thing with these on your own!

notes:
time this activity, give them 1.5 minutes

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

<!-- .slide: data-background-image="images/gunDeaths.jpg" data-background-size="contain" -->

notes:
Here's a pretty brazen example of how to lie with viz. I'll give you a minute to analyze this and tell me what's wrong with this graph.

Some people will claim the Y-axis should always start from the bottom - at zero - to avoid confusion.

---

<!-- .slide: data-background-image="images/keelingCurve.svg" data-background-size="contain" -->

notes:
however, the Keeling Curve is an interesting counter-argument. This is the famous graph that was the original evidence for global warming, showing the rate at which atmospheric carbon dioxide was growing. 

Does anyone know why it's generally accepted to show the y-axis like this, without it starting at the zero axis?

---


## First glance at programming

To do coding-related anything with a computer, we need to understand some basics of programming - so let's got to it!

notes: now we will start with some basics of how to install/open things and learn some basics of data structures

This will be review for folks who have done some programming before, and it will seem strange and new.  Both things are ok!  Everybody can learn something new here.

---

# To Python!

notes: *now open up python part 1*

---

---

# Notes on HW & Quizzes

* Reading quizzes due before class (so you have 2 tonight, but the 2nd is due later tomorrow)
* Homework due before *next* class

notes:
go to HW - 2 parts, one written (yes its hokey, but important)

now we'll have time to install stuff!

also ask me questions!


