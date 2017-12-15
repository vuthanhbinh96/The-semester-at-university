import pyperclip
#nhap thu vien pyperclip de su dung
message = 'THIS IS MY SECRET MESSAGE.'
#khai bao noi dung can ma hoa
key = 13
#khai bao khoa
mode = 'encrypt'
#lua chon cach ma hoa hoac giai ma
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#khai bao 26 chu de ma hoa
translated = ''
#khai bao dung de chua ket qua sau khi ma hoa
message = message.upper()
#viet hoa chuoi ky tu can ma hoa
for symbol in message:
#chay ma hoa tren moi ky tu trong tin nhan
    if symbol in LETTERS:
#neu ky tu trong LETTERS thi thuc hien
        num = LETTERS.find(symbol)
#tim ra so cua ky tu
        if mode == 'encrypt':
#neu la ma hoa
            num = num + key
#lay gia tri cua ky tu cong voi gia tri cua key
        elif mode == 'decrypt':
#neu la dich ma
            num = num - key
#lay gia tri cua ky tu cong voi gia tri cua key
        if num >= len(LETTERS):
#gia tri cua ky tu lon hon 26 thi tru di 26
            num = num - len(LETTERS)
        elif num < 0:
#gia tri cua ky tu nho hon 26 thi cong them 26
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
#gan cac ky tu sau khi ma hoa vao
    else:
        translated = translated + symbol
#gan cac ky tu khong co trong LETTERS vao
print(translated)
#in ra ket qua sau khi ma hoa
pyperclip.copy(translated)
