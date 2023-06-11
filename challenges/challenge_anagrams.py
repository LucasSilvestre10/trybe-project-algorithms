def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return ("", "", False)

    sorted_first_string = quicksort_string(first_string.lower())
    sorted_second_string = quicksort_string(second_string.lower())

    return (
        sorted_first_string,
        sorted_second_string,
        sorted_first_string == sorted_second_string,
    )


def quicksort_string(s):
    if len(s) <= 1:
        return s
    pivot = s[0]
    left = ""
    right = ""
    for c in s[1:]:
        if c < pivot:
            left += c
        else:
            right += c
    return quicksort_string(left) + pivot + quicksort_string(right)
