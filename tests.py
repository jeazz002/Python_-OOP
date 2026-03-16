text = input()

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'"

new_text = ''
text2 = ''

s = text.split()
for i in range(len(text)):
    if text[i].isalpha() == True or text[i].isspace() == True:
        text2  += text[i]
s2 = text2.split()

print(s2)
for i in range(len(s)):
    for j in range(len(s2[i])):
        rotate = len[s2[i]]
        if s[i][j].isalpha() == True and s[i][j] == s[i][j].lower():