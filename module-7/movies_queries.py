# Cindy Hernandez
# Mod 7.2
#12/1/24


import mysql.connector
from mysql.connector import Error


# Step 1: Connect to the MySQL database
config = {
    "user": "movies_user",  # Use your MySQL username
    "password": "popcorn",   # Use your MySQL password
    "host": "127.0.0.1",     # Localhost if running MySQL locally
    "database": "movies",    # Use your MySQL database name
    "raise_on_warnings": True
}


# Establish a connection to the database
db = mysql.connector.connect(**config)
cursor = db.cursor()

# Query 1: Select all fields from the 'studio' table, including studio_id
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
print("-- Displaying Studio Records --")
for studio in studios:
    print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}\n")

# Query 2: Select all fields from the 'genre' table
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("\n-- Displaying Genre Records--")
for genre in genres:
    print(f"Genre ID: {genre[0]}\nGenre Name: {genre[1]}\n")

# Query 3: Select movie names and runtime for movies with a run time of less than 2 hours
cursor.execute("SELECT DISTINCT film_name, film_runtime FROM film WHERE film_runtime < 120")  # 120 minutes = 2 hours
short_movies = cursor.fetchall()
print("\n-- Displaying Short Film Records --")
if short_movies:
    for movie in short_movies:
        print(f"Film Name: {movie[0]}\nRuntime: {movie[1]}")
else:
    print("No movies found with runtime less than 2 hours.")

# Query 4: Get a list of film names and directors, grouped by director, removing duplicates
cursor.execute("SELECT film_director, GROUP_CONCAT(DISTINCT film_name ORDER BY film_name) FROM film GROUP BY film_director ORDER BY film_director")
directors_movies = cursor.fetchall()
print("\n -- Displaying Director Records in Order --")
if directors_movies:
    for director, films in directors_movies:
        print(f"Director: {director}\nMovies: {films}\n")
else:
    print("No director data found.")

# Step 3: Close the cursor and database connection
cursor.close()
db.close()
