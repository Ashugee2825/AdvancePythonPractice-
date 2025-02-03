class Demo:
    def disp(self, a=None, b=None):
        if a is None and b is None:
            print("Inside disp with 0 Para")
        elif b is None:
            print("Inside disp with 1 Para")
        else:
            print("Inside disp with 2 Para")

d = Demo()
d.disp()  # Inside disp with 0 Para
d.disp(10)  # Inside disp with 1 Para
d.disp(10, 20)  # Inside disp with 2 Para


