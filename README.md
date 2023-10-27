![map of massachusetts car crashes in 2021](/final.png)
# Project Description
This poster shows all car crashes that happened in 2021 in Massachusetts. Each dot represents a crash, and the color of the dot represents the severity of the crash.
I used Python to visualize the data on the poster from a dataset, and I used Gimp to edit the image.

# Project Purpose
I created this poster so that I could practice writing in Python, as well as to create something that I'm proud of and can show to other people. I originally planned only
to create the map of crashes with no text. But, I wanted anyone looking at this poster to take something away from it. So, I wrote a message about
the danger and consequences of cars and the right direction to move in. The idea of transitioning faster to alternative and safer modes of transportation was 
the original motivation behind looking at car crash data, so I wanted this poster to send that message.

# Project Workflow and Interesting Challenges/Notes
1. Download table of all car crashes in Massachusetts in 2021 as ma-crash-data-0.csv
3. Clean data and save it as ma-crash-data-1.csv
   **- A small but significant amount of the crashes in this dataset did not have coordinates for where the crash happened, but every crash had a town name. The best way that I could find around this was to download a list of all towns in Massachusetts and their coordinates. I used that data along with a slight random factor to get a point that I could show on the map of where the crash roughly was.**
5. Download table of all towns in Massachusetts and their coordinates as ma-cors.txt
6. Write modify-cors.py to use ma-cors.txt and ma-crash-data-1.csv to create ma-crash-data-2.csv
7. Edit ma.png to create the image to render the crashes on, map.png
8. Write draw.py to render the data from ma-crash-data-2-csv. onto map.png
   **- When converting the coordinate data from the crashes, I used two points on the map to determine how to convert the coordinates to points that I would graph on the map. I got the coordinates of those point from google maps, and the locations on the plot from the map image. This ended up in all of the crashes being plotted on the map incorrectly and the entirety of the dots being skewed. I realized that using just two points wasn't precise enough to get an accurate number to convert from longitutde/latitude coordinates to points on the graph. So, I gathered many more points to calculate how to convert them, and this fixed the problem. **
10. Make final edits to the image
    **- A small amount of dots were outside of the border of Massachusetts due to the random calculation of some crash coordinates (see images/render.png). This was inevitable, and unless I spent a lot more time quantifiying the entire border of Massachusetts and writing a lot more code, those dots had to exist. I decided with the scope of the project, that was not worth it. I simply erased them in Gimp since a few crashes don't not make a significant difference in the image.**
