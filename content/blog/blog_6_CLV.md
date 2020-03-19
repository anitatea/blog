title: What's a customer worth? Modeling customer lifetime value
Date: 2020-02-17
Slug: CLV
image: /images/blog/blog_6.jpeg

<!-- https://images.pexels.com/photos/919436/pexels-photo-919436.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260 -->

Recently, I've been taking advantage of an app called [Sweatabl](https://apps.apple.com/ca/app/sweatabl/id1354451699) to discover free workout classes near me. While I love to switch up my workout routine and explore the fitness community freely, I can't help but wonder that this definitely makes for a much trickier Customer Lifetime Value (CLV) calculation.


Whether in E-Commerce, retail or workout classes, there is an investment in customers (acquisition costs, offline ads, promotions, discounts, etc.) to generate revenue and be profitable. These actions make some customers incredibly valuable in terms of lifetime value for the business. Other customers do go away, however they do so silently; they don't have to tell us they're leaving.

I wanted to model customer data and see how it can be used to predict a customer's lifetime value. The data we'll use is an online retail dataset downloaded from [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/online+retail).

### Import the data


```python
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel("Online Retail.xlsx")
df.head()
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
      <th>InvoiceNo</th>
      <th>StockCode</th>
      <th>Description</th>
      <th>Quantity</th>
      <th>InvoiceDate</th>
      <th>UnitPrice</th>
      <th>CustomerID</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>536365</td>
      <td>85123A</td>
      <td>WHITE HANGING HEART T-LIGHT HOLDER</td>
      <td>6</td>
      <td>2010-12-01 08:26:00</td>
      <td>2.55</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>1</th>
      <td>536365</td>
      <td>71053</td>
      <td>WHITE METAL LANTERN</td>
      <td>6</td>
      <td>2010-12-01 08:26:00</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>2</th>
      <td>536365</td>
      <td>84406B</td>
      <td>CREAM CUPID HEARTS COAT HANGER</td>
      <td>8</td>
      <td>2010-12-01 08:26:00</td>
      <td>2.75</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>536365</td>
      <td>84029G</td>
      <td>KNITTED UNION FLAG HOT WATER BOTTLE</td>
      <td>6</td>
      <td>2010-12-01 08:26:00</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>536365</td>
      <td>84029E</td>
      <td>RED WOOLLY HOTTIE WHITE HEART.</td>
      <td>6</td>
      <td>2010-12-01 08:26:00</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
  </tbody>
</table>
</div>



Clean the data and make a new dataframe. For our analysis, all we need is CustomerID, InvoiceDate (without the time) and we'll make a new columns called 'Sales'.


```python
import datetime as dt

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']).dt.date
df = df[pd.notnull(df['CustomerID'])]
df = df[(df['Quantity']>0)]
df['Sales'] = df['Quantity'] * df['UnitPrice']
df = df[['CustomerID', 'InvoiceDate', 'Sales']]
```


```python
df.head()
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
      <th>CustomerID</th>
      <th>InvoiceDate</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17850.0</td>
      <td>2010-12-01</td>
      <td>15.30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>17850.0</td>
      <td>2010-12-01</td>
      <td>20.34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17850.0</td>
      <td>2010-12-01</td>
      <td>22.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17850.0</td>
      <td>2010-12-01</td>
      <td>20.34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17850.0</td>
      <td>2010-12-01</td>
      <td>20.34</td>
    </tr>
  </tbody>
</table>
</div>



Let's see how many unique customers.


```python
df['CustomerID'].nunique()
```




    4339



### Shape of your data

For CLV models, the following nomenclature is used:

`Frequency`: number of repeat purchases the customer has made. This means that it’s one less than the total number of purchases.

`T`: age of the customer in whatever time units chosen (daily, in our dataset). This is equal to the duration between a customer’s first purchase and the end of the period under study.

`Recency`: age of the customer when they made their most recent purchases. This is equal to the duration between a customer’s first purchase and their latest purchase. (Thus if they have made only 1 purchase, the recency is 0.)

We'll be using the [Lifetimes package](https://github.com/CamDavidsonPilon/lifetimes), developed by Cameron Davidson-Pilon, data scientist at Shopify. If your data is not in this format, there are useful functions in the documentation to transform your data.


