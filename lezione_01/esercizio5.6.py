age:int= input(("inserire un'età valida  ."))

if age < 2:
    print("the person is a baby")
if 2<= age < 4:
    print("the person is a toddler")
if 4<= age < 13:
    print("the person is a kid")
if 13 <= age <= 20:
    print("the person is a teenager")
if 20 <= age < 65:
    print("the person is a teenager")
if age > 65:
    print("the person is an elder")
else:
    print("inserisci età valida")