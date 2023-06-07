# sqlalchemy-challenge
## **Background:**

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

**Part 1: Analyze and Explore the Climate Data**
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib.

**Precipitation Analysis:**
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method.
7. Use Pandas to print the summary statistics for the precipitation data.

**Station Analysis:**
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
- List the stations and observation counts in descending order.
- Answer the following question: which station id has the greatest number of observations?
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
- Filter by the station that has the greatest number of observations.
- Query the previous 12 months of TOBS data for that station.
- Plot the results as a histogram with bins=12
5. Close your session

**Part 2: Design Your Climate App**
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes.

## **Sources:**
### **Part 1:**
- The basis for the code used in the "# Use Pandas to calculate the summary statistics for the precipitation data" portion of the "Exploratory Precipitation Analysis" section in "/SurfsUp/climate_starter.ipynb" was found from https://www.w3schools.com/python/pandas/ref_df_describe.asp
- Some of the basis for the code used in the "Design a query to find the most active stations (i.e. which stations have the most rows?) List the stations and their counts in descending order." portion of the "Exploratory Station Analysis" section in "/SurfsUp/climate_starter.ipynb" was found from https://www.geeksforgeeks.org/python-sqlalchemy-func-count-with-filter/

### **Part 2:**