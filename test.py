def unlist_nonrecursive(x):
    y = []
    for element in range(0, len(x) - 1):
        if str(x[element + 2]) == "[":
            y.append(list(str(x)[1:-1]))

        elif str(x[element + 2]) != "[":
            break


        return y


      
print(unlist_nonrecursive([[[[1], [2,3], 4]]]))