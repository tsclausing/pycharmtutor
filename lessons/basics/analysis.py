"""
Code Analysis and the Green Light

GOAL: Understand PyCharm's analysis & inspection features which help
      us write working code faster and more consistently across teams.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.1: Code analysis overview
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Let PyCharm help you prevent bugs and write clean code.

# Look in the top right corner of this editor window. See the red light?
# 1. Hover your mouse over the red light for a summary of issues in this file
# 2. Hover over and click each issue's location marker (behind the scroll bar)
# 3. Hover over each issue in the code below for an in-line summary

import functools as unused
import notfound

class Foo(Object):
    def buz(self):
        True
    def buz(self):
        open = 'open'
        print(open)

def bar():
    return True
    print(1,
         2,
        )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.2: Configuring file analysis
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# My recommendation is to leave the analysis level set at the defaults,
# however, sometimes there is a need to relax it a bit (or button it up!)

# 1. Cmd|Ctrl + Shift + A
# 2. Type "analys" and choose "Configure Current File Analysis"

# This allows you to adjust the per-file analysis level

# 3. Click "Configure Inspections" in the dialogue box
# 4. Expand the "Python" menu item and adjust to your liking

# For fun, create a new inspection profile. Profiles created here
# may be used in the next step ...


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.3: Detailed inspection
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Cmd|Ctrl + Shift + A
# 2. Type "inspec" and choose "Inspect Code"
# 3. Select the "File" radio button and a profile from Lesson 1.2 above

# Bask int he glorious wealth of warnings and errors in the Inspection
# pane. Click around in there!

# For fun, now that you know how to find all of these issues ...
# fix them and re-run the detailed inspection until they're all gone!


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson Recap
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# You now understand how to
# - View a summary of inspection issues in a file
# - Jump to inspection issues from the scroll bar
# - View in-line issue summaries
# - Adjust the per-file analysis level
# - Adjust the overall analysis level for Python code inspections
# - Run the powerful Inspection tool

# OK, I get it. You're jumping around files, interacting with the
# IDE, and responding when it points out code issues. Let's
# write some Python already!


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NEXT LESSON ...
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Jump to "authoring.py" they way you got here, OR ...
#
# Place the cursor on `authoring` on the line below

from lessons.basics import authoring
print(authoring.__file__)

# 1. Cmd|Ctrl + Shift + A
# 2. Type "decla" and choose "Declaration" to jump to the
#    next lesson!
