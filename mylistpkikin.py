daftar_belanja = ["es buah","es teles","es campur"]

def tambah_item (item):
    daftar_belanja.append(item)
    print(f'"{item}"terah ditambahkan ke taftar belanja.')
def tampilkan_daftar():
    if daftar_belanja:
        print("\nDasftar belanja:")
        for i,item in enumerate(daftar_belanja,1):
            print(f"{i}.{item}")

    else:
        print("\nDaftar belanja kosong,")
def hapus_item(index):
    if 0 <= index < len (daftar_belanja):
        item = daftar_belanja.pop(index)
        print(f'"{item}" telah di hapus dari daftar brlanja.')
    else:
        print("index tidak valid.")
while True:
    print("\nMenu:")
    print("1. tambah item")
    print("2. lihat daftar belanja")
    print("3. hapus item")
    print("4. keluar")

    pilihan =input("pilih menu(1-4):")

    if pilihan == "1":
        item = input("masukan nama item: ")
        tambah_item(item)
    elif pilihan == "2":
        tampilkan_daftar()
    elif pilihan == "3":
        tampilkan_daftar()
        index = int(input("masukan nomor item yang ingin di hapus: "))- 1
        hapus_item(index)
    elif pilihan == "4":
        print ("terima kasih.")
        break
    else:
        print("silahkan coba lagi. ")
        
        
        


                  


