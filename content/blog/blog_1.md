title: Featuring... Feature Engineering!
Date: 2019-12-09
Slug: feature-engineering
image: /images/blog/blog_1.jpeg


<!-- https://images.pexels.com/photos/1036936/pexels-photo-1036936.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260 -->


As someone with an engineering background, I was naturally drawn to the concept of Feature Engineering and excited to take my first dive into machine learning through finding organization and insights from messy data – real world data.

<img src='https://pics.me.me/real-world-datasets-boton-nouse-oricess-0-gi-i-think-i-49704783.png' width="200">

Feature engineering is the way of extracting features (variables) from data and transforming them into features that are suitable for Machine Learning algorithms.

There are 3 main steps:

1. Feature Selection – All features aren’t equal. Therefore certain features which are more important than others will affect the accuracy of the prediction model. Methods of Feature Selection include correlation coefficient scores, Ridge regression, LASSO, and ElasticNet.

2. Feature Transformation – Filling missing data values, scaling, and binning are common forms of transformation. To reduce skewness of the data when we do this, a log scale is used. We all know real world data is messy

3. Feature Extraction – Large datasets are generally found to be redundant, therefore we’d want to reduce dimensionality of these features. To do so, constructing combination of our features extracts the features important to our model.

Suppose we’re given flight time data and asked to predict the price of a flight based on the departure and arrival times.


```python
df = df[['dep_time', 'arrival_time','duration', 'prices']]
df
```

<img src='https://github.com/anitatea/blog/blob/master/content/images/before.png?raw=true' width="100">


We want to have 'dep_time' and 'arrival_time' in similar formats that are easier to analyse. How could we simplify these features for our model (and us) to understand?

One way to interpret this data is we can bin the times to sections of time in a 24 hour scale. Night [0-5], Morning [6-11], Afternoon [12-17] and Evening [18-23] will be our bins. Note: For 'Arrival Time', we can drop the date landed, as it is captured in 'Duration'.

Binning Departure Time ('dep_time'):


```python
df['departure_t'] = pd.to_datetime(df1['dep_time'], format='%H:%M')

a = df.assign(dept_session=pd.cut(df['departure_t'].dt.hour,
    [0,6,12,18,24],labels=['Night','Morning','Afternoon','Evening']))

df['departure_S'] = a['dept_session']
df
```

<img src='https://github.com/anitatea/blog/blob/master/content/images/dep_after.png?raw=true' width="200">

Binning Arrival Time:


```python
arr_time = df['arrival_time'].str.split(' ').str[0]

df['arrival_t'] = pd.to_datetime(arr_time, format='%H:%M')

a = df.assign(arr_session=pd.cut(df['arrival_t'].dt.hour,
    [0,6,12,18,24],labels=['Night','Morning','Afternoon','Evening']))

df['arrival_S'] = a['arr_session']
df
```

<img src='https://github.com/anitatea/blog/blob/master/content/images/arr_after.png?raw=true' width="700">

Visualizing what we just did:

<img src='https://github.com/anitatea/blog/blob/master/content/images/dep_plot.png?raw=true' width="300">

<img src='https://github.com/anitatea/blog/blob/master/content/images/arr_plot.png?raw=true' width="300">

Within a few minutes of working with our data, we can hypothesize that a majority of people leave in the morning and majority of people arrive in the evening. This quick analysis can help airports focus customer service efforts based on frequencies of flyers to ride-share organizations optimizing drivers on hand for those rushing in and out of the airport.

This is just one simple example of feature engineering - there's so much more to explore!

Feature engineering is an important art of transforming raw data into features that better represent the data for machine learning and can make or break your model.
