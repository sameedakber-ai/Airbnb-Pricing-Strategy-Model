import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.basemap import Basemap

import statsmodels.api as sm

import os

def get_airbnb_data(city, data_to_fetch):


    """
    Get Calendar, listings and reviews data for a city
    
    INPUT
    city (string) - city to fetch data for
    data_label (string) - which data to fetch: calendar, listings or reviews
                                         
    OUTPUT
    pandas DataFrame
    """
    data_labels = {'calendar': 'calendar.csv', 
                     'listings': 'listings.csv',
                     'reviews': 'reviews.csv'}
        
    return pd.read_csv(os.path.join(city, data_labels[data_to_fetch]))


def to_date_time(col):
    col = pd.to_datetime(calendar[col])
    return col

def to_numeric(col):
    col = col.replace('[\$,]', '', regex=True).str.rstrip('.0').
          astype(np.float)
    return col

def plot_geographical(latitude_list, longitude_list, distribution_1, distribution_2):

    """
    Overly city geographical map with city listings scatter plot

    INPUT
    lat_0 (float) - lower left corner latitude in geographical plot
    lat_1 (float) - upper right corner latitude in geographical plot
    lon_0 (float) - lower left corner longitude in geographical plot
    lon_1 (float) - upper right corner longitude in geographical plot
    lat (array, type float) - Latitude of listings
    lon (array, type float) - Longitude of listings
    price_distribution (array, type float) - Listing prices
    activity_distribution (array, type float) - Number of listing reviews per month
    
    OUTPUT
    matplotlib.Baseplot object overlaid with scatter plt of listings
    """
    lat_0 = latitude.min()
    lat_1 = latitude.max()
    lon_0 = longitude.min()
    lon_1 = longitude.max()

    #Set up geographical map of Seattle by projecting actual map onto a cylindrical plane
    fig = plt.figure(figsize=(10,10))
    m = Basemap(projection='cyl', resolution='c', 
                llcrnrlat=lat_0, urcrnrlat=lat_1,
               llcrnrlon=lon_0, urcrnrlon=lon_1)
    
    #Draw Basemap by plotting coastlines, country lines and county lines 
    m.drawcoastlines(linewidth=1)    
    m.drawcountries(linewidth=1)
    m.drawcounties(color='red', linewidth=1)
    
    #Produce scatter plot on top of Basemap
    m.scatter(longitude, latitude, c=distribution_1, s=distribution_2*15, cmap='cividis', alpha=0.2)
    
    plt.colorbar(label='price ($)')
    price_quantile_95 = price_distribution.quantile(0.94)
    plt.clim(0, price_quantile_99)
    
    #Set up legend for activity distribution 
    for a in [1,3,5]:
        plt.scatter([], [], c='k', alpha=0.5, s=a*15, label=str(a)+' review(s) / month')
        
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='lower left')
    
    plt.show()

