from connect_mysql import connect_database

def update_member_age(member_id, new_age):
    conn = connect_database()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try: 
        cursor = conn.cursor()

        # Ensure that member exists
        select_query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(select_query, (member_id,))
        member = cursor.fetchone()
        if member is None:
            print("Member does not exist.")
            return

        
        # SQL query to update member's age with values and the placeholders
        update_query = "UPDATE Members SET age = %s WHERE id = %s"

        # To execute the query
        cursor.execute(update_query, (new_age, member_id))
        conn.commit()
        print("Member's age updated successfully.")
        
    # except block to handle errors
    except Exception as e:
        print("An error occurred:", e)
        conn.rollback()



    finally:
        cursor.close()
        conn.close()

