---
title: Lecture 9, Part 2
layout: lecture
include_vega: true
visible_lec: true
visible_n: true
---

<!-- .slide: class="titleslide" -->

# Intro to Programming & Data Viz
<div style="height: 6.0em;"></div>
## Jill P. Naiman
## Summer 2020
## Lecture 9, Part 2

---

## This part of lecture 9

 1. 3D Computer Graphics
   * 3D Graphics Tools
   * Visual Effects tools
 1. Validation 
 1. Publishing
 
notes: so today we're going to talk a bit about some "high-end" graphics tools  and about how rendering works

AVL talked a bit about this with us 2 weeks ago, and here we will just mention a few things before moving back to Idyll

---

<br>
<br>
<br>

# TOPIC 1: 3D Computer graphics

---

## A fun ~2 min movie from Pixar

[Check out this link here](https://www.youtube.com/watch?v=NEzJH-JrAdw)
 
notes: this a fun link to see how folks from pixar describe what they do

---

## 3D Computer Graphics

 * Composed of virtual 3D objects
 * Often time evolving (animated)
 * Displayed on 2D screens
 * Attempts to simulate photorealism to some extent
 
notes: note these can also be displayed on 3D screens, but the way that happens is a little different

---

## Computer Graphics Terms

 * Real-time vs Pre-Rendered graphics
 * Frames vs Timesteps

<img src="images/timestepframestep.gif" width="600"/>

notes:
real-time graphics refresh the screen faster than the eye perceives, usually at least 30 times a second. Pre-rendered can take all the time in the world.

Frames are individual images that when strung together in time create the illusion of motion. They are the "timesteps" of a movie. But scientific data also have "timesteps" which may not be synchronized with the speed of the movie.

You'll notice in this GIF, the frame rate and the time step rate are different - we are zooming out quicker than we are updating the data in the images

---

## Computer Graphics Acronyms

 * VFX - visual effects
 * CGI - computer graphics imagery
 * FPS - frames per second
 * GUI - graphic user interface
 * HUD - heads up display
 
notes: you aren't required to remember any of these, but if you see them pop up, here they are

---

## Common Frame Rates

 * 24 FPS - theatrical films
 * 30 FPS - TV and specialty theaters
 * 48 FPS, 60 FPS - video games, interactive graphics, virtual reality
 * 120 FPS - really good virtual reality

<iframe width="560" height="315" src="https://www.youtube.com/embed/pfiHFqnPLZ4?rel=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

notes:

you can note if you try to follow the 15 or 30 FPS (frames per second) with your eye you see that it is jumpy

24 fps is considered the absolute minimum necessary frequency so that people don't perceive individual frames.

48 fps is widely considered so fast the human eye can't perceive any separation at all - but 60 fps is safer.

if you watch a TV and it seems distractingly smooth, it's probably doing frame interpolation to make 30fps content play back at 60fps.

This youtube video actually only plays at 60FPS, so the 120 ball is kind of pointless.

---

## Common Resolutions

 * 1024 x 768 - standard definition or SD (3:4)
 * 1920 x 1080 - high definition or HD (16:9)
 * 3840 x 2160 - ultra high definition or UHD or 4k (16:9)

<img src="images/resolutions.png" width="600"/>

notes:
Often people refer to these formats as 1k or 2k or 4k in graphics, referring to the number of pixels along the horizontal axis.

While these are the most common formats today, there's a long history of a crazy variety of formats. Cinemascope had a ratio of 2.35:1 which was wider than modern wide screens. Also fun fact, it didn't have a resolution because it was film before? digital. 

---

## Common File Formats

 * Images: JPG, PNG, TIF, EXR
 * Video: MOV, MP4, AVI
 * Codec: H.264, ProRes, DNxHD

notes:
There are many more formats, but because these are either lossless or extremely space efficient, they are the most popular.

EXR in particular is special because it can store many image layers including DEEP images which store depth information.

ProRes is only available on Apple, and DNxHD is Windows

---

## 3D Geometry

All 3D geometry is represented as:

<div class="left">
 <ul>
 <li>Points</li>
 </ul>
</div>

<div class="right">
	<img src="images/points.png" width="100%">
</div>


notes: how do we represent geometry in space? one way is points...

---

## 3D Geometry

All 3D geometry is represented as:

<div class="left">
 <ul>
 <li>Points</li>
 <li>Edges</li>
 </ul>
 
</div>

<div class="right">
	<img src="images/edges.png" width="100%">
</div>

---

## 3D Geometry

All 3D geometry is represented as:

<div class="left">
 <ul>
 <li>Points</li>
 <li>Edges</li>
 <li>Surfaces</li>
 </ul>

 
</div>

<div class="right">
	<img src="images/surfaces.png" width="100%">
</div>


notes: we can connect these points and images to make surfaces

---

## 3D Geometry

All 3D geometry is represented as:

<div class="left">
 <ul>
 <li>Points</li>
 <li>Edges</li>
 <li>Surfaces</li>
 <li>Volumes</li>
 </ul>
 
</div>

<div class="right">
	<img src="images/voxels.png" width="100%">
</div>


notes: or we can give the 3D surfaces some depth and make them into shapes

here these 3D cubes are called "voxels" which are similar to 2D "pixels" but for volumes

---

## 3D Geometry

<iframe src="https://player.vimeo.com/video/169599296?color=949494&title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

Link: https://player.vimeo.com/video/169599296?color=949494&title=0&byline=0&portrait=0

notes:

You can convert between points, surfaces and volumes, ofthen to really cool effects like shown - you can get some bananas permutations.

---

## 3D Geometry

Surfaces can be encoded as:

<div class="left">
 <ul>
 <li>Implicit primitives</li>
 </ul>
 
</div>

<div class="right">
	<img src="images/primitive.png" width="100%">
</div>


notes:
primitives are defined by mathematical functions. This sphere is defined by a center position and a radius.

---

## 3D Geometry

Surfaces can be encoded as:

<div class="left">
 <ul>
 <li>Implicit primitives</li>
 <li>Polygonal Meshes</li>
 </ul>
 
</div>

<div class="right">
	<img src="images/quadsSmall.jpg" width="100%">
</div>


notes:
Quadrilaterals are a good way to see the flow of geometry, which artists like, but quads can bend.

---

## 3D Geometry

Surfaces can be encoded as:

<div class="left">
 <ul>
 <li>Implicit primitives</li>
 <li>Polygonal Meshes</li>
 </ul>
 
</div>

<div class="right">
	<img src="images/triangles.png" width="100%">
</div>


notes:
Triangles cannot bend because three points define a plane. So automatic geometry like the stuff you use in science is more often going to be triangles.

---

## 3D Geometry

Surfaces can be encoded as:

<div class="left">
 <ul>
 <li>Implicit primitives</li>
 <li>Polygonal Meshes</li>
 <li>NURBS or Bezier Surfaces</li>
 </ul>
 
</div>

<div class="right">
	<img src="images/nurbs.png" width="100%">
</div>

notes:
This is a NURBS sphere. You can see the control vertices are floating off the surface. Every patch on the surface is influenced by many of the neighboring points.

Here if I wanted to deform this surface, I could pull at one of the blue points and the shape of the surface would change.

---

## 3D Geometry

Surfaces can be encoded as:

<div class="left">
<ul>
 <li>Implicit primitives</li>
 <li>Polygonal Meshes</li>
 <li>NURBS or Bezier Surfaces</li>
 <li>Subdivision Surfaces</li>
 </ul>

 
</div>

<div class="right">
	<img src="images/subdivs.png" width="100%">
</div>


notes:
Subdivision surfaces are like those adaptive volumes we saw last week. You can add detail where you want it.

---

## 3D Geometry

Datasets with many fields called "attributes":

<div class="left">
<ol>
 <li>Transform Attributes (translate, rotate, scale)</li>
 </ol>
 
</div>

<div class="right">
	<img src="images/xyz.gif" width="100%">
</div>


notes:
These transform attributes are the same for all objects.

Recall we discussed some of these in earlier classes for 2D plots.  Same principle here.

---

## 3D Geometry

Datasets with many fields called "attributes":

<div class="left">
<ol>
 <li>Transform Attributes (translate, rotate, scale)</li>
 <li>Shape Attributes (radius, bumpyness, twistyness)</li>
 </ol>
 
</div>

<div class="right">
	<img src="images/attributes.gif" width="100%">
</div>


notes:
shape attributes depend totally on what the shape is.

These are something you won't really see in 2D unless you start modifying 2D shapes with some weird transforms.

---

## Rendering

Rendering is the process of flattening a 3-dimensional scene into a flat image.

How do photographic cameras accomplish this?

---

## Photographic Rendering

 1. White light leaves a light source like the sun

---

## Photographic Rendering

 1. White light leaves a light source like the sun
 1. The light bounces off an object like a ball or a leaf, and inherits the object's color

---

## Photographic Rendering

 1. White light leaves a light source like the sun
 1. The light bounces off an object like a ball or a leaf, and inherits the object's color
 1. Colored light arrives at the camera lens

---

## Photographic Rendering

 1. White light leaves a light source like the sun
 1. The light bounces off an object like a ball or a leaf, and inherits the object's color
 1. Colored light arrives at the camera lens
 1. The camera lens directs the light to a specific location on the CCD sensor, effectively a pixel

---

## Photographic Rendering

 1. White light leaves a light source like the sun
 1. The light bounces off an object like a ball or a leaf, and inherits the object's color
 1. Colored light arrives at the camera lens
 1. The camera lens directs the light to a specific location on the CCD sensor, effectively a pixel
 1. The camera processor stores the color of the light at the location of the pixel

---

## Photographic Rendering

 1. White light leaves a light source like the sun
 1. The light bounces off an object like a ball or a leaf, and inherits the object's color
 1. Colored light arrives at the camera lens
 1. The camera lens directs the light to a specific location on the CCD sensor, effectively a pixel
 1. The camera processor stores the color of the light at the location of the pixel

If we want to simulate this process in computer graphics software, how many light rays do we need to calculate? 

---

## Photographic Rendering

Trick question, that's WAAAAYYYYY too expensive!

Why?

The light rays that never arrive at the camera are a totally wasted calculation. They don't contribute to the final image at all.

Is there a better way?

---

## Raytracing

Raytracing does this process backwards:

 1. A light ray starts at a camera position and travels toward/through a specific image pixel
 1. The light ray bounces off objects in the scene
 1. If the bounced light arrives at a light, it is recorded as "lit"
 1. If the light ray never arrives at an object or a light, it is recorded as the background color, usually black

This way, we only calculate the path of one light ray for each pixel. It's efficient!

---

## Raytracing

Houdini VEX path tracer

<iframe src="https://player.vimeo.com/video/331150010" width="640" height="412" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

Link: https://player.vimeo.com/video/331150010

---

## Raytracing

Q: How does the renderer handle procedural (formula-driven) geometry?

A: Micropolygon dicing

Q: How does the renderer handle volumetric data that doesn't just "bounce"?

A: Volume ray marching

notes:
The renderer will divide interpolated or dense geometry into smaller and smaller polygons until they are smaller than the image pixel being calculated. These smaller-than-a-pixel polygons are called micropolygons.

In volume ray marching, a ray steps through a volume and accumulates opacity at regular intervals. Each interval generates a bounce to figure out lighting. Once it reaches 100% opacity, it stops ray marching.

---

## Shaders

Shaders are code that tells the renderer what something looks like. There are many types:

 1. Vertex Shaders
 1. Geometry Shaders
 1. Fragment or Pixel or Material Shaders
 1. Lens Shaders

notes:

basically, a shader tells a light ray that hits an object, "hey!" you hit something that is glass and so it should bend light like glass, or something like a leaf so it should be bumpy like a leaf

---

## The Secrets of Photorealism

<div class="left">

<br>
 
</div>

<div class="right">
	<img src="images/dull.png" width="100%">
</div>

notes:
this is a very dull and not-realistic looking image

---

## The Secrets of Photorealism

<div class="left">
 <ol>
 <li>Lighting changes everything - use realistic light sources</li>
 </ol>
 
</div>

<div class="right">
	<img src="images/light.png" width="100%">
</div>


---

## The Secrets of Photorealism

<div class="left">
 <ol>
 <li>Lighting changes everything - use realistic light sources</li>
 <li>Photographs have motion blur - use a motion blur algorithm</li>
 </ol>
 
</div>

<div class="right">
	<img src="images/mblur.png" width="100%">
</div>


---

## The Secrets of Photorealism

<div class="left">
 <ol>
 <li>Lighting changes everything - use realistic light sources</li>
 <li>Photographs have motion blur - use a motion blur algorithm</li>
 <li>Photographs have depth of field - use a depth of field algorithm</li>
 </ol>

 
</div>

<div class="right">
	<img src="images/dof.png" width="100%">
</div>

---

## The Secrets of Photorealism

<div class="left">
 <ol>
 <li>Lighting changes everything - use realistic light sources</li>
 <li>Photographs have motion blur - use a motion blur algorithm</li>
 <li>Photographs have depth of field - use a depth of field algorithm</li>
 <li>Scenes need backgrounds - embed your dataset inside a contextual dataset</li>
 </ol>

 
</div>

<div class="right">
	<img src="images/background.png" width="100%">
</div>

---

## The Secrets of Photorealism

<div class="left">
 <ol>
 <li>Lighting changes everything - use realistic light sources</li>
 <li>Photographs have motion blur - use a motion blur algorithm</li>
 <li>Photographs have depth of field - use a depth of field algorithm</li>
 <li>Scenes need backgrounds - embed your dataset inside a contextual dataset</li>
 <li>Indirect light is everywhere - use an "ambient occlusion" algorithm</li>
 </ol>
 
</div>

<div class="right">
	<img src="images/ambient.png" width="100%">
</div>

---

## The Secrets of Photorealism

<div class="left">
<ol>
 <li>Lighting changes everything - use realistic light sources</li>
 <li>Photographs have motion blur - use a motion blur algorithm</li>
 <li>Photographs have depth of field - use a depth of field algorithm</li>
 <li>Scenes need backgrounds - embed your dataset inside a contextual dataset</li>
 <li>Indirect light is everywhere - use an "ambient occlusion" algorithm</li>
 <li>The world is fractal - increase detail with procedural noise and instancing</li>
 </ol>

 
</div>

<div class="right">
	<img src="images/detail.png" width="100%">
</div>

---

## OpenGL

Before most computers could show graphics of any kind, several companies began to compete for proprietary formats.

A company called Silicon Graphics stepped in and created an Open Source specification for computer graphics called OpenGL. 

To this day, most software graphics you see are rendered using some version of OpenGL - including the whole Mac operating system.

notes:
Many other open source projects have copied this model, such as OpenCV (computer vision), OpenCL (gpus), and OpenMP (multi-processing).

---

## WebGL

OpenGL is primarily intended for C-style programming.

WebGL implements the same set of tools for rendering through a web browser. This allows us to natively render 3D content on the internet!

---

## Three.js

Three.js is a javascript library that uses WebGL to create interactive 3D graphics that render in web browsers. 

It is meant to be more user-friendly than raw WebGL code.

---

## SketchFab & ipyvolume

SketchFab uses WebGL to render YOUR 3D data in a 3D viewport in a web browser. 

[SketchFab.com](https://sketchfab.com)

ipyvolume uses WebGL to render volumes to your jupyter notebook.

---

## Scientific Visualization Tools

 * yt
 * ParaView
 * VisIt
 * VMD
 * Vapor
 
 notes: there is a lot of overlap between what scientists & visual effects/special effects artists are trying to do, but their data formats are usually quite differnt
 
 so far we've looked at "yt" for scientific viz

---

## Visual Effects Tools

 * Blender - for developers
 * Maya - for animators
 * Houdini - for dynamics

notes: we haven't covered any viz effects tools, but AJ will step in at the end of our class next week to talk about Houdini & show some fun things you can try

---

## Scientific Viz Tools VERSUS Visual Effects Tools

<img src="images/versus.png" width="800"/>

notes: here is a quick comparision chart to show key differences between yt like we've been using & a special effects tool like houdini

---

## Scientific Viz Tools VERSUS Visual Effects Tools

<img src="images/ytiniVersus.png" width="800"/>

[ytini](www.ytini.com)

[Astroblend](www.astroblend.com)

notes:
several of us at the NCSA worked on ytini so that Houdini could use some of the features of yt natively!

This is also true of Dr. Naiman's work on Astroblend.

---

<br>
<br>
<br>

# Topic 2: Cinematic-type viz in practice

---

## Rendering in 3D: From 3D objects to images

Our task is to take our physical description of 3D space and convey to the computer how to bounce light around.

We talked about this in abstract but today we'll get practicle:
1. learn how to turn our numerical simulations into 3D geometry files
1. make aesthetic choices motivated by physics
1. load our models into MeshLab to "debug"
1. load final(ish) models into Sketchfab to make 3D movies

---

## Where we are going

<div style="float:center;width:98%;margin-right:14px;" class="sketchfab-embed-wrapper"><iframe width="800" height="500" src="https://sketchfab.com/models/ece18031ea59414f8b4a506a7d45a62e/embed" frameborder="0" allow="autoplay; fullscreen; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

notes:
just a reminder of where we are going -- we're goingt make some interactive movies with your 3D data

---

## Software

1. Setup a Sketchfab account
1. Local: Download MeshLab (Mac) *or* 3Dviewer for windows
1. Web: [Creators3d online viewer](https://www.creators3d.com/online-viewer)

notes: actually pause in class to do this!

---

## Planets - Texture Mapping

<!-- .slide: data-background-image="images/textureMapping/textureMapping.001.jpeg" data-background-size="auto 75%" -->

notes: we will do something called texture mapping where we "wrap" a high resolution image on a low resolution mesh object

here you can see how this works for a face, and it indeed looks creepy

---

## Planets - Texture Mapping

<!-- .slide: data-background-image="images/textureMapping/textureMapping.002.jpeg" data-background-size="auto 75%" -->

notes: we will do this with our planets as we will have very low resolution spheres

why? this is actually a graphics trick that is widely used - it turns out is more computationally intensive to render lots of polygons than few polygons and high resolution textures

---

## Planets - Texture Mapping

<!-- .slide: data-background-image="images/textureMapping/textureMapping.003.jpeg" data-background-size="auto 75%" -->

notes: here are a few of the texture maps that are included with the files you'll download for your 3D movies

---

<!-- .slide: data-background-image="images/objFiles/objFiles.001.jpeg" data-background-size="auto 95%" -->

notes: we'll go through the code in a moment, but basically, you'll run some code with what sorts of "planets" your planet simulations are and you'll end up with a directory called something like "MyPlanetSystem"

in this directory you will have the planet textures and two files an *obj*, or object file, and an *mtl*, or material, file

these files do different things to combine to make your model

---

<!-- .slide: data-background-image="images/objFiles/objFiles.002.jpeg" data-background-size="auto 95%" -->

notes: your obj file gives vertex information geometric locations where we should "pin" our texture maps

the vertexes tell us where each "square" that makes up our sphere goes - you can see this sort of in this image here

---

<!-- .slide: data-background-image="images/objFiles/objFiles.003.jpeg" data-background-size="auto 95%" -->

notes: our material files can give us information about background colors (which we won't be using) and also the names of any texture maps we'll be using like "sun_texture1.jpg" for example

---

<!-- .slide: data-background-image="images/objFiles/objFiles.004.jpeg" data-background-size="auto 95%" -->


notes: you will use these files to import into MeshLab and upload to sketchfab

I *highly* recommend you look at them in MeshLab first since processing models to Sketchfab takes a while!

---

<!-- .slide: data-background-image="images/objFiles/objFiles.005.jpeg" data-background-size="auto 95%" -->

notes: some tips and tricks - for sketchfab be sure you select *all* files to upload

---

<!-- .slide: data-background-image="images/objFiles/objFiles.006.jpeg" data-background-size="auto 95%" -->

notes: when debugging in MeshLab when you first upload you might see some black spheres - to fix this go to the "Render" part of the tool bar and select "Color" and then "Per Mesh"

---

<!-- .slide: data-background-image="images/miscSlides/miscSlides.005.jpeg" data-background-size="auto 95%" -->

notes: if you have tried a few different models and are ready to start making things more complex, you can start adding in physically modivated sizes and planet textures to your viz

for example, depending on the mass of your star, it should have a different size and color as shown by this chart right here

---

<!-- .slide: data-background-image="images/miscSlides/miscSlides.006.jpeg" data-background-size="auto 95%" -->

notes: the same thing is true of planets - depending on their mass, they usually have different size

additionally, their mass and size determines what type of planet - is it earth like and therefore you should use a mars/earth texture?  Or is it more jupyter like and you should use a jupyter or saturn texture?

is it far out from the star and gaseous? If so, maybe a neptune texture

---

# Let's do some 3D planets with Python!


