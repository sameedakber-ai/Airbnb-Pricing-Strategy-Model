def get_airbnb_data(city, data_label):
    
    """
    Get Calendar, listings and reviews data for a city
    
    INPUT
    city (string) - city to fetch data for
    data_label (string) - which data to fetch: calendar, listings or reviews
                                         
    OUTPUT
    pandas DataFrame
    """
    data_to_fetch = {'calendar': 'calendar.csv', 
                     'listings': 'listings.csv',
                     'reviews': 'reviews.csv'}
        
    return pd.read_csv(os.path.join(city, data_to_fetch[data_label]))


