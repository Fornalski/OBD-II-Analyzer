import obd

print("connecting to OBD")

connection = obd.OBD(portstr="/dev/ttyACM0")

if connection.is_connected():
	print("polaczono!!!")
	
	rpm = connection.query(obd.commands.RPM)
	print("RPM:", rpm.value)

	volts = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
	print("Voltage:", volts.value)

	speed = connection.query(obd.commands.SPEED)
	print("Speed:", speed.value)

	Coolant_temp = connection.query(obd.commands.COOLANT_TEMP)
	print("Coolant temperature", Coolant_temp)

	throttle_poz = connection.query(obd.commands.THROTTLE_POS)
	print("throttle position:", throttle_poz.value)

	MAF = connection.query(obd.commands.MAF)
	print("Mass Air Flow:", MAF.value)

	fuel_Level = connection.query(obd.commands.FUEL_LEVEL)
	print("Fuel level:", fuel_Level.value)

	run_Time = connection.query(obd.commands.RUN_TIME)
	print("Run time:", run_Time.value)

	fuel_Rate = connection.query(obd.commands.FUEL_RATE)
	print("Fuel usege:" , fuel_Rate)

else:
	print("Conection not working")
connection.close()
