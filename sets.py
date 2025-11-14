# # 1
# # Boshlang'ich o'zgaruvchi: "fruits" deb nomlangan set o'zgaruvchi yaratamiz
# fruits = {"apple", "banana"}
#
# # 1-vazifa: "cherry" mevasini qo'shish
# # add() metodi: Setga yangi element qo'shadi, agar element allaqachon mavjud bo'lsa, hech narsa qilmaydi
# # Misol: {"apple", "banana"} + "cherry" -> {"apple", "banana", "cherry"}
# result1 = fruits.add("cherry")
# print("1-vazifa natijasi:", fruits)  # Natija: {'apple', 'banana', 'cherry'}
#
# # 2-vazifa: "banana" mevasini o'chirish
# # remove() metodi: Setdan belgilangan elementni o'chiradi, agar element topilmasa xato (KeyError) chiqaradi
# # Misol: {"apple", "banana", "cherry"} - "banana" -> {"apple", "cherry"}
# result2 = fruits.remove("banana")
# print("2-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry'}
#
# # 3-vazifa: "kiwi" mevasini qo'shish
# # add() metodi: Setga yangi element qo'shadi
# # Misol: {"apple", "cherry"} + "kiwi" -> {"apple", "cherry", "kiwi"}
# result3 = fruits.add("kiwi")
# print("3-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi'}
#
# # 4-vazifa: "apple" setda mavjudligini tekshirish
# # in operatori: Element setda mavjud bo'lsa True, aks holda False qaytaradi
# # Misol: "apple" in {"apple", "cherry", "kiwi"} -> True
# result4 = "apple" in fruits
# print("4-vazifa natijasi:", "yes" if result4 else "no")  # Natija: yes
#
# # 5-vazifa: "tropicals" setini yaratish va "fruits" ga qo'shish
# # update() metodi: Setga boshqa iterable (masalan, boshqa set) elementlarini qo'shadi
# # Misol: {"apple", "cherry", "kiwi"} + {"pineapple", "banana"} -> {"apple", "cherry", "kiwi", "pineapple", "banana"}
# tropicals = {"pineapple", "banana"}
# result5 = fruits.update(tropicals)
# print("5-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple', 'banana'}
#
# # 6-vazifa: "banana" ni o'chirish (xatolik bermasi uchun)
# # discard() metodi: Setdan belgilangan elementni o'chiradi, agar element topilmasa xato chiqarmaydi
# # Misol: {"apple", "cherry", "kiwi", "pineapple", "banana"} - "banana" -> {"apple", "cherry", "kiwi", "pineapple"}
# result6 = fruits.discard("banana")
# print("6-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}
#
# # 7-vazifa: "fruits" va "tropicals" farqini topish
# # difference() metodi: Birinchi setda bo'lib, ikkinchi setda bo'lmagan elementlarni qaytaradi
# # Misol: {"apple", "cherry", "kiwi", "pineapple"} - {"pineapple", "banana"} -> {"apple", "cherry", "kiwi"}
# result7 = fruits.difference(tropicals)
# print("7-vazifa natijasi:", result7)  # Natija: {'apple', 'cherry', 'kiwi'}
#
# # 8-vazifa: Yangi unique "fruits" nomli setga saqlash
# # Setning o'zi elementlarni takrorlanmas qiladi, shuning uchun faqat yangi nom bilan saqlash kifoya
# # Misol: {"apple", "cherry", "kiwi", "pineapple"} ni "unique_fruits" ga ko'chirish
# unique_fruits = fruits
# result8 = unique_fruits
# print("8-vazifa natijasi:", result8)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}
#
# # 9-vazifa: Barcha mevalarni alifbo bo'yicha tartiblash
# # sorted() funksiyasi: Iterable (masalan, set) elementlarini alifbo tartibida ro'yxat sifatida qaytaradi
# # Misol: {"apple", "cherry", "kiwi", "pineapple"} -> ['apple', 'cherry', 'kiwi', 'pineapple']
# result9 = sorted(fruits)
# print("9-vazifa natijasi:", result9)  # Natija: ['apple', 'cherry', 'kiwi', 'pineapple']
#
# # 10-vazifa: Yakuniy holatni chop etish
# # Faqat joriy setni chop qilish uchun hech qanday metod ishlatmaymiz
# print("10-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}
# # 2
# # Boshlang'ich o'zgaruvchi: "colors" deb nomlangan set o'zgaruvchi yaratamiz
# colors = {"red", "green", "blue"}
#
# # 1-vazifa: "yellow" ni qo'shish
# # add() metodi: Setga yangi element qo'shadi, agar element allaqachon mavjud bo'lsa, hech narsa qilmaydi
# # Misol: {"red", "green", "blue"} + "yellow" -> {"red", "green", "blue", "yellow"}
# result1 = colors.add("yellow")
# print("1-vazifa natijasi:", colors)  # Natija: {'red', 'green', 'blue', 'yellow'}
#
# # 2-vazifa: "green" ni o'chirish
# # discard() metodi: Setdan belgilangan elementni o'chiradi, agar element topilmasa xato chiqarmaydi
# # Misol: {"red", "green", "blue", "yellow"} - "green" -> {"red", "blue", "yellow"}
# result2 = colors.discard("green")
# print("2-vazifa natijasi:", colors)  # Natija: {'red', 'blue', 'yellow'}
#
# # 3-vazifa: "blue" ni tekshirish
# # in operatori: Element setda mavjud bo'lsa True, aks holda False qaytaradi
# # Misol: "blue" in {"red", "blue", "yellow"} -> True
# result3 = "blue" in colors
# print("3-vazifa natijasi:", "Found" if result3 else "Not Found")  # Natija: Found
#
# # 4-vazifa: Yangi set yaratish
# # extra_colors deb nomlangan yangi set yaratamiz, unda "black", "white", "red" ranglari bo'ladi
# # Misol: extra_colors = {"black", "white", "red"}
# extra_colors = {"black", "white", "red"}
# print("4-vazifa natijasi:", extra_colors)  # Natija: {'black', 'white', 'red'}
#
# # 5-vazifa: colors va extra_colors ni birlashtirish
# # union() metodi: Ikkala setning barcha elementlarini birlashtirib, yangi set qaytaradi
# # Takrorlanadigan elementlar faqat bir marta olinadi
# # Misol: {"red", "blue", "yellow"} | {"black", "white", "red"} -> {"red", "blue", "yellow", "black", "white"}
# result5 = colors.union(extra_colors)
# print("5-vazifa natijasi:", result5)  # Natija: {'red', 'blue', 'yellow', 'black', 'white'}
#
# # 6-vazifa: colors setidan extra_colors bilan umumiy bo'lmaganlarni olish
# # difference_update() metodi: Setdan boshqa set bilan umumiy elementlarni o'chiradi, natija o'z setda saqlanadi
# # Misol: {"red", "blue", "yellow"} - {"black", "white", "red"} -> {"blue", "yellow"}
# result6 = colors.difference_update(extra_colors)
# print("6-vazifa natijasi:", colors)  # Natija: {'blue', 'yellow'}
#
# # 7-vazifa: colors va extra_colors kesishmasini topish
# # intersection() metodi: Ikkala setda umumiy bo'lgan elementlarni yangi set sifatida qaytaradi
# # Misol: {"blue", "yellow"} & {"black", "white", "red"} -> set() (umumiy element yo'q)
# result7 = colors.intersection(extra_colors)
# print("7-vazifa natijasi:", result7)  # Natija: set()
#
# # 8-vazifa: Set uzunligini topish
# # len() funksiyasi: Setdagi elementlar sonini qaytaradi
# # Misol: {"blue", "yellow"} -> 2
# result8 = len(colors)
# print("8-vazifa natijasi:", result8)  # Natija: 2
#
# # 9-vazifa: Bo'sh setni nusxalab yangi set yaratish va tozalash
# # copy() metodi: Setning nusxasini yaratadi
# # clear() metodi: Setdagi barcha elementlarni o'chiradi, bo'sh set qoldiradi
# # Misol: {"blue", "yellow"} nusxasi -> bo'sh set
# new_set = colors.copy()
# new_set.clear()
# print("9-vazifa natijasi:", new_set)  # Natija: set()
#
# # 10-vazifa: Har bir bo'sh joydan so'ng setni chop etish
# # Faqat joriy setni chop qilish uchun hech qanday metod ishlatmaymiz
# print("10-vazifa natijasi:", colors)  # Natija: {'blue', 'yellow'}
# 3

