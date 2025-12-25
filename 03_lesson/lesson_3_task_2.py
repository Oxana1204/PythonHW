from smartphone import Smartphone

catalog = [
    Smartphone("Honor", "20Pro", "+79115106160"),
    Smartphone("Samsung", "Galaxy S21", "+79115106161"),
    Smartphone("Realme", "P3 Ultra", "+79115106162"),
    Smartphone("Xiaomi", "Redmi A5", "+79115106163"),
    Smartphone("IPhone", "17 Pro Max", "+79115106164")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand}-{smartphone.phone_model}.\
        {smartphone.phone_number}")
