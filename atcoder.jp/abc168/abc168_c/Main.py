import math
a,b,h,m=(int(x) for x in input().split())
h=h+m/60
rad=math.radians(min(math.fabs(h-m/5),math.fabs(12-math.fabs(h-m/5)))*360/12)
print(math.sqrt(a*a+b*b-2*a*b*math.cos(rad)))