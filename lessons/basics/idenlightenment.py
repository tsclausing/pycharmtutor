"""
IDEnlightenment

A handful of simple charms to help you along your journey.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.1: Find Any Command
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# You arrived here after running the tests by following the instructions
# in the README file, right? Either way, let's run them again ... but this
# time we'll try out PyCharm's *built-in Python console* and learn a sweet
# new charm.

# 1. Select the following two lines of code with the mouse
import unittest
unittest.TextTestRunner().run(unittest.defaultTestLoader.discover('tests'))

# 2. Press the "Find any action" keyboard shortcut
# - Mac users press: Cmd + Shift + A
# - Win users press: Ctrl + Shift + A

# 3. Type "execute selec" and choose "Execute selection in console"

# Whoa! You just ran code from a file IN PyCharm, IN a Python Console.
# That was awesome.

# Commit the two things you just learned to memory:
# - You can find *ANY* command in PyCharm with [Cmd|Ctrl] + Shift + A
# - You can play with Python code from your project files interactively!


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.2: Terminal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Even with all of PyCharm's great features, there are still times when
# it's helpful to drop to a command line to get something done.

# 1. [Ctrl|Cmd] + Shift + A
# 2. Type "open ter" and choose "Open Terminal"
# 3. Run the tests *again* by running the following in your terminal
# python -m unittest discover tests

# Sweet! We've run the tests three ways now, so you don't *ever* have
# an excuse again for not running tests in your projects :)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.3: Keymap Cheat Sheets
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PyCharm loves keyboard shortcuts. Grab a Keymap Cheat Sheet for your OS here:
import webbrowser
webbrowser.open('http://www.jetbrains.com/pycharm/webhelp/keymap-reference.html')

# The pycharmtutor lessons will probably refer to [Cmd|Ctrl] + Shift + A
# actions instead of specific keyboard shortcuts in order to keep things
# simple for all users. Use the cheat sheet for you OS for details.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson Recap
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# So, you've only been using PyCharm for 5 minutes and you've already:

# - Run unit tests with PyCharm's awesome test runner
# - Jumped to this lesson file with a keyboard shortcut
# - Learned a charm to find *any* action in PyCharm
# - Ran selected Python code in an embedded Python console
# - Ran unit tests from the command line *in* PyCharm
# - Downloaded a keymap cheat sheet for your OS

# Whoa.

# For fun, take a few minutes to hack on the "find any action" input
# until you stumble across more great features.