# Code written by Joseph Nelson.
import pandas as pd
def interpret_dftest(dftest):
    dfoutput = pd.Series(dftest[0:2], index=['Test Statistic','p-value'])
    return dfoutput

# function to keep just the zipcode and not extra text
def split_zip(row):
    return row.split()[-1]

# function to generate ARIMA model and plot train, test, predictions
import matplotlib.pyplot as plt
def model_plot(train=None, test=None, arima_preds=None, title=None, vertlim=None):

    plt.figure(figsize=(10,5))
    plt.plot(train, label='Training data')
    if test is not None:
        plt.plot(test, label='Testing data')
    plt.plot(arima_preds, '--', label='Testing preds',color='green')
    plt.legend()
    plt.title(title)
    plt.ylim(vertlim)
    plt.show()

# function to manually gridsearch ARIMA
from statsmodels.tsa.arima.model import ARIMA
def arima_gs(train, prange, qrange):
    # Starting AIC, p, and q.
    best_aic = 99*(10**16) # start with a crazy huge number
    best_p = 0
    best_q = 0

    # Use nested for loop to iterate over values of p and q.
    for p in prange:
        for q in qrange:


            # Insert try and except statements.
            try:

                # Fitting an ARIMA(p, 1, q) model.
                print(f'Attempting to fit ARIMA({p}, 1, {q})')

                # Instantiate ARIMA model.
                arima = ARIMA(endog=train, order=(p, 1, q)).fit()


                # Print out AIC for ARIMA(p, 1, q) model.
    #             print(f'The AIC for ARIMA({p},1,{q}) is: {arima.aic}')

                # Is my current model's AIC better than our best_aic?
                if arima.aic < best_aic:

                    # If so, let's overwrite best_aic, best_p, and best_q.
                    best_aic = arima.aic
                    best_p = p
                    best_q = q

            except:
                print(f"Error with p={p}, q={q}")
                pass
    print()
    print()
    print('MODEL FINISHED!')
    print(f'Our model that minimizes AIC on the training data is the ARIMA({best_p},1,{best_q}).')
    print(f'This model has an AIC of {best_aic}.')

# function to return latitude and longitude of geographical location
# # referenced this for folium: https://www.google.com/url?q=https://nbviewer.jupyter.org/github/ThibautBremand/Coursera_Capstone/blob/master/1-Toronto_Clustering_By_Venues_Categories.ipynb&sa=D&source=editors&ust=1618488051134000&usg=AFQjCNE_3Vf3-Uy6y6eHUiUF8iBE2q7M6g

import geocoder
def geographical_coordinate(city, state):
    city = str(city)
    state = str(state)

    lat_lng_coords = None

    # loop until we get the coordinates
    while(lat_lng_coords is None):
        g = geocoder.arcgis(city + ', ' + state) # I want the WA map to be centered on the middle of WA state
        lat_lng_coords = g.latlng

    latitude_wa = lat_lng_coords[0]
    longitude_wa = lat_lng_coords[1]
    return city, state, latitude_wa, longitude_wa

# function to generate folium map
import folium
def my_map(latitude_wa, longitude_wa, zoom, circle_color, df, color_index=0):
    map_wa = folium.Map(width=1000, height=700,location=[latitude_wa, longitude_wa], zoom_start=zoom)

    for ind in range(df.shape[0]):
        lat = df.loc[ind,'lat']
        lng = df.loc[ind,'lng']
        if color_index != 0:
            color_val = df.loc[ind,str(color_index)]

        folium.CircleMarker([lat,lng], radius = 5,
            color=circle_color[color_val], fill=True,
            fill_color=circle_color[color_val],
            fill_opacity=0.5).add_to(map_wa)

    return map_wa

