class Test:
    def __init__(self,x):
        self,a=x
    def get_data(self):
        print("Some Code to fetch data form data base")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()
t1=Test(5)
t1.f1()
t2.f1()