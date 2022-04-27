price = int(input("Введите сумму заказа: "))
tips = price * 0.18 #чаевые 18%
taxes = price * 0.13 #налог 13%
print("Сумма чаевых: ", "%.2f"%tips, "\nНалог: ", "%.2f"%taxes, "\nОбщий итог: ", "%.2f"%(price+tips+taxes), sep="")
