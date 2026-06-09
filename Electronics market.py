#=========================
# electronic Market System 
#=========================

import time 
import random 


Employees={
    "john":10087,
    "alex":"@19765",
    "wilson":"aj78585A",
    "dany":9663656
}

Customers={
    
}

def decorator(func):
    def wrapper(*arg,**kwargs):
        print("Welcome to Walwark ^_^\n")
        res=func(*arg,**kwargs)
        print("Thank For Shopping ^_^")
        return res
    return wrapper


class Product:
    def __init__(self,product,price,offer):
        self.product=product
        self.price=price
        self.offer=offer
        
    def showproducts(self):
        print(f"Product: {self.product}")
        print(f"Price: ${self.price}")
        print(f"{self.offer}")
        print("----------------------")
        
monitor1=Product("ASUS TUF Gaming – 27' QHD (2560x1440), 180Hz",199.00,"No offer")
monitor2=Product("Acer SA3 23.8-inch Full HD (1920 x 1080) , 144 Hz, Black,",104.00,"%10 offer")
monitor3=Product("MSI 31.5 Curved FHD (1920x1080) HDMI DP 165Hz Gaming Monitor",174.00,"was $245")
monitor4=Product("Samsung 27 Essential S3 (S36GD) FHD 100Hz Curved Monitor",139.00,"%20 offer")
monitor5=Product("LG 27 IPS FHD 144Hz Overclock Monitor with AMD FreeSync G",109.00,"No offer")

#  GPU 
gpu1 = Product("RTX 4060 8GB", 299, "No offer")
gpu2 = Product("RTX 4060 Ti 8GB", 399, "Was 449")
gpu3 = Product("RTX 4070 12GB", 549, "%10 off")
gpu4 = Product("RX 7600 8GB", 269, "%5 off")
gpu5 = Product("RX 7800 XT 16GB", 499, "Was 549")
gpu6 = Product("RTX 4080 16GB", 999, "%8 off")
gpu7 = Product("RTX 4090 24GB", 1599, "No offer")
gpu8 = Product("RX 7700 XT 12GB", 399, "%7 off")
gpu9 = Product("RX 7900 XT 20GB", 749, "Was 799")
gpu10 = Product("RTX 3060 12GB", 249, "%12 off")


# RAM 
ram1 = Product("Corsair Vengeance 16GB DDR4", 45, "No offer")
ram2 = Product("Kingston Fury 32GB DDR5", 95, "%10 off")
ram3 = Product("G.Skill Trident Z 32GB DDR5 RGB", 119, "Was 139")
ram4 = Product("Crucial 16GB DDR5 5600MHz", 59, "No offer")
ram5 = Product("TeamGroup 64GB DDR5", 189, "%15 off")
ram6 = Product("ADATA 16GB DDR4 3200MHz", 39, "No offer")
ram7 = Product("Corsair Dominator 32GB DDR5", 149, "%5 off")
ram8 = Product("Patriot Viper 32GB DDR5", 109, "Was 129")
ram9 = Product("Samsung 16GB DDR5", 69, "%8 off")
ram10 = Product("G.Skill Ripjaws 64GB DDR5", 199, "No offer")


#  CPU 
cpu1 = Product("Intel i5-13400F", 179, "No offer")
cpu2 = Product("Intel i7-13700K", 379, "%8 off")
cpu3 = Product("AMD Ryzen 5 7600X", 229, "Was 249")
cpu4 = Product("AMD Ryzen 7 7800X3D", 399, "%5 off")
cpu5 = Product("Intel i9-13900K", 529, "Was 599")
cpu6 = Product("Intel i3-12100F", 99, "No offer")
cpu7 = Product("AMD Ryzen 9 7900X", 449, "%6 off")
cpu8 = Product("AMD Ryzen 5 5600X", 149, "Was 179")
cpu9 = Product("Intel i7-12700K", 319, "%10 off")
cpu10 = Product("AMD Ryzen 7 5800X3D", 299, "No offer")


