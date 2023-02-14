# celkovy pocet objed jedal
food= open("text/papanie.txt", 'r')
lines = len(food.readlines())
print("celkovy pocet objednanych jedal:", lines)

# coho je kolko
def kolko(letter):
    food=open("text/papanie.txt", 'r')
    text=food.read()
    return text.count(letter)
print(" zelene:",kolko('z'),"\n","cervene:",kolko('c'),"\n","modre:",kolko('m'),"\n","oranzove:",kolko('o'))

# viac ako 20 ppl ci ee
x = kolko('z'); y = kolko('c'); z = kolko('m'); q = kolko('o')
obeds=[x,y,z,q]
for n in obeds:
    if (n<20) and (n==5):
        print ("objednalo si menej ako 20 ludi:", n, "modre (m)")

