def sum_list(my_list):
    total = 0
    for number in my_list:
        total += number
    return total

my_list = [1, 2, 3, 4, 5]
hasil = sum_list(my_list)
print(hasil)