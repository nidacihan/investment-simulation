def yatirim_simulatoru():
    print("\nYatırım Simülatörüne hoş geldiniz!\n")


    try:
        baslangic_tutar = float(input("Başlangıç yatırım tutarını girin (TL): "))
        faiz_orani = float(input("yıllık faiz oranını girin (%):")) /100
        sure = int(input("Yatırım süresini girin (yıl):"))
        hesaplama_sikligi = input("Faiz hesaplama sıklığını seçin (yıllık/aylık): ").strip().lower()


        if hesaplama_sikligi == "aylık":
            donem_sayisi = sure * 12
            donemsel_faiz = faiz_orani / 12
        elif hesaplama_sikligi == "yıllık":
            donem_sayisi = sure
            donemsel_faiz = faiz_orani
        else:
            print("Hatalı giriş! Sadece 'yıllık' veya 'aylık' seçebilirsiniz.")
            return


        toplam_tutar = baslangic_tutar
        print("\nyatırım simülasyonu sonuçları:")
        print(f"{'dönem':<10}{'Dönem Başlangıcı (TL)':<25}{'kazanç':<15}{'toplam tutar':<20}")


        for donem in range(1, donem_sayisi + 1):
            kazanc = toplam_tutar * donemsel_faiz
            donem_baslangici = toplam_tutar
            toplam_tutar += kazanc
            print(f"{donem:<10}{donem_baslangici:<25.2f}{kazanc:<15.2f}{toplam_tutar:<20.2f}")

        print(f"\ntoplam kazanç: {toplam_tutar - baslangic_tutar:.2f} TL")

    except ValueError:
        print("hatalı giriş! lütfen sayısal bir değer giriniz.")

if __name__ == "__main__":
    yatirim_simulatoru()