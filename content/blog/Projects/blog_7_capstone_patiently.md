title: Using emergency room hospital data to predict wait times
Date: 2020-03-12
Slug: patientlywaiting
image: ./images/blog/blog_7.jpeg
<!-- https://images.pexels.com/photos/127873/pexels-photo-127873.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260 -->

Have you ever stepped foot in the emergency room of a hospital in Toronto either for a loved one or perhaps yourself, only to be met with a grueling long wait until you see any medical professional?

It sucks. And there should definitely be a better system, right? Having volunteered at Toronto Western Hospital Emergency Department and being able to experience both sides of the system, I wanted to dig deep at what's really going on and to actually do something about it.

<img src="https://github.com/anitatea/patiently_waiting/raw/master/static/img/ss.png?raw=true width=300">



Technologies Used
*Python
*Pandas
*pipenv - for local storage of credentials
*Beautiful Soup - Web Scraping
*SKLearn pipelines
*DataFrameMapper
*HDBSCAN clustering
*Flask
*Google Maps API

### Introduction

PATIENTLY WAITING was created as my capstone project for the Data Science Immersive program at Bitmaker / General Assembly. A beta version of this application can be found here! Check emergency room wait times around Toronto by choosing a day: https://patientlywaiting.herokuapp.com/

### Data Gathering

Detailed administrative data on date, patient flow, current and past examinations in Ontario was provided by:
* [National Ambulatory Care Reporting System (NACRS)](https://www.cihi.ca/en/national-ambulatory-care-reporting-system-metadata)

* [Canadian Institude for Health Information (CIHI)](https://www.cihi.ca/en/access-data-and-report)

### Data Modeling

The ability to accurately and reliably predict waiting times at walk-in hospital facilities can increase both patient satisfaction and hospital efficiency via a better management of patient flow. My web-app implements machine learning (ML) models to predict waiting times in the Emergency Room (ER) of the largest public hospital in the Greater Toronto Area (GTA).

Several machine learning (ML) techniques were evaluated to find the most accurate and useful prediction to a user. I chose [Gradient Boosting](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) among other regression models explored for predicting wait times.

**PATIENTLY WAITING** is currently in beta testing. If you notice any bugs, have any questions or suggestions, I'd love to hear from you: [anita.tran38@gmail.com](anita.tran38@gmail.com?subject=PatientlyWaiting).

<img src="https://media.makeameme.org/created/me-patiently-waiting-399b1150e6.jpg" width=300>

### Planned Future Enhancements

* Docker for hosting database, nginx and flask web app
* Google API to read your location
* Actively scrape hospital data as it is released per month on hqontatio.ca
* Generate best route to hospital using combinatorial optimization

If you’d like to play around with the tool, a beta version is running here: https://patientlywaiting.herokuapp.com/

The complete project source code (which is still in the process of being updated) can be found on [GitHub](https://github.com/anitatea/patiently_waiting).


```python

```
