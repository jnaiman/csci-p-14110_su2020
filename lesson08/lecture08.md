---
title: Lecture 8
layout: lecture
visible_lec: true
visible_n: true
---
<!-- .slide: class="titleslide" -->

# Intro to Programming & Data Viz
<div style="height: 6.0em;"></div>
## Jill P. Naiman
## Summer 2020
## Lecture 8

---

## Last time

 * Maps & their projections
 * Mappable data with geopandas & GeoJSON
 * Beginning interactivity with ipywidgets
 
notes:
this time we'll do a very brief intro into mapable data & interactivity with ipywidgets

we'll end by combining them to make interactive maps!

---

## This time

 * object-oriented programming & Updating object traits with `traitlets`
 * Linked views with bqplot
 * Crash Course in Astronomy & intro to the Planetary Dataset
 
notes:
this time we'll cover how to "link" data with bqplot and we'll get a brief intro to the dataset we'll be using for the rest of the days of the class -- the planetary dataset from the Kepler sattelite

these will sort of be despirate topics but we'll but them together in the coding portion of the class today, so stick with me as best you can!

---

<br>
<br>
<br>

# Topic #1: Object Oriented Crash Course

---

# Background: Object-Oriented Programming

<img src="images/vehicles.jpg" width="700"/>

notes:
What are some traits every vehicle has?

---

## Object-Oriented Programming

Vehicles:
 * number of wheels
 * color
 * weight

notes:
this set of traits won't necessarily be useful for things that aren't vehicles. 

---

## Object-Oriented Programming

class Vehicles:
 * int: number of wheels
 * string: color
 * float: weight

notes:
in object-oriented programming, we can use this "class" keyword to create a new object type "vehicle" which has traits that are the data types we're already familiar with - integers, floats, strings, booleans, etc.

This is like buying salad at the grocery store. You can either buy lettuce, onions, croutons, and dressing separately, or you can buy prepackaged salads with different combinations of those things already put together.

---

## Updating Traits

class Vehicles:
 * int: number of wheels
 * string: color
 * float: weight

```#python
myVehicle = Vehicles()
myVehicle.number_of_wheels = 4
myVehicle.color = 'brown'
myVehicle.weight = 2.5 # tons
```

notes:
Using this sort of idea, I can make an "object" that has some information stored about it, let's call this object `myVehicle` and I can set these attributes or *traits* of my vehicle using the `.` notation

---

## Updating Traits

class Vehicles:
 * int: number of wheels
 * string: color
 * float: weight

```#python
myVehicle = Vehicles()
myVehicle.number_of_wheels = 4
myVehicle.color = 'brown'
myVehicle.weight = 2.5 # tons
```

Function that acts on an object of the Vehicles class:

```#python
def paint_a_vehicle(vehicle):
...
```

notes:
now let's say I make a function that paints my car, certainly the `myVehicle` object should change in color!

---

## Updating Traits

class Vehicles:
 * int: number of wheels
 * string: color
 * float: weight

```#python
myVehicle = Vehicles()
myVehicle.number_of_wheels = 4
myVehicle.color = 'brown'
myVehicle.weight = 2.5 # tons
```

Function that acts on an object of the Vehicles class:

```#python
def paint_a_vehicle(vehicle):
...
```

"Observe" changes in our object:

```#python
myVehicle.observe(paint_a_vehicle, ['color'])
```

notes:
to do that we have to make sure the myVehicle object is sort of waiting and *observing* for a change in its color so that once we run this function, this *trait* of myVehicle gets updated

---

## Updating Traits

```#python
import traitlets

class Vehicles(traitlets.HasTraits):
    number_of_wheels = traitlets.Int()
    color = traitlets.Unicode() # basically another name for string
```

notes:
how would this look fully in python?

First, we would start with the Vehicles class (here I'm leaving out the weights trait for brievity)

---

## Updating Traits

```#python
import traitlets

class Vehicles(traitlets.HasTraits):
    number_of_wheels = traitlets.Int()
    color = traitlets.Unicode() # basically another name for string
```

```#python
myVehicle = Vehicles()
myVehicle.number_of_wheels = 4
myVehicle.color = 'brown'
```

notes:
then we would define an object of this class, like before

---

## Updating Traits

```#python
import traitlets

class Vehicles(traitlets.HasTraits):
    number_of_wheels = traitlets.Int()
    color = traitlets.Unicode() # basically another name for string
```

```#python
myVehicle = Vehicles()
myVehicle.number_of_wheels = 4
myVehicle.color = 'brown'
```

OR

```#python
myVehicle = Vehicles(number_of_wheels = 4, color = 'brown')
```

notes:
alternitavely we could define it in one like like this which is sort of nice & compact

---

## Updating Traits

```#python
import traitlets

class Vehicles(traitlets.HasTraits):
    number_of_wheels = traitlets.Int()
    color = traitlets.Unicode() # basically another name for string
```

```#python
myVehicle = Vehicles(number_of_wheels = 4, color = 'brown')
```


```#python
def paint_a_vehicle_blue(change):
	change['owner'].color = 'blue'
```


notes:
then we would make that function that changes the car's paint

note that I've written it a little different here with this "change" and 'owner' -- we'll talk about that when we do some hands-on Python stuff

---

## Updating Traits

```#python
import traitlets

class Vehicles(traitlets.HasTraits):
    number_of_wheels = traitlets.Int()
    color = traitlets.Unicode() # basically another name for string
```

```#python
myVehicle = Vehicles(number_of_wheels = 4, color = 'brown')
```


```#python
def paint_a_vehicle_blue(change):
	change['owner'].color = 'blue'
```

In this case, we are watching the trait `color` for changes.  When a change
occurs, the function `paint_a_vehicle_blue` is called.  The argument is a *dict* with
these values:

 * `new`: the new value the trait has
 * `old`: the previous value
 * `type`: the type of change
 * `owner`: the object that owns this trait
 * `name`: the name of the trait

notes:
then we would make that function that changes the car's paint

note that I've written it a little different here with this "change" and 'owner' -- we'll talk about that when we do some hands-on Python stuff

basically, this "change" is an object called a dict or dictionary -- which is basically like the sorts of objects we used when we used Pandas and selected columns

---

## Updating Traits

```#python
import traitlets

class Vehicles(traitlets.HasTraits):
    number_of_wheels = traitlets.Int()
    color = traitlets.Unicode() # basically another name for string
```

```#python
myVehicle = Vehicles(number_of_wheels = 4, color = 'brown')
```


```#python
def paint_a_vehicle_blue(change):
	change['owner'].color = 'blue'
```

```#python
myVehicle.observe(paint_a_vehicle_blue, ['color'])
```

notes:
finally, we have to observe this change when the function gets called so that the myVehicle color actually gets changed!
