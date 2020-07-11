class Cont:

    def __init__(self, client, number):
        self.client = client
        self.number = number
        self.money = 0

    def pull_money(self, value):
        self.money += value

    def push_money(self, value):
        self.money -= value
    
    def report(self):
        print("Cont number "+self.number+" has "+str(self.money))

class ContSpecial(Cont):

    def __init__(self, client, number, limit):
        Cont.__init__(self, client, number)
        self.limit = limit
    
cont = Cont("Me","1234-56")
cont.pull_money(200)
cont.push_money(3.65)
cont.report()

cont_spec = ContSpecial("You", "65-4321", 2000)
print(cont_spec)
print(cont_spec.client)