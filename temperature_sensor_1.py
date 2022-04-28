import time
import os
import glob

os.system('modprobe w1-gpio') 
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def get_temp(): #Function to read the value of Temperature
    file = open(device_file, 'r') #open the file
    lines = file.readlines() #read the lines in the file 
    file.close() #close the file 
 
    trimmed_data = lines[1].find('t=') #find the "t=" in the line
 
    if trimmed_data != -1:
        temp_string = lines[1][trimmed_data+2:] #trim the string only to the temperature value
        temp_c = float(temp_string) / 1000.0 #divide the value of 1000 to get actual value
        return temp_c #return the value 

print(get_temp())
#28-01205b57a7d7