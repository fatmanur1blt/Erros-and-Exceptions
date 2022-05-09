def tam_sayi_cevir():
    while True:
        girdi=input("Bir ondalık sayi giriniz:")
        try:
            girdi=float(girdi)
            print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))
            break
        except:
            print("{} girdisi ondalık tipe çevrilemiyor".format(girdi))
            pass
        tam_sayi_cevir()