```python
from lifetimes.plotting import *
from lifetimes.utils import *

data = summary_data_from_transaction_data(df, 'CustomerID', 'InvoiceDate', monetary_value_col='Sales', observation_period_end='2011-12-9')
data.head()
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
      <th>frequency</th>
      <th>recency</th>
      <th>T</th>
      <th>monetary_value</th>
    </tr>
    <tr>
      <th>CustomerID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12346.0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>325.0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>12347.0</th>
      <td>6.0</td>
      <td>365.0</td>
      <td>367.0</td>
      <td>599.701667</td>
    </tr>
    <tr>
      <th>12348.0</th>
      <td>3.0</td>
      <td>283.0</td>
      <td>358.0</td>
      <td>301.480000</td>
    </tr>
    <tr>
      <th>12349.0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>18.0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>12350.0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>310.0</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>



`CustomerID 12346` made one purchase only (no repeat), so his frequency and recency are 0 and their age is 325 days (e.g. the duration between his first purchase and the end of the period in the analysis).

### Frequency/Recency analysis using the BG/NBD model


```python
from lifetimes import BetaGeoFitter

bgf = BetaGeoFitter(penalizer_coef=0.0)
bgf.fit(data['frequency'], data['recency'], data['T'])
print(bgf)
```

    <lifetimes.BetaGeoFitter: fitted with 4339 subjects, a: 0.00, alpha: 68.89, b: 6.75, r: 0.83>


Let's say a customer made a purchase every day for three weeks straight and then hasn't had any activity for months. Chances are the probability of this customer being "alive" is very slim.

On the other hand, if a customer consistently makes a purchase every couple of months, they're more likely to be "alive".


```python
from lifetimes.plotting import plot_frequency_recency_matrix
import matplotlib.pyplot as plt
%matplotlib inline

fig = plt.figure(figsize=(12,8))
plot_frequency_recency_matrix(bgf);
```

<img src = 'https://github.com/anitatea/blog/blob/master/content/images/output_19_1.png?raw=true'>

Customers who have purchased frequently and purchased recently will likely be the best customers in the future. (bottom-right corner).

Customers who have purchased a lot but not recently (top-right corner), have probably gone.

Let's go back to our customers and rank their expected number of purchases.


```python
t = 1
data['predicted_purchases'] = bgf.conditional_expected_number_of_purchases_up_to_time(t, data['frequency'], data['recency'], data['T'])
data.sort_values(by='predicted_purchases').tail(5)
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
      <th>frequency</th>
      <th>recency</th>
      <th>T</th>
      <th>monetary_value</th>
      <th>predicted_purchases</th>
    </tr>
    <tr>
      <th>CustomerID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14606.0</th>
      <td>88.0</td>
      <td>372.0</td>
      <td>373.0</td>
      <td>135.890114</td>
      <td>0.201005</td>
    </tr>
    <tr>
      <th>15311.0</th>
      <td>89.0</td>
      <td>373.0</td>
      <td>373.0</td>
      <td>677.729438</td>
      <td>0.203269</td>
    </tr>
    <tr>
      <th>17841.0</th>
      <td>111.0</td>
      <td>372.0</td>
      <td>373.0</td>
      <td>364.452162</td>
      <td>0.253053</td>
    </tr>
    <tr>
      <th>12748.0</th>
      <td>113.0</td>
      <td>373.0</td>
      <td>373.0</td>
      <td>298.360885</td>
      <td>0.257581</td>
    </tr>
    <tr>
      <th>14911.0</th>
      <td>131.0</td>
      <td>372.0</td>
      <td>373.0</td>
      <td>1093.661679</td>
      <td>0.298312</td>
    </tr>
  </tbody>
</table>
</div>



### Assessing model fit

Let's see how correct our model actually is. We can compare our data versus artificial data simulated with our fitted model's parameters.


```python
from lifetimes.plotting import plot_period_transactions

plot_period_transactions(bgf);
# train test split is being done underneath
```

<img src = 'https://github.com/anitatea/blog/blob/master/content/images/output_25_1.png?raw=true'>

We now partition the dataset into a calibration period dataset and a holdout dataset - just like cross-validation in machine learning models.
This is important as we want to test how our model performs on data not yet seen.


```python
from lifetimes.utils import calibration_and_holdout_data

summary_cal_holdout = calibration_and_holdout_data(df, 'CustomerID', 'InvoiceDate',
                                        calibration_period_end='2011-06-08',
                                        observation_period_end='2011-12-9' )   
print(summary_cal_holdout.head())
```

                frequency_cal  recency_cal  T_cal  frequency_holdout  \
    CustomerID                                                         
    12346.0               0.0          0.0  141.0                0.0   
    12347.0               2.0        121.0  183.0                4.0   
    12348.0               2.0        110.0  174.0                1.0   
    12350.0               0.0          0.0  126.0                0.0   
    12352.0               3.0         34.0  112.0                3.0   

                duration_holdout  
    CustomerID                    
    12346.0                  184  
    12347.0                  184  
    12348.0                  184  
    12350.0                  184  
    12352.0                  184  


Perform fitting on the `_cal` columns, and test on the `_holdout` columns.


