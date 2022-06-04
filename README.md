# Data-Collection-Pipeline

> An implementation of an industry grade data collection pipeline that runs scalably in the cloud.

## Step by Step Process

In this Data Collection pipeline project, I have collected tabular data and images from a website(https://www.boohoo.com). This data will be stored in a relational database and data lake in the cloud.

## Step 1: Selecting a Website

Being a lover of everything about fashion and beauty, there are three website i wanted to scrape:
1. https://www.cultbeauty.co.uk
2. https://www.boohoo.com
3. https://www.prettylittlething.com

After discusing this sites with my peers, i have decided to base my data collection project on boohoo.com website. The products on this website displays all the useful information that when collected could be used to provide business value.

## Step 2: Scraping

I have defined a class and some  methods to navigate the website. Sellenium and Request and request is being imported to scrape the website.
Before being able to access the website, accept cookies iframe appeared. Which was clicked immediately from the initializer to be able to access the data.
