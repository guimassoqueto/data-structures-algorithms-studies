#! /usr/bin/python3

# the lists must be ordered before you call this function, 
# for sorting both lists see merge_sort below
def merge(list1: list, list2: list) -> list:
    final_list = [] # define an empty array

    # while list1 AND list2 are not empty 
    while len(list1) > 0 and len(list2) > 0: 

        # if the smallest element in list1 is smaller than the smallest element in list2
        if list1[0] < list2[0]:
            # insert the element at the end of final_list
            list1.reverse()
            final_list.append(list1.pop())
            list1.reverse()

        # in contrast, insert the element of list2  at the end of final list
        else:
            list2.reverse()
            final_list.append(list2.pop())
            list2.reverse()

    # return the final list with the remaining elements appended in it 
    return final_list + list1 + list2


# Some arbritrary list you want to sort
def merge_sort(some_list: list):
    if len(some_list) < 1: raise IndexError("The list must have at leat 1 element in it")

    # is the list has only one element, return it
    if len(some_list) == 1: return some_list

    # get the middle index of the list 
    half_index = int(len(some_list) / 2)

    # call the merge_sort recursivelly with the first half of original list as parameter
    sorted_first_half = merge_sort(some_list[:half_index])

    # call the merge_sort recursivelly with the last half of original list as parameter
    sorted_second_half = merge_sort(some_list[half_index:])

    # return the merged list, finally ordered
    return merge(sorted_first_half, sorted_second_half)


# from random import randint
# if __name__ == "__main__":

#    while True:
#        list_len = randint(1, 11)
#        random_list = [randint(1, 100) for a in range(list_len)]
#        my_algo_list = merge_sort(random_list)
#        correct_value = sorted(random_list)

#        if my_algo_list != correct_value:
#            print("input list: ", random_list, "\nmy list: ", my_algo_list, "\ncorrect_list: ", correct_value)
#            break

#        print("OK")
