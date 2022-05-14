import main
import datetime

hours, minutes, seconds = map(int, input("Введите время №1: ").split())
t1 = datetime.time(hours, minutes, seconds)
hours, minutes, seconds = map(int, input("Введите время №2: ").split())
t2 = datetime.time(hours, minutes, seconds)
print(main.after(t1, t2))