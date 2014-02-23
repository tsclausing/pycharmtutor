"""
Debugging code in PyCharm

GOAL: Use "Run" & "Debug" configurations for great good.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.1: Running a script
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# So, here's a script to do a thing a random-ish number of times

import random


def some_thing_to_do(stuff):
    print('Doing', stuff)


def do_random_times(thing):
    n = random.randint(0, 5)
    print('About to do some thing {n} times!'.format(n=n))
    map(thing, range(n))
    print('Finished!')

do_random_times(some_thing_to_do)


# Let's run it, but not in the console this time. We're going to
# run this file as a script!

# 1. Find debugging.py in the Project pane (<-- over there!)
#    in the folder: pycharmtutor/lessons/basics/

# 2. Right click on the debugging.py file and select
#    "Run 'debugging'"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.2: Debugging a script
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The PyCharm debugger is AWESOME.

# 1. Find this line of code above:
#    do_random_times(some_thing_to_do)

# 2. Click once in the gutter to the left of that line. The line
#    should highlight red with a red dot in the gutter

# 3. Right click "debugging.py" in the Project files pane and
#    select "Debug 'debugging'"

# The "Debug" pane should have appeared below the editor and
# the script should be paused at the call to `do_random_times`

# Let's step through our script!

# 1. In the Debug pane, find the "Step Into" icon and click it
#    I'm not telling you where it is so that you have to look
#    around :)

# You're now inside the call to `do_random_times`. Step Into
# will take you inside function calls both in your script and
# in your dependencies. It's easy to go down the rabbit hole and
# forget how you got there ...

# 2. Stop debugging by clicking on the Stop button in the Debug pane
# 3. Start debugging again, but this time click the Step Over icon

# Nothing happened? YES, it did. The debugger ran `do_random_times`
# and the script finished.

# 4. Click the Console tab in the Debug pane to see the output!


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.3: Run Configurations
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# We'll talk about Run and Debug configurations in detail in a
# future lesson. For now,look for a drop-down menu in the top
# right corner of the IDE, above the editor. The selected item
# should be "debugging".

# 1. Click the drop-down and select "Edit Configurations..."
# 2. You're now viewing the Debug Configuration named "debugging"
# 3. Poke around a bit, and hit Cancel

# Run and Debug Configurations can do a lot of things every time
# you run or debug your scripts:
# * Pass params to the script
# * Set up an environment
# * Run with a specific Python interpreter
# * Run from a different current working directory
# * Add stuff to the PYTHONPATH
# * And act as a sort of build tool: run outside scripts or chain
#   Configurations to accomplish a more complex task.

# To run a specific configuration, just select it from the
# drop-down menu and click the Green play button. That's it.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson Recap
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# You now understand how to
# - Run any script in your project from the Project files pane
# - Set breakpoints and debug any file
# - Step into and step over function calls
# - Basic Run & Debug configurations (and what they can do!)

# For fun, take a look at the Run Configuration that was created
# early on when we ran the pycharmtutor Unit Tests!


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NEXT LESSON ...
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# That's it for now :(

# If you found this helpful or interesting, please help grow the
# lesson count by forking and submitting a pull request!
