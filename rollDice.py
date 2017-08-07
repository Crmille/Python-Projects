
# roll.py
import random

def roll( size ):
    """Subroutine that returns the random number.
    This is built exclusively so it may be called by
    other programs."""
    return int(random.randint(1, size))


def rollDice( size, amount = 1, display = False ):
    """Subroutine that sums the total from roll().
    Assumes that if amount is not parameterized then is 1"""
    
    if display == False:
        total = 0
        for i in range(1, amount):
            total = total + roll(size)
        return total
    else:
        dicePool = [0] * amount
        total = 0
        
        for i in range( amount ):
            dicePool[i] = roll(size)
            total = total + dicePool[i]
        
        print("\nRolling ",amount,"d",size,"!")
        print("\nDice Pool:",dicePool,"Score:",total)
        # return total, dicePool
    
    if __name__=='__main__':
        rollDice()