import convertmatauang

def main():

    print("Convert dari Euro Ke Rupiah")
    a = int(input ("Masukkan nilai Euro: "))

    hasil = convertmatauang.EuroKeRupiah (a)
    print("Hasil dari Convert Euro Ke Rupiah adalah: ", hasil, "Rupiah")

    print("Convert dari Dollar Ke Rupiah")
    b = int(input("Masukkan nilai Dollar: "))

    hasil = convertmatauang.DollarKeRupiah(b)
    print("Hasil dari Convert Dollar Ke Rupiah adalah: ", hasil, "Rupiah")

    print("Convert dari Rupee Ke Rupiah")
    c = int(input("Masukkan nilai Rupee: "))

    hasil = convertmatauang.RupeeKeRupiah(c)
    print("Hasil dari Convert Rupee Ke Rupiah adalah: ", hasil, "Rupiah")

if __name__ == "__main__":
    main()
