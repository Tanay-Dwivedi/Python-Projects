from collections import defaultdict


def group_anagram(a):
    grouped = defaultdict(list)
    for i in a:
        sorted_word = " ".join(sorted(i))
        grouped[sorted_word].append(i)
    return grouped.values()


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagram(words))
