import obd

from connection import connect
connection = connect()
def print_RPM():
    rpm = connection.query(obd.commands.RPM)
    rpm_value = rpm.value
    return  rpm_value

print(print_RPM())