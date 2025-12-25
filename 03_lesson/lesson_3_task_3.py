from address import Address
from Mailing import Mailing

to_address = Address(160014, "Вологда", "Мальцева", 52, 600)
from_address = Address(117312, "Москва", "Вавилова", 21, 1)

mailing = Mailing(to_address, from_address, 1500, "1524920524")
print(mailing)
