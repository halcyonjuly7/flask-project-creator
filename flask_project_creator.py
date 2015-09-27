import re
import os
from project_creator import *

clear = lambda: os.system("cls")

print("""
Welcome to the flask project creator. When asked about the pages to be created please 
use this format: home_page, profile_page, index_page, that is name whatever you want the page
to be followed by an underscore then page i.e. '_page'\n\n """)



print("""
What would you like to do today?
choose a number:

1.create a project?
2.add an app to an existing project?
3.delete an app of an existing project?
4.add a page or pages to an existing app?
5 delete a page or pages of an existing app?
""")

choice = int(input("choice: "))

while choice not in (1,2,3,4,5):
	choice = int(input("""

It seems you did not choose a number within th choices.

choose a number:

1.create a project?
2.add an app to an existing project?
3.delete an app of an existing project?
4.add a page or pages to an existing app?
5 delete a page or pages of an existing app?
"""))



clear()
choice_action(choice)










	



    
