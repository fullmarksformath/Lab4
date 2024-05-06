from hal import hal_input_switch as switch
from hal import hal_led as led
import time
from time import sleep
from tqdm import tqdm

led.init()
switch.init()

import time 
 
start_time = time.time() 
duration = 5  # Replace with the number of seconds you want the loop to run for 
 
while (time.time() - start_time) < duration: 
    if switch.read_slide_switch()==1:
        led.set_output(1)
        sleep(0.2)
        led.set_output(0)
        sleep(0.2)

    elif switch.read_slide_switch()==0:
        start_time = time.time() 
        duration = 5  # Replace with the number of seconds you want the loop to run for 
        while (time.time() - start_time) < duration: 
            led.set_output(1)
            sleep(0.1)
            led.set_output(0)
            sleep(0.1)
            pass

