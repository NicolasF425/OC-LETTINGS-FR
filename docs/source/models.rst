Models and database structure
=============================

Database : SQLite for the developpement

Model : Letting
---------------

Application : lettings

Fields :

title : string

address (foreigne key) : Address linked to this letting

Model : Address
---------------

Adress field for a letting

fields : 

number : integer

street : string

city : string

state : 2 caracters

zip_code : integer

country_iso_code : 3 caracters

Model : Profile
---------------

Based on the Django User model. Application : profiles.

fields :

user : foreign key to a Django User model

favorite_city : string
