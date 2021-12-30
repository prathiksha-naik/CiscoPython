class A:
    def __init__(self):
        self.stack_list=[]
    def push(self,val):
        self.stack_list.append(val)
    def pop(self):
        b=self.stack_list[-1]
        del self.stack_list[-1]
        return b
stack_object=A()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
