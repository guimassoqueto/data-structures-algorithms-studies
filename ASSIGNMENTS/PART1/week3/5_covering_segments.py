#! /usr/bin/python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    min_seg_val, max_seg_val = 1_000_000_001, -1_000_000_001
    points = []
    for s in segments:
        if s.start < min_seg_val: min_seg_val = s.start
        if s.end > max_seg_val: max_seg_val = s.end
        points.append((s.start, s.end))

    points.sort(key = lambda tup: tup[1], reverse = True)

    
    for seg_val in range(min_seg_val, max_seg_val + 1):
        j = 0
        while j < len(points):
            min_number, max_number = points[j]
            if  min_number <= seg_val <= max_number: 
                print(f'{seg_val} in {points[j]}')
            j += 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    #print(len(points))
    #print(*points)
