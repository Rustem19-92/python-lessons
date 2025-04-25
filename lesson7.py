# ismlar = ['Cаша', 'Маша', 'Даша']
# print("Привет " + ismlar[0] + "! Как дела?")
# print(ismlar[2] + " спросила Сашу, пойдёт ли гулять " + ismlar[1] + "?" )
# print(f"{ismlar[0]} и {ismlar[2]} друзья")


# sonlar = [10, -3, 15.0, 228, 1992, 333.3]
# print(sonlar)
# sonlar[3] = sonlar[3] + 2
# sonlar[2] = 5.0
# sonlar[0] = sonlar[1] + sonlar[5]
# sonlar[0] = sonlar[4] - 992
# sonlar[2] = sonlar[1] * 3
# del sonlar[1]
# print(sonlar)

# t_shaxslar = ['Iosif Stalin','Nikola Tesla', 'Sharof Rashidov']
# z_shaxslar = ['Sam Altman', 'Vladimir Putin', 'Djenifer Lopez']


# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\n\
# zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan\n\
# suhbat qilishni istar edim")

friends = []
friends.append('Саша')
friends.append('Маща')
friends.append('Даща')
friends.append('Алёша')
friends.append('Николай')
print(friends)

# friends.remove('Маща')
# print(friends)

# friends.insert(0, 'Абдумалик')
# friends.insert(4, 'Мохирбек')
# print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-2))
mehmonlar.append(friends.pop(1))
print("\nПришедшие гости: ", mehmonlar)



# #Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga 
# # kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# print("\nПришедшие гости: ", mehmonlar)
