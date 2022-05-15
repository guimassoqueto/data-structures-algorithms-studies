#! /bin/python3 
from itertools import count
import sys

# Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
# specifies an integer 𝑛. Finally, the last line contains integers stop 1 , stop 2 , . . . , stop 𝑛 .

# Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
# on a full tank, and there are gas stations at distances stop 1 , stop 2 , . . . , stop 𝑛 along the way, output the
# minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
# reach the destination, output −1.

# done
def compute_min_refills(distance: int, tank: int, stops: list) -> int:
    if distance <= tank: return 0

    refuels = 0
    starting_point = 0

    for i in range(len(stops)):
        has_stop = False
        while stops[i] - starting_point <= tank:
            if i == len(stops): break
            has_stop = True
            i += 1
            
            if has_stop:
                starting_point = stops[i]
                refuels += 1
                if starting_point + tank >= distance:
                    return refuels
            else: 
                return -1

    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
# done