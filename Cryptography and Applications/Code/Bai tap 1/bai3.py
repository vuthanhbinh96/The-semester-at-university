import pyperclip
#nhap thu vien pyperclip de su dung
message = 'CHIEUNAYOVUONHOA'
#khai bao noi dung can ma hoa
key1 = 3
key2 = 6
#khai bao khoa
mode = 'encrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num * key1 + key2
        elif mode == 'decrypt':
            num = (num - key2)/key1
        if num >= len(LETTERS):
            num = num % len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print(translated)
pyperclip.copy(translated)
