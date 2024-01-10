import emoji

print(emoji.emojize("Hey there peeps:call_me_hand:"))
emj = input("Input your emoji name: ")
inp_emj = ":" + emj + ":"
print("The emoji for", emj, "is", emoji.emojize(inp_emj))
