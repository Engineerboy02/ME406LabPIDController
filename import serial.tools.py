import serial
import serial.tools.list_ports

#print ('Search ports...')
#ports = list(serial.tools.list_ports.comports())

#for p in ports:
    #print ('-- Find ports --')
    #print (p)

#Port = str(input("Please enter the number of the COM port for USB Serial port: "))

#comPort = "COM"+Port

#print(comPort)



def serial_ports():

    # produce a list of all serial ports. The list contains a tuple with the port number, 
    # description and hardware address
    #
    ports = list(serial.tools.list_ports.comports())  

    # return the port if 'USB' is in the description 
    for port_no, description, address in ports:
        if 'USB Serial Port' in description:
            return port_no
        
print(serial_ports())