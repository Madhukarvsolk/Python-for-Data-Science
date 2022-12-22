hours = input("enter hours: ")
rate = input("enter rate: ")
h = float(hours)
r = float(rate)

if h > 40 :
    reg = h*r 
    otp = (h - 40.0) * (r*0.5)
    xp = reg + otp
    print("pay:", xp)
else:
    xp = h*r
    print("pay:", xp )
