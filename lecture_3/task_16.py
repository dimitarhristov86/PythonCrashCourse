# Задача 16. Хотел предлага два вида стаи: студио и апартамент.
# Напишете програма, която изчислява цената за целия престой за студио и апартамент.
# Цените зависят от месеца на престоя:

# Prices:
# Studio: may & octomber-50lv/night, june & september-75.20lv/night, july & august-76lv/night
# Apartment: may & octomber-65lv/night, june & september-68.70lv/night, july & august-77lv/night

# Предлагат се и следните отстъпки:
# За студио, при повече от 7 нощувки през май и октомври: 5% намаление.
# За студио, при повече от 14 нощувки през май и октомври: 30% намаление.
# За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# За апартамент, при повече от 14 нощувки, без значение от месеца: 10% намаление.

# Входни данни
# Входът се чете от конзолата и съдържа точно два реда:
# На първия ред е месецът – May, June, July, August, September или October.
# На втория ред е броят на нощувките – цяло число в интервала [0 … 200].

# Изходни данни
# Да се отпечатат на конзолата два реда:
# На първия ред: "Apartment: { цена за целият престой } lv."
# На втория ред: "Studio: { цена за целият престой } lv."
# Цената за целия престой да е форматирана с точност до два символа след десетичния знак.

try:
    desired_month = input("Please select month(May-October)\n> ").lower()
    days = int(input("Select stays(whole number between 0-200)\n>"))
    if desired_month == "may" or desired_month == "october":
        apartment_price = 65
        studio_price = 50
        if days <= 7:
            apartment_total_price = apartment_price * days
            studio_total_price = (studio_price * days)
            print(f"Apartment:", format(apartment_total_price, ".2f"), "lv")
            print(f"Studio:", format(studio_total_price, ".2f"), "lv")
        elif 7 < days < 14:
            apartment_price = 65
            studio_price = 50
            studio_discount_price = studio_price - (0.05 * studio_price)
            apartment_total_price = (apartment_price * days)
            studio_total_price = days * studio_discount_price
            print(f"Apartment:", format(apartment_total_price, ".2f"), "lv")
            print(f"Studio:", format(studio_total_price, ".2f"), "lv")
        elif days >= 14:
            apartment_price = 65
            studio_price = 50
            apartment_discount_price = apartment_price - (0.10 * apartment_price)
            studio_discount_price = studio_price - (0.10 * studio_price)
            apartment_total_price = apartment_discount_price * days
            studio_total_price = studio_discount_price * days
            print(f"Apartment:", format(apartment_total_price, ".2f"), "lv")
            print(f"Studio:", format(studio_total_price, ".2f"), "lv")
    elif desired_month == "june" or desired_month == "september":
        if days >= 14:
            apartment_price = 68.70
            studio_price = 75.20
            apartment_discount_price = apartment_price - (0.10 * apartment_price)
            studio_discount_price = studio_price - (0.20 * studio_price)
            apartment_total_price = apartment_discount_price * days
            studio_total_price = studio_discount_price * days
            print(f"Apartment:", format(apartment_total_price, ".2f"), "lv")
            print(f"Studio:", format(studio_total_price, ".2f"), "lv")
        elif 0 < days < 14:
            apartment_price = 68.70
            studio_price = 75.20
            apartment_total_price = (apartment_price * days)
            studio_total_price = (studio_price * days)
            print(f"Apartment:", format(apartment_total_price, ".2f"), "lv")
            print(f"Studio:", format(studio_total_price, ".2f"), "lv")
    elif desired_month == "july" or desired_month == "august":
        if days >= 14:
            apartment_price = 77
            studio_price = 76
            apartment_discount_price = apartment_price - (0.10 * apartment_price)
            apartment_total_price = apartment_discount_price * days
            studio_total_price = studio_price * days
            print(f"Apartment:", format(apartment_total_price, ".2f"), "lv")
            print(f"Studio:", format(studio_total_price, ".2f"), "lv")
        elif 0 < days < 14:
            apartment_price = 77
            studio_price = 76
            apartment_total_price = apartment_price * days
            studio_total_price = studio_price * days
            print(f"Apartment:", format(apartment_total_price, ".2f"), "lv")
            print(f"Studio:", format(studio_total_price, ".2f"), "lv")
except ValueError:
    print("Wrong data input, try again! ")
