from spellchecker import SpellChecker

correct = SpellChecker()

word = input("Enter a Word: ")
if word in correct:
    print("Correct spelling")
else:
    correct_word = correct.correction(word)
    print("The correct spelling is:", correct_word)
