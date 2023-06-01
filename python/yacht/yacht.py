YACHT = "yatch"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "poker"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"

def score(dice, category):
    match category:
        case "yatch":
            return check_yatch(dice)
        
        case "ones":
            return check_number_decision(dice,1)
        
        case "twos":
            return check_number_decision(dice,2)
        
        case "threes":
            return check_number_decision(dice,3)
        
        case "fours":
            return check_number_decision(dice,4)
        
        case "fives":
            return check_number_decision(dice,5)
        
        case "sixes":
            return check_number_decision(dice,6)
        
        case "full_house":
            return check_full_house(dice)
        
        case "poker":
            return check_poker(dice)
        
        case "little_straight":
            return  check_straight(dice, 0)

        case "big_straight":
            return check_straight(dice , 1)

        case "choice":
            return choice(dice)

def check_yatch(dice):

    result = all(number == dice[0] for number in dice)
    if result:
        return 50
    else:
        return 0
    
def check_number_decision(dice , selection):
    result = 0

    for d in dice:
        if d == selection:
            result += d

    return result

def check_full_house(dice):

    dice.sort()

    if not all(d == dice[0] for d in dice):
        if all(d == dice[0] for d in dice[:3]):
            if all(d == dice[3] for d in dice[-2:]):
                return sum(dice)
            else:
                return 0
        elif all(d == dice[4] for d in dice[-2:]):  
            if(all(d == dice[0] for d in dice[:2])):
                return sum(dice)
            else:
                return 0
    
        else:
            return 0
    else: 
        return 0

def check_poker(dice):
    dice.sort()

    if all(d == dice[0] for d in dice[:4]):
        return sum(dice[:4])
    elif all(d == dice[4] for d in dice[-4:]):
        return sum(dice[-4:])
    else:
        return 0

def check_straight(dice , type):
    dice.sort()

    if len(dice) == len(set(dice)):
        if (dice[4] - dice[0]) <= 4:
            if type == 1 and dice[0] == 2:
                return 30
            elif type == 0 and dice[0] == 1:
                return 30    
            else:
                return 0
        else:
            return 0
    else: 
        return 0

def choice(dice):
    return sum(dice)
