---
layout: syllabus
title: Syllabus
---

# Course Description

This course is an introduction to programming methods with an emphasis on data visualization and computational modeling. The increasing prevalence of massive data sets and falling computational barriers have rendered computational modeling and data visualization necessary in most of the contemporary sciences. With this in mind, this course prepares students to select and properly undertake commonly encountered modeling and visualizing tasks. The course first teaches relevant concepts from programming using hands-on activities. Students then apply their new programming skills to guided problems of orbital motions of multiple planetary systems (like that around our sun and other stars) and end the course with both two- and three-dimensional interactive movies of their datasets using a variety of visualization libraries and methods.
	

## Statement of Learning Philosophy				
Because there are many ways to approach a problem, there are thus many ways to learn effective problem solving techniques in a particular field.  With this in mind, we will be cultivating a “growth mindset” in this class with predominantly inquiry based activities - in other words, we will spend a little bit of time talking about science but a lot more time actually doing science because this is how we will improve our skills.  


## Prerequisites					
A good working knowledge of geometry, trigonometry, and algebra. Students must bring a full-sized laptop computer (not a netbook) to each class meeting. No previous programming experience is required.

## Course Schedule
Days will be split roughly into two parts, with the first spent on programming or data visualization concepts and the second spent on hands-on coding with these concepts.  	


Below is an approximate outline of the course and required and *optional* reading for each lesson.  It is recommended that you do the reading the night before the day its listed with.
This course is always under development and  the
course outline below is subject to some flexibility; students will be encouraged
to provide feedback on the topics covered, particularly toward the end.  Topics
that are of particular interest will be emphasized.

