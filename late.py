#!/usr/bin/env python3

import evdev
from evdev import ecodes
import time 
import colorsys 
from plasma import auto


# --- CONFIGURATION --- IMPORTANT: Replace these values with your actual GPIO
# pins and number of pixels.  The `auto()` function is smart enough to figure
# out what to do with the string.  Format:
# "DEVICE_TYPE:GPIO_DATA:GPIO_CLOCK:pixel_count=NUMBER" Example:
# "APA102:14:15:pixel_count=40" for 40 pixels on BCM pins 14 (clock) and 15
# (data)
DEVICE_DESCRIPTOR = "APA102:14:15:pixel_count=8"
device_path = '/dev/input/event0'
# Set a delay between updates (in seconds)
FPS = 60.0
UPDATE_DELAY = 1.0 / FPS

# --- MAIN SCRIPT ---

print("Initializing Plasma LED device...")
try:
    # Use the `auto()` function from the plasma library to set up the device.
    # It parses the descriptor string to configure the correct driver.
    plasma = auto(default=DEVICE_DESCRIPTOR)
except ValueError as e:
    print(f"Error: Could not initialize the device. {e}")
    print("Please check your DEVICE_DESCRIPTOR string for correct formatting and pin numbers.")
    exit()

print("Device initialized successfully.")
print("Press Ctrl+C to exit.")

# Part 1: Solid Color Test
print("Setting all pixels to solid red for 3 seconds...")
plasma.set_all(255, 0, 0)
plasma.show()
time.sleep(3)


# Part 2: Solid Color Test on keyboard input
print("Setting all pixels to solid red for 3 seconds...")
plasma.set_all(255, 255, 255)
plasma.show()
time.sleep(3)

# Part 2: Rainbow Cycle Test
# print("Starting rainbow cycle pattern...")
# try:
#     spacing = 360.0 / plasma.get_pixel_count()
#     start_time = time.time()
    
#     while True:
#         # Calculate a hue value based on time to create a flowing animation
#         hue = int(time.time() * 100) % 360
        
#         for x in range(plasma.get_pixel_count()):
#             # Calculate the hue for each pixel
#             offset = x * spacing
#             h = ((hue + offset) % 360) / 360.0
            
#             # Convert HSV to RGB and set the pixel color
#             r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
#             plasma.set_pixel(x, r, g, b)

#         # Send the pixel data to the LED strip
#         plasma.show()
        
#         # Wait a short while before the next frame
#         time.sleep(UPDATE_DELAY)

# except KeyboardInterrupt:
#     print("\nExiting. Clearing LEDs...")
#     plasma.set_clear_on_exit(True)
#     plasma.show() # The atexit handler will clear the LEDs, but this is a good habit.


