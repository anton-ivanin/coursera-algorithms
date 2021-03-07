inversions = 0


def sort(unsorted_list):
    global inversions
    list_len = len(unsorted_list)
    if list_len >= 2:
        half_len = list_len // 2
        sublist1 = sort(unsorted_list[0:half_len])
        sublist2 = sort(unsorted_list[half_len:list_len])
        sorted_list = list()
        i = 0
        j = 0
        len1 = len(sublist1)
        len2 = len(sublist2)
        for k in range(list_len):
            if i >= len1:
                sorted_list.append(sublist2[j])
                j += 1
            elif j >= len2:
                sorted_list.append(sublist1[i])
                i += 1
                # inversions += 1
            elif sublist1[i] < sublist2[j]:
                sorted_list.append(sublist1[i])
                i += 1
            else:
                sorted_list.append(sublist2[j])
                j += 1
                inversions += len1 - i
        return sorted_list
    else:
        return [unsorted_list[0]]


new_list = list()
with open("IntegerArray.txt", "r") as file:
    for line in file:
        new_list.append(int(line))

# new_list = list(range(10))
# new_list.sort(reverse=True)
sorted_new_list = sort(new_list)
print(inversions)
