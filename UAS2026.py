import random

def main():
    while True:
        print("Masukkan angka antara 1 - 100")
        angka_awal = int(input("Input angka pertama: "))

        hitung = 0  # counter untuk menghitung berapa kali nilai dicetak

        while True:
            hitung += 1

            if hitung == 3:
                # pada percobaan ke-3, user input manual
                angka_random = int(input("Masukkan angka manual (ke-3): "))
            else:
                # selain ke-3, tetap random
                angka_random = random.randint(1, 100)

            print(f"Nilai ke-{hitung}: {angka_random}")

            if angka_random > angka_awal:
                print("Bilangan lebih besar, coba lagi...")
                angka_awal = angka_random  # update supaya dibandingkan lagi
            elif angka_random < angka_awal:
                print("Anda benar! Bilangan lebih kecil.")
                print(f"Bilangan terakhir: {angka_random}")
                break
            else:
                print("Nilai sama, generate lagi...")

        ulang = input("Apakah ingin mengulang? (Y/N): ").strip().upper()
        if ulang != "Y":
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()