import digitalio
import board
import usb_hid
import time
import busio
import adafruit_ssd1306
from digitalio import DigitalInOut, Direction
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import terminalio
import pulseio
import pwmio
import rotaryio
import neopixel
from rainbowio import colorwheel
import colorsys
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Create an instance of the Keyboard class
keyboard = Keyboard(usb_hid.devices)


# Create an instance of the KeyboardLayoutUS class
keyboard_layout = KeyboardLayoutUS(keyboard)

# Define the pin connected to the data line of the WS2812 LED
pixel_pin = board.GP16

# Define the number of LEDs in the strip
num_pixels = 1

# Create a Neopixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

# Turn on the LED to a specific RGB color
pixels[0] = (255, 0, 0)  # Set the color to red (255, 0, 0)

# Alternatively, you can specify the color using hexadecimal representation
# pixels[0] = 0xFF0000  # Set the color to red

# You can also set the brightness level
# pixels.brightness = 0.5  # Set the brightness level to 50%


#--------------------------------------------
#pixel pin neopixel

#pixel_pin = board.GP23
#num_pixels = 1



#pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

#-------------------------------------------------------

#smd 3528 RGB LED PIN under key------------------------------

led_red_pin = board.GP12
led_green_pin = board.GP11
led_blue_pin = board.GP10





led_red = pwmio.PWMOut(led_red_pin)
led_green = pwmio.PWMOut(led_green_pin)
led_blue = pwmio.PWMOut(led_blue_pin)

#------------------------------------------------


#smd 3528 RGB LED indicator

led1_red_pin = board.GP13
led1_green_pin = board.GP15
led1_blue_pin = board.GP14





led1_red = pwmio.PWMOut(led1_red_pin)
led1_green = pwmio.PWMOut(led1_green_pin)
led1_blue = pwmio.PWMOut(led1_blue_pin)

#encoder 
encoder = rotaryio.IncrementalEncoder(board.GP8, board.GP7)
switch = digitalio.DigitalInOut(board.GP6)
switch.switch_to_input(pull=digitalio.Pull.DOWN)

switch_state = None
last_position = encoder.position

#rgb-----

def set_rgb_color(red_value, green_value, blue_value):
    led_red.duty_cycle = int((65535 / 255) * (255 - red_value))
    led_green.duty_cycle = int((65535 / 255) * (255 - green_value))
    led_blue.duty_cycle = int((65535 / 255) * (255 - blue_value))
    
def set1_rgb_color(red_value, green_value, blue_value):
    led1_red.duty_cycle = int((65535 / 255) * (255 - red_value))
    led1_green.duty_cycle = int((65535 / 255) * (255 - green_value))
    led1_blue.duty_cycle = int((65535 / 255) * (255 - blue_value))


#initial rgb
    
set_rgb_color(255, 0, 255)

set1_rgb_color(0, 0, 255)

#------------------------------------


#display something idk
displayio.release_displays()

# Use for I2C
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_ssd1306.SSD1306(display_bus, width=128, height=64)


# Create a text group (2023) (DEC)
text_group = displayio.Group()
text_area = label.Label(terminalio.FONT, text="MACROPAD 1.101", color=0xFFFFFF)
text_area.x = 10
text_area.y = 20
text_group.append(text_area)




# # text group previous
# 
# 
# 
# #-------------
# 
# text_area = label.Label(terminalio.FONT, text="", color=0xFFFFFF)
# text_area.x = 10
# text_area.y = 20

#------------------------IMAGE NEW PROJECT----------------------


# Load your image  ( Image group ) ------------------------------------------------

#1st Image-----------------------------------
image_file = open("adof.bmp", "rb")  # Replace with the path to your image file
image = displayio.OnDiskBitmap(image_file)
image_sprite = displayio.TileGrid(image, pixel_shader=displayio.ColorConverter())

# Create a group to hold the image
image_group = displayio.Group()
image_group.append(image_sprite)

#second image-------------------------------
image_file2 = open("makima.bmp", "rb")  # Replace with the path to your second image file
image2 = displayio.OnDiskBitmap(image_file2)
image_sprite2 = displayio.TileGrid(image2, pixel_shader=displayio.ColorConverter())

# Create a second group to hold the second image
image_group2 = displayio.Group()
image_group2.append(image_sprite2)

#3rd image ---------------------------------
image_file3 = open("skull.bmp", "rb")  # Replace with the path to your second image file
image3 = displayio.OnDiskBitmap(image_file3)
image_sprite3 = displayio.TileGrid(image3, pixel_shader=displayio.ColorConverter())

# Create a second group to hold the second image
image_group3 = displayio.Group()
image_group3.append(image_sprite3)

#-----------------------------------------------------------------------------------------

# Rotate the display 180 degrees
display.rotation = 0


print("Welcome Sir"), print("rp2040_alpha"), print("version 1.10.2")



