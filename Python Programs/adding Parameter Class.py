class phone:
    def set_color(self,color):
        self.color=color
        
    def set_cost(self,cost):
        self.cost=cost
        
    def show_color(self):
        print(self.color)
    
    def show_cost(self):
        print(self.cost)
        
    def make_call(self):
        print("making a Call")
    
    def play_game(self):
        print("Playing Game")
        
p2 = phone()

p2.set_color(input("Inter the Color Name= "))
p2.set_cost(input("Inter the Color Cost= "))

p2.show_color()
p2.show_cost()

    
    
    