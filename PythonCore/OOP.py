class car:
    def __init__(self):
        self.name="Bmw"
        self.price=100
        self.model="M"
    def start(self):
        print("car is starting")
    def accelerate(self):
        print("car is accelerating")
    def stop(self):
        print("car is stopping")
    def display(self):
        print(self.name)
        print(self.price)
        print(self.model)
def main():
    c=car()
    print(c.name)
    c.start()
    c.accelerate()
    c.stop()
if __name__=="__main__":
    main()
