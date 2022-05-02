class computer:
    def __init__(self, cpu, ram):
        print("in init")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config of computer is: %d %d"%(self.cpu, self.ram))
        print("test", self.ram, "test2", self.cpu)

def main():
    r1 = computer(12,14)

    r1.config()


if __name__ == "__main__":
    main()



