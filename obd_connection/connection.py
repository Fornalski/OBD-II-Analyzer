import obd
import time

port = "/dev/ttyACM0"

def connect():
    print(f"connecting OBD-II system on port {port}...")

    try:
        connection = obd.OBD(portstr=port)
        time.sleep(2)

        if connection.is_connected():
            print("Connected to OBD interface")
            return connection
        else:
            print("Not connected")
    except Exception as e:
        print(f"Connection error: {e}")