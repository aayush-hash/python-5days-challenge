#write a program to fill in a letter template given below with name and date


letter = '''Dear <|Name|>,
Your are selected!
<|Date|> '''

print(letter.replace("<|Name|>","Aayush").replace("<|Date|>","30 Oct 2025"))