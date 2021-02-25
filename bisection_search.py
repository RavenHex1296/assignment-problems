import math


def bisection_search(entry, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    midpoint = math.floor((low + high) / 2)

    while sorted_list[midpoint] != entry:
        if sorted_list[midpoint] < entry:
            low = midpoint + 1
            midpoint = math.floor((low + high) / 2)

        elif sorted_list[midpoint] > entry:
            high = midpoint - 1
            midpoint = math.floor((low + high) / 2)

    return midpoint

print("Asserting bisection_search")
assert bisection_search(14, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 9
print("PASSED")

#b. Consider the list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]. Lets see how many interactions we can do before there is only 1 number left. First we choose midpoint 7 (7.5 rounded down). We are left with either [0, 1, 2, 3, 4, 5, 6] or [8, 9, 10, 11, 12, 13, 14, 15]. Thats 1 iteraction. 

#If we continue with the left list, we will end up with 2 lists of length three ([0, 1, 2] and [4, 5, 6]). This is our second iteraction. If we go onto a third iteraction, we get midpoints 1 and 5 respectively. After this, our low and high points will end up equaling eachother, ending with 3 iterations. 

#Looking at [8, 9, 10, 11, 12, 13, 14, 15]. The midpoint will be either 11 or 12 (no matter what you choose the list will be split into one with length 3 and one with length 4). We'll use 11 as our midpoint because I used math.floor() in my code. After this second iteraction, we are left with [8, 9, 10] and [12, 13, 14, 15]. The list [8, 9, 10] will only need 1 more iteraction. If we look at [12, 13, 14, 15], we can continue for more iteractions. Our midpoint is then 13, leaving us with list [12] and [14, 15] after this third iteraction. We can ignore the first list and use the second since we are looking for the most number of iterations. For iteration 4, we get a "midpoint" of 14. If 14 isn't our number still, then we update the low value in midpoint to be 15 (which happens to be our high). Thus, the max number of iteractions for a list of 16 elements is 4.