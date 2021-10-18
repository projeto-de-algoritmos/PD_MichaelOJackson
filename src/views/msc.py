def msc(sequence):
    longest_subsequence_ending_with = []
    backreference_for_subsequence_ending_with = []
    current_best_end = 0
    for curr_elem in range(len(sequence)):
        longest_subsequence_ending_with.append(1)
        backreference_for_subsequence_ending_with.append(None)
        for prev_elem in range(curr_elem):
            subsequence_length_through_prev = (longest_subsequence_ending_with[prev_elem] + 1)
            if ((sequence[prev_elem] < sequence[curr_elem]) and
                    (subsequence_length_through_prev >
                         longest_subsequence_ending_with[curr_elem])):
                longest_subsequence_ending_with[curr_elem] = (subsequence_length_through_prev)
                backreference_for_subsequence_ending_with[curr_elem] = prev_elem
        if (longest_subsequence_ending_with[curr_elem] >
                longest_subsequence_ending_with[current_best_end]):
            current_best_end = curr_elem
    best_subsequence = []
    current_backreference = current_best_end
    while current_backreference is not None:
        best_subsequence.append(sequence[current_backreference])
        current_backreference = (backreference_for_subsequence_ending_with[current_backreference])
    best_subsequence.reverse()
    return best_subsequence
