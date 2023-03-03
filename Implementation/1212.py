def check(my_str):
    compare_str = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i in range(len(my_str)):
        if my_str[i] == compare_str[i]:
            count += 1
        else:
            break

    return count

T = int(input())

for i in range(T):
    strstr = input()
    print("#{0} {1}".format(i+1,check(strstr)))