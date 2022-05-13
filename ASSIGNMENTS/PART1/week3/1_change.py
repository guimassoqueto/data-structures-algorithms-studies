# Uses python3
import sys
from math import floor

# Done
def get_change(m: int) -> int:
    return floor(m / 10) + floor((m % 10) / 5) + (m % 5)


if __name__ == '__main__':
   m = int(sys.stdin.read())
   print(get_change(m))
#Done
