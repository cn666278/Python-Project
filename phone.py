# Passing any amount of values

def make_phone(brand, *parts):
    print("Making a " + brand + " phones need to have these following parts: ")
    for part in parts:
        print("- " + part)


#make_phone('Huawei', 'leica camera', 'jingdongfang screen', 'double audio', 'blueteeth 6.0')
#make_phone("Xiaomi", 'samsung screen', 'double audio', 'blueteeth 5.0')