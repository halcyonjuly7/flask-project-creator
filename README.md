

Flask-Project-Creator
---------------------
**What is Flask-Project-Creator?**
Flask-Project-Creator is a boiler plate template for your flask app
packed with many features. It creates a scalable, manageable and modular folder structure so your app structure won't be a mess. Inspired by the recommended app structure for scalable apps on Miguel Grinbergs  O'reilly Video "An Introduction to flask".

**Flask-Project-Creator Features**:

 - flask-admin integration with a different look and an admin login page included
 - celery integration
 - flask-socketio integration
 - add an app and even specify the pages you want for that app
 - auto blueprint registration when you add an app
 - auto views file  update when you add a page 
 - auto create html files and css files for every page you create




**Why use Flask-Project-Creator**?

 - if you're tired of creating the same boilerplate over and over again
 - if you'd want to focus on getting down to the nitty gritty of making your app
 - if you want a sane, scalable, and modular folder structure for you flask project


**How to use  Flask-Project-Creator?**

just run the **flask_project_creator.py** inside the folder after you've downloaded or cloned this project. 

**Example**:

Creating a project called **Music_Store** with an app of **music** and the pages of
 **index, about, home**

  

**output:**

	
	
	config/
		config.py
	
	celery_workers.py
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
		
		misc_files/
			helper_functions.py
			workers.py
			socketio.py
	
		static/
			admin/
				css/
					index.css
					sb2admin.css
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
			admin/
				master.html
				
			admin_templates/
				admin_login.html
				admin_base.html
				
			base_templates/
				music_base.html
				
			macros_template/
				macros.html
				
			error_templates/
				400.html
				401.html
				500.html
				
			music/
				index.html
				about.html
				home.html
		
		
	
	
				
		
	


----------


so what happened to the pages you specified? the pages are already written in you views.py file inside the appropriate app folder

> please note that pywin32com is needed if you want to launch your project after you created it. If you haven't downloaded it yet. download it here http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/

The options when you run **flask_project_creator.py** are:

 - add an app/apps
 - delete an app/apps
 - add a page/pages






----------
**ALL ARGUMENT NEED NOT BE ENCLOSED IN QOUTES**

**add an app/apps** takes key-value pairs of an app name and it's pages
the pages have to be inclosed in a brace **[]** and if you want to add multiple apps separate the key-value pairs by a comma like below:

> this option automatically registers each app on the root \__init__.py
> each app is a blueprint and the blueprint name is the app name you specified.  

*Single app*:

> if you want top level access to your routes you should specify an app called **main** this app will be the top most routes of your app. If you want to have an **index** page for each of your apps then give index as one of the app's value,


    main = [index, contacts]
*Multiple apps*:

    main = [index, contacts],
    careers = [index, search, jobs]
    


----------


**delete an app/apps** is the opposite of **add an app/apps** it takes any number of apps you have in your project as it's arguments and deletes it

> this option also automatically removes the registered app from the root \__init__.py file as well remove the static and templates folder containing the app

*Single app:*

	main 
*Multiple apps:*

    main, careers


----------


**add a page/pages ** adds a new page to the app you specifiy it takes a key-value pair of an app and the pages you want to add inside a brace **[]** 

> this option also automatically adds the page in the views.py file
> of the approriate app as well as create  a css and an html file for each added page

*Single app add page:*
   

     services = [index, showcase]

*Multiple apps with multiple pages:*

    services = [index, showcase], 
    accounts = [index, settings]
  
  


----------




 



   

    