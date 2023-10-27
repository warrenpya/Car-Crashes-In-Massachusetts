import csv
import random

""" modify-cors.py finds every crash in ma-crash-data-1.csv that does not
have longitude and latitude coordinates. It then generates approximate
coordinates for the crash using the crash's town name and data from
ma-cors.txt,and writes the updated crash data to ma-crash-data-2.csv.
"""

# Original crash data
file_ma_crash_old = open('data/ma-crash-data-1.csv',newline='')
crash_reader = list(csv.reader(file_ma_crash_old, delimiter=',', quotechar='"'))

# A table of all towns and cities in ma and their latitude and longitude coordinates
file_ma_cors = open('data/ma-cors.txt',newline='')
cors_reader = list(csv.reader(file_ma_cors, delimiter=',', quotechar='"'))

# Copy of original crash data to write to
file_ma_crash_new = open('data/ma-crash-data-2.csv','w',newline='')
crash_writer = csv.writer(file_ma_crash_new, delimiter=',', quotechar='"')


""" Since there are no coordinates and only a town name for some crashes,
the coordinates of the crash must be generated approximately. This is done by
taking the coordinates for the center of the town that the crash is in and values
for the average massachusetts town radius, and randomly picking a point somewhere
in that town's approximate area.
"""
#Average radius of massachusetts towns in latitude degrees
TOWN_RADIUS_LAT = 0.04191
#Average radius of massachusetts towns in longitude degrees
TOWN_RADIUS_LON = 0.05305


#Find each crash with missing coordinates, generate new ones, and write them to the new file
for i, crash in enumerate(crash_reader):
    if(crash[3] == ''):
        row_output = crash[0:2]
        for cors in cors_reader:
            if(crash[4].lower() == cors[0].lower()):
                #Random noise added so that crashes are not all in the exact town center
                rand_lat = round(TOWN_RADIUS_LAT * random.randint(-10000,10000) / 10000,5)
                rand_lon = round(TOWN_RADIUS_LON * random.randint(-10000,10000) / 10000,5)
                #The new coordinates are the town center plus the random noise
                row_output.append(float(cors[1]) + rand_lat)
                row_output.append(float(cors[2]) + rand_lon)
                break
        crash_writer.writerow(row_output)
    else:
        crash_writer.writerow(crash)
file_ma_crash_new.close()


