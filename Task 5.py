small = float(input("Введите количество литровых бутылок: "))
big = float(input("Введите количество больших бутылок: "))
print('Вы получите $', "%.2f"%(small*0.1+big*0.25), sep="")
# %.2f позволяет выводить 2 знака после запятой, sep позволяет выбрать разделитель выводимых данных
