# price calculator script made by Samuel Burgess on 15'th Feb 2022
price = float(input("what is the price?: "))
type = str(input("what item type is it: "))

if price > 10 and type == "food":
    total = (price * 0.6)
elif price > 10 and type == "eletrical":
    total = (price * 0.7)
elif price > 10:
    total = (price * 0.8)
else:
    total = price
print({f"price is {total})
