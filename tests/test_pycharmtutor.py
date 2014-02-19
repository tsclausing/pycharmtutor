import sys
import unittest
import warnings

from lib import string

IS_MAC = sys.platform == 'darwin'


class TestSetup(unittest.TestCase):

    def test_os(self):
        """
        Warn (but pass) if not running on OS X
        """
        if not IS_MAC:
            message = string.lstripml('''
            ********
            Warning: pycharmtutor has lacking support and documentation for non-mac systems.
            ********''')
            warnings.warn(message)
        pass

    def test_python_path(self):
        """
        Ensure the pycharmtutor project is on the Python path
        """
        assert [p for p in sys.path if 'pycharmtutor' in p]

    #
    # the following tests are run for their side effects only
    #

    def test_welcome_message(self):
        go_to_file_shortcut = 'Cmd + Shift + O' if IS_MAC else 'Ctrl + Shift + N'

        print(string.lstripml("""
            START HERE ... LESSON 1 BELOW ...

            =============================================================
            =  W e l c o m e   t o   t h e   P y C h a r m   T u t o r  =
            =============================================================

            PyCharm is a very powerful editor that has many features,
            too many to explain in a tutor such as this. The tutor is
            designed to describe enough of the features that you will
            be able to easily use PyCharm as an all-purpose Python IDE.

            The approximate time required to complete the tutor is 60
            minutes, depending upon how much time is spent with
            experimentation.

            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Lesson 1:  IDENLIGHTENMENT

            Press the keyboard shortcut below to open the "Go to file"
            quick navigation:

            {go_to_file_shortcut}

            Start typing the title of this lesson and hit return to
            open "idenlightenment.py" from lessons/basics/

            Now, just follow the instructions in the file!
        """.format(
            go_to_file_shortcut=go_to_file_shortcut,
        )))