# function to plot calculated mean
def agg_income_plt(df, ytext = None, title = None,
hor_lim = None, ver_lim = None, alpha=0.2):
    fig = plt.figure(figsize=(5,8))
    ax = plt.subplot(111)
    # plot median income with vehicle resale instance
    plt.plot(df.index,df.iloc[:,:100],alpha=alpha)

    # plot median of all incomes, for trend
    plt.plot(df.index,df.mean(axis=1),color='black',linestyle='-',marker='o',ms=10)
    x = range(8)
    plt.xticks(x, ['0','1','2','3','4','5','6','7'])
    plt.xlabel('Resale number')
    plt.ylabel(ytext)
    plt.title(title)
    plt.xlim(hor_lim)
    plt.ylim(ver_lim)
    plt.show()
    fig.savefig(f'../images/{title}.png')

# Function to sort venues in descending order
def return_most_common_venues(row, features, num_top_venues):
    # Remove the key zip x city x station_latitude x station_longitude from the row
    row_categories = row.iloc[len(features):]

    # Sort ascending
    row_categories_sorted = row_categories.sort_values(ascending=False)

    # Return the top num_top_venues
    return row_categories_sorted.index.values[0:num_top_venues]

# function to find top 10 venues
import numpy as np
def display_venues(num_top_venues, features, stationall_grouped):
    indicators = ['st', 'nd', 'rd']

    # create columns according to number of top venues
    columns = ['zip','city','station_latitude','station_longitude']

    for ind in np.arange(num_top_venues):
        try:
            columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
        except:
            columns.append('{}th Most Common Venue'.format(ind+1))

    # create a new dataframe, and set it with the column names
    neighborhoods_venues_sorted = pd.DataFrame(columns=columns)

    # add the keys from the grouped dataframe (Postal code x Borough x Neighborhood)
    neighborhoods_venues_sorted['zip'] = stationall_grouped['zipcode']
    neighborhoods_venues_sorted['city'] = stationall_grouped['city']
    neighborhoods_venues_sorted['station_latitude'] = stationall_grouped['station_latitude']
    neighborhoods_venues_sorted['station_longitude'] = stationall_grouped['station_longitude']

    # loop through each row
    for ind in np.arange(stationall_grouped.shape[0]):
        neighborhoods_venues_sorted.iloc[ind, len(features):] = \
        return_most_common_venues(stationall_grouped.iloc[ind, :], features, num_top_venues)

    return neighborhoods_venues_sorted

# function for ranking venue frequency by zip code, for the 10 most dense zip codes
def venue_freq(neighborhoods_venues_sorted, num_top_venues):

    # create columns according to number of top venues
    columns = ['zip','city']

    for ind in np.arange(num_top_venues):
        try:
            columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
        except:
            columns.append('{}th Most Common Venue'.format(ind+1))

    # create a new dataframe, and set it with the column names above
    zipcode_venues_sorted = pd.DataFrame(columns=columns)

    # fill in 'zip' column
    zipcode_venues_sorted['zip'] = neighborhoods_venues_sorted['zip'].value_counts().index[:10]

    # fill in 'city' column
    for ind in range(10):
        # for this zipcode
        zipcode = zipcode_venues_sorted.loc[ind,'zip']

        # fill in the 'city' column
        zipcode_venues_sorted.loc[ind,'city'] = neighborhoods_venues_sorted[neighborhoods_venues_sorted['zip']==zipcode]['city'].value_counts().index[0]

        # all venues at this zipcode
        city_venue = neighborhoods_venues_sorted[neighborhoods_venues_sorted['zip']==zipcode].iloc[:,4:]

        # instantiate empty list of sorted venues
        sorted_venues = []

        # which venue is most commonly ranked
        for index in range(10):
            venue_counts = city_venue.iloc[:,index].value_counts()

            current_length = len(sorted_venues)

            for start_index in range(10):
                if venue_counts.index[start_index] in sorted_venues:
                    start_index += 1
                else:
                    sorted_venues.append(venue_counts.index[start_index])
                    break

        # fill in venue ranking columns
        zipcode_venues_sorted.iloc[ind, len(columns)-10:] = sorted_venues

    return zipcode_venues_sorted

