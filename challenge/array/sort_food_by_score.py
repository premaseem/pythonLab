# find the favorite food based on the score

food = ['donuts', 'pancakes', 'bacon', 'waffles', 'eggs', 'bagels']
score = [0, 0, 0, 0, 0, 0]

d = {'donuts': 0, 'pancakes': 0, 'bacon': 0, 'waffles': 0, 'eggs': 0, 'bagels': 0}

print("Answer y for yes and n for no.")
user_input = input("Do you like foods with holes? ")
if user_input == 'y':
    score[0] = score[0] + 1
    score[5] = score[5] + 1
    d["donuts"] += 1
    d["bagels"] += 1
user_input2 = input("Do you like food that usually come with syrup?")
if user_input2 == 'y':
    d["bacon"] += 1
    d["eggs"] += 1
user_input3 = input("Does your food have red and white? ")
if user_input3 == 'y':
    d["waffles"] += 1

user_input4 = input("Does your food start with a b?")
if user_input4 == 'y':
    d["bagels"] += 1
user_input5 = input("Does your food have yolk in it?")
if user_input5 == 'y':
    d["eggs"] += 1
user_input6 = input("Does your food have a smooth surface without holes?")
if user_input == 'y':
    d["pancakes"] += 1

print("score list of food is:", score)
sorted_food = sorted(d.items(), key=lambda t: t[1], reverse=True)

rank = 1
print("Your Favorite food in order of score is : ")
print("rank, Food,   score")
for ele in sorted_food:
    print(rank, ele[0], ele[1])
    rank += 1
