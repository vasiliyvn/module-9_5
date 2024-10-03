
class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start:int, stop:int, step=1):
        self.start,self.stop,self.step =start,stop,step
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')
    def __iter__(self):
        self.pointer = self.start-self.step
        return self
    def __next__(self):#__next__ - метод увеличивающий атрибут pointer на step. 
        # В зависимости от знака атрибута step итерация завершиться либо когда pointer станет
        # больше stop, либо меньше stop. Учтите это при описании метода.
        self.pointer += self.step
        if (self.step>0 and self.pointer>self.stop) or (self.step<0 and self.pointer<self.stop):
            raise StopIteration
        return self.pointer



try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
