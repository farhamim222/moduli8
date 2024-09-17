import mysql.connector
from mysql.connector import Error


def get_airport_by_icao(icao_code):
    try:

        connection = mysql.connector.connect(
        port="3307",
            database='lp',
            user='root',
            password='Mitoina33'
        )

        if connection.is_connected():
            # Create a cursor for executing queries
            cursor = connection.cursor()

            # SQL query to fetch airport name and municipality by ICAO code
            query = """
                SELECT name, municipality
                FROM airport
                WHERE ident = %s
            """
            cursor.execute(query, (icao_code,))

            # Fetch the result
            result = cursor.fetchone()

            if result:
                print(f"Airport: {result[0]}")
                print(f"Municipality: {result[1]}")
            else:
                print(f"No airport found with ICAO code '{icao_code}'.")

    except Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the connection is closed
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# Main program
if __name__ == "__main__":
    icao_code = input("Enter the airport ICAO code: ").upper()
    get_airport_by_icao(icao_code)
