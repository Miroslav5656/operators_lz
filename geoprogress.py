b=int(input())
q=int(input())
n=int(input())
if -10000<=b<=10000 and 1<=q<=50 and 2<=n<=100 :
    print((b*((q**n)-1))/(q-1)) #считает сумму геом прогрессии
else :
    print("Введите другие значения")