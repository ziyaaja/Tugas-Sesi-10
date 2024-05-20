def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    
    return luas, keliling

panjang = 5
lebar = 3

luas, keliling = hitung_persegi_panjang(panjang, lebar)
print(f"Luas: {luas}, Keliling: {keliling}")
