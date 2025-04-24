kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor" 
viloyat = "Samarqand"

      
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati")

print("Пожалуйста, введите данные:")
kocha = input("Улица: ")
mahalla = input("Махалля: ")
tuman = input("Район: ")
viloyat = input("Область: ")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")  

print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
      tuman + " tumani,\n" + viloyat + " viloyati")


manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())