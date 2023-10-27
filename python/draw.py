from matplotlib import image 
from matplotlib import pyplot as plt 
import csv
import time

"""draw.py plots each crash from ma-crash-data-2.csv onto the map of Massachusetts."""

"""Each item in marks consists of latitude and longitude coordinates of a
point and its corresponding x and y coordinates on the graph. These values are
used for converting lat/lon coordinates from the crash data into x/y points on the graph
"""

marks = [[42.086114, -73.508254, 93, 936],\
        [42.071886, -70.238677, 1807, 953],\
        [42.871462, -70.817183, 1505, 372],\
        [42.745974, -73.264836, 229, 469],\
        [42.310207, -70.882847, 1476, 784],\
        [42.692683, -70.630237, 1603, 511],\
        [42.303902, -70.915115, 1451, 789]]

    
def get_y_scalar_and_origin(marks):
    """Calculates the ratio of a latitude coordinate to a y point on the graph.
    Also calculates the lat coordinate that corresponds to 0 on the graph.
    This could be accomplished with only one lat coordinate and its corresponding
    y point on the graph, but this leads to an innacurate result. Taking the average
    of many pairs of lat coordinates and their corresponding y points produces
    a more accurate result."""

    #Sum of ratios of lat cors to y points
    y_scalar_sum = 0
    #Sum of lat cors that correspond to y = 0 on the graph
    origin_lat_sum = 0
    
    for i in range(len(marks)):
        for j in range(len(marks)):
             if(i == j):
                 pass
             else:
                 sub_y_scalar = (marks[i][0] - marks[j][0]) / (marks[j][3] - marks[i][3]) 
                 y_scalar_sum += sub_y_scalar
                 origin_lat_sum += marks[i][0] + marks[i][3] * sub_y_scalar
                 
    #Average ratio of a lat cor to a y point on the graph            
    y_scalar_sum /= len(marks) * (len(marks) - 1)
    #Average lat cor that corresponds to y = 0 on the graph
    origin_lat_sum /= len(marks) * (len(marks) - 1)
    return [y_scalar_sum, origin_lat_sum]

 
def get_x_scalar_and_origin(marks):
    """Calcuates the same thing as get_y_scalar_and_origin, but for longitude
    coordinates and x points on the graph."""
    
    #Sum of ratios of lon cors to x points
    x_scalar_sum = 0
    #Sum of lon cors that correspond to x = 0 on the graph
    origin_lon_sum = 0
    for i in range(len(marks)):
        
        for j in range(len(marks)):
             if(i == j):
                 pass
             else:
                 sub_x_scalar = (marks[i][1] - marks[j][1]) / (marks[j][2] - marks[i][2])
                 x_scalar_sum += sub_x_scalar
                 origin_lon_sum += marks[i][1] + marks[i][2] * sub_x_scalar

    #Average ratio of a lon cor to a y point on the graph
    x_scalar_sum /= len(marks) * (len(marks) - 1)
    #Average lon cor that corresponds to x = 0 on the graph
    origin_lon_sum /= len(marks) * (len(marks) - 1)
    return[x_scalar_sum * -1, origin_lon_sum]


#Get the values that are used to convert lat/lon cors to x/y points on the graph
y_scalar = get_y_scalar_and_origin(marks)[0]
origin_lat = get_y_scalar_and_origin(marks)[1]
x_scalar = get_x_scalar_and_origin(marks)[0]
origin_lon = get_x_scalar_and_origin(marks)[1]


def lat_to_y(lat):
    """Converts a lat cor to a y point on the graph."""
    diff = origin_lat - lat
    return diff / y_scalar

def lon_to_x(lon):
    """Converts a lon cor to an x point on the graph."""
    diff = lon - origin_lon
    return diff / x_scalar


#Prepare to draw on the image
file_ma_crash = open('data/ma-crash-data-2.csv',newline='')
crash_reader = list(csv.reader(file_ma_crash, delimiter=',', quotechar='"'))
image = image.imread('images/map.png')


#Print tallies for types of crashes to be used in text on the image
print("total crashes: " + str(len(crash_reader)))
fatal_count = 0
injury_count = 0
for row in crash_reader:
    if(row[1].lower() == 'fatal injury'):
        fatal_count += 1
    elif(row[1].lower() == 'non-fatal injury'):
        injury_count += 1
print("fatal crashes: " + str(fatal_count))
print("injury crashes: " + str(injury_count))


#Draw on the image
for i,crash in enumerate(crash_reader[:1000]):
    #Keep track of rendering progress
    if i % 1000 == 0:
        print(i)
        print(time.perf_counter())
    #Choose color of dot based on crash type
    color = None
    if(crash[1].lower() == 'fatal injury'):
        color = 'red'
    elif(crash[1].lower() == 'non-fatal injury'):
        color = 'yellow'
    else:
        color = 'lightgray'
    #Plot each crash
    plt.plot(lon_to_x(float(crash[3])),lat_to_y(float(crash[2])),\
             marker='s',color=color, ms=0.4,markeredgewidth=0.0)

plt.axis('off')
plt.imshow(image)
plt.savefig('images/final.png',dpi=1000)
