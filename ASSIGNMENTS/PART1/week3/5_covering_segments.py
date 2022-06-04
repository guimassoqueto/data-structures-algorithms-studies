#! /usr/bin/python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    number_of_segments = len(segments)
    points = []
    #write your code here
    for s in segments: points += list(range(s.start, s.end + 1))
    
    result = []
    _dict = {}
    for i in points:
        _dict.setdefault(i, 0)
        _dict[i] += 1

    max_count = max(_dict.values())
    for k, v in _dict.items(): 
        if v == max_count:
            result.append(k) 
    
    print(points)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    #print(len(points))
    #print(*points)