**Required texts:**

 * [Python for Everybody](https://www.py4e.com/book.php) is a free, online book for Python fundamentals.  The HTML version [is linked right here](https://www.py4e.com/html3/).
 * There is a free online book, <a href="https://serialmentor.com/dataviz/">Fundamentals of Data Visualization by Claus O. Wilke</a> that provies a lot of nice examples and serves as an intro to the *optional* Tamara Munzner book listed below.  It has an <a href="https://serialmentor.com/dataviz/bibliography.html">annotated bibliography at the end</a> that gives a few references for books in data viz that include programming. It is built from the linked <a href="https://github.com/clauswilke/dataviz">GitHub repo</a>.  Note that this book is focused on static (not interactive) visualizations.


*Optional texts:*
 * <a href="https://www.amazon.com/Visualization-Analysis-Design-AK-Peters/dp/1466508914/ref=sr_1_2?crid=1WC409BVX1489&keywords=visualization+analysis+and+design&qid=1580082878&sprefix=visualization%2Caps%2C158&sr=8-2">Visualization Analysis & Design, Tamara Munzner</a>
 * Edward Tufte wrote a series of visualization books that are often thought of as foundational to the field.  These include <a href="https://www.amazon.com/Visual-Display-Quantitative-Information/dp/0961392142/ref=sr_1_1?keywords=edward+tufte+books&qid=1580082986&sr=8-1">The Visual Display of Quantitative Information</a>, <a href="https://www.amazon.com/Beautiful-Evidence-Edward-R-Tufte/dp/0961392177/ref=sr_1_2?keywords=edward+tufte+books&qid=1580082986&sr=8-2">Beautiful Evidence</a>, <a href="https://www.amazon.com/Envisioning-Information-Edward-R-Tufte/dp/0961392118/ref=sr_1_3?keywords=edward+tufte+books&qid=1580082986&sr=8-3">Envisioning Information</a>, and <a href="https://www.amazon.com/Visual-Explanations-Quantities-Evidence-Narrative/dp/0961392126/ref=sr_1_4?keywords=edward+tufte+books&qid=1580082986&sr=8-4">Visual Explanations: Images and Quantities, Evidence and Narrative<a>
 * Additional references will be added as needed.

Acronyms for books:
 * Py4E: Python for Everybody
 * VAD: Visualization Analysis & Design
 * FDA: Fundamentals of Data Visualization
 * SC: Software Carpentry (links will be given)

| Day   | Topics  | Reading |
|-------|---------|------|
| Day 1: June 29 | Intro to class, Intro to programming | 1. Py4E: Ch. 1, 2, 6 & 8 <br> Note: some of this reading covers conditionals (Ch. 3) & iterations (Ch. 5) which are covered tomorrow in class. <br> *Optional*: [Intro to Jupyter Notebook Video](https://www.youtube.com/watch?v=3C9E2yPBw7s) <br> *Optional*: [Software Carpentry (SC) Variables lesson](http://swcarpentry.github.io/python-novice-gapminder/02-variables/index.html) and [SC's conversion lesson](http://swcarpentry.github.io/python-novice-gapminder/03-types-conversion/index.html)
| Day 2: June 30 | Programming syntax, flow control | 1. Py4E: Ch. 3 & 5 (you can just skim the Try & Except section) <br> *Optional*: [Loops Lecture, IS452](https://github.com/elliewix/IS-452-Spring2020/blob/master/Lectures/Week-02-ExpressionsAndLoops.ipynb) and [if-then Lecture, IS452](https://github.com/elliewix/IS-452-Spring2020/blob/master/Lectures/Week-07-BooleansPt1-if-else.ipynb) <br> *Optional*: [SC's loops lesson](http://swcarpentry.github.io/python-novice-gapminder/12-for-loops/index.html)
| Day 3: July 1  | Data storage & operations, functions | 1. Py4E: Ch. 4 & 7 <br> 2. [SC's Data with Pandas lesson](http://swcarpentry.github.io/python-novice-gapminder/07-reading-tabular/index.html) <br> *Optional:* [IS452's notebook on functions](https://github.com/elliewix/IS-452-Spring2020/blob/master/Lectures/Week-05-Functions.ipynb)
| Day 4: July 2 | What is data viz? |  1. <a href="https://serialmentor.com/dataviz/introduction.html">FDA, Ch. 1: Introduction</a> <br> 2. <a href="https://serialmentor.com/dataviz/proportional-ink.html">FDA, Ch. 17: The principle of proportional ink</a> <br> *Optional*: <a href="http://swcarpentry.github.io/python-novice-gapminder/08-data-frames/index.html">More DataFrame operations with Pandas</a> <br> *Optional:* <a href="https://medium.com/multiple-views-visualization-research-explained/same-data-multiple-perspectives-curse-of-knowledge-in-visual-data-communication-d827c381f936">Same Data, Multiple Perspectives</a> <br> *Optional:* VAD, Ch. 1: What's Viz, and Why Do It? 
| Day 5: Holiday! | NA |  1. <a href="https://serialmentor.com/dataviz/aesthetic-mapping.html">FDA, Ch. 2: Visualizing data: Mapping data onto aesthetics</a> <br> *Optional:* VAD, Ch. 2: What: Data Abstraction <br> *Optional*: <a href="http://swcarpentry.github.io/python-novice-gapminder/08-data-frames/index.html">More DataFrame operations with Pandas</a>
| Day 6: July 6  | Intro to colors & colormaps |  1. <a href="https://serialmentor.com/dataviz/color-basics.html">FDA, Ch. 4: Color scales</a> <br> 2. <a href="https://www.csc2.ncsu.edu/faculty/healey/PP/">Perception in Visualization (pay attention to the parts about color) </a>- **NOTE:** its to just glance over this! <br> *Optional*: VAD, Ch. 10: Map Color and Other Channels <br> *Optional*: <a href="https://jiffyclub.github.io/palettable/#documentation">Palettable Docs</a>
| Day 7: July 7 | Sci Viz vs. Info viz, beginning interactivity | TBD
| Day 8: July 8 | Comparing viz, beginning 3D viz (grammar-of-graphics, bqplot, linked data views if time) | TBD
| Day 9: July 9 | Publish your viz | TBD
| Day 10: July 10 | 3D graphics concepts, Online interactive 3D geometry with Sketchfab | NA

# Learning Outcomes

Students will demonstrate an understanding of data visualization as it relates to plotting datasets related to the orbits of planets around stars and/or motion of stars in galaxies.  By the end of the course, students will have a basic understanding of programming and  the “best practices” behind data visualization.  In particular, each student will be able to:	
 * Understand programming fundamentals of iterative programs, conditional statements and data input and output
 * Understand how to use the programming language Python to perform a variety of calculations
 * Have a basic understanding of how a computer solves equations that we cannot do analytically and be able to manipulate different computer solvers to do so.
 * Have a basic understanding of some of the considerations that go into making a scientific visualization - computer memory considerations, color, time sampling, etc
 * Make 2 and 3 dimensional movies from their scientific calculations
 * Have a basic understanding of the tools available to share both scientific and other forms of data visualization on the web including online notebooks and online 3D rendering software

# Course Materials

There is no required physical textbook for this course.  All course materials will be posted to
the GitHub repository at https://github.com/jnaiman/csci-p-14110_su2020.

As the course progresses, a list of recommended readings available online will be generated for
each class.  


# About Your Instructor

Dr. Jill Naiman's background is in theoretical and computational astrophysics with a current research emphasis on scientific data visualization.  She is currently a Visiting Scholar at the Advanced Visualization Lab at the National Center for Supercomputing Applications.  She is currently involved in projects related to increasing access to industry-standard special effects software for scientists - more info can be found <a href="http://ytini.com">here</a> and <a href="http://astroblend.com">here</a>.  Information about her research and outreach efforts can be found <a href="http://astronaiman.com">here</a>.



# Class Participation Policy	

Leaders are expected to clearly articulate issues and problems and how analytical tools can help. The way we foster this in the course is that you must participate in the classroom discussion. You are not required to “speak up” during every class session, but you do need to attend and contribute to the class and/or forum discussion over the course.  

Leaders are also expected to foster productive environments for those around them. Those in this class come from a variety of backgrounds and comfort levels with the material and programming - it is expected that all students (and instructor!) will remain cognizant of this fact at all times and any demeaning language or behavior will not be tolerated.
										
# Academic Integrity	

Please review and reflect on the academic integrity policy of Harvard Summer School, https://www.summer.harvard.edu/resources-policies/student-responsibilities to which we subscribe. By turning in materials for review, you certify that all work presented is your own and has been done by you independently. 

If, in the course of your writing, you use the words or ideas of another writer or programmer, proper acknowledgement must be given. Not to do so is to commit plagiarism, a form of academic dishonesty. If you are not absolutely clear on what constitutes plagiarism and how to cite sources appropriately, now is the time to learn. Please ask me!

Please be aware that the consequences for plagiarism or other forms of academic dishonesty will be severe. Students who violate university standards of academic integrity are subject to disciplinary action.
					
					
# Accessibility Statement	

To obtain accessibility-related academic adjustments and/or auxiliary aids (academic and physical) students must contact the Accessibility Services Office. Please see their website for more information: https://www.summer.harvard.edu/resources-policies/accessibility-services		
			
			 		
# Sources

No curriculum develops in a vacuum.  Here are some sources to check out that were used in this one's development:

* [Khan Academy](https://www.khanacademy.org/science/ap-physics-1/ap-centripetal-force-and-gravitation/newtons-law-of-gravitation-ap/e/gravity-and-orbits-ap1)
* [Astronomy Crash Course](https://www.youtube.com/watch?v=0rHUDWjR5gg&list=PL8dPuuaLjXtPAJr1ysd5yGIyiSFuh0mIL)
* [Physics Crash Course](https://www.youtube.com/watch?v=ZM8ECpBuQYE)
* [Circular Motion Jupyter Notebook](http://www.astrojack.com/uniform-circular-motion-animation-in-python/)
* [Gravity Experiment Notebook](https://nbviewer.jupyter.org/github/engineersCode/EngComp3_tourdynamics/blob/master/notebooks_en/1_Catch_Motion.ipynb) from [a larger computational engineering class](https://github.com/engineersCode/EngComp3_tourdynamics)
* [Kepler's Orbits](https://github.com/katiebreivik/Keplers_Laws/blob/master/Keplers_Laws.ipynb) and [more info available here](http://gk12.ciera.northwestern.edu/classroom/2018/Python%20and%20Keplers%20Laws.pdf)
* [Binary Motion](http://hosting.astro.cornell.edu/academics/courses/astro201/kepler_binary.htm)
