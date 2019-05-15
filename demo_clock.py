
import lcddriver
import time
import datetime


display = lcddriver.lcd()

try:
    print("Writing to display")
    display.lcd_display_string("No time to waste", 1) 
    while True:
        display.lcd_display_string(str(datetime.datetime.now().time()), 2) 

except KeyboardInterrupt: 
    print("Cleaning up!")
    display.lcd_clear()
