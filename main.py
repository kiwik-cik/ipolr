n=int(input("Введите число: "))
prost=list(range(n+1))
prost[1]=0
for i in range(n+1):
    if prost[i]!=0:
        for j in range(i+i,n+1,i):
            prost[j]=0
prime_numbers = set(prost) #Преобразование в множество и удаление 0
prime_numbers.remove(0)

for number in prime_numbers: #Вывод простых чисел
    print(number)