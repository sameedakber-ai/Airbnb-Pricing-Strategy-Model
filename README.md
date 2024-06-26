## Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#project-motivation)
3. [File Descriptions](#file-descriptions)
4. [Results](#results)
5. [Licensing, Authors and Acknowledgements](#licensing-authors-and-acknowledgements)


# Installation

The following libraries will need to be installed and/or updated to run the code in Anaconda v4.6 running python v3.*.
+ basemap -> conda install conda-forge::basemap
+ scikit-learn -> conda update scikit-learn


# Project Motivation

Airbnb is an online marketplace that provides accomodation sharing services to its users. Members use the online platform to arange or offer lodging. A new member intent on hosting would find pricing information valuable. Given airbnb's city data for Seattle for the year of 2016, I want to better understand:

1. How can we predict listing prices? What factors influence listing prices in Seattle? And how do they relate to price?
2. How does price vary with time at specific locations in Seattle?
3. How does monthly activity (number of guest bookings per month) relate to price at different locations in Seattle?

# File Descriptions

There is a single notebook contained in this repository to showcase work related to the above questions. Code is supplemented with ample documentation in the form of inline comments, docstrings and markdown cells. 

There is an additional .py file containing functions used in the main notebook.

# Results

The main findings can be found in the post available [here](https://medium.com/@sameedakber.ai/this-is-what-you-should-be-charging-as-a-host-on-airbnb-insights-from-airbnbs-seattle-data-4edea1f8d87c)

# Licensing, Authors and Acknowledgements

Airbnb data obtained from the Inside Airbnb site is sourced from publicly available information and is subject to the 'Creative Commons CC0 1.0 Universal' license. Additional licensing information can be found [here](http://insideairbnb.com/get-the-data.html). Feel free to use this code in any way you like!