# Motherboard 
mb1 = Product("ASUS B660M-A DDR4", 119, "No offer")
mb2 = Product("MSI B650 Tomahawk", 199, "%10 off")
mb3 = Product("Gigabyte Z790 AORUS Elite", 259, "Was 299")
mb4 = Product("ASRock B760 Pro RS", 149, "No offer")
mb5 = Product("ASUS X670-E Hero", 449, "%12 off")
mb6 = Product("MSI B550 Gaming Plus", 109, "No offer")
mb7 = Product("ASUS Z690 Prime", 189, "%7 off")
mb8 = Product("Gigabyte B650M DS3H", 129, "Was 149")
mb9 = Product("ASRock X570 Steel Legend", 169, "%5 off")
mb10 = Product("MSI Z790 Carbon", 329, "No offer")


#  PSU
psu1 = Product("Corsair CV550 550W", 49, "No offer")
psu2 = Product("Cooler Master 650W Bronze", 69, "%10 off")
psu3 = Product("Seasonic 750W Gold", 99, "Was 119")
psu4 = Product("EVGA 850W Gold", 129, "%8 off")
psu5 = Product("Corsair RM1000x 1000W", 169, "Was 189")
psu6 = Product("Thermaltake 600W", 55, "No offer")
psu7 = Product("Antec 750W Bronze", 79, "%6 off")
psu8 = Product("Gigabyte 850W Gold", 119, "Was 139")
psu9 = Product("be quiet! 1000W Platinum", 199, "%10 off")
psu10 = Product("MSI 650W Bronze", 65, "No offer")


#  SSD 
ssd1 = Product("Samsung 970 EVO Plus 1TB", 69, "No offer")
ssd2 = Product("WD Black SN850X 2TB", 129, "%12 off")
ssd3 = Product("Crucial P3 Plus 1TB", 55, "No offer")
ssd4 = Product("Kingston NV2 2TB", 89, "%10 off")
ssd5 = Product("Samsung 990 Pro 2TB", 159, "Was 179")
ssd6 = Product("ADATA XPG 1TB", 49, "No offer")
ssd7 = Product("Lexar NM790 2TB", 99, "%8 off")
ssd8 = Product("Seagate FireCuda 1TB", 79, "Was 99")
ssd9 = Product("WD Blue 2TB SATA", 69, "%5 off")
ssd10 = Product("Crucial MX500 1TB", 59, "No offer")

#  Keyboard 
key1 = Product("Logitech G213", 49, "No offer")
key2 = Product("Razer Huntsman Mini", 89, "%10 off")
key3 = Product("Corsair K70 RGB", 129, "Was 149")
key4 = Product("SteelSeries Apex 3", 59, "No offer")
key5 = Product("Redragon K552", 39, "%15 off")
key6 = Product("HyperX Alloy FPS", 69, "No offer")
key7 = Product("Razer BlackWidow V4", 139, "%8 off")
key8 = Product("Logitech G915", 199, "Was 229")
key9 = Product("Keychron K6", 79, "%5 off")
key10 = Product("MSI Vigor GK30", 45, "No offer")

#  Mouse 
mouse1 = Product("Logitech G502 Hero", 49, "No offer")
mouse2 = Product("Razer DeathAdder V2", 59, "%10 off")
mouse3 = Product("SteelSeries Rival 3", 29, "Was 39")
mouse4 = Product("Corsair Harpoon RGB", 39, "No offer")
mouse5 = Product("Glorious Model O", 69, "%12 off")
mouse6 = Product("Logitech G Pro X", 129, "No offer")
mouse7 = Product("Razer Viper Mini", 39, "%5 off")
mouse8 = Product("ASUS ROG Gladius", 79, "Was 99")
mouse9 = Product("HyperX Pulsefire", 49, "%8 off")
mouse10 = Product("Redragon M711", 25, "No offer")

# Headphones 
head1 = Product("HyperX Cloud II", 79, "No offer")
head2 = Product("Razer BlackShark V2", 99, "%10 off")
head3 = Product("SteelSeries Arctis 7", 129, "Was 149")
head4 = Product("Logitech G Pro X", 99, "No offer")
head5 = Product("Corsair HS80 RGB", 119, "%8 off")
head6 = Product("Sony WH-CH720N", 149, "No offer")
head7 = Product("Razer Kraken X", 49, "%5 off")
head8 = Product("JBL Quantum 400", 79, "Was 99")
head9 = Product("HyperX Cloud Alpha", 89, "%10 off")
head10 = Product("SteelSeries Arctis Nova 1", 59, "No offer")

#  Case 
case1 = Product("NZXT H510", 69, "No offer")
case2 = Product("Corsair 4000D Airflow", 89, "%10 off")
case3 = Product("Cooler Master TD500", 99, "Was 119")
case4 = Product("Lian Li Lancool 216", 109, "No offer")
case5 = Product("Phanteks P400A", 79, "%12 off")
case6 = Product("NZXT H7 Flow", 129, "No offer")
case7 = Product("DeepCool Matrexx 50", 59, "%5 off")
case8 = Product("ASUS TUF GT301", 99, "Was 119")
case9 = Product("MSI MPG Gungnir", 139, "%8 off")
case10 = Product("Thermaltake S100", 49, "No offer")

# iPhone 
iphone1 = Product("iPhone 13 128GB", 599, "No offer")
iphone2 = Product("iPhone 14 128GB", 699, "%10 off")
iphone3 = Product("iPhone 15 128GB", 799, "Was 899")
iphone4 = Product("iPhone 15 Pro 256GB", 1099, "%5 off")
iphone5 = Product("iPhone 15 Pro Max 256GB", 1199, "Was 1299")
iphone6 = Product("iPhone 12 64GB", 499, "No offer")
iphone7 = Product("iPhone 11 64GB", 399, "%8 off")
iphone8 = Product("iPhone 14 Pro 256GB", 999, "Was 1099")
iphone9 = Product("iPhone 15 Plus 128GB", 899, "%6 off")
iphone10 = Product("iPhone SE 2022", 349, "No offer")

mon=[monitor1,monitor2,monitor3,monitor4,monitor5]
gpu=[gpu1, gpu2, gpu3, gpu4, gpu5, gpu6, gpu7, gpu8, gpu9, gpu10]
ram=[ram1, ram2, ram3, ram4, ram5, ram6, ram7, ram8, ram9, ram10]
cpu=[cpu1, cpu2, cpu3, cpu4, cpu5, cpu6, cpu7, cpu8, cpu9, cpu10]
motherboard=[mb1, mb2, mb3, mb4, mb5, mb6, mb7, mb8, mb9, mb10]
powersupply=[psu1, psu2, psu3, psu4, psu5, psu6, psu7, psu8, psu9, psu10]
ssd=[ssd1, ssd2, ssd3, ssd4, ssd5, ssd6, ssd7, ssd8, ssd9, ssd10]
keyboard=[key1, key2, key3, key4, key5, key6, key7, key8, key9, key10]
mouse=[mouse1, mouse2, mouse3, mouse4, mouse5, mouse6, mouse7, mouse8, mouse9, mouse10]
headphone=[head1, head2, head3, head4, head5, head6, head7, head8, head9, head10]
computercase=[case1, case2, case3, case4, case5, case6, case7, case8, case9, case10]
iphone=[iphone1, iphone2, iphone3, iphone4, iphone5, iphone6, iphone7, iphone8, iphone9, iphone10]


class Cart:
    def __init__(self):
        self.cart=[]
        
    def AddingProducts(self,product,quantity):
        self.cart.append((product,quantity))
       

class Customer:
    def __init__(self,emailORphone,code):
        self.emailORphone=emailORphone
        self.code=code
def displayingLogForPay(invoice):

    while True:

        emailORphone = input(
            "Enter Phone number or Email: "
        ).strip().lower()

        if len(emailORphone) == 0:
            print("Please Enter Phone number or Email")
            continue

        print("Wait a second....")
        time.sleep(3)

        rand = random.randint(100000,900000)

        print("We Have Sent a code verification to You!")
        print(f"Your Code is : {rand}")

        while True:
            try:
                verification = int(input("Please Enter the Code: "))
            except ValueError:
                print("Invalid Code")
                continue
            if verification == rand:
                print("\n===== CART =====")
                for product, qty in addingcart.cart:
                    print(f"{product.product} x{qty}")
                    print(f"\nTotal Price : ${invoice.total()}")
                
                    yn = input("Are You Sure ? (YES OR NO): ")
                    if yn.lower() == "yes":
                        print("Processing Payment...")
                        time.sleep(3)
                        print("Successfully Payment !")
                        return emailORphone, rand
                    else:
                        print("Payment Cancelled !")
                        return None

            else:
                print("Wrong Code!")



class LoginForEmployees:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    
def DisplayingLoginForEmp():
    while True:
        name=input("Name: ")
        password=input("Password: ")
        if name.lower() in Employees and Employees[name.capitalize()] == password:
            print(f"Hi {name} !")
        else:
            print("Invalid Name or Passowrd")
            print("Please Try Again !")
            continue
        return(name,password)



class Invoices:
    def __init__(self,inv):
        self.inv=inv
    
    def total(self):
        total_price=0
        for product,quantity in self.inv.cart:
            total_price+=product.price*quantity
        return total_price


addingcart = Cart()
@decorator
def User_interactive_interface():
    while True:
        print("1.Monitors")
        print("2.GPU")
        print("3.RAM")
        print("4.CPU")
        print("5.Motherboard")
        print("6.PSU")
        print("7.SSD")
        print("8.Keyboard")
        print("9.HeadPhone")
        print("10.Case")
        print("11.iPhone")
        print("12.Mouse")
        print("13.I'm an Employee")
        print("14.Checkout")
        
        choice=int(input("\nPlease Enter a number of choice : "))
        if choice not in range(1,15):
            print("Invalid Choice")
            continue
        
        elif choice == 1:
            for monitor in mon:
                monitor.showproducts()
                add = input("Add to CART or press enter: ")
                if add.lower() == "add":
                    try:
                        qty = int(input("Quantity: "))
                        addingcart.AddingProducts(monitor,qty)
                    except ValueError:
                        print("Invalid Quantity")
                
                    
        elif (choice ==2):
            print("")
            for GPU in gpu:
                GPU.showproducts()
                add=input("Add to CART or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(GPU, qty)
                    
        elif (choice ==3):
            print("")
            for RAM in ram:
                RAM.showproducts()
                add=input("Add to CART or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(RAM, qty)
                
        elif (choice ==4):
            print("")
            for CPU in cpu:
                CPU.showproducts()
                add=input("Add to CART(type add/no) or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(CPU, qty)
        elif (choice ==5):
            print("")
            for mo in motherboard:
                mo.showproducts()
                add=input("Add to CART or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(mo, qty)
        elif (choice ==6):
            print("")
            for PSU in powersupply:
                PSU.showproducts()
                add=input("Add to CART or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(PSU, qty)
        elif (choice ==7):
            print("")
            for SSD in ssd:
                SSD.showproducts()
                add=input("Add to CART or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(SSD, qty)
        elif (choice ==8):
            print("")
            for HEAD in headphone:
                HEAD.showproducts()
                add=input("Add to CART or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(HEAD, qty)
        elif (choice ==9):
            print("")
            for KEY in keyboard:
                KEY.showproducts()
                add=input("Add to CART or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(KEY, qty)
        elif (choice ==10):
            print("")
            for CASE in computercase:
                CASE.showproducts()
                add=input("Add to CART or press enter: ")
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(CASE, qty)
        elif (choice ==11):
            print("")
            for I in iphone:
                I.showproducts()
                add=input("Add to CART or press enter: ")
                
                if add.lower()=="add":
                    qty = int(input("Quantity: "))
                    addingcart.AddingProducts(I, qty)
        elif choice == 12:
            print("")
            for m in mouse:
                m.showproducts()
                add = input("Add to CART or press enter: ")
                if add.lower() == "add":
                    try:
                        qty = int(input("Quantity: "))
                        addingcart.AddingProducts(m, qty)
                    except ValueError:
                        print("Invalid Quantity")
                    
        elif (choice ==13):
            print("")
            data=DisplayingLoginForEmp()
            employee=LoginForEmployees(*data)
            break
        
        elif choice == 14:

            if not addingcart.cart:
                print("Cart is Empty")
                continue
            invoc = Invoices(addingcart)
            data = displayingLogForPay(invoc)
            if data:
                cust = Customer(*data)
            break
            
User_interactive_interface()