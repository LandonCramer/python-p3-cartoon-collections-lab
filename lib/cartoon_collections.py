def roll_call_dwarves(names):
    for i in range(len(names)):
        print(f"{i+1}. {names[i]}")
    

def summon_captain_planet(planeteer_calls):
    caption = []
    for call in planeteer_calls:
        capital = call.capitalize() + "!"
        caption.append(capital)
    return caption
# summon_captain_planet(["earth", "wind", "fire", "water", "heart"])

def long_planeteer_calls(list_calls):
    for call in list_calls:
        if len(call) > 4:
            return True
    return False
    
cheeses = ["cheddar", "gouda", "camembert"]
def find_the_cheese(list_str):

    for cheese in list_str:
        if cheese in cheeses:
            return cheese
    return None
    