# chat-app
This is a simple chat app built with Django, Tailwind, and jQuery.

How to start the app
-

To start the app, open two separate terminal windows and follow these steps:

1. In the first terminal window, navigate to the project directory and run `python manage.py runserver`. This will start the Django development server and serve the app on your localhost.
2. In the second terminal window, navigate to the project directory and run `python manage.py tailwind start`. This will start the Tailwind compiler and watch for changes to your CSS files.

Troubleshooting:
-

  ### Storing the Django secret key
  
  To store the Django secret key securely, you can follow these steps:

  1. Generate a new secret key using a secure random generator.
  2. Store the secret key in an environment variable or in a separate file that is not tracked by version control.
  3. Load the secret key in your Django settings file using os.environ.
  
  You can also watch this [video guide](https://www.youtube.com/watch?v=bPR3Q0BFFzw&ab_channel=ZackPlauch%C3%A9) or read this [StackOverflow post](https://stackoverflow.com/questions/15209978/where-to-store-secret-keys-django) for more information.

  ### Tailwind installation guide 
   
  If you encounter any issues while installing Tailwind, you can refer to this [installation guide](https://django-tailwind.readthedocs.io/en/latest/installation.html) for help.
  


  ### jQuery 
   
  To add jQuery functionality to your app, you can download the latest version from the  [official website](https://releases.jquery.com/)<br>
  
  For example, to add a like button functionality, you can add a click event listener to the button and use jQuery to send an AJAX request to your Django backend.
 
  ### Collecting static files

  If you make any changes to your static files (e.g., CSS, JavaScript), you will need to run `python manage.py collectstatic` to collect all the files into the static directory.

  ### Math filters

  If you need to perform math operations in your Django templates, you can use the `django-mathfilters` library. You can install it using the command `pip install django-mathfilters`.