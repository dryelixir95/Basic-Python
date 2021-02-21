pilihan = "y"
while (pilihan != 'n'):
    nilai_ujian_teori = float(input("masukkan nilai ujian teori? "))
    nilai_ujian_praktek = float(input("masukkan nilai ujian praktek? "))
    nilai1, nilai2 = nilai_ujian_teori, nilai_ujian_praktek

    if nilai1 >= 70 and nilai2 >= 70:
        print("Selamat, anda lulus!")
    elif nilai1 >= 70 and nilai2 <70:
        print("Anda harus mengulang ujian praktek")
    elif nilai1 < 70 and nilai2 >= 70:
        print("Anda harus mengukang ujian teori")
    else:
        print("Anda harus mengulang ujian teori dan praktek")
        break
    pilihan = input("\n\n\nApakah anda ingin menghitung ulang(y/n)? ")
