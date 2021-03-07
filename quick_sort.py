comparisons = 0


def get_pivot(unsorted_list, pivot_rule, beg_index, end_index):
    if pivot_rule == 0:
        return unsorted_list[beg_index]
    elif pivot_rule == 1:
        return unsorted_list[end_index - 1]
    elif pivot_rule == 2:
        middle_index = beg_index + (end_index - beg_index - 1) // 2
        start_element = unsorted_list[beg_index]
        final_element = unsorted_list[end_index - 1]
        middle_element = unsorted_list[middle_index]
        if start_element < final_element:
            if start_element > middle_element:
                return start_element
            else:
                if middle_element < final_element:
                    return middle_element
                else:
                    return final_element
        else:
            if final_element > middle_element:
                return final_element
            else:
                if middle_element < start_element:
                    return middle_element
                else:
                    return start_element
    else:
        raise IndexError


def initial_swap(unsorted_list, pivot_rule, beg_index, end_index):
    if pivot_rule == 0:
        pass
    elif pivot_rule == 1:
        start_element = unsorted_list[beg_index]
        final_element = unsorted_list[end_index - 1]
        unsorted_list[beg_index] = final_element
        unsorted_list[end_index - 1] = start_element
    elif pivot_rule == 2:
        middle_index = beg_index + (end_index - beg_index - 1) // 2
        start_element = unsorted_list[beg_index]
        final_element = unsorted_list[end_index - 1]
        middle_element = unsorted_list[middle_index]
        if start_element < final_element:
            if start_element > middle_element:
                pass
            else:
                if middle_element < final_element:
                    unsorted_list[beg_index] = middle_element
                    unsorted_list[middle_index] = start_element
                else:
                    unsorted_list[beg_index] = final_element
                    unsorted_list[end_index - 1] = start_element
        else:
            if final_element > middle_element:
                unsorted_list[beg_index] = final_element
                unsorted_list[end_index - 1] = start_element
            else:
                if middle_element < start_element:
                    unsorted_list[beg_index] = middle_element
                    unsorted_list[middle_index] = start_element
                else:
                    pass
    else:
        raise IndexError


def quick_sort(unsorted_list, pivot_rule, beg_index=0, end_index=0):
    global comparisons

    if end_index == 0:
        end_index = len(unsorted_list)

    list_len = end_index - beg_index

    if list_len >= 2:

        comparisons += list_len - 1

        pivot = get_pivot(unsorted_list, pivot_rule, beg_index, end_index)
        initial_swap(unsorted_list, pivot_rule, beg_index, end_index)
        i = beg_index + 1

        for j in range(beg_index, end_index):

            cur_j = unsorted_list[j]

            if cur_j < pivot:
                cur_i = unsorted_list[i]
                unsorted_list[i] = cur_j
                unsorted_list[j] = cur_i
                i += 1

        unsorted_list[beg_index] = unsorted_list[i - 1]
        unsorted_list[i - 1] = pivot

        if i - 1 > beg_index:
            quick_sort(unsorted_list, pivot_rule, beg_index, i - 1)

        if i < end_index:
            quick_sort(unsorted_list, pivot_rule, i, end_index)


new_list = list()

with open("QuickSort.txt", "r") as file:
    for line in file:
        new_list.append(int(line))

# new_list = [8, 2, 4, 5, 7, 1]
quick_sort(new_list, 2)
print(comparisons)
