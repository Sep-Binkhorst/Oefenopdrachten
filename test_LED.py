import pyvisa

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n")

identification = device.query("*IDN?")
print(identification)

for voltage in range(0, 1023):
    device.query(f"OUT:CH0 {voltage}")
    print(voltage)