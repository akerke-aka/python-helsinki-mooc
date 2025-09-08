"""
City bikes
----------
Functions for working on a file containing location data from the stations for city bikes in Helsinki.

Functions:
- get_station_data(filename: str): reads the names and locations of all the stations in the file, and returns them in a dictionary
- distance(stations: dict, station1: str, station2: str): returns the distance between the two stations given as arguments
- greatest_distance(stations: dict):  returns a tuple, with the two stations with the maximum distance
"""
def get_station_data(filename: str):
    stations = {}
    with open(filename) as new_file:
        for line in new_file:
            parts = line.strip().split(';')
            # skips header line
            if parts[0] == "Longitude" and parts[1]== "Latitude":
                continue
            else:
                # use station name as key, coordiantes as value
                stations[parts[3]] = (float(parts[0]), float(parts[1]))
    return stations 

def distance(stations: dict, station1: str, station2: str):
    import math
    longtitude1, latitude1 = stations[station1]
    longtitude2, latitude2 = stations[station2]
    x_km = (longtitude1 - longtitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    import math
    max_distance = 0
    st_x = ""
    st_y = ""
    for station_x in stations:
        for station_y in stations:
            if station_x != station_y:
                dist  = distance(stations, station_x, station_y)
                if dist > max_distance:
                    max_distance = dist
                    st_x = station_x
                    st_y = station_y
    return st_x, st_y, max_distance

