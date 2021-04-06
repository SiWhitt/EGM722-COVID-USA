import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import chartify as chartify
import matplotlib.patches as mpatches
import matplotlib.lines as mlines



import pandas as pd
from cartopy.feature import ShapelyFeature


from shapely.geometry import Point, LineString, Polygon












""" Load the shapefile of the USA"""

outline = gpd.read_file('data_files/USA_Shapefile-states-29.shp')
outline = outline.to_crs(epsg=4326)



""" Load Excel spreadsheet containing US COVID Stats"""

COVID_Data = 




# create a figure of size 20x60 (representing the page size in inches)
myFig = plt.figure(figsize=(10, 10))

myCRS = ccrs.UTM(18)  # create a Universal Transverse Mercator reference system to transform our data.
ax = plt.axes(projection=ccrs.Mercator())  # finally, create an axes object in the figure, using a Mercator
# projection, where we can actually plot our data.



# first, we just add the outline of USA using cartopy's ShapelyFeature
outline_feature = ShapelyFeature(outline['geometry'], myCRS, edgecolor='k', facecolor='w')
xmin, ymin, xmax, ymax = outline.total_bounds
ax.add_feature(outline_feature)  # add the features we've created to the map.

ax.set_extent([xmin, xmax, ymin, ymax], crs=myCRS) # set the extent to the boundaries of the NI outline

ax. set(title='USA - States plus Washington DC') # Apply Title to Map of Ireland with Towns

myFig.savefig('map.png', bbox_inches='tight', dpi=300) #Save Map of USA as png file

"""Use chartify to create COVID figures for USA"""

