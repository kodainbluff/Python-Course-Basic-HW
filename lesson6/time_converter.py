#This programm will convert the number you type in into days, hours, minuts and seconds. This program treats this number as seconds
time = int(input("Будь ласка введіть число від 0 до 8640000. Це число буде конвертовано з секунд в дні, години, хвилини та секунди: "))
if time >= 8640000:
    print("Error. The number is too big!")

minutes, seconds = divmod(time, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)

days_arg1 = "день"
days_arg2 = "дні"
days_arg3 = "днів"
days_exceptions1 = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
days_exceptions2 = [1, 21, 31, 41, 51, 61, 71, 81, 91]
 
if days in days_exceptions1:
   print(f"Ви ввели наступний час в секундах: {time}. Конвертований час становить: {days} {days_arg2}, {hours:02}:{minutes:02}:{seconds:02}")
elif days in days_exceptions2:
    print(f"Ви ввели наступний час в секундах: {time}. Конвертований час становить: {days} {days_arg1}, {hours:02}:{minutes:02}:{seconds:02}")
else: 
    print(f"Ви ввели наступний час в секундах: {time}. Конвертований час становить: {days} {days_arg3}, {hours:02}:{minutes:02}:{seconds:02}")