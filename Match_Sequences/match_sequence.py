from difflib import SequenceMatcher

text1 = input("Enter the first sentence: ")
text2 = input("Enter the second sentence: ")

sequence_score = SequenceMatcher(None, text1, text2).ratio()

print(f"The entered texts are {sequence_score * 100} % similar")
