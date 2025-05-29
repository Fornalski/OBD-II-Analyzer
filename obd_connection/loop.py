import time
import obd

def run_till_i_stop(connection):
    try:
        while True:
            time.sleep(1)
            rpm = connection.query(obd.commands.RPM)
            print("current RPM:", rpm.value)
    except KeyboardInterrupt:
        print("\nProgram stopped due to use Ctrl+C")
    finally:
        print("\nConnection to OBD closing...")
        connection.close()