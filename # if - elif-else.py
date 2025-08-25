# if - elif-else 
# print grade obtained by the folling rule
# >=80%     A
# >=60%     B
# >=40%     c
# otherwise F
m1= int(input('enter marks1:'))
m2= int(input('enter marks2:'))
m3= int(input('enter marks3:'))
m4= int(input('enter marks4:'))
m5= int(input('enter marks5:'))
per = (m1+m2+m3+m4+m5)/5
if per >= 80:
    grade ='A'
elif per >= 60 :
    grade ='B'
elif per>= 40:
    grade= 'c'
else :
    grade='F'
print('Grade=' ,grade)
    
