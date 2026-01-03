class Football:
    def __init__(self,name,team,goal):
        self.name = name
        self.team=team
        self.goal=goal
    def shoot(self):
        print("shooting")
    def runnning(self):
        print("runnning")
    def rest(self):
        print("resting")
    def display(self):
        print(self.name)
        print(self.team)
        print(self.goal)
        print(self.age)
        print(self.height)
def main():
    f1 = Football("Football",1,1)
    f1.age=19
    f1.height=5
    f1.shoot()
    f1.runnning()
    f1.rest()
    f1.display()
if __name__ == "__main__":
    main()