#! /bin/python3 
from itertools import count
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
    # se o valor da primeira parada for maior que o limite de combustivel, retorna -1
    #if the value of the first stop is greater than the full tank limit, return -1
    if tank < stops[0]: return -1

    # se a distancia for menor que o limite de combustivel, retorna 0
    # if the distance is less than the full tank limit, return 0
    if distance <= tank: return 0

    if stops[-1] != distance: stops.append(distance)

    i = 0
    while stops[i] <= tank: i += 1

    distance -= stops[i - 1]
    stops = [stop - stops[i - 1] for stop in stops[i:]]
    
    if compute_min_refills(distance, tank, stops) < 0: return -1

    return 1 + compute_min_refills(distance, tank, stops)


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
