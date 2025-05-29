import obd

current_data = {
    "RPM": None,
    "SPEED": None,
    "THROTTLE_POSITION": None,
    "VOLTAGE": None,
    "COOLANT_TEMP": None,
    "FUEL_LVL": None,
    "RUN_TIME": None
}


def update_rpm(r):
    current_data["RPM"] = r.value.magnitude if r.value is not None else None

def update_speed(r):
    current_data["SPEED"] = r.value.magnitude if r.value is not None else None

def update_voltage(r):
    current_data["VOLTAGE"] = r.value.magnitude if r.value is not None else None

def update_coolant_temp(r):
    current_data["COOLANT_TEMP"] = r.value.magnitude if r.value is not None else None

def update_throttle(r):
    current_data["THROTTLE_POSITION"] = r.value.magnitude if r.value is not None else None

def update_fuel_lvl(r):
    current_data["FUEL_LVL"] = r.value.magnitude if r.value is not None else None

def update_run_time(r):
    current_data["RUN_TIME"] = r.value.magnitude if r.value is not None else None

def watching(connection):
    connection.watch(obd.commands.RPM, callback=update_rpm)
    connection.watch(obd.commands.SPEED, callback=update_speed)
    connection.watch(obd.commands.THROTTLE_POS, callback=update_throttle)
    connection.watch(obd.commands.CONTROL_MODULE_VOLTAGE, callback=update_voltage)
    connection.watch(obd.commands.COOLANT_TEMP, callback=update_coolant_temp)
    connection.watch(obd.commands.FUEL_LEVEL, callback=update_fuel_lvl)
    connection.watch(obd.commands.RUN_TIME, callback=update_run_time)

    connection.start()