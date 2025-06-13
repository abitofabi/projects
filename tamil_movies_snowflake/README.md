# Tamil Movie Trends Analytics on Snowflake

This project analyzes a Tamil movies dataset using Snowflake to uncover insights about directors, genres, actors, and the relationship between hero ratings and movie ratings.

## Dataset

The dataset includes columns such as:
- MovieName, Genre, Rating, Director, Actor
- PeopleVote, Year, Hero_Rating, movie_rating, content_rating

## Project Setup

- Created a Snowflake table `tamil_movies` with appropriate data types.
- Loaded the dataset CSV into the table using Snowflake UI and `COPY INTO` command.

## Key Analysis Queries

1. Top directors by average movie rating (minimum 3 movies directed).
2. Most popular genres by total movie count and average rating.
3. Correlation between hero rating and movie rating.
4. Top actors by number of movies and average rating (minimum 5 movies).

## How to Run

1. Create the Snowflake table using `create_table.sql`.
2. Load the CSV data into the `tamil_movies` table.
3. Run the queries in `queries.sql` to get insights.

## Optional

- Visualize results using Power BI or Tableau connected to Snowflake.
- Extend the dataset with more features or do time series trend analysis.
