L = [1, 2, 3, 4, 5, 6, 7, 8]

def sum_list(L, i = 0):
    if len(L) == i:
        return 0
    return sum_list(L, i + 1) + L[i]
print(sum_list(L))

# print(L)