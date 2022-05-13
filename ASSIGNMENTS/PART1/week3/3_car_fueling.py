#! /bin/python3 
import sys

# Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
# specifies an integer 𝑛. Finally, the last line contains integers stop 1 , stop 2 , . . . , stop 𝑛 .

# Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
# on a full tank, and there are gas stations at distances stop 1 , stop 2 , . . . , stop 𝑛 along the way, output the
# minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
# reach the destination, output −1.

# d = distance
# m = max car's travel distance on full tank
# stops = where stops are located

def compute_min_refills(distance: int, tank: int, stops: list):
    loop = len(stops)
    index_count = 0
    while loop:
        if distance <= 0:
            return 0
        current_stop = stops[index_count]
        entered_if = False
        if tank < current_stop:
            entered_if = True
            previous_stop_index = index_count - 1
            previous_stop_location = stops[previous_stop_index]
            distance -= previous_stop_location
            stops = [stop - stops[index_count - 1] for stop in stops[index_count:]]
            
        if not entered_if: index_count += 1
        else:
            entered_if = False
            index_count = 0
            loop = len(stops)

    return 1


compute_min_refills(950, 400, [200, 375, 550, 750])

# if __name__ == '__main__':
#     d, m, _, *stops = map(int, sys.stdin.read().split())
#     print(compute_min_refills(d, m, stops))
