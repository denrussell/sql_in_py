from connect_mysql import connect_database

def add_member(members_id, name, age):
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()

        
            # SQL query to add a new member with values and the placeholders
            query = "INSERT INTO Members (id, name, age) VALUES (%s,%s,%s)"

            # To execute the query
            cursor.execute(query, (members_id, name, age))
            conn.commit()
            print("Member added successfully.")
        
        # except block to handle errors
        except Exception as e:
            print("An error occurred:", e)



        finally:
            cursor.close()
            conn.close()

