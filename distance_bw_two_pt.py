print('point1')
x1 = eval(input('enter x1 coordinate : '))
y1 = eval(input('enter x2 coordinate : '))
print('point2')
x2 = eval(input('enter x2 coordinate : '))
y2 = eval(input('enter y2 coordinate : '))
l1 = (x2-x1)**2 + (y2-y1)**2
distance = l1**0.5
print('distance between two points is as follows')
print('(',x1,y1,')','(',x2,y2,')=',distance)f