#! /usr/bin/python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    number_of_segments = len(segments)
    indexes = set([i for i in range(number_of_segments)])

    points = []
    for s in segments:
        points.append(tuple(range(s.end, s.start -1, -1)))

    points.sort(key = lambda list: list[0], reverse = True)
    for idx, _tuple in enumerate(points): points[idx] = set(_tuple) # optional

    results = set()

    dict_sets, nums_set = {}, set()
    i = 0
    while i < number_of_segments:
        for num in points[i]:
            if num in nums_set: continue
            dict_sets.setdefault(num, {i})
            
            j = i + 1
            while j < number_of_segments:
                if num in points[j]:
                    dict_sets[num].add(j)
                    if dict_sets[num] == indexes: results.add(num)
                j += 1
            nums_set.add(num)
        i += 1
    del nums_set

    if results: return results

    print(max(indexes))

    return set()

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
