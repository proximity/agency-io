# Agency IO

Agency IO is a digital sign in system which is simple to setup and
maintain.

1. It allows employees to tap their name to log in or out.
2. Guests to sign in
3. Tap and hold a guests name to delete them from the roster.

## Front-end

1. Install asset dependencies: `npm install`
2. Run gulp while developing `gulp watch`

## Back-end

1. Install VirtualEnv `sudo pip install virtualenv`
2. Initialize VirtualEnv `virtualenv env`
3. Install dependencies `env/bin/pip install -r requirements.txt`
4. Copy the __.env.dist__ file to __.env__ and update the parameters
5. Run dev server `env/bin/python src/manage.py runserver`
6. Create a superuser `env/bin/python src/manage.py createsuperuser`
