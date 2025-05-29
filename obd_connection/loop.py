import time
from obd_connection.data_collecting import current_data, watching

def run_till_i_stop(connection):
    watching(connection)
    try:
        while True:
            print(current_data)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram stopped due to use Ctrl+C")
    finally:
        print("\nConnection to OBD closing...")
        connection.close()