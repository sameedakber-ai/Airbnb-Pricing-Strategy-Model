import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.basemap import Basemap

import statsmodels.api as sm

import os
import math

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
    return pd.to_datetime(col)

def to_numeric(col):
    return col.replace('[\$\,\%]', '', regex=True).astype(np.float)

def plot_time_series(dates, prices):
    #create axes and figure
    fig, ax = plt.subplots(figsize=(12,8)) 
    ax.grid(True)

    #Select x-tick locations and x_tick label formatting
    year = mdates.YearLocator(month=1)    
    month = mdates.MonthLocator(interval=2)
    year_format = mdates.DateFormatter('%Y:%m')
    month_format = mdates.DateFormatter('%m')

    #Set x-ticks as selected above
    ax.xaxis.set_minor_locator(month)
    ax.xaxis.grid(True, which='minor')
    ax.xaxis.set_major_locator(year)
    ax.xaxis.set_major_formatter(year_format)

    plt.plot(dates, prices, "-b")
    plt.xlabel('time')
    plt.ylabel('average listing price')


def plot_geographical(latitude_list, longitude_list, distribution_1, distribution_2):

    """
    Overly city geographical map with city listings scatter plot

    INPUT
    latitude_list - latitudes of listings
    longitude_list - longitudes of listings
    distribution_1 - distribution of first feature
    distribution_2 - distribution of second feature
    
    OUTPUT
    matplotlib.Baseplot object overlaid with scatter plt of listings
    """
    lat_0 = latitude_list.min()
    lat_1 = latitude_list.max()
    lon_0 = longitude_list.min()
    lon_1 = longitude_list.max()

    #Set up geographical map of Seattle by projecting actual map onto a cylindrical plane
    fig = plt.gcf()
    fig.set_size_inches(15, 12)

    m = Basemap(projection='cyl', resolution='c', 
                llcrnrlat=lat_0-0.05, urcrnrlat=lat_1+0.05,
               llcrnrlon=lon_0-0.05, urcrnrlon=lon_1+0.05)
    
    #Draw Basemap by plotting coastlines, country lines and county lines 
    m.drawcoastlines(linewidth=0.5)    
    m.drawcountries(linewidth=0.5)
    m.drawcounties(color='red', linewidth=0.8)
    
    #Produce scatter plot on top of Basemap
    m.scatter(longitude_list, latitude_list, c=distribution_1, s=distribution_2*5, cmap='viridis', alpha=0.4)
    
    plt.colorbar(label='price ($)')
    quantile_98 = distribution_1.quantile(0.98)
    plt.clim(0, quantile_98)
    
    #Set up legend for activity distribution 
    for a in [2,4,6]:
        plt.scatter([], [], c='k', alpha=0.5, s=a*5, label=str(a)+' accommodates')
        
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='lower left')

    plt.show()


def get_phi_score(confusion_matrix):
    n = confusion_matrix.sum().sum()
    row_totals = confusion_matrix.sum(axis=1)
    column_totals = confusion_matrix.sum(axis=0)
    # emp_array = np.empty(confusion_matrix.shape)
    cum_sum = 0
    for i in range(confusion_matrix.shape[0]):
        for j in range(confusion_matrix.shape[1]):
            temp = row_totals[i]*column_totals[j]/n
            cum_sum+=(confusion_matrix.iloc[i,j]-temp)**2/temp
    return math.sqrt(cum_sum/n)



def drop_cols(df, max_unique_entries = 50, min_unique_entries=2):
    """
    INPUT
    df - pandas dataframe
    max_unique_entries - Drop any column that has unique entries more than max unique entries
    min_unique_entries - Drop any column that contains only 1 unique 
    entry
    
    OUTPUT
    df - modified dataframe
    """
    for col in df.select_dtypes(include=['object']).columns:
        if (df[col].unique().shape[0] > max_unique_entries) or (df[col].unique().shape[0] < min_unique_entries):
            df.drop(col, axis=1, inplace=True)
    return df
