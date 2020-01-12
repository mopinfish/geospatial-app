# Geodjango

This app is based on the [geodjango tutorial](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/).
To set-up and run it, you have to install [Compose](https://docs.docker.com/compose/install/)

## Set-up the project

*Migrate the database*

    $ docker-compose run web python manage.py migrate

*Load the data*

    $ docker-compose run web python manage.py shell
    >>> from world import load
    >>> load.run()

*Create a super user*

    $ docker-compose run web python manage.py createsuperuser

## Run the project

*Get the container IP*

For Linux users, you can simply use `localhost`.

*Run the app*

Now you can run the app with:

    $ docker-compose up

and browse http://localhost:8000/admin