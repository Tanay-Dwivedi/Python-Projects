from better_profanity import profanity

text = input("Enter a sentence: ")
censored_text = profanity.censor(text)
print(censored_text)
