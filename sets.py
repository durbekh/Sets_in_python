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
























