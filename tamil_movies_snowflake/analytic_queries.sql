-- Top Directors by Average Movie Rating (min 3 movies)
SELECT Director, ROUND(AVG(Rating), 2) AS avg_rating, COUNT(*) AS movies_directed
FROM tamil_movies
GROUP BY Director
HAVING COUNT(*) >= 3
ORDER BY avg_rating DESC;

-- Most Popular Genres by Movie Count
SELECT Genre, COUNT(*) AS total_movies, ROUND(AVG(Rating), 2) AS avg_rating
FROM tamil_movies
GROUP BY Genre
ORDER BY total_movies DESC;

-- Correlation between Hero Rating and Movie Rating
SELECT 
    ROUND(CORR(Hero_Rating, movie_rating), 2) AS correlation_hero_vs_movie
FROM tamil_movies
WHERE Hero_Rating IS NOT NULL AND movie_rating IS NOT NULL;

-- Top Actors by Number of Movies and Average Rating (min 5 movies)
SELECT Actor, COUNT(*) AS total_movies, ROUND(AVG(Rating), 2) AS avg_rating
FROM tamil_movies
GROUP BY Actor
HAVING COUNT(*) >= 5
ORDER BY avg_rating DESC;
