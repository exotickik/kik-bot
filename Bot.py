nama = None
riwayat = []
flag = ["riwayat", "hapus riwayat"]

while True:

    chat = input("YOU : ").strip().lower()

    if chat not in flag:
        riwayat.append(chat)

    if chat == "keluar":
        res = f"KIK BOT : Sampai jumpa!"
        print(res)
        riwayat.append(res)
        break

    elif chat.startswith(("halo","hai")):
        if chat.startswith(("halo")):
            res = f"KIK BOT : halo juga! ada yang bisa saya bantu?"
            print(res)
            riwayat.append(res)
        elif chat.startswith(("hai")):
            res = f"KIK BOT : hai juga! ada yang bisa saya bantu?"
            print(res)
            riwayat.append(res)

    elif chat.startswith(("siapa kamu")):
        res = f"KIK BOT : aku chatbot buatan KIK menggunakan Python!"
        print(res)
        riwayat.append(res)

    elif chat.startswith(("nama saya")):
        nama_baru = chat[10:].strip()
        if nama_baru:
            nama = nama_baru
            res = f"KIK BOT : oke aku ingat nama kamu {nama}"
            print(res)
            riwayat.append(res)
        else:
            res = f"KIK BOT : siapa nama kamu?"
            print(res)
            riwayat.append(res)
        
    elif chat.startswith(("siapa nama saya")):
        if nama is None:
            res = f"KIK BOT : aku belum tau nama kamu"
            print(res)
            riwayat.append(res)
        else:
            res = f"KIK BOT : nama kamu adalah {nama}"
            print(res)
            riwayat.append(res)

    elif chat == "riwayat":
        if not riwayat:
            res = f"KIK BOT : riwayat chat belum ada"
            print(res)
        else:
            res = f"KIK BOT : Riwayat Percakapan :"
            print(res)
            for i in range(len(riwayat)):
                print(i+1,riwayat[i])
                
    elif chat == "hapus riwayat":
        if not riwayat:
            res = f"Belum ada riwayat, tidak ada yang dihapus"
            print(res)
        else:
            riwayat.clear()
            res = f"Riwayat berhasil dihapus"
            print(res)

    else:
        res = f"KIK BOT : maaf aku belum mengerti"
        print(res)
        riwayat.append(res)