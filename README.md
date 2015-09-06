Markup : ##PennAppsXII Healthy Router##

This web app takes a Philadelphia address and returns the nearest bicycle rental station, and a link from that station to the nearest 1) farmer's market, and 2) healthy corner store. All three datasets were provided by OpenPhillyData at OpenPhillyData.org. The purpose of the application is to help improve high levels of obesity by offering Philadelphians:

    1. Healthy eating options
    2. Light, enjoyable exercise options

![Alt text](/img/DemoHome.png?raw=true)

The application was built on Flask, with all database queries and processing done through MongoDB. The most important aspect of this project was geospatial indexing, a feature of MongoDB which allowed for proximity-based calculations to be made. The only geospatial feature for which another resource had been used was for geocoding-- i.e., retreiving the initial latitude and longitude coordinates from the user's input. For this I used the OpenCage Geocoder API through Python's GeoPy client.

![Alt text](/img/DemoRoute1.png?raw=true)

Visualization was done primarily through Folium, a python package which allows python data to be visualized using Leaflet.js.

![Alt text](/img/DemoRoute2.png?raw=true)
![Alt text](/img/DemoRoute3.png?raw=true)
![Alt text](/img/DemoRoute4.png?raw=true)

Future improvements in mind include bike-path expansion using bike-path datasets provided (currently there are minimal bikepaths shown in proximity), additional nodes such as parks in proximity to markets or bike stations, shortest-path bike travel. 
