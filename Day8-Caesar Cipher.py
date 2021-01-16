

#-----------------------------
#Day 8
import Caesar_Logo
multiple=1
print(Caesar_Logo.logo)

def cesar(text,shift,direction):
    end_word=""
    for i in (text):
        if i in alphabet:
            index= alphabet.index(i)
            if direction=="encode":
                i=alphabet[index+shift]
                end_word= end_word+i
            else:
                i=alphabet[index-shift]
                end_word=end_word+i
        else:
            end_word= end_word+i
    print('The {} text is {}'.format(direction,end_word))



use_again="yes"
while use_again=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = list(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))
    if shift>26:
        multiple=shift%26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2*multiple
    cesar(text, shift, direction)
    use_again = input("Do you want to use this app again? Yes/No").lower()




