from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, LCD_FONT

def create_device():
    # Configuration parameters for the LED matrix device
    cascaded = 1  # Number of cascaded MAX7219 LED matrices
    block_orientation = 0  # Block orientation (0, 90, -90)
    rotate = 0  # Rotation (0=0°, 1=90°, 2=180°, 3=270°)
    reverse_order = False  # Set True if blocks are in reverse order
    
    serial = spi(port=0, device=0, gpio=noop())
    return max7219(serial, cascaded=cascaded, block_orientation=block_orientation,
                   rotate=rotate, blocks_arranged_in_reverse_order=reverse_order)

def display_slow_scrolling_message(device, message):
    print("Displaying slow scrolling message")
    show_message(device, message, fill="white", font=proportional(LCD_FONT), scroll_delay=0.1)

# Main execution
device = create_device()
slow_scroll_message = "The quick brown fox jumps over the lazy dog"
display_slow_scrolling_message(device, slow_scroll_message)