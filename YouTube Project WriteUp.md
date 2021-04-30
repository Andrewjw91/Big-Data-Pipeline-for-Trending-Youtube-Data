# Data Pipeline Implementation for YouTube Data

Andrew Wong

## Abstract

The goal of this project was to engineer a storage and processing pipeline using efficient and scalable methods for big data. The large dataset I obtained from Kaggle contains Trending YouTube Video data from 11 different countries. I processed and stored the data into a relational database to perform EDA and produce categorical and geographical insights. I implemented these queries and algorithms into an interactive web-app to allow users to visualize their data of interest.

## Design

The motivation of this project was to deploy an interactive web application that allows users to easily pull visualizations and insights from the YouTube Trending Video dataset. I created algorithms to allow users to return data filtered by video category, date, and country with just a few clicks. This application can provide useful insights to marketing/advertising teams that are looking to target specific YouTube channels. The geographical filtering also allows useful insight into the differences in media consumption by category between different countries.

## Data

The dataset contains 500,000+ (and counting) trending YouTube Videos from the past 9 months. The Kaggle dataset is updated daily with the 200 Trending Videos for each country. The countries include India, USA, Great Britain, Germany, Canada, France, Russia, Brazil, Mexico, South Korea, and, Japan.

Each country's data is stored as a separate table within a relational SQL database. A few feature highlights include channel title, views, category, likes and dislikes. The video description field can include up to 5000 (1-2 pages!) characters and does not follow any categorical or conventional format. Removing the following columns: description, comments disabled, ratings disabled, resulted in a 70% filesize reduction to the database.

## Algorithms

I used Python libraries (sqlalchemy, pandas) to create an engine to read and query the SQL database into dataframes. 

-Engineered algorithms to aggregate and return only the data filtered by the user. Some of the algorithm aggregations include: Top Trending Categories by country, Most Frequent Trending Channels, Most Frequent Trending Channels by Category

-Converted data objects into standardized datetime

-Created dictionary mapping to return the category value from categoryID without having to iterate through and overwrite 500,000+ values.

I implemented and deployed these algorithms into a web application built using Streamlit. The backend code behind the buttons and drop-down selections apply user inputs into the algorithms.

## Tools

-SQLite DB Browser for relational database storage

-Pandas and SqlAlchemy for data aggregation and querying

-Matplotlib and Seaborn for plotting

-Streamlit for Web-app deployment

