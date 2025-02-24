from connect_mysql import connect_database

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()

        
            # SQL query to add a new workout session with values and the placeholders
            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s,%s,%s,%s)"

            # To execute the query
            cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
            conn.commit()
            print("Workout added successfully.")
        
        # except block to handle errors
        except Exception as e:
            print("An error occurred:", e)



        finally:
            cursor.close()
            conn.close()

