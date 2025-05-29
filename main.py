from os import close
import time
from obd_connection.connection import connect
from obd_connection.loop import run_till_i_stop



connection = connect()

if connection:
    print("Working...")
    run_till_i_stop(connection)

