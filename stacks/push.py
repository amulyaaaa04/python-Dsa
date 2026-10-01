class stack:
    def __init__(self):
        self._a=[]
        self._top=None
    def push(self,data):
        ar=[0]
        self._top=0
        self.ar=data
        self._a=self.ar
    def peek(self):
        ar=[]
stack=stack()
stack.push(10)
print(stack._a)