# TFA_Project_2020_Spring

### Group Information
UNIs: [xw2697,xm2237]

Group name: Project Group 18

The link to the server running my application: https://xw2697.uk.r.appspot.com/

### What is it?
This Django based web framework tries to keep tracks of all the known squirrels and plans to start with Central Park. 
The data used are from the 2018 Central Park Squirrel Census. The web contains Apps such as map and sightings. 
From map, users can have a view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.
From sightings, users can get a view of lists all squirrel sightings with links to view each sighting, a view to
a particular squirrel and general stats about the sightings.


### Detailed Features
This web framework includes views:

* A map that displays the location of the squirrel sightings. Located at: /map

* A view lists all squirrel sightings and corresponding links to view each sighting. 
It has fields: (1)Unique Squirrel ID, (2)Date and (3)Link to unique squirrel sighting. Located at: /sightings

* A view to update a particular sighting. It has fields: (1)Latitude, (2)Longitude, (3)Unique Squirrel ID, (4)Shift, 
(5)Date and (6)Age. Located at: /sightings/<unique-squirrel-id>

* A view of general stats about the sightings. It includes infomations: (1)Total number of squirrels, 
(2)Total numbers and percentages of different Shifts, (3)Missing data infomation about Shifts,
(4)Total numbers and percentages of different Ages, (5)Missing data infomation about Ages.
Located at: /sightings/stats


### Where to get it?
The source code is currently available on GitHub at: https://github.com/xw2697/TFA_Project


### Dependencies
All necessary dependencies are specified in the requirements.txt
