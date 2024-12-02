# Cindy Hernandez
# Mod 8.2
# 12/1/24


import mysql.connector

# Connection configuration
config = {
    "user": "movies_user",  
    "password": "popcorn",   
    "host": "127.0.0.1",     
    "database": "movies",    
    "raise_on_warnings": True
}

# Create connection function
def create_connection():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Show films function
def show_films(cursor, title):
    print(f"\n-- {title} --")
    query = """
        SELECT 
            film_name AS Name, 
            film_director AS Director, 
            genre_name AS Genre, 
            studio_name AS 'Studio Name'
        FROM 
            film 
        INNER JOIN genre ON film.genre_id = genre.genre_id 
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(f"Film Name: {row[0]}")
        print(f"Director: {row[1]}")
        print(f"Genre Name: {row[2]}")
        print(f"Studio Name: {row[3]}")
        print()

# Insert a new film into the film table, bypassing the release date
def insert_film(cursor, conn):
    query = """
        INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime)
        VALUES (%s, %s, %s, %s, %s)
    """
    data = ("Princess Bride", "Rob Reiner", 7, 7, 98)  # No release date provided, bypassing it
    cursor.execute(query, data)
    conn.commit()

# Update the genre of the film 'Alien' to Horror 
def update_film_genre(cursor, conn):
    query = """
        UPDATE film
        SET genre_id = 10  
        WHERE film_name = 'Alien'
    """
    cursor.execute(query)
    conn.commit()

# Delete the movie 'Gladiator'
def delete_film(cursor, conn):
    query = """
        DELETE FROM film WHERE film_name = 'Gladiator'
    """
    cursor.execute(query)
    conn.commit()

# Main function
def main():
    # Establish connection and create cursor
    conn = create_connection()
    if not conn:
        return  # Exit if connection fails
    
    cursor = conn.cursor()

    try:
        # Show films before any operations
        show_films(cursor, "DISPLAYING FILMS")

        # Insert a new film
        insert_film(cursor, conn)
        show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

        # Update film genre for 'Alien' to Horror
        update_film_genre(cursor, conn)
        show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

        # Delete 'Gladiator' film
        delete_film(cursor, conn)
        show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
