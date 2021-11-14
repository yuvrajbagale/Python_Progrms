class Parent:
    def ass_name(self,name):
        self.name= name

    def show_name(self):
        print("Name is", self.name)


class child(Parent):
    def ass_age(self, age):
        self.age = age

    def show_age(self):
        print("age is", self.age)


class Grandchild(child):
    def ass_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        print("gender is", self.gender)

g1 = Grandchild()

g1.ass_name("Yuvraj")
g1.ass_age(27)
g1.ass_gender("Male")

g1.show_name()
g1.show_age()
g1.show_gender()