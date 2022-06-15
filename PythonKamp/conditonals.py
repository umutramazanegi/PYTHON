istenenkredi=100000
hesap=9502
mimimumolmasigerekenhesap=10000
if hesap>=mimimumolmasigerekenhesap:
    print("Kredi verilebilir.")
elif hesap>= 9000 and hesap<=9500: #iki kuralinde geçerli olmasi demek. or iki kuraldan biri gecerli olsun
    print("Mudure sorulacak")
elif hesap>= 9501 and hesap<=9999: #iki kuralinde geçerli olmasi demek. or iki kuraldan biri gecerli olsun
    print("Genel Mudure sorulacak")
else:
    print("Kredi verilmez")