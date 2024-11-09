import hashlib

with open("before.sha256","r") as f:
    ans256 = f.read().strip()

with open("afterme2.txt","r") as f:
    opdata = f.read().strip()

with open("after.txt","r") as f:
    orgdata = f.read().strip()

xxxx = "acer ache acme acre agar agee agha agma agra ahem akee amah amex arak arar arch area areg cage cake came cara care cark carr ceca cere cham char cher crag cram crax cree each ecce eche eger egma ekka emma exam gaea gaga gage game gare gear geck geek gere germ ghee gram gree greg haar hack haem haha haka hake hame hare hark harm hear hech heck hehe heme hera here herm herr kaka kama kame kara keck keek maam maar mace mach mack mage magg make mama mara marc mare marg mark marm marx meek meer mega merc mere merk raca race rach rack raga rage ragg rake rama rare reak ream rear reck reek rhea xema"
xxxx = xxxx.split(" ")

stxxxs = "stacks stages stakes stares starks starrs steaks steams stears steeks steers steres straes strags"
stxxxs = stxxxs.split(" ")

xixx = "aire cire eigg eire giga girr hick high hike hire kick kier kike kirk mica mice mick mike mime mira mire mirk rice rich rick riem riga rigg rima rime"
xixx = xixx.split(" ")

bxing = "bring being"
bxing = bxing.split(" ")

xxxxxing = "agreeing amercing charging charking charming charring checking cheeking cheering cracking cramming creaking creaming emceeing emerging garaging greeking maraging marching reaching rearming recceing reeching remaking"
xxxxxing = xxxxxing.split(" ")


for j in stxxxs:
    for k in xixx:
        for l in bxing:
            for m in xxxxxing:
                ndata = opdata.replace("xxxxxing",m)
                ndata = ndata.replace("stxxxs",j)
                ndata = ndata.replace("xixx",k)
                ndata = ndata.replace("bxing",l)
                assert len(ndata) == 717
                if hashlib.sha256(ndata.encode()).hexdigest() == ans256:
                    print(ndata)
print("done")

# CHECK
for i in range(len(orgdata)):
    if orgdata[i] == 'x':
        if ndata[i] not in 'hackergamex':
            print("NO " ,i)
    else:
        if orgdata[i] != ndata[i]:
            print("NO" ,i)

# 写CHECK的时候是因为没发现自己把一个txy写成了the .. 卡了我一小时去找,应该是try的
# https://quinapalus.com/      