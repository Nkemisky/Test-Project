age = 2
# 2-8 2 dollar ticket
# 65 a five dollar ticket
# 10 dollars for everyone else 

if not ({age >= 2 and age <= 8} or age >= 65):
    print("you pay 10 dollars and you are not a child or senior")
else:
    print("you are a child or senior")
