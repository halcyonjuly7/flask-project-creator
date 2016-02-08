import re
import os
from project_creator.choice_helpers import ChoiceHelpers

clear = lambda: os.system("cls")

print("""                                                                                                                                  
                                                                                                                                     
                                                                                                                                     
                                                                                                                                     
                                                                                                                                     
                                                                                                                                     
 _______  __           ___           _______. __  ___    .______   .______        ______          __   _______   ______ .___________.
|   ____||  |         /   \         /       ||  |/  /    |   _  \  |   _  \      /  __  \        |  | |   ____| /      ||           |
|  |__   |  |        /  ^  \       |   (----`|  '  /     |  |_)  | |  |_)  |    |  |  |  |       |  | |  |__   |  ,----'`---|  |----`
|   __|  |  |       /  /_\  \       \   \    |    <      |   ___/  |      /     |  |  |  | .--.  |  | |   __|  |  |         |  |     
|  |     |  `----. /  _____  \  .----)   |   |  .  \     |  |      |  |\  \----.|  `--'  | |  `--'  | |  |____ |  `----.    |  |     
|__|     |_______|/__/     \__\ |_______/    |__|\__\    | _|      | _| `._____| \______/   \______/  |_______| \______|    |__|     
                                                                                                                                     
                       ______ .______       _______      ___   .___________.  ______   .______                                       
                      /      ||   _  \     |   ____|    /   \  |           | /  __  \  |   _  \                                      
                     |  ,----'|  |_)  |    |  |__      /  ^  \ `---|  |----`|  |  |  | |  |_)  |                                     
                     |  |     |      /     |   __|    /  /_\  \    |  |     |  |  |  | |      /                                      
                     |  `----.|  |\  \----.|  |____  /  _____  \   |  |     |  `--'  | |  |\  \----.                                 
                      \______|| _| `._____||_______|/__/     \__\  |__|      \______/  | _| `._____|                                 


""")                                                                                                          
print("""
What would you like to do today?
choose a number:

1.create a project?
2.add an app/apps?
3.delete an app/apps?
4.add a page/pages?
5.add api/api's
6.add api endpoint/endpoints
""")

choice = int(input("choice: "))

while choice not in (1, 2, 3, 4, 5, 6):
	choice = int(input("""

It seems you did not choose a number within th choices.

choose a number:

1.create a project?
2.add an app/apps?
3.delete an app/apps?
4.add a page/pages?
5.add api/api's
6.add api endpoint/endpoints
"""))


clear()
choosen_number = ChoiceHelpers(choice)
choosen_number.choice_action()

clear()









	



    
