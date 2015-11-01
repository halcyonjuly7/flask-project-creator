

Flask-Project-Creator
---------------------

Creates a scalable folder structure for your Flask project in seconds 

just run the **flask_project_creator.py** inside it's folder after you've downloaded or cloned this project

**example**:

Creating a project called **Music_Store** with an app of **music** and the pages of
 **index,about,home**

  

**output:**

	
	
	config/
		config.py
	
	run.py
	
	Music_Store/
		__init__.py
		apps/
			admin/
				admin_views.py
				admin_forms.py
				admin_models.py
			music/
				forms.py
				views.py
				models.py
		static/
			admin/
				css/
				img/
				font/
				scripts/
				
			music/
				css/
					index.css
					about.css
					home.css
				img/
				font/
				scripts/
		templates/
			admin_templates/
			base_templates/
			music/
				index.html
				about.html
				home.html
		
		
	
	
				
		
	

so what happened to the pages you specified? the pages are already written in you views.py file inside the appropriate app folder

> please note that pywin32com is needed if you want to launch your project after you created it. If you haven't downloaded it yet. download it here http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/

The options when you run **flask_project_creator.py** are:

 - add an app/apps
 - delete an app/apps
 - add a page/pages






----------
**ALL ARGUMENT NEED NOT BE ENCLOSED IN QOUTES**

**add an app/apps** takes key-value pairs of app name and it's pages
the pages have to be inclosed in a brace **[]** and if you want to add multiple apps separate the key-value pairs by a comma like below:

> this option also automatically registers each app on the root \__init__.py
> each app is a blueprint and the blueprint name is the app name you specified

*Single app*:

    New_App = [new_page, new_page2]
*Multiple apps*:

    New_App = [new_page, new_page2], New_App2 = [new_page]
    


----------


**delete an app/apps** is the opposite of **add an app/apps** it takes any number of apps you have in your project as it's arguments and deletes it

> this option also automatically removes the registered app from the root \__init__.py file as well remove the static and templates folder containing the app

*Single app:*

	App_to_be_deleted
*Multiple apps:*

    App_to_be_deleted, App_to_be_deleted2


----------


**add a page/pages ** adds a new page to the app you specifiy it takes a key-value pair of an app and the pages you want to add inside a brace **[]** 

> this option also automatically adds the page in the views.py file
> of the approriate app as well as create  a css and an html file for each added page

*Single app add page:*
   

     App = [new_added_page, new_added_page2]

*Multiple apps with multiple pages:*

    App = [new_added_page,new_added_page2], 
    App2 = [new_page]
  
  


----------




 



   

    