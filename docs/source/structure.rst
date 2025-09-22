Project Structure
=================

project main components
-----------------------

The project is organized as follows:

- **oc_lettings_site/**: main Django configuration (settings, urls, wsgi).
- **lettings/**: Django app managing property listings.
- **profiles/**: Django app managing user profiles.
- **manage.py**: Django utility script for commands (migrations, running the server, etc.).
- **docs/**: documentation generated with Sphinx.

Django models, views and urls
-----------------------------

Models :

- Address
- Letting
- Profile

Views :

- oc_lettings_site.views.index : main view for the site
- lettings.views.index : display the list of lettings
- lettings.views.letting : display the details for a letting
- profiles.views.index : display the list of the users
- profiles.views.profile : display the details for a user

URLs :

- / → base url
- /lettings/ → display lettings list
- /lettings/<int:letting_id>/ → detailed letting
- /profiles/ → plofiles list
- /profiles/<str:username>/ → details for a user