button = digitalio.DigitalInOut(board.GP17)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

btn1_pin = board.GP5
btn2_pin = board.GP3
btn3_pin = board.GP4
btn4_pin = board.GP2



cc = ConsumerControl(usb_hid.devices)
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)







btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN


# ... (jjj existing code)

# Define the threshold for holding btn4 (adjust as needed)
hold_threshold = 1.0  # in seconds
hold_threshold2 = 3.0
hold_threshold3 = 7.0
# Initialize a variable to store the start time when btn4 is pressed
btn4_pressed_time = None
btn4_pressed = False


btn3_pressed_time = None
btn3_pressed = False
# ... (jj existing code)


def show_button_pressed(button_name):
    display.fill(0)
    text_area.text = button_name + " is pressed"
    display.show(text_area)

profile = 0  # Initialize the profile variable



while True:
   
 #neo pixel here-------------------------------------   
  

        
 #ALSO ENCODER CODE   
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            
        print(current_position)
        print("volume increasing||||||-------")
        
    elif position_change < 0:
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
            
        print(current_position)
        print("volume decreasing------|||||||||")
        
    last_position = current_position
    
    # Calculate the RGB values based on the hue
   
    
    if not switch.value and switch_state is None:
        switch_state = "pressed"
    if switch.value and switch_state == "pressed":
        print("Playing/Pause")
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        switch_state = None

    if btn1.value:
        keyboard.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.ESCAPE)
        time.sleep(0.5)
        print("Task Manager")
      
        
    if btn2.value:
        keyboard.send(Keycode.GUI, Keycode.R)  # Open the Run dialog
        time.sleep(0.5)
        keyboard_layout.write("discord")  # Type "discord" into the Run dialog
        time.sleep(0.5)
        keyboard.send(Keycode.ENTER)  # Press Enter to launch Discord
        time.sleep(0.3)
        print("Launching Discord")

        
        
    if btn3.value:
#         keyboard.send(Keycode.GUI, Keycode.R)  # Open the Run dialog
#         time.sleep(0.5)
#         keyboard_layout.write("spotify")  # Type "spotify" into the Run dialog
#         time.sleep(0.5)
#         keyboard.send(Keycode.ENTER)  # Press Enter to launch Spotify
#         time.sleep(0.3)
#         print("Launching Spotify")
        if btn3_pressed_time is None:
            # Button has just been pressed
            btn3_pressed_time = time.monotonic()

        # Check if the button has been held for the hold_threshold
        if time.monotonic() - btn3_pressed_time > hold_threshold:
            # btn4 is held down
            print("Project YT290-D")
            keyboard.send(Keycode.GUI, Keycode.R)
            time.sleep(0.1)
            keyboard_layout.write("https://cj.polau.win")
            time.sleep(0.2)
            keyboard.send(Keycode.ENTER)  # Press Enter to launch Spotify
            time.sleep(0.3)
            # Add your hold-down action here, such as displaying the image
            display.show(image_group3)
            time.sleep(1)  # Display the image for 1 second (adjust as needed)
            # Optional: Add additional actions for holding down btn4
        else:
           keyboard.send(Keycode.GUI, Keycode.R)  # Open the Run dialog
           time.sleep(0.5)
           keyboard_layout.write("spotify")  # Type "spotify" into the Run dialog
           time.sleep(0.5)
           keyboard.send(Keycode.ENTER)  # Press Enter to launch Spotify
           time.sleep(0.3)
           print("Launching Spotify")

            
    else:
        # Button is not pressed, reset the timer
        btn3_pressed_time = None


    if btn4.value:
        
#         keyboard.send(Keycode.CONTROL, Keycode.M)
#         time.sleep(0.3)
#         print("Toggling Discord Mic Mute")

        if btn4_pressed_time is None:
            # Button has just been pressed
            btn4_pressed_time = time.monotonic()
        elapsed_time = time.monotonic() - btn4_pressed_time
        # Check if the button has been held for the hold_threshold
        
        
        if time.monotonic() - btn4_pressed_time > hold_threshold:
            # btn4 is held down
            print("Hail HI##ler  ???")
            # Add your hold-down action here, such as displaying the image
            keyboard.send(Keycode.GUI, Keycode.R)
            time.sleep(0.1)
            keyboard_layout.write("https://chat.openai.com/")
            time.sleep(0.2)
            keyboard.send(Keycode.ENTER)  # Press Enter to launch Spotify
            time.sleep(0.3)
            keyboard.send(Keycode.CONTROL, Keycode.Y)
            time.sleep(0.3)
            print("Disconnected From VC")
            

        else:
            # btn4 is pressed but not held down
            keyboard.send(Keycode.CONTROL, Keycode.M)
            time.sleep(0.3)
            print("Toggling Discord Mic Mute")

            
    else:
        # Button is not pressed, reset the timer
        btn4_pressed_time = None
        
        
        

        





