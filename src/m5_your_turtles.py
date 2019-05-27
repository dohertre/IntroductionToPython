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
maroonturtle.pen = rg.Pen('maroon', 5)
maroonturtle.speed = 50

olivegreenturtle = rg.SimpleTurtle('turtle')
olivegreenturtle.pen = rg.Pen('pale green', 3)
olivegreenturtle.speed = 30

size = 60

for m in range(18):
    maroonturtle.draw_square(size)

    maroonturtle.pen_up()
    maroonturtle.left(20)
    maroonturtle.pen_down()

for o in range(18):
    olivegreenturtle.forward(70)

    olivegreenturtle.pen_up()
    olivegreenturtle.left(10)
    olivegreenturtle.pen_down()

    olivegreenturtle.forward(10)

    olivegreenturtle.pen_up()
    olivegreenturtle.left(80)
    olivegreenturtle.pen_down()

    olivegreenturtle.forward(10)

    olivegreenturtle.pen_up()
    olivegreenturtle.left(10)
    olivegreenturtle.pen_down()

    olivegreenturtle.forward(70)


window.close_on_mouse_click()



