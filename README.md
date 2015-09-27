

Flask-Project-Creator
---------------------

Creates a scalable folder structure for your Flask project in seconds 

just run the **flask_project_creator.py** inside it's folder after you've downloaded or cloned this project

**example**:

Creating a project called **Music** with the pages of
 **indexpage,aboutpage,homepage**

  

**output:**

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
		-\config
			-config.py				    
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

The options when you run **flask_project_creator.py** are:

 - add an app/apps
 - delete an app/apps
 - add a page/pages
 - delete a page/pages





----------
**ALL ARGUMENT NEED NOT BE ENCLOSED IN QOUTES**

**add an app/apps** takes key-value pairs of app name and it's pages
the pages have to be inclosed in a brace **[]** and if you want to add multiple apps separate the key-value pairs by a comma like below:
*Single app*:

    New_App = [new_page,new_page2]
*Multiple apps*:

    New_App = [new_page,new_page2],New_App2 = [new_page]
    


----------


**delete an app/apps** is the opposite of **add an app/apps** it takes any number of apps you have in your project as it's arguments and deletes it

*Single app:*

	App_to_be_deleted
*Multiple apps:*

    App_to_be_deleted,App_to_be_deleted2


----------


**add a page/pages ** adds a new page to the app you specifiy it takes a key-value pair of an app and the pages you want to add inside a brace **[]**

*Single app add page:*
   

     App = [new_added_page,new_added_page2]

*Multiple apps add page:*

    App = [new_added_page,new_added_page2],App2 = [new_page]
  
  


----------


**delete a page/pages** does the opposite of **add a page/pages** but still takes a  key-value pair of an app name and the pages to be deleted enclosed in a brace

*Single app delete page:*
 

     App = [page_to_delete,page_to_delete2]

*Multiple app delete page:*

    App = [page_to_delete,page_to_delete2], App2 = [page]

 



   

    