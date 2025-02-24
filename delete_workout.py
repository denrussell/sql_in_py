from connect_mysql import connect_database

def delete_workout_session(session_id):
    conn = connect_database()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try: 
        cursor = conn.cursor()

        # Ensure that workout session exists
        select_query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(select_query, (session_id,))
        workout_session = cursor.fetchone()
        if workout_session is None:
            print("Workout session does not exist.")
            return

        
        # SQL query to delete workout session with values and the placeholders
        delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"

        # To execute the query
        cursor.execute(delete_query, (session_id,))
        conn.commit()
        print("Workout session deleted successfully.")
        
    # except block to handle errors
    except Exception as e:
        print("An error occurred:", e)
        conn.rollback()



    finally:
        cursor.close()
        conn.close()
