meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
# print(meme_dict)
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
# print(word)

if word in meme_dict.keys():
    print("Kata yang anda ketik adalah:", word)
    print("Arti dari kata anda adalah:", meme_dict.get(word))
else:
    print("Kata tidak ada")

