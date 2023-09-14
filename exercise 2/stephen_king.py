import sqlite3

# Read the file and copy content to a list
with open('stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = [line.strip().split(',') for line in file]

# Establish a connection with the database
conn = sqlite3.connect('stephen_king_adaptations.db')
c = conn.cursor()

# Create the table
# c.execute('''CREATE TABLE stephen_king_adaptations_table
#              (movieID text, movieName text, movieYear text, imdbRating real)''')
#
# # Insert the content into the table
# c.executemany('INSERT INTO stephen_king_adaptations_table VALUES (?,?,?,?)', stephen_king_adaptations_list)
#
# # Commit the transaction
# conn.commit()

# Loop for user to search movies
while True:
    print("1. Search by movie name")
    print("2. Search by movie year")
    print("3. Search by movie rating")
    print("4. STOP")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter the movie name: ")
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (name,))
        rows = c.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No such movie exists in our database.")
    elif choice == '2':
        year = input("Enter the movie year: ")
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (year,))
        rows = c.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No movies were found for that year in our database.")
    elif choice == '3':
        rating = float(input("Enter the movie rating: "))
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating>=?", (rating,))
        rows = c.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No movies at or above that rating were found in the database.")
    elif choice == '4':
        break
    else:
        print("Invalid option. Please try again.")

# Close the connection
conn.close()