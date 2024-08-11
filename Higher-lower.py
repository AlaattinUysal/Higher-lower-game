import random
from game_data import data
from art import vs
from art import logo

# def add_new_country(country_name,times_visited,cities):
#   new_country = {}
#   new_country["country"] = country_name
#   new_country["visits"] = times_visited
#   new_country["list_of_cities"] = cities

# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")


def play_game():
  print(logo)
  turns = 0

  while True:
    number = random.randint(1, len(data) - 1)
    number2 = random.randint(1, len(data) - 1)
    for first_choice in data:
      first_choice = data[number]
      A = first_choice['follower_count']

     

    for second_choice in data:
      second_choice = data[number2]
      B = second_choice['follower_count']
    
         
      
    print(
      f"Compare A: {first_choice['name']} , {first_choice['description']} , from {first_choice['country']} "
    )

    print(vs)
    
    print(
      f"Against B: {second_choice['name']} , {second_choice['description']} , from {second_choice['country']} "
    )

    follower = input("Who has more followers? Type 'A' or 'B': ").lower()

    if(follower == 'a' and A > B) or (follower == 'b' and B>A):
      turns += 1
      print(f"You're right , current_score = {turns}.")
    elif A == B :
     for third_choice in data:
      number = random.randint(1, len(data) - 1)
      third_choice = data[number3]
      B = third_choice['follower_count']
     if(follower == 'a' and A > B) or (follower == 'b' and 
          B>A):
       turns += 1
       print(f"You're right , current_score = {turns}.")
     else:
         print(f"Sorry,that's wrong your final score = {turns}")
         break


    else:
      print(f"Sorry,that's wrong your final score = {turns}")
      break


play_game()
