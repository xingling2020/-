import math
import time
sl = input("水的总数量：")
sl =int(sl)
def er(sl):
    if sl==0:
      return "0"
    se=""
    while sl>0:
     se=str(sl%2)+se
     sl=sl//2
    return se
if sl>0:
    k=math.log2(sl)
else:
 k=0
k=math.ceil(k)
for bottle in range(sl):
    b=er(bottle).zfill(k)
    print(bottle,b)
time.sleep(1)
print(f"需要{k}只老鼠")
