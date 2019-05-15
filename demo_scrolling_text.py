
import lcddriver
import time


display = lcddriver.lcd()


try:
	print("Press CTRL + C for stop this script!")

	def long_string(display, text = '', num_line = 1, num_cols = 20):
		
		if(len(text) > num_cols):
			display.lcd_display_string(text[:num_cols],num_line)
			time.sleep(1)
			for i in range(len(text) - num_cols + 1):
				text_to_print = text[i:i+num_cols]
				display.lcd_display_string(text_to_print,num_line)
				time.sleep(0.2)
			time.sleep(1)
		else:
			display.lcd_display_string(text,num_line)


	
	long_string(display, "Hello World!", 1)
	time.sleep(1)

	
	long_string(display, "Hello again. This is a long text.", 2)
	display.lcd_clear()
	time.sleep(1)

	while True:
		
		long_string(display, "Hello friend! This is a long text!", 2)

except KeyboardInterrupt: 
	print("Cleaning up!")
	display.lcd_clear()
