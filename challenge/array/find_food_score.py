# find the favorite food based on the score

food = ['donuts', 'pancakes', 'bacon', 'waffles', 'eggs', 'bagels']
score = [0,0,0,0,0,0]

print("Answer y for yes and n for no.")
user_input = input("Do you like foods with holes? ")
if user_input == 'y':
    score[0] = score[0] + 1
    score[5] = score[5] + 1
user_input2 = input("Do you like food that usually come with syrup?")
if user_input2 == 'y':
    score[2] = score[2] + 1
    score[4] = score[4] + 1
user_input3 = input("Does your food have red and white? ")
if user_input3 == 'y':
    score[3] = score[3] + 1
user_input4 = input("Does your food start with a b?")
if user_input4 == 'y':
    score[2] = score[2] + 1
user_input5 = input("Does your food have yolk in it?")
if user_input5 == 'y':
    score[5] = score[5] + 1
user_input6 = input("Does your food have a smooth surface without holes?")
if user_input == 'y':
    score[1] = score[1] + 1

print("score list of food is:",score)
sorted_list = sorted(score, reverse=True)
highest_score = sorted_list[0]
sorted_list.remove(highest_score)
second_highest_score = sorted_list[1]

max_index = score.index(highest_score)
max_index_second = score.index(second_highest_score)

print("Your Favorite food with highest score is: ", food[max_index])
print("Your second Favorite food  is: ", food[max_index_second])