```python
from lifetimes.plotting import plot_calibration_purchases_vs_holdout_purchases

bgf.fit(summary_cal_holdout['frequency_cal'], summary_cal_holdout['recency_cal'], summary_cal_holdout['T_cal'])
plot_calibration_purchases_vs_holdout_purchases(bgf, summary_cal_holdout);
```

<img src = 'https://github.com/anitatea/blog/blob/master/content/images/output_29_1.png?raw=true'>

### Predicting customer transactions

Let's say we want to predict the purchases of `CustomerID = 12347` in the next 10 days.


```python
t = 10 # predict purchases in 10 periods
individual = data.loc[12347]
# below function is an alias to `bfg.conditional_expected_number_of_purchases_up_to_time`
bgf.predict(t, individual['frequency'], individual['recency'], individual['T'])
```




    0.1572774363164109



Our model is saying that this customer's future transaction is 0.157 in 10 days. Note that this is not a percentage, but what an individual's future purchases might look like.

### Estimating customer lifetime value using Gamma-Gamma model of monetary value

In our analysis, we haven't yet taken into account the economic value (Sales) of each transaction and only focused on the occurrences.

We want to predict the likely spend per transaction in the future for a customer.

To estimate the economic value, we use the Gamma-Gamma submodel.

For this estimation, we filter for customers who had at least one repeat purchase.


```python
returning_customers = data[data['frequency']>0]
returning_customers.head()
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
      <th>frequency</th>
      <th>recency</th>
      <th>T</th>
      <th>monetary_value</th>
      <th>predicted_purchases</th>
    </tr>
    <tr>
      <th>CustomerID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12347.0</th>
      <td>6.0</td>
      <td>365.0</td>
      <td>367.0</td>
      <td>599.701667</td>
      <td>0.015656</td>
    </tr>
    <tr>
      <th>12348.0</th>
      <td>3.0</td>
      <td>283.0</td>
      <td>358.0</td>
      <td>301.480000</td>
      <td>0.008956</td>
    </tr>
    <tr>
      <th>12352.0</th>
      <td>6.0</td>
      <td>260.0</td>
      <td>296.0</td>
      <td>368.256667</td>
      <td>0.018697</td>
    </tr>
    <tr>
      <th>12356.0</th>
      <td>2.0</td>
      <td>303.0</td>
      <td>325.0</td>
      <td>269.905000</td>
      <td>0.007172</td>
    </tr>
    <tr>
      <th>12358.0</th>
      <td>1.0</td>
      <td>149.0</td>
      <td>150.0</td>
      <td>683.200000</td>
      <td>0.008340</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(returning_customers)
```




    2790



Apply the Gamma-Gamma model.


```python
from lifetimes import GammaGammaFitter
ggf = GammaGammaFitter(penalizer_coef = 0)
ggf.fit(returning_customers['frequency'],
        returning_customers['monetary_value'])
print(ggf)
```

    <lifetimes.GammaGammaFitter: fitted with 2790 subjects, p: 2.10, q: 3.45, v: 485.57>


Estimate of average transaction value for each customer.


```python
print(ggf.conditional_expected_average_profit(
        data['frequency'],
        data['monetary_value']
    ).head(10))
```

    CustomerID
    12346.0    416.917667
    12347.0    569.988807
    12348.0    333.762672
    12349.0    416.917667
    12350.0    416.917667
    12352.0    376.166864
    12353.0    416.917667
    12354.0    416.917667
    12355.0    416.917667
    12356.0    324.008941
    dtype: float64


Finally, computing the total CLV! We'll be using the [Discounted Cash Flow method](https://en.wikipedia.org/wiki/Discounted_cash_flow) adjusting for cost of capital.


```python
# refit the BG model to the data (with money value) dataset
bgf.fit(data['frequency'], data['recency'], data['T'])

CLV = ggf.customer_lifetime_value(
    bgf, #the model to use to predict the number of future transactions
    data['frequency'],
    data['recency'],
    data['T'],
    data['monetary_value'],
    time=12, # months
    discount_rate=0.01 # monthly discount rate ~ 12.7% annually
)
```


```python
CLV.sort_values(ascending=False).head(10)
```




    CustomerID
    14646.0    222128.930290
    18102.0    178895.333435
    16446.0    175531.468535
    17450.0    147476.621010
    14096.0    127589.202889
    14911.0    109442.132668
    12415.0     96290.227222
    14156.0     89410.334970
    17511.0     67660.407580
    16029.0     58729.618772
    Name: clv, dtype: float64



`CustomerID 14646` is estimated to have a CLV of over $200K. Using this analysis, I can see the value it can bring such as identifying traits and features of valuable customers.
