This web application is intended to mimic a google search page. You enter text into the search bar and hit enter and you are taken to another page that reflects your search in the search bar at the top of the page. I designed this based on how web app looks on my laptop, but resizing the page does move the text box and not the background image making it look a lot less realistic. If I were to add on to this I would work on making all the elements dynamically resize. But that was beyond the scope of this project.

To run this app create a flask-app directory. Within that directory create two subdirectories: static, and templates. The css files and background images should go in the /static directory and the html files should go in the /templates directory. The flask.app belongs in the main /flask-app directory.  

Once you have your flask environment set up, you can run this app from the /flask-app directory with the command flask run
