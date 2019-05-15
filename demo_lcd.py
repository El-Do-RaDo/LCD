
import lcddriver
import time


display = lcddriver.lcd()


try:
    while True:
        
        print("Writing to display")
        display.lcd_display_string("Hello World", 1) 
        display.lcd_display_string("GIH", 2) 
        
        display.lcd_display_string("RVS", 3)
        display.lcd_display_string("777", 4)  
        time.sleep(2)                                     
        display.lcd_clear()                               
        time.sleep(2)                                     
        
except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
    
