# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

s = int(input("Введите сколько журавликов делают Петя, Катя, Сережа вместе :"))
np = 1
ns = 1
nk = 4
if int(s/(np+ns+nk)) != float(s/(np+ns+nk)):
    print("Введено неверное число")
else:
    print(f"Петя сделал   {int(s/(np+ns+nk)*np)}")
    print(f"Сережа сделал {int(s/(np+ns+nk)*ns)}")
    print(f"Катя сделала  {int(s/(np+ns+nk)*nk)}")


