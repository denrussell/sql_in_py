'''Advanced Data Analysis in Gym Management System
Task 1: SQL BETWEEN usage'''

from connect_mysql import connect_database

def get_members_in_age_range(start_age, end_age):
    
    conn = connect_database()
    if conn is None:
        print("Failed to connect to the database.")
        return
    
    try: 
        cursor = conn.cursor()

    
        query = "SELECT members_id, name, age FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(query, (start_age, end_age))
    
    
        members = cursor.fetchall()

        if members:
            for member in members:
                print(member)
        else:
            print("No members found in specified age range.")

        return members
    
    
    # except block to handle errors
    except Exception as e:
        print("An error occurred:", e)
        conn.rollback()


    finally:
        cursor.close()
        conn.close()