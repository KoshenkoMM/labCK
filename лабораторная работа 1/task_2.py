symbol = 4
line = 25
number_stroc = 50
str_given = 100
disceta = 1.44 #Мб

weight_str = symbol * line
weight_page = weight_str * number_stroc
weight_book = weight_page * str_given
weight_disceta = disceta * 1024 * 1024 # Перевод Мб в байты
books = weight_disceta // weight_book

print("Количество книг, помещающихся на дискету:", int(books))