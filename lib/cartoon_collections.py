def roll_call_dwarves(dwarves = ["Dopey", "Grumpy", "Bashful"]):
     for i, name in enumerate(dwarves, start=1):
        print(f"{i}. {name}")


def summon_captain_planet(planeteer_calls = ["earth", "wind", "fire", "water", "heart"]):
     planeteer_calls = [name.capitalize() + '!' for name in planeteer_calls]
     return planeteer_calls
   
def long_planeteer_calls(assorted_words = ["two", "go", "industrious", "bop"]):
     return any(len(word) > 4 for word in assorted_words)
     

def find_the_cheese(soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]):
     if "cheddar" in soup:
        return "cheddar"
     else:
        return None
    