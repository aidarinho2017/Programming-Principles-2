import time
import math

def calculate_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000.0) # Convert milliseconds to seconds
    return math.sqrt(number)
number = 25100
delay_ms = 2123
result = calculate_square_root(number, delay_ms)
print(f"The square root of {number} is {result} (after {delay_ms} milliseconds)")