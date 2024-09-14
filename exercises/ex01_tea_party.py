"""Goal: calculate the cost of a tea party given a number of people"""
__author__: str = "730764770"

def main_planner(guests: int) -> None:
    """combined all functions below to compute costs with one input, guests"""
    print("A Cozy Tea Party for " + str(guests) + "People!")
    print("Tea Bags:" + str(tea_bags(people = guests)))
    print("Treats: " + str(treats(people = guests)))
    print("Cost: $" + str(cost(tea_count = tea_bags(people = guests), treat_count = treats(people = guests))))
    #Issue: couldn't concat the strings with function calls
    #Solution: had to add str to be able to concat the strings


def tea_bags(people: int) -> int:
    """Multiply amt of people by two to find amt of tea bags"""
    return (people * 2)

def treats(people: int) -> int:
    """Number of treats per person"""
    return (int(tea_bags(people = people) * 1.5))

def cost(tea_count: int, treat_count:int) -> float:
    """Computes cost of tea bags and treats combined"""
    return ((tea_count * .5) + (treat_count * .75))

if __name__ == "__main__":
    main_planner(guests = int(input("How many guests are attending your tea party?")))