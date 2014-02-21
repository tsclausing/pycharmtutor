"""
Authoring code in PyCharm

GOAL: Learn basic charms for efficiently authoring Python code.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.1: Moving blocks
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Because, sometimes you just need to move some code up or down.

foo()

def foo():
    """
    This function is defined after we try to call it! Oh no!
    """
    print('Move me above the call to foo()')

# 1. Place the cursor on the line `def foo():`
# 2. Cmd|Ctrl + Shift + Up

# WHAT? Did you just see that?!? PyCharm moved the whole function
# above the previous statement, adding white space and everything.

# 3. Option|Alt + Shift + Up|Down will move a single line instead
#    of the whole block.

# These commands, like all others, are easy to find with the
# Cmd|Ctrl + Shift + A charm by searching for:
# - Move Statement Up
# - Move Line Up


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.2: Comments
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Sometimes, you just need to comment or un-comment some code.

# 1. Select the lines below and execute them in the console. See
# those assertions fail!

tropical, leafy, italian = ('coconut', 'spinach', 'spaghetti')

assert 'coconut' is leafy
# assert 'coconut' is tropical
assert 'spinach' is italian
# assert 'spinach' is leafy
assert 'spaghetti' is tropical
# assert 'spaghetti' is italian

# 2. Move the cursor to the first assert statement
# 3. Hold Cmd|Ctrl and press '/' six times to toggle each assertion!

# Select and execute the assertion lines again and there will be
# no errors :)

# But comments aren't just good for turning code on and off. They're
# great for documentation. Let's work on this function's docstring:

def food_facts():
    """
    1. Place the cursor at the end of each line *in the docstring* below
       and press Ctrl + Space to complete the comment!

    Coconut is tr
    Spinach is le
    Spaghetti is ita
    """
    return {'coconut': 'tropical',
            'spinach': 'leafy',
            'spaghetti': 'italian'}

# Wowza! PyCharm will auto-complete names in comments! That's going to
# be super helpful when writing documentation.

# Let's do more completion magic ...


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.3: Code Completion
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# For a lesson on authoring code, we sure haven't done much authoring.
# Let's fix that, and let PyCharm work for us.

class Add__init__MethodToMe():
    """
    1. Add an init method below by beginning to type `def __i` and
    hitting Return|Enter to accept the method completion.
    """



    # ^^ your `def __init__(self):` code here

    # On the first line of your new __init__ method, let's call super(),
    # but let's use a builtin Live Template to remember the syntax:

    # 2. Place your cursor on the first line of your __init__ method
    # 3. Cmd|Ctrl + Shift + A
    # 4. Type 'live tem' and select "Insert Live Template"
    #    and choose the "super" option to generate a super call!

# Nice. A fast way to override predefined methods and call super.

# For fun, experiment with writing your own Live Templates and injecting
# them into this file!

# Now, let's write some code to add up the digits in a string and round to
# the nearest hundred:

digits = '123456789123456789123456789123456789'



# ^^ your code here
# Example: round(sum(map(int, digits)), -2)

# Notice that as you type function names, PyCharm auto-suggests
# functions! While the auto suggestion popup is open, hit F1
# to bring up any function's documentation!

# After you're done, place the cursor on any of the functions you
# called and press F1 to bring up docs inline. Handy!


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson 1.4: Customizing Code Completion
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# I prefer aggressive code completion, but some people don't!
# Here's how to configure auto completion to your liking:

# Cmd|Ctrl + Shift + A
# Type "code compl" and choose "Code Completion"

# Select and apply your preferences in the Code Completion settings.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lesson Recap
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# You now understand how to
# - Toggle comments
# - Auto complete names in docstrings
# - Move blocks of code around
# - Use built-in code completion
# - Get contextual function documentation
# - Configure code completion

# Alright. Now we're writing and documenting code efficiently so
# it's time to run and debug some code!


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NEXT LESSON ...
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Jump to "debugging.py" they way you got here, OR ...
#
# Double-tap the Shift key to open "Search Everywhere" and type
# "debugging.py" to jump to the file!
#
# "Search Everywhere" is a quick way to find files, classes,
# actions, and more, without knowing exactly what you're looking
# for.
