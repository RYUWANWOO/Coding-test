import sys

input = sys.stdin.readline


def buy_joon(asset, prices):
    stock = 0
    my_asset = asset
    for price in prices:
        stock += my_asset // price
        my_asset = my_asset % price
        if my_asset == 0:
            break

    return stock * prices[-1] + my_asset


def buy_seong(asset, prices):
    stock = 0
    my_asset = asset

    for i in range(len(prices)-4):
        if prices[i] < prices[i+1] < prices[i+2] < prices[i+3]:
             my_asset += stock * prices[i+3]
             stock = 0

        if prices[i] > prices[i+1] > prices[i+2] > prices[i+3]:
            stock += my_asset // prices[i+3]
            my_asset = my_asset % prices[i+3]

    return my_asset + stock * prices[-1]

asset = int(input())

prices = list(map(int, input().split()))


if buy_joon(asset,prices) < buy_seong(asset,prices):
    print("TIMING")
elif buy_joon(asset,prices) > buy_seong(asset,prices):
    print("BNP")
else:
    print("SAMESAME")
