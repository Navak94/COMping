import sys
import glob
import serial
import os
import subprocess

def serial_ports():

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('COM AINT WORKIN')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
if __name__ == '__main__':
    comavailable = str(serial_ports()).replace("[","").replace("]","")
    print(comavailable)
    if comavailable == "":
        print("Nothing found on COM")
    BOOL = input("Proceed with ping scan?  ")
    if BOOL == "yes":
        for y in range(1,73): # input 
            for x in range(0,256): # ip's to scan through
                output= os.popen('ping ' + "192.168."+str(y)+"." + str(x)).read()
                print(output)
