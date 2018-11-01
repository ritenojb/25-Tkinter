"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # TODO: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root =tkinter.Tk()

    # ------------------------------------------------------------------
    # TODO: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame = ttk.Frame(root, padding=20)
    frame.grid()
    # ------------------------------------------------------------------
    # TODO: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    button = ttk.Button(frame, text='Button')
    button.grid()
    # ------------------------------------------------------------------
    # TODO: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    printing_button = ttk.Button(frame, text='Greeting')
    printing_button['command'] = (lambda: print_greeting())
    printing_button.grid()
    # ------------------------------------------------------------------
    # TODO: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    my_entry_box= ttk.Entry(frame)
    my_entry_box.grid()

    entry_button = ttk.Button(frame, text='Print Entry')
    entry_button['command'] = (lambda: print_contents(my_entry_box))
    entry_button.grid()
    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    second_entry_box = ttk.Entry(frame)
    second_entry_box.grid()
    second_entry_button = ttk.Button(frame, text='Print Multiples')

    second_entry_button.grid()
    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.mainloop()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
def print_greeting():
    print('Hello')

def print_contents(entry_box):
    contents_of_entry_box = entry_box.get()
    print(contents_of_entry_box)

def print_multiples(second_entry_box):
    s = second_entry_box.get()
    n = int(s)


main()
