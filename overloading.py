class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None :
            print(x*y)
        elif x!=None:
            print(x*x)
        else :
            print("No output")
            
a=Area()
a.find_area(10)
a.find_area(20,0)
a.find_area()

