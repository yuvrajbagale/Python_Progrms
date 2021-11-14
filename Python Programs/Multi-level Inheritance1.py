class Parent():
    def assign_name(self,name):
        self.name= name

    def show_name(self):
        return self.name


class child(Parent):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age


class grandchild(child):
    def assign_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

g1 = grandchild()

g1.assign_name("Akshay")
g1.assign_age(27)
g1.assign_gender("Male")

g1.show_name()
g1.show_age()
g1.show_gender()