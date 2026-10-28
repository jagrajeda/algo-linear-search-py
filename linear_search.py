def linear_search(value_to_find, array_to_search_through):
    for i in range(len(array_to_search_through)):
        if array_to_search_through[i] == value_to_find:
            return i
    return None
# okay my linear search function passed all three

def linear_search_global(value_to_find, array_to_search_through):
    # I messed up and I need to add an accumulator to append to
    # I will declare that matching_value is my accumulator
    matching_values =[]
    for i in range(len(array_to_search_through)):
        if array_to_search_through[i] == value_to_find:
            matching_values.append(i)
        # I need to return my matching values not return i
    return matching_values

