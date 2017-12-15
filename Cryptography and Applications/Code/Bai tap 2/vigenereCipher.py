import pyperclip
#nhap thu vien vao
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#khai bao chu de ma hoa
def main():
#ham chinh
    myMessage = """Alan Mathison Turing was a British mathematician,logician, cryptanalyst, and computer scientist. He was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov-Zhabotinsky reaction, which were first observed in the 1960s. Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant Turing a statutory pardon if enacted."""
#khai bao noi dung ma hoa
    myKey = 'ASIMOV'
#khai bao khoa
    myMode = 'encrypt'
#khai bao ma hoa
    if myMode == 'encrypt':
        translated = encryptMessage(myKey,myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey,myMessage)
    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')
def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')
def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')
def translateMessage(key, message, mode):

    translated = []
#khai bao bien chua ket qua
    keyIndex = 0
#khai bao chi so cua khoa = 0
    key = key.upper()
#bien khoa thanh chu viet hoa
    for symbol in message:
        num = LETTERS.find(symbol.upper())
#viet hoa cac ky tu trong thu can ma hoa
        if num != -1:

            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])
            num %= len(LETTERS)
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)
if __name__ == '__main__':
    main()
