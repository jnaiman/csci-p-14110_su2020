---
layout: syllabus
title: Syllabus
---

# Course Description

This course is an introduction to programming methods as they pertain to numerical solutions to the astrophysics problem of motion under the influence of multiple gravitating bodies and the visualization of this information. The increasing prevalence of massive data sets and falling computational barriers have rendered computational modeling and data visualization necessary in most of the contemporary sciences. With this in mind, this course prepares students to select and properly undertake commonly encountered modeling and visualizing tasks. The course first teaches relevant concepts from programming using hands-on activities. Students then apply their new programming skills to guided problems of orbital motions of multiple planetary systems (like that around our Sun and other stars) and end the course with both two and three dimensional interactive movies of their datasets.	

## Statement of Learning Philosophy				
Because there are many ways to approach a problem, there are thus many ways to learn effective problem solving techniques in a particular field.  With this in mind, we will be cultivating a “growth mindset” in this class with predominantly inquiry based activities - in other words, we will spend a little bit of time talking about science but a lot more time actually doing science because this is how we will improve our skills.  


## Prerequisites					
A good working knowledge of geometry, trigonometry, and algebra. Students must bring a full-sized laptop computer (not a netbook) to each class meeting. No previous programming experience is required.

## Course Schedule
Days will be split roughly into two parts, with the first spent on astrophysical or data visualization concepts and the second spent on programming with these concepts.  	

Below is a draft schedule - subject to slight changes depending on class pace/interests.

| Day   | Topics
|-------|---------
| Day 1 | Intro to class <br> Intro to gravity <br> Intro to programming
| Day 2 | More on gravity <br> The 2 body problem <br> More on intro to programming
| Day 3 | Compare 2 body analytically and numerically
| Day 4 | The Multi-body problem in 2D - planetary simulations <br> Different numerical solvers
| Day 5 | The Multi-body problem in 3D - planetary and galactic simulations
| Day 6 | What is sci/data viz? Lying with data. <br> Simple 2D movies, data manipulation with Pandas, interactivity
| Day 7 | Data organization, filtering <br> more interactivity, info-viz (grammar-of-graphics, bqplot, linked data views if time)
| Day 8 | Representations of data, Graphical concepts <br> 3D plotting in Python & widgets <br> Optional: deploying to the web
| Day 9 | 3D grapchics concepts <br> Online interactive 3D geometry with Sketchfab
| Day 10 | Types of viz (know your audience!) <br> Where to go from here, finalize projects and Viz party!

# Learning Outcomes

Students will demonstrate an understanding of computational physics as it relates to calculating the orbits planets around stars and/or motion of stars in galaxies and visualizing these orbits with a variety of methods.  By the end of the course, students will have a basic understanding of how objects move under the force of gravity and basic concepts behind data visualization.  In particular, each student will be able to:	

 * Understand how to use the programming language Python to perform calculations
Solve for the motion of two stars analytically (“by hand” or “with pen and paper”) through their physical understanding of gravity.
 * Have a basic understanding of how a computer solves equations that we cannot do analytically and be able to manipulate different computer solvers to do so.
 * Use a computer to calculate the orbits of 2 or more bodies under the influence of their gravitational forces, and in the case of 2 bodies, understand why this calculation may not always match the real, analytical solution, and what this means for the accuracy of any scientific computation.
 * Have a basic understanding of some of the considerations that go into making a scientific visualization - computer memory considerations, color, time sampling, etc
 * Make 2 and 3 dimensional movies from their scientific calculations
* Have a basic understanding of the tools available to share both scientific and other forms of data visualization on the web

# Course Materials

There is no textbook for this course.  All course materials will be posted to
the GitHub repository at https://github.com/jnaiman/csci-p-14110.

As the course progresses, a list of recommended readings will be generated for
each class.  


# About Your Instructor

Dr. Jill Naiman's background is in theoretical and computational astrophysics with a current research emphasis on scientific data visualization.  She is currently a Visiting Scholar at the Advanced Visualization Lab at the National Center for Supercomputing Applications.  She is currently involved in projects related to increasing access to industry-standard special effects software for scientists - more info can be found <a href="http://ytini.com">here</a> and <a href="http://astroblend.com">here</a>.  Information about her astrophysical research and outreach efforts can be found <a href="http://astronaiman.com">here</a>.



# Class Participation Policy	

Leaders are expected to clearly articulate issues and problems and how analytical tools can help. The way we foster this in the course is that you must participate in the classroom discussion. You are not required to “speak up” during every class session, but you do need to attend and contribute to the class and/or forum discussion over the semester.  

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
