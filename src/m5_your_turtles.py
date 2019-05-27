"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Rebekah Doherty.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

maroonturtle = rg.SimpleTurtle('turtle')
maroonturtle.pen = rg.Pen('maroon', 6)
maroonturtle.speed = 50

plumturtle = rg.SimpleTurtle('turtle')
plumturtle.pen = rg.Pen('plum', 5)
plumturtle.speed = 50

slategreyturtle = rg.SimpleTurtle('turtle')
slategreyturtle.pen = rg.Pen('slate grey', 3)
slategreyturtle.speed = 150

midnightblueturtle = rg.SimpleTurtle('turtle')
midnightblueturtle.pen = rg.Pen('midnight blue', 7)
midnightblueturtle.speed = 50

size1 = 60
size2 = 120

for s in range(50):
    slategreyturtle.forward(20)

    slategreyturtle.pen_up()
    slategreyturtle.left(90)
    slategreyturtle.pen_down()

    slategreyturtle.forward(20)

    slategreyturtle.pen_up()
    slategreyturtle.left(90)
    slategreyturtle.pen_down()

    slategreyturtle.forward(20)

    slategreyturtle.pen_up()
    slategreyturtle.left(90)
    slategreyturtle.pen_down()

    slategreyturtle.forward(15*s)


for b in range(50):
    midnightblueturtle.forward(50)

    midnightblueturtle.pen_up()
    midnightblueturtle.left(120)
    midnightblueturtle.pen_down()

for p in range(18):
    plumturtle.draw_square(size2)

    plumturtle.pen_up()
    plumturtle.left(20)
    plumturtle.pen_down()

for m in range(18):
    maroonturtle.draw_square(size1)

    maroonturtle.pen_up()
    maroonturtle.left(20)
    maroonturtle.pen_down()



window.close_on_mouse_click()



