
#raw_value to voltage
raw_value = 700
voltage = raw_value * (3.3/1024)
print(voltage)

voltage = 2.28
#voltage to raw_value
raw_value = voltage * (1024/3.3)
print(raw_value)