# students = {'Ali', 'Vali', 'Sami'}
# result1 = students.add("Aziz")
# print("1-vazifa natijasi:", students)
# result2 = students.remove("Sami")
# print("2-vazifa natijasi:", students)
# result3 = "Jamishid" in students
# print("3-vazifa natijasi:", result3)
# result4 = students.add("Jamishid")
# print("4-vazifa natijasi:", students)
# new_students = {"Vali" , "Diyor"}
# result5 = students.update(new_students)
# print("5-vazifa natijasi:", result5)
# result6 = students.intersection(new_students)
# print("6-vazifa natijasi:", result6)
# result7 = students.difference(new_students)
# print("7-vazifa natijasi:", result7)
# graduates = {"Ali", "Jamshid"}
# print("8-vazifa natijasi:", graduates)
# result8 = graduates.symmetric_difference(students)
# print("9-vazifa natijasi:", result8)
# print("10-vazifa natijasi:", students)
# # 4
# numbers = {1, 2, 3, 4}
# result11 = numbers.add(5)
# print("1-vazifa natijasi:", numbers)
# result12 = numbers.discard(2)
# print("2-vazifa natijasi:", numbers)
# result13 = 10 in numbers
# print("3-vazifa natijasi:", result13)
# more_nums = {3, 6, 7}
# print("4-vazifa natijasi:", more_nums)
# result14 = numbers.update(more_nums)
# print("5-vazifa natijasi:", result14)
# result15 = numbers.intersection(more_nums)
# print("6-vazifa natijasi:", result15)
# result16 = numbers.difference(more_nums)
# print("7-vazifa natijasi:", result16)
# result17 = numbers.union(more_nums)
# print("8-vazifa natijasi:", result17)
# result18 = max(more_nums)
# result19 = min(more_nums)
# print("9-vazifa natijasi:", result18)
# print("10-vazifa natijasi:", result19)
# print("11-vazifa natijasi:", more_nums)
# # 5
# animals = {'cat', 'dog', 'fish'}
# result20 = animals.add("rabbit")
# print("1-vazifa natijasi:", animals)
# result21 = animals.remove("dog")
# print("2-vazifa natijasi:", animals)
# result22 = "parrot" in animals
# print("3-vazifa natijasi:", result22)
# result23 = animals.add("parrot")
# print("4-vazifa natijasi:", animals)
# more_animals = {'cat', 'lion'}
# print("5-vazifa natijasi:", more_animals)
# result24 = more_animals.update(animals)
# print("6-vazifa natijasi:", result24)
# result25 = animals.difference(more_animals)
# print("7-vazifa natijasi:", result25)
# result26 = sorted(animals)
# print("8-vazifa natijasi:", result26)
# result27 = len(animals)
# print("9-vazifa natijasi:", result27)
# print("10-vazifa natijasi:", animals)
# # 6
# cart = {'milk', 'bread', 'cheese'}
# result28 = cart.add("butter")
# print("1-vazifa natijasi:", cart)
# result29 = cart.remove("milk")
# print("2-vazifa natijasi:", cart)
# result30 = "jam" in cart
# print("3-vazifa natijasi:", cart)
# result31 = cart.add("jam")
# print("4-vazifa natijasi:", cart)
# new_items = {"bred" , "yogurt"}
# print("5-vazifa natijasi:", new_items)
# result32 = cart.update(new_items)
# print("6-vazifa natijasi:", result32)
# result33 = cart.difference(new_items)
# print("7-vazifa natijasi:", result33)
# result34 = cart.intersection(new_items)
# print("8-vazifa natijasi:", result34)
# result35 = bool(cart)
# print("9-vazifa natijasi:", result35)
# print("10-vazifa natijasi:", cart)
# # 7
# subjects = {'Math', 'Physics'}
# result36 = subjects.add("Biology")
# print("1-vazifa natijasi:", subjects)
# result37 = subjects.discard("Math")
# print("2-vazifa natijasi:", subjects)
# result38 = "Chemistry" in subjects
# print("3-vazifa natijasi:", result38)
# result39 = subjects.add("Chemistry")
# print("4-vazifa natijasi:", subjects)
# extra = {"History" , "Physics"}
# print("5-vazifa natijasi:", extra)
# result40 = subjects.union(extra)
# print("6-vazifa natijasi:", result40)
# subjects_copy = subjects.copy()
# print("7-vazifa natijasi:", subjects_copy)
# result41 = subjects_copy.add("Geography")
# print("8-vazifa natijasi:", result41)
# result42 = subjects.symmetric_difference(subjects_copy)
# print("9-vazifa natijasi:", result42)
# print("10-vazifa natijasi:", subjects)
# # 8
# cities = {'Tashkent', 'Samarkand'}
# result43 = cities.add("Bukhara")
# print("1-vazifa natijasi:", cities)
# result44 = cities.remove("Samarkand")
# print("2-vazifa natijasi:", cities)
# result45 = "Khiva" in cities
# print("3-vazifa natijasi:", result45)
# uzbek_cities = {"Andijon" , "Namangan" , "Tashkent"}
# print("4-vazifa natijasi:", uzbek_cities)
# result46 = cities.difference(uzbek_cities)
# print("5-vazifa natijasi:", result46)
# result47 = cities.intersection(uzbek_cities)
# print("6-vazifa natijasi:", result47)
# result48 = sorted(cities)
# print("7-vazifa natijasi:", cities)
# result49 = len(cities)
# print("8-vazifa natijasi:", result49)
# print("9-vazifa natijasi:", cities)
# # 9
# brands = {'Nike', 'Adidas'}
# result50 = brands.add("Puma")
# print("1-vazifa natijasi:", brands)
# result51 = brands.discard("Adidas")
# print("2-vazifa natijasi:", brands)
# result52 = "Reebok" in brands
# print("3-vazifa natijasi:", result52)
# result53 = brands.add("Reebok")
# print("4-vazifa natijasi:", brands)
# local_brands = {'Nike', 'Sabr'}
# print("5-vazifa natijasi:", local_brands)
# result54 = brands.union(local_brands)
# print("6-vazifa natijasi:", result53)
# result55 = brands.difference(local_brands)
# print("7-vazifa natijasi:", result54)
# brands_copy = brands.copy()
# print("8-vazifa natijasi:", brands_copy)
# result56 = brands_copy.clear()
# print("9-vazifa natijasi:", brands_copy)
# print("10-vazifa natijasi:", brands)
# # 10
# books = {'1984', 'Hamlet', 'Inferno'}
# result57 = books.add("Animal Farm")
# print("1-vazifa natijasi:", books)
# result58 = books.remove("Inferno")
# print("2-vazifa natijasi:", books)
# result59 = "Hamlet" in books
# print("3-vazifa natijasi:", result59)
# result60 = books.add("Fahrenheit 451")
# print("4-vazifa natijasi:", books)
# new_books = {'1984', 'Dune'}
# print("5-vazifa natijasi:", new_books)
# result61 = books.update(new_books)
# print("6-vazifa natijasi:", result61)
# result62 = books.difference(new_books)
# print("7-vazifa natijasi:", result62)
# result64 = books.intersection(new_books)
# print("8-vazifa natijasi:", result64)
# result65 = sorted(books)
# print("9-vazifa natijasi:", books)
# print("10-vazifa natijasi:", books)
# # 11
# invited = {'Ali', 'Vali', 'Salim'}
# arrived = {'Vali', 'Sami'}
# result66 = invited.add("Aziza")
# print("1-vazifa natijasi:", invited)
# result67 = invited.intersection(arrived)
# print("2-vazifa natijasi:", result67)
# result68 = invited.difference(arrived)
# print("3-vazifa natijasi:", result68)
# result69 = invited.union(arrived)
# print("4-vazifa natijasi:", result69)
# result70 = invited.clear()
# print("5-vazifa natijasi:", invited)
# result71 = arrived.discard("Sami")
# print("6-vazifa natijasi:", arrived)
# result72 = arrived.add("Sardor")
# print("7-vazifa natijasi:", arrived)
# result73 = invited.difference(arrived)
# print("8-vazifa natijasi:", result73)
# result74 = len(arrived)
# print("9-vazifa natijasi:", result74)
# print("10-vazifa natijasi:", invited)
# print("11-vazifa natijasi:", arrived)
# # 12
# udemy = {'Alisher', 'Dilshod', 'Malika'}
# coursera = {'Malika', 'Zafar'}
# result75 = udemy.add("Shahnoza")
# print("1-vazifa natijasi:", udemy)
# result76 = udemy.intersection(coursera)
# print("2-vazifa natijasi:", result76)
# result77 = coursera.difference(udemy)
# print("3-vazifa natijasi:", result77)
# result78 = coursera.union(udemy)
# print("4-vazifa natijasi:", result78)
# udemy_copy = udemy.copy()
# print("5-vazifa natijasi:", udemy_copy)
# result79 = udemy_copy.discard("Dilshod")
# print("6-vazifa natijasi:", udemy_copy)
# result80 = udemy.difference(coursera)
# print("7-vazifa natijasi:", result80)
# result81 = sorted(udemy)
# print("8-vazifa natijasi:", udemy)
# result82 = len(udemy)
# result83 = len(coursera)
# print("9-vazifa natijasi:", result82)
# print("10-vazifa natijasi:", result83)
# print("11-vazifa natijasi:", udemy)
# print("12-vazifa natijasi:", coursera)
# print("13-vazifa natijasi:", udemy_copy)
# # 13
# it_vacancy = {'Azamat', 'Javlon', 'Sarvar'}
# design_vacancy = {'Javlon', 'Sabrina'}
# result84 = it_vacancy.add("Komila")
# print("1-vazifa natijasi:", it_vacancy)
# result85 = it_vacancy.difference(design_vacancy)
# print("2-vazifa natijasi:", result85)
# result86 = it_vacancy.intersection(design_vacancy)
# print("3-vazifa natijasi:", result86)
# result87 = it_vacancy.symmetric_difference(design_vacancy)
# print("4-vazifa natijasi:", result87)
# result89 = it_vacancy.union(design_vacancy)
# print("5-vazifa natijasi:", result89)
# union_copy = result89.copy()
# print("6-vazifa natijasi:", union_copy)
# result90 = union_copy.discard("Sarvar")
# print("7-vazifa natijasi:", union_copy)
# result91 = it_vacancy.difference(design_vacancy)
# print("8-vazifa natijasi:", result91)
# result92 = len(it_vacancy)
# result93 = len(design_vacancy)
# print("9-vazifa natijasi:", result92)
# print("10-vazifa natijasi:", result93)
# result94 = sorted(it_vacancy)
# result95 = sorted(design_vacancy)
# print("11-vazifa natijasi:", result94)
# print("12-vazifa natijasi:", result95)
# # 14
# students = {'Ali', 'Soliha', 'Bobur'}
# checked = {'Bobur', 'Ali'}
# result96 = checked.add("Gulbahor")
# print("1-vazifa natijasi:", checked)
# result97 = students.difference(checked)
# print("2-vazifa natijasi:", result97)
# print("3-vazifa natijasi:", checked)
# result98 = checked.union(students)
# print("4-vazifa natijasi:", result98)
# result99 = len(checked)
# print("5-vazifa natijasi:", result99)
# result_copy =result98.copy()
# result100 = result_copy.discard("Ali")
# print("6-vazifa natijasi:", result_copy)
# result101 = students.symmetric_difference(checked)
# print("7-vazifa natijasi:", result101)
# result102 = len(students)
# result103 = len(checked)
# print("8-vazifa natijasi:", result102)
# print("9-vazifa natijasi:", result103)
# result104 = students.intersection(checked)
# print("10-vazifa natijasi:", result104)
# # 15
# toshkent_trip = {'Olim', 'Rustam', 'Ziyoda'}
# samarkand_trip = {'Ziyoda', 'Kamola'}
# result105 = toshkent_trip.add("Nodira")
# print("1-vazifa natijasi:", toshkent_trip)
# result106 = toshkent_trip.intersection(samarkand_trip)
# print("2-vazifa natijasi:", result106)
# result107 = toshkent_trip.difference(samarkand_trip)
# print("3-vazifa natijasi:", result107)
# result108= toshkent_trip.union(samarkand_trip)
# print("4-vazifa natijasi:", result108)
# result109 = toshkent_trip.symmetric_difference(samarkand_trip)
# print("5-vazifa natijasi:", result109)
# result110 = toshkent_trip.discard("Ziyoda")
# print("6-vazifa natijasi:", toshkent_trip)
# copy_set = toshkent_trip.copy()
# copy_clear = copy_set.clear()
# print("7-vazifa natijasi:", copy_set)
# result111 = len(toshkent_trip)
# result112 = len(samarkand_trip)
# print("8-vazifa natijasi:", result111)
# print("9-vazifa natijasi:", result112)
# result113 = sorted(toshkent_trip)
# result114= sorted(samarkand_trip)
# print("10-vazifa natijasi", result113)
# print("11-vazifa natijasi:", result114)
# #16
# online_orders = {'Ulugbek', 'Shoira', 'Ibrohim'}
# cash_orders = {'Ibrohim', 'Dilshod'}
# result125 = online_orders.add("Muzaffar")
# print("1-vazifa natijasi:", online_orders)
# result126 = cash_orders.difference(online_orders)
# print("2-vazifa natijasi:", result126)
# result127 = online_orders.intersection(cash_orders)
# print("3-vazifa natijasi:", result127)
# result128 = online_orders.symmetric_difference(cash_orders)
# print("4-vazifa natijasi:", result128)
# result129 = sorted(online_orders.union(cash_orders))
# print("5-vazifa natijasi:", result129)
# copy_set3 = online_orders.copy()
# print("6-vazifa natijasi:", copy_set3)
# result130 = copy_set3.clear()
# print("7-vazifa natijasi:", copy_set3)
# result131= len(online_orders)
# result132 = len(cash_orders)
# print("8-vazifa natijasi:", result131)
# print("9-vazifa natijasi:", result132)
# result133 = cash_orders.discard("Dilshod")
# print("10-vazifa natijasi:", cash_orders)
# #17
# football = {'Otabek', 'Ali'}
# basketball = {'Ali', 'Javohir'}
# result134 = football.add("Farrux")
# print("1-vazifa natijasi:", football)
# result135 = football.intersection(basketball)
# print("2-vazifa natijasi:", result135)
# result136 = football.difference(basketball)
# print("3-vazifa natijasi:", result136)
# result137 = basketball.difference(football)
# print("4-vazifa natijasi:", result137)
# result138 = football.union(basketball)
# print("5-vazifa natijasi:", result138)
# result139 = football.symmetric_difference(basketball)
# print("6-vazifa natijasi:", result139)
# result140= football.discard("Ali")
# print("7-vazifa natijasi:", football)
# basket_copy = basketball.copy()
# print("8-vazifa natijasi:", basket_copy)
# result141 = basket_copy.clear()
# print("9-vazifa natijasi:", basket_copy)
# #18
# registered = {'a@gmail.com', 'b@gmail.com', 'c@gmail.com'}
# verified = {'b@gmail.com', 'c@gmail.com', 'd@gmail.com'}
# result142 = registered.add("e@gmail.com")
# print("1-vazifa natijasi:", registered)
# result143 = registered.difference(verified)
# print("2-vazifa natijasi:", result143)
# result144 = registered.intersection(verified)
# print("3-vazifa natijasi:", result144)
# result145= registered.union(verified)
# print("4-vazifa natijasi:", result145)
# result146 = registered.difference(verified)
# print("5-vazifa natijasi:", result146)
# result147 = registered.symmetric_difference(verified)
# print("6-vazifa natijasi:", result147)
# result148 = sorted(registered)
# print("7-vazifa natijasi:", result148)
# result149 = len(registered)
# result150 = len(verified)
# print("8-vazifa registered uzunligi:", result149)
# print("9-vazifa verified uzunligi:", result150)
# result151 = registered.discard("c@gmail.com")
# print("10-vazifa natijasi:", registered)
# #19
# present = {'Asilbek', 'Nodir', 'Gulnoza'}
# late = {'Gulnoza', 'Madina'}
# result152 = present.add("Madina")
# print("1-vazifa natijasi:", present)
# result153 = late.difference(present)
# print("2-vazifa natijasi:", result153)
# result154 = present.difference(late)
# print("3-vazifa natijasi:", result154)
# result155 = present.union(late)
# print("4-vazifa natijasi:", result155)
# result156 = present.symmetric_difference(late)
# print("5-vazifa natijasi:", result156)
# result157 = present.discard("Asilbek")
# print("6-vazifa natijasi:", present)
# present_copy = present.copy()
# print("7-vazifa natijasi:", present_copy)
# result158 = present_copy.clear()
# print("8-vazifa natijasi:", present_copy)
# result159 = sorted(present)
# print("9-vazifa natijasi:", result159)
# # 20
# taken = {'Lola', 'Shoxrux', 'Muhammad'}
# returned = {'Muhammad', 'Lola'}
# result160 = taken.add("Suhrob")
# print("1-vazifa natijasi:", taken)
# result161 = returned.difference(taken)
# print("2-vazifa natijasi:", result161)
# result162 = taken.difference(returned)
# print("3-vazifa natijasi:", result162)
# result163 = taken.union(returned)
# print("4-vazifa natijasi:", result163)
# result164 = taken.difference(returned)
# print("5-vazifa natijasi:", result164)
# result165 = taken.symmetric_difference(returned)
# print("6-vazifa natijasi:", result165)
# result166 = taken.discard("Shoxrux")
# print("7-vazifa natijasi:", taken)
# taken_copy = taken.copy()
# print("8-vazifa natijasi:", taken_copy)
# result167 = sorted(taken_copy)
# print("9-vazifa natijasi:", taken_copy)
















































