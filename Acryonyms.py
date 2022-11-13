user_phrase = "Institute of Electrical and Electronics Engineers"

acronym = ""
for word in user_phrase.split(' '):
    if word[0].islower(): continue
    acronym += word[0] + "."

print(acronym)
