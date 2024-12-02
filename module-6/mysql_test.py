import mysql.connector

# Connect to the database
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# Function to create connection
def create_connection():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to delete duplicate studios
def delete_duplicate_studios(cursor, conn):
    query = """
    DELETE s1
    FROM studio s1
    JOIN studio s2
      ON s1.studio_name = s2.studio_name
      AND s1.studio_id > s2.studio_id;
    """
    cursor.execute(query)
    conn.commit()

# Function to display films
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

def main():
    conn = create_connection()
    if not conn:
        return  # Exit if connection fails
    
    cursor = conn.cursor()

    try:
        # Show films before any operations
        show_films(cursor, "DISPLAYING FILMS")

        # Delete duplicate studios
        delete_duplicate_studios(cursor, conn)
        print("\n-- Displaying Studio Records After Cleanup --")
        show_films(cursor, "DISPLAYING FILMS AFTER CLEANUP")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
