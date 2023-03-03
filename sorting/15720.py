import sys
input = sys.stdin.readline

b,c,d = map(int,input().split())

hambuger = list(map(int,input().split()))
side_dise = list(map(int,input().split()))
drink = list(map(int,input().split()))

hambuger.sort(reverse=True)
side_dise.sort(reverse=True)
drink.sort(reverse=True)

min_idx = min(b,c,d)

discount_charge = 0
for i in range(min_idx):
    tmp =  ( hambuger[i] + side_dise[i] + drink[i] ) * 0.9
    discount_charge += tmp

print(sum(hambuger)+sum(side_dise)+sum(drink))
print(int(discount_charge + sum(hambuger[min_idx:])+sum(side_dise[min_idx:])+sum(drink[min_idx:])))
