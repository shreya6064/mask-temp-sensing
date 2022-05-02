import time
import os
import glob

import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd


lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)

lcd_columns = 16
lcd_rows = 2



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

#print(get_temp())

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
#print(lcd_rs)
txt = get_temp()
print("Taken temperature")
lcd.message = str(txt)
#print(type(lcd.message))

time.sleep(7.0)
lcd.clear()