# def roll_call_dwarves(names):
#     for i in range(len(names)):
#         print(f"{i+1}. {names[i]}")
    

# def summon_captain_planet(planeteer_calls):
#     caption = []
#     for call in planeteer_calls:
#         capital = call.capitalize() + "!"
#         caption.append(capital)
#     return caption
# # summon_captain_planet(["earth", "wind", "fire", "water", "heart"])

# def long_planeteer_calls(list_calls):
#     for call in list_calls:
#         if len(call) > 4:
#             return True
#     return False
    
# cheeses = ["cheddar", "gouda", "camembert"]
# def find_the_cheese(list_str):

#     for cheese in list_str:
#         if cheese in cheeses:
#             return cheese
#     return None
    
    
def roll_call_dwarves(dwarfs):
    counter = 1
    for i in range(len(dwarfs)):
        print(f"{i + 1}. {dwarfs[i]}")
        
        
# roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])

def summon_captain_planet(calls):
    result = []
    for call in calls:
        result.append(f"{call.title()}!")
    return result

# planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
# summon_captain_planet(planeteer_calls) 

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False
        
# short_words = ["puff", "go", "two"]
# print(long_planeteer_calls(short_words))
# assorted_words = ["two", "go", "industrious", "bop"]
# print(long_planeteer_calls(assorted_words))

cheeses = ["cheddar", "gouda", "camembert"]
def find_the_cheese(snacks):
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None

# snacks = ["crackers", "gouda", "thyme"]
# print(find_the_cheese(snacks))