from main1 import Time
import main1

h, m, s = map(int, input("Введите время №1: ").split())
t1 = Time(h, m, s)
h, m, s = map(int, input("Введите время №2: ").split())
t2 = Time(h, m, s)
print(main1.after(t1, t2))
