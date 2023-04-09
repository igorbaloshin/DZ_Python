# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

n = int(input("Введите номер билета :"))

sum1 = 0
sum2 = 0
i = 0
while n > 0:
    if i < 3:
        x = n % 10
        sum1 = sum1 + x
        n = n // 10
        i += 1
    elif i < 6:
        x = n % 10
        sum2 = sum2 + x
        n = n // 10
        i += 1
    else:
        i += 1
        break
    
    
if i > 6:
    print("Ввели неправильный номер билета")       
elif sum1 == sum2:
    print("Билет счастливый")
else:
    print("Билет не счастливый")
    
    
    
    
