# function that prints a single line
def new_line():
   print()

# function that prints three lines by calling new_line() function
def three_lines():
   new_line()
   new_line()
   new_line()

# function that prints nine lines by calling three_lines() function
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# function that prints 25 lines by calling 2 nine_lines(), 2 three_lines() and a new_line() function
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

# function call to clear_screen() function
clear_screen()
    
    
