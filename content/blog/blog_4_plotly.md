title: Epic visualizations to plot epidemics
Date: 2020-01-27
Slug: dash-plotly
image: /images/blog/blog_4.jpeg
<!-- https://images.pexels.com/photos/1164536/pexels-photo-1164536.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260 -->

Data visualization is one of my favourite creative outlets - to draw out deeper insights from meaningful data. Like this.

<img src= 'http://lh6.ggpht.com/_gKQKwLZ8XUs/S9imwa3sgvI/AAAAAAAACiE/vM0kklCnsAk/s800/Graphjam-Essay.jpg'>

(Image source: [Graphjam.com](https://www.boredpanda.com/35-extremely-funny-graphs-and-charts/?utm_source=duckduckgo&utm_medium=referral&utm_campaign=organic))

Visualization packages in Python is far from scarce and there are great options for static graphs.

However, as data gets more complex and understanding becomes more distant, there is an obvious need for interactive visualizations to more easily explore data.

### What's [Dash](https://plot.ly/)

*"Bringing data science out of the lab and into the business.*

Formally only available for enterprise, Dash is now an open source library (free!) for creating interactive web-based visualizations. Highly interactive web application using Python or R.

HTML/CSS/JavaScript not required *(... and the door is that-a-way)*.

What I think makes it powerful is it is able to incorporate all the functionalities of Python for data manipulation and much more.

Amazon, Cisco, Shell, among other worldwide enterprises have been embracing this tool for large scale deployments.  

### Let's Get Started

Pretty straight forward. More details for updates on the [Dash installation page](https://dash.plot.ly/installation).


```python
pip install dash
```

### Sample Interactive Bar Chart

I used data from the [Centers for Disease Control and Prevention on Drug Poisoning Mortality by State in the United States](https://data.cdc.gov/NCHS/NCHS-Drug-Poisoning-Mortality-by-State-United-Stat/44rk-q6r2). I'm going to build an interactive bar chart that shows absolute deaths per state in 2016 and 2017. (The dataset has been updated on April 29, 2019 and so I believe this is the most accurate dataset to this date.)

Bring in all the dash modules and pandas for reading and manipulating the data. I saved this file as `bar_app.py`:


```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd # to manipulate our data
```

For this simple example, I'm choosing to import the `plotly.graph_objs` whereas the documentation uses dcc.graph to build the plot.

Writing this article, I felt that it was easier to use the plotly graph object since there were a lot more examples online than there were the plain `dcc.graph` for the simple cases.

This is my preference and I do find it more straightforward to demonstrate this example.

Reading in the first few pieces of data and filtering for deaths by state in 2016 and 2017:


```python
df = pd.read_csv('data/NCHS_-_Drug_Poisoning_Mortality_by_State__United_States.csv')
df.iloc[:,:7].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Year</th>
      <th>Sex</th>
      <th>Age Group</th>
      <th>Race and Hispanic Origin</th>
      <th>Deaths</th>
      <th>Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama</td>
      <td>1999</td>
      <td>Both Sexes</td>
      <td>All Ages</td>
      <td>All Races-All Origins</td>
      <td>169</td>
      <td>4430143</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alabama</td>
      <td>2000</td>
      <td>Both Sexes</td>
      <td>All Ages</td>
      <td>All Races-All Origins</td>
      <td>197</td>
      <td>4447100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alabama</td>
      <td>2001</td>
      <td>Both Sexes</td>
      <td>All Ages</td>
      <td>All Races-All Origins</td>
      <td>216</td>
      <td>4467634</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alabama</td>
      <td>2002</td>
      <td>Both Sexes</td>
      <td>All Ages</td>
      <td>All Races-All Origins</td>
      <td>211</td>
      <td>4480089</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alabama</td>
      <td>2003</td>
      <td>Both Sexes</td>
      <td>All Ages</td>
      <td>All Races-All Origins</td>
      <td>197</td>
      <td>4503491</td>
    </tr>
  </tbody>
</table>
</div>




```python
# I only need State, Year and Deaths column
df = df[['State', 'Year','Deaths']]
```


```python
# check unique states
df['State'].unique()
```




    array(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
           'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
           'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
           'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
           'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
           'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
           'New Jersey', 'New Mexico', 'New York', 'North Carolina',
           'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
           'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
           'Texas', 'United States', 'Utah', 'Vermont', 'Virginia',
           'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'],
          dtype=object)




```python
# 'United States' is obviously not a state. I suspect it captures deaths that are uncategorized.
# For our example, we'll drop these rows.

indexUS = df[df['State'] == 'United States'].index
df = df.drop(indexUS)
```


```python
# filter for 2016
df_2016 = df[df['Year'] == 2016]

# filter for 2016
df_2017 = df[df['Year'] == 2017]
```

Now that the data is simply tabulated by state and total deaths; we can build out the bars in our graph.

The convention for plotly is that each item being plotted is usually called a `trace`. In this example, we want to plot State vs. Deaths.


```python
trace1 = go.Bar(x=df_2016['State'], y=df_2016['Deaths'], name='2016',
        marker=dict(color='rgb(55, 83, 109)') # darker blue
        )
trace2 = go.Bar(x=df_2017['State'], y=df_2017['Deaths'], name='2017',
        marker=dict(color='rgb(26, 118, 255)') # lighter blue
        )
```

Now were ready to build out the actual Dash app.


```python
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Drug Poisoning in the United States in 2016 & 2017'),
    html.Div(children='''(Hover over bars to view death count)'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2],
            'layout':
            go.Layout(title='Drug Poisoning Mortality by State in 2016 & 2017', barmode='group')
        })
])
```

Most of the structure is dash building the app, using HTML components and creating the figure dictionary, containing instructions to build the graph and customize layout.

What I love is the simplicity of how dash integrates HTML components beautifully without having to deal with the standard HTML/CSS/JS boilerplate required for most modern web apps that you see.

Since I'm dealing with various code styles, Atom is my preferred editor to manage matching brackets, parentheses and such.

`dcc.Graph` defines the figure using a using a dictionary that contains the actual figure, plotted data and layout options. In this case, the layout was needed to define the title and bar type graph.



Once the app is laid out, we need to make sure it can run:


```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

Running this in your terminal:


```python
python bar_app.py
```

Here's our nice interactive graph:

<img src = 'https://github.com/anitatea/blog/blob/master/content/videos/dash_example.gif?raw=true'>

Pretty great when you think how much engagement you can get with a simple application of 35 lines of code. You can find the above example available on github.

Not only is the layout and look of dash clean and report-ready; Dash also took care of scaling the interactivity on different browsers. So we can focus on beautiful, pure python!

The entire code:


```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('NCHS_-_Drug_Poisoning_Mortality_by_State__United_States.csv')

df = df[['State', 'Year','Deaths']]

indexUS = df[df['State'] == 'United States'].index
df = df.drop(indexUS)

df_2016 = df[df['Year'] == 2016]
df_2017 = df[df['Year'] == 2017]

trace1 = go.Bar(x=df_2016['State'], y=df_2016['Deaths'], name='2016',
        marker=dict(color='rgb(55, 83, 109)'))
trace2 = go.Bar(x=df_2017['State'], y=df_2017['Deaths'], name='2017',
        marker=dict(color='rgb(26, 118, 255)'))

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Drug Poisoning in the United States in 2016 & 2017'),
    html.Div(children='''(Hover over bars to view death count)'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2],
            'layout':
            go.Layout(title='Drug Poisoning Mortality by State in 2016 & 2017', barmode='group')
        })
])
if __name__ == '__main__':
    app.run_server(debug=True)
```

### For Fun: A More Complex Example

<a target="_blank" rel="noopener noreferrer" href="http://epic-epidemic.herokuapp.com/">
  <img src="https://github.com/anitatea/blog/blob/master/content/images/dash_heatmap.png?raw=true" alt="Dash Heatmap" >
</a>

Dash's real power shines in its ability to combine complex interactions - again all with Python. Dash provides several interactive components out of the box including Dropdowns, Multi-Select Dropdowns, Mapping, Radio Buttons, Checkboxes, Sliders, and Text Input. All of them can be easily constructed and tied into your plots to drive various interactive options.

For a more complex demo, check out my dashboard using the same data, featuring:
* Slider between years of 2012 - 2017
* Fully interactive heatmap of the United States
* Drop down selection to show total counts of death

Here's the [link](https://epic-epidemic.herokuapp.com/) to the dashboard. Layout inspired by examples from the Dash-Plotly gallery.

### Final Thoughts

I've only scratched the surface of this powerful yet simplistic tool. My favourite pieces:
* Quick for building web-based visualization tools without prior knowledge of JavaScript and other web technologies
* Default dashboard is already responsive
* Ability to save, zoom, pan and interact with the display, on the display

Presenting data-driven visualizations to non-technical colleagues can be a struggle, as if you are speaking two different languages without Google Translate. I've seen more than my fair share of presentations and the truly successful ones were the most engaging with their audience.
