title: Generating fake data with Mimesis
Date: 2020-02-03
Slug: mimesis
image: ./images/blog/blog_5.jpeg
<!-- https://images.pexels.com/photos/2315712/pexels-photo-2315712.jpeg?auto=compress&cs=tinysrgb&h=650&w=940 -->

The Fitbit I got during the holidays got me thinking. How do these health app developers get their data to test their data? Do they really survey thousands of people about their personal data or manually input health data one by one?
Isn't there a more efficient way to get this data?

<img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fmemecrunch.com%2Fmeme%2F7VYF%2Ffake-people%2Fimage.png&f=1&nofb=1>

For this blog, let me tell you where "fake" things (data) will come in handy.

### Introducing Mimisis

The ability to generate mock but valid data comes in handy in app development, where you need to work with databases. Filling in the database by hand is a time-consuming and tedious process, which can be done in three stages — gathering necessary information, post-processing the data and coding the data generator itself. It gets really complicated when you need to generate not just 10–15 users, but 100–150 thousand users (or other types of data). In this article as well as the two following ones we will introduce you to a tool, which immensely simplifies generating mock data, initial database loading and testing in general.
Mimesis is a Python library, which helps generate mock data for various purposes. The library was written with the use of tools from the standard Python library, and therefore, it doesn’t have any side dependencies. Currently the library supports 32 languages and 21 class providers, supplying various data.



```python
from mimesis import Person, Generic, Address
person = Person('en')
```


```python
person.full_name()
```




    'Tory Parker'



Our regular imports:


```python
from mimesis import Person, Science, Text
import pandas as pd
```

Instantiate our languages:


```python
person = Person('en')
science = Science('en')
text = Text('en')
```

For this example, I'll make 50 patients:


```python
data = []
for _ in range(0,50):
    data.append((person.full_name(), person.gender(), person.age(), person.weight(), person.height(), science.dna_sequence(length=10), science.rna_sequence(length=10), text.answer()))

data = pd.DataFrame(data)


data.columns = ['name','gender', 'age','weight(kg)', 'height(m)', 'dna_sequence', 'rna_sequence', 'smoker']

```
