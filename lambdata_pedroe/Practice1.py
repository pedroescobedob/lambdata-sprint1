import random
INPUT = [1,2,3,4,5]
PEEPS = ["Pedro", "James", "Zach"]
class Stats:
    def __init__(self, vector, useless = random.randint(1,10)):
        self.vector = vector # DON'T FORGET TO RENAME ARGUMENT
        self.useless = useless
    def meanz(self): # SELF!!! INSIDE FUNCTION
        return sum(self.vector)/len(self.vector)
rudy = Stats(INPUT)
james = Stats(INPUT)
def report():
    print(f"The random number is {rudy.useless} and the mean is {rudy.meanz()}")
    print(f"The random person is {random.choice(PEEPS)}")
if __name__ == "__main__":
    print(rudy.useless)
    print(james.useless)
    print(report())