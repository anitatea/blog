title: Can you doodle with Python?
Date: 2019-12-23
Slug: turtle
image: /images/blog/blog_2.jpeg

<!-- https://images.pexels.com/photos/1051075/pexels-photo-1051075.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260 -->


Throughout all my years in elementary school to engineering at UofT, my notes have always been decorated with swirls, spirals and circular doodles. Well now all my notes are now digital... but my noodle still wants to doodle.

<img src= 'https://i.kym-cdn.com/photos/images/original/001/152/468/e60.png' width='200'>

Let's see how we can do this with Python. Math can help us do the trick.

### [The Recamán Sequence](http://mathworld.wolfram.com/RecamansSequence.html)

Let me introduce: The Recamán Sequence. It features a simple sequence of integers, which processed with Python, can produce some beautiful doodles.

Here are the rules:
1. Start at zero.
2. Every step you take will be 1 more than the last step.
3. If it’s possible to step backward (negatively), do so. Backward steps are only allowed if the resulting location is positive (greater than zero) and if that number has not occurred in our sequence yet. Otherwise step forward.

Here's an example. Let's look at the beginning of the sequence:
Start at zero.
- 0

Our step size will be 1. Stepping backward would put us at -1 (from 0) which is not allowed. We step forward.
- 0 -> 1

Next step size is 2. Stepping backward would put us at -1 (from 1) therefore we will step forward again.
- 0 -> 1 -> 3

### Turtle Graphics
A relatively simple library, using a relative cursor (the 'turtle') which we will be following on a Cartesian plane. It has three attributes: location, orientation and a pen (the 'turtle').
Anyone with Python can get started with Turtle! It's already pre-packaged in the Python standard library.

### The Code
First, let's import the library and set-up our drawing canvas.


```python
import turtle
window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
doodle = turtle.Turtle()  # A good name for our turtle
doodle.shape("turtle")
doodle.speed(10)
scale = 5  # Not a turtle setting - used to scale the drawing
```

Now I'll move our turtle pen to start on the left. This will give our turtle more room to work with.


```python
doodle.penup()
doodle.setpos(-390, 0) # Set on a Cartesian plane, e.g. (x,y)
doodle.pendown()
```

A few other housekeeping items.


```python
doodle.color('navy') # Our pen color
doodle.fillcolor('black') # Our turtle color

current = 0   # Here's how we know where we are
seen = []  # A list to keep track of where we've been
```

Take a step forward if our result is positive and if we have not been there before.


```python
# Step increases by 1 each time
for step_size in range(1, 100):

    backwards = current - step_size

    # Step backwards if its positive and we've never been there before
    if backwards > 0 and backwards not in seen:
        doodle.setheading(90)  # 90 degrees is pointing straight up
        # 180 degrees means "draw a semicircle"
        doodle.circle(scale * step_size/2, 180)
        current = backwards
        seen.append(current)

    # Otherwise, go forward
    else:
        doodle.setheading(270)  # 270 degrees is straight down
        doodle.circle(scale * step_size/2, 180)
        current += step_size
        seen.append(current)

turtle.done()
```

<img src= 'https://github.com/anitatea/blog/blob/master/content/images/turtle.png?raw=true'>

<img src= 'https://github.com/anitatea/blog/blob/master/content/images/turtle_vid.gif?raw=true'>

All done! The concatenated code for this article is below for your reference to try the whole thing by yourself.


```python
import turtle
window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
doodle = turtle.Turtle()  # A good name for our turtle
doodle.shape("turtle")
doodle.speed(0)
scale = 5  # Not a turtle setting - used to scale the drawing

doodle.penup()
doodle.setpos(-390, 0)
doodle.pendown()

doodle.color('navy')
doodle.fillcolor('black')

current = 0   # Here's how we know where we are
seen = []  # A list to keep track of where we've been

# Step increases by 1 each time
for step_size in range(1, 100):

    backwards = current - step_size

    # Step backwards if its positive and we've never been there before
    if backwards > 0 and backwards not in seen:
        doodle.setheading(90)  # 90 degrees is pointing straight up
        # 180 degrees means "draw a semicircle"
        doodle.circle(scale * step_size/2, 180)
        current = backwards
        seen.append(current)

    # Otherwise, go forwards
    else:
        doodle.setheading(270)  # 270 degrees is straight down
        doodle.circle(scale * step_size/2, 180)
        current += step_size
        seen.append(current)

turtle.done()
```
