#! /usr/bin/python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    listOfTuples = []
    for s in segments:
        listOfTuples.append((s.start, s.end))

    sortedBeg = sorted(listOfTuples, key=lambda x: x[0])
    sortedEnd = sorted(listOfTuples, key=lambda x: x[1])

    thrhold = sortedBeg[0][0] - 1

    listOfPoints = []
    length = len(sortedEnd) - 1
    for i in range(length):
        beg, end = sortedEnd[i]
        if beg > thrhold:
            listOfPoints.append(end)
            thrhold = end

    if listOfPoints[-1] < sortedEnd[-1][0]:
        if sortedEnd:
            listOfPoints.append(sortedEnd[-1][0])

    return listOfPoints

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
