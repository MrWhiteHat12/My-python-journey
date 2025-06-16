import time
import sys

text = "This will look like it's being typed..."
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)  # 50ms delay per character
print()  # for newline
