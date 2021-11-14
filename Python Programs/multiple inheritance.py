class Parent1:
    def assign_str_one(self,str1):
        self.str1 = str1

    def show_str_one(self):
        print("String One is",self.str1)

class Parent2:
    def assign_str_two(self,str2):
        self.str2 = str2

    def show_str_two(self):
        print("String Two is",self.str2)

class child(Parent1,Parent2):
    def ass_str_three(self,str3):
        self.str3=str3

    def show_str_three(self):
        print("string is Three",self.str3)
c1 = child()

c1.assign_str_one("one")
c1.assign_str_two("two")
c1.ass_str_three("three")

c1.show_str_one()
c1.show_str_two()
c1.show_str_three()