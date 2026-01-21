
user_input = int(input("Будь ласка введіть число. Цифри цього числа будуть перемножуватися до тих пір поки добуток операції не буде становити 9 або менше. "))

while user_input > 9:
    product = 1
    while user_input >0:
        num = user_input % 10
        user_input = user_input // 10
        product = product * num
    user_input = product
    print(product)