# plot silhouette score and intertia score
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
def plot_silhouette(group_cluster):
    sil_scores = []
    inertia_scores = []
    for k in range(2, 20):
        kmc = KMeans(n_clusters=k, random_state=2021)
        kmc.fit(group_cluster)
        sil_score = silhouette_score(group_cluster, kmc.labels_)
        sil_scores.append(sil_score)
        inertia_score = kmc.inertia_
        inertia_scores.append(inertia_score)

    scores_df = pd.DataFrame({
        'k': list(range(2,20)),
        'sil': sil_scores,
        'inertia': inertia_scores
    })

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12,4))
    ax[0].plot(list(range(2, 20)),scores_df['sil'])
    ax[0].set_title('Silhouette score')
    ax[1].plot(list(range(2, 20)),scores_df['inertia'])
    ax[1].set_title('Inertia score')
    plt.show()

# calculate driving distance, and save the 2 smallest
# https://towardsdatascience.com/driving-distance-between-two-or-more-places-in-python-89779d691def#1c17
import requests
import json
def driving_distance(stations_far):
    drive_list1 = []
    drive_list2 = []
    for ind in range(stations_far.shape[0]):
        # instantiate empty list
        dist_sublist = []

        # origin coordinate
        lat1 = latitude[ind]
        lng1 = longitude[ind]

        # calculate distance for all coordinate pairs
        for i in range(stations_far.shape[0]):
            lat2 = latitude[i]
            lng2 = longitude[i]

            r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lng1},{lat1};{lng2},{lat2}?overview=false""")
            # then you load the response using the json libray
            # by default you get only one alternative so you access 0-th element of the `routes`
            routes = json.loads(r.content)
            route_1 = routes.get("routes")[0]
            dist_sublist.append(route_1['distance']*0.000621371192) # distance in meters converted to miles

        # sort dist_sublist
        dist_sublist = np.sort(dist_sublist)

        # append 2 shortest distances to drive_list
        try:
            drive_list1.append(dist_sublist[1])
        except:
            drive_list1.append(dist_sublist[0])

        try:
            drive_list2.append(dist_sublist[2])
        except:
            drive_list2.append(dist_sublist[0])

        if ind%5==0:
            print(f'Completed {ind} locations')

        return drive_list1, drive_list2

# Loop through each station location and retrieve its venues
def get_nearby_venues(stations, CLIENT_ID, CLIENT_SECRET, VERSION):
    zipcode=stations['zip']
    city=stations['city']
    latitude=stations['latitude']
    longitude=stations['longitude']

    venues_list=[]

    for zipcode, city, lat, lng in zip(zipcode, city, latitude, longitude):

        # create the API request URL to explore the neighbourhood using FoursquareAPI
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
            CLIENT_ID,
            CLIENT_SECRET,
            VERSION,
            lat,
            lng,
            CONST_venuesRadiusScan,
            CONST_venuesLimit)

        # make the GET request
        results = requests.get(url).json()["response"]['groups'][0]['items']

        # return only relevant information for each nearby venue : name, latitude, longitude, and the categories' names
        venues_list.append([(
            zipcode,
            city,
            lat,
            lng,
            v['venue']['name'],
            v['venue']['location']['lat'],
            v['venue']['location']['lng'],
            v['venue']['categories'][0]['name']) for v in results])

        time.sleep(1) # rest for 1 second before doing this again

    # add the venues to a dataframe
    nearby_venues = pd.DataFrame([item for venues_list in venues_list for item in venues_list])
    nearby_venues.columns = [
                        'Zipcode',
                        'City',
                        'Station Latitude',
                        'Station Longitude',
                        'Venue',
                        'Venue Latitude',
                        'Venue Longitude',
                        'Venue Category']
    return nearby_venues
