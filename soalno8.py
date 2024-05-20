def temukan_bilangan_terbesar(my_list):
    if not my_list:
        return None

    bilangan_terbesar = my_list[0] 
    for bilangan in my_list:
        if bilangan > bilangan_terbesar:
            bilangan_terbesar = bilangan
    return bilangan_terbesar

my_list = [10, 20, 5, 30, 15]
output = temukan_bilangan_terbesar(my_list)
print("Bilangan terbesar dalam list adalah:", output)
