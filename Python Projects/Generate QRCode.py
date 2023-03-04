from lib2to3.pgen2.pgen import generate_grammar
import qrcode 

def generate_code():
    text = input("Enter text: ")
    name = input("Enter the name of image: ")

    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save(name + ".png")


generate_code()