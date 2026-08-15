-- ==========================================================
-- NETFLIX CONTENT ANALYTICS
-- 40 SQL QUERIES
-- Author : Varalakshmi
-- ==========================================================

-- 1. View all records
SELECT * FROM netflix_titles;

-- 2. Count total records
SELECT COUNT(*) AS Total_Titles FROM netflix_titles;

-- 3. Display all Movies
SELECT * FROM netflix_titles
WHERE type='Movie';

-- 4. Display all TV Shows
SELECT * FROM netflix_titles
WHERE type='TV Show';

-- 5. Total Movies
SELECT COUNT(*) AS Total_Movies
FROM netflix_titles
WHERE type='Movie';

-- 6. Total TV Shows
SELECT COUNT(*) AS Total_TV_Shows
FROM netflix_titles
WHERE type='TV Show';

-- 7. List all distinct ratings
SELECT DISTINCT rating
FROM netflix_titles;

-- 8. List all distinct countries
SELECT DISTINCT country
FROM netflix_titles;

-- 9. List all distinct genres
SELECT DISTINCT listed_in
FROM netflix_titles;

-- 10. Latest release year
SELECT MAX(release_year)
FROM netflix_titles;

-- 11. Oldest release year
SELECT MIN(release_year)
FROM netflix_titles;

-- 12. Average release year
SELECT AVG(release_year)
FROM netflix_titles;

-- 13. Top 10 countries by content
SELECT country, COUNT(*) AS Total
FROM netflix_titles
GROUP BY country
ORDER BY Total DESC
LIMIT 10;

-- 14. Top 10 directors
SELECT director, COUNT(*) AS Total
FROM netflix_titles
WHERE director IS NOT NULL
GROUP BY director
ORDER BY Total DESC
LIMIT 10;

-- 15. Rating distribution
SELECT rating, COUNT(*) AS Total
FROM netflix_titles
GROUP BY rating
ORDER BY Total DESC;

-- 16. Content released after 2015
SELECT title, release_year
FROM netflix_titles
WHERE release_year > 2015;

-- 17. Content released before 2000
SELECT title, release_year
FROM netflix_titles
WHERE release_year < 2000;

-- 18. Count content by release year
SELECT release_year, COUNT(*) AS Total
FROM netflix_titles
GROUP BY release_year
ORDER BY release_year;

-- 19. Count Movies and TV Shows
SELECT type, COUNT(*) AS Total
FROM netflix_titles
GROUP BY type;

-- 20. Top 10 genres
SELECT listed_in, COUNT(*) AS Total
FROM netflix_titles
GROUP BY listed_in
ORDER BY Total DESC
LIMIT 10;

-- 21. Top 10 cast members
SELECT cast, COUNT(*) AS Total
FROM netflix_titles
WHERE cast IS NOT NULL
GROUP BY cast
ORDER BY Total DESC
LIMIT 10;

-- 22. Count content by country
SELECT country, COUNT(*) AS Total
FROM netflix_titles
GROUP BY country
ORDER BY Total DESC;

-- 23. Count content by director
SELECT director, COUNT(*) AS Total
FROM netflix_titles
GROUP BY director
ORDER BY Total DESC;

-- 24. Movies with PG-13 rating
SELECT title
FROM netflix_titles
WHERE rating='PG-13';

-- 25. TV Shows with TV-MA rating
SELECT title
FROM netflix_titles
WHERE rating='TV-MA';

-- 26. Movies from India
SELECT title
FROM netflix_titles
WHERE country='India';

-- 27. Movies from United States
SELECT title
FROM netflix_titles
WHERE country='United States';

-- 28. Count titles by month added
SELECT MONTH(date_added) AS Month,
COUNT(*) AS Total
FROM netflix_titles
GROUP BY MONTH(date_added)
ORDER BY Month;

-- 29. Count titles by year added
SELECT YEAR(date_added) AS Year,
COUNT(*) AS Total
FROM netflix_titles
GROUP BY YEAR(date_added)
ORDER BY Year;

-- 30. Top 5 release years
SELECT release_year, COUNT(*) AS Total
FROM netflix_titles
GROUP BY release_year
ORDER BY Total DESC
LIMIT 5;

-- 31. Longest movie duration
SELECT *
FROM netflix_titles
ORDER BY duration DESC
LIMIT 1;

-- 32. Total content per rating
SELECT rating,
COUNT(*) AS Total
FROM netflix_titles
GROUP BY rating;

-- 33. Movies containing 'Love'
SELECT title
FROM netflix_titles
WHERE title LIKE '%Love%';

-- 34. TV Shows containing 'Life'
SELECT title
FROM netflix_titles
WHERE title LIKE '%Life%';

-- 35. Count content added each month
SELECT MONTHNAME(date_added) AS Month,
COUNT(*) AS Total
FROM netflix_titles
GROUP BY MONTHNAME(date_added);

-- 36. Count content added each day
SELECT DAYNAME(date_added) AS Day,
COUNT(*) AS Total
FROM netflix_titles
GROUP BY DAYNAME(date_added);

-- 37. Top 20 newest releases
SELECT title, release_year
FROM netflix_titles
ORDER BY release_year DESC
LIMIT 20;

-- 38. Top 20 oldest releases
SELECT title, release_year
FROM netflix_titles
ORDER BY release_year
LIMIT 20;

-- 39. Movies sorted alphabetically
SELECT title
FROM netflix_titles
WHERE type='Movie'
ORDER BY title;

-- 40. TV Shows sorted alphabetically
SELECT title
FROM netflix_titles
WHERE type='TV Show'
ORDER BY title;