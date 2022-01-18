from django.shortcuts import render

# Create your views here.

def atbashCipher(request):
    plainTxt="plainTxt"
    cipherTxt="cipherTxt"

    if request.method == 'POST':
        if request.POST.get("form_type") == 'encrypt':
            txt=request.POST.get('plainTxt')
            cipherTxt=encrypt(txt)
            print("encrypt "+txt+ " "+ cipherTxt)
        elif request.POST.get("form_type") == 'decrypt':
            txt=request.POST.get('cipherTxt')
            plainTxt=decrypt(txt)
            print("decrypt "+txt+ " "+ plainTxt)
    keys={'plainTxt':plainTxt,'cipherTxt':cipherTxt}
    return render(request, 'atbash/index.html', keys)



def encrypt(plainTxt):
    cipherTxt=""
    for char in plainTxt:
        if char.isupper():
            cipherTxt+=chr(90-(ord(char)-65)%26)
        elif char==" ":
            cipherTxt+=" "
        elif char.islower():
            cipherTxt+=chr(122-(ord(char)-97)%26)
        else:
            cipherTxt+=char
    return cipherTxt

def decrypt(cipherTxt):
    plainTxt=""
    for char in cipherTxt:
        if char.isupper():
            plainTxt+=chr(90-(ord(char)-65)%26)
        elif char==" ":
            plainTxt+=" "
        elif char.islower():
            plainTxt+=chr(122-(ord(char)-97)%26)
        else:
            plainTxt+=char
    return plainTxt


