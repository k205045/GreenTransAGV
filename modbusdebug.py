from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

client = ModbusClient("192.168.8.149",502)
client.connect()
rr = client.read_holding_registers(9200,10,unit=0)
dec = BinaryPayloadDecoder.fromRegisters(rr.registers,byteorder=Endian.Big,wordorder=Endian.Big)
dec = dec.decode_string(10).decode()
print(rr,"value=",dec)
print(rr,"value=",rr.registers)
