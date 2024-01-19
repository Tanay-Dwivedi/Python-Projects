def rec_binarySearch(target, sequence, first, last):
    if first > last:
        return False
    else:
        mid = (last + first) // 2
        if sequence[mid] == target:
            return True
        elif target < sequence[mid]:
            return rec_binarySearch(target, sequence, first, mid - 1)
        else:
            return rec_binarySearch(target, sequence, mid + 1, last)


# Example usage:
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = rec_binarySearch(target, sequence, 0, len(sequence) - 1)

if result:
    print(f"{target} is present in the sequence.")
else:
    print(f"{target} is not present in the sequence.")
