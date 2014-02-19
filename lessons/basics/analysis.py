"""
Code Analysis and the Green Light

GOAL: Understand PyCharm's analysis & inspection features which help
      us write working code faster and more consistently across teams.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.1: Code analysis overview
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Hover your mouse over the red light for a summary of issues
# 2. Hover and click each issue's location marker behind the scroll bar
# 3. Hover over each issue in the code for an in-line summary

import functools as unused
import notfound

class Foo(Object):
    def buz(self):
        pass
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
# however, sometimes there is a need to relax a bit.

# 1. [Cmd|Ctrl] + Shift + A
# 2. Type "analys" and choose "Configure Current File Analysis"

# This allows you to adjust the per-file analysis level

# 3. Click "Configure Inspections" in the dialogue box
# 4. Expand the "Python" menu item and adjust to your liking

# For fun, create a new inspection profile. Profiles created here
# may be used in the next step ...


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.3: Detailed inspection
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. [Cmd|Ctrl] + Shift + A
# 2. Type "inspec" and choose "Inspection"

# Run your profile against this file and bask int he glorious wealth
# of warnings and errors.

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NEXT LESSON ...
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TODO: next lesson
