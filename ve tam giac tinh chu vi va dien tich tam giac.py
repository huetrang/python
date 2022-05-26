import turtle
import math
tg=turtle.Turtle()
tg.pensize(5)
a = 100
for i in range(3):
    tg.fd(a)
    tg.lt(120)
    
cv = a * 3 
dt = math.sqrt((cv/2)*((cv/2)-a)**3) #dt = can bac 2 cua nua chu vi nhan voi nua chu vi luy thua 3 vì là tam giác đều
#được tính theo công thức math.sqrt(s*(s-a)*(s-b)*(s-c)) trong đó s là cv/2 , a,b,c là 3 cạnh của tam giác 
#hàm sqrt là căn bậc 2
print("chu vi tam giác = " + (str(cv)))
print("diện tích tam giác = " + (str(int(dt))))
