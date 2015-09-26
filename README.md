
#Flask-Project-Creator
Creates a scalable folder structure for your Flask app in seconds 

example usage:

    path = r"C:\Users\Hello\Desktop"
    project_name = "Music"
    project  = ClassBasedProject(folder_location = path, folder_name = project_name)
    project.create_project("indexpage","aboutpage","homepage")

output:

    _\Music
	    _\apps
	    -__init__.py
		    -\Music
		    -__init__.py
			    -\indexpage
				    -__init__.py
				    -routes.py
			    -\aboutpage
				    -__init__.py
				    -routes.py
			    -\homepage
				    -__init__.py
				    -routes.py				    
	    -\static
		    -\css
			    -\Music
				    -indexpage.css
				    -aboutpage.css
				    -homepage.css
		    -\font
		    -\img
	    
	    -\templates
		    -\Music
			    -indexpage.html
			    -aboutpage.html
			    -homepage.html
	    -run.py
	    -__init__.py

you there are also other methods:
such as :

 - add_app
 - delete_app
 - add_page
 - delete_page


**add_app** takes key-value pairs of an app name and it's pages
the pages have to be inclosed in a brace **[]** like below:

    project.add_app(New_App = ["new_page","new_page2"])

**delete_app** is the opposite of add_app it takes any number of apps you have in your project as it's arguments



    project.delete_app("App_to_be_deleted","App_to_be_deleted2")

**add_page** adds a new page to the app you specifiy it takes a key-value pair of an app and the pages you want to add inside a brace

    project.add_page(Music = ["new_added_page",new_added_page2"]

**delete_page** does the opposite of **add_page** but still takes a  key-value pair of an app name and the pages to be deleted enclosed in a brace

    project.delete_page(App_name = ["page_to_delete",page_to_delete2"]

 



   

    