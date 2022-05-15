#! /bin/python3
distance, tank, stops = (950, 400, [200, 375, 550, 750])

def compute_min_refill(distance: int, tank: int, stops: list) -> int:
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

print(compute_min_refill(distance, tank, stops))