def strToint(str):
    temp = str.split()
    length = len(temp)
    output = []
    for i in range(length):
        output.append(int(temp[i]))
    return output

def recognize(str):
    while 1:     
        try:
            output = int(str)
            break
        except:
            str = input("输入数不为数字，请重新输入：")
    return output

def yihuo(str):
    length = len(str)
    temp = 0
    for i in range(length):
        temp = temp ^ str[i]
    return temp

def machine(str):
    if yihuo(str) == 0:
        str[str.index(max(str))] -= 1
        return str
    else:
        length = len(str)
        for i in range(length):
            for j in range(str[i]):
                temp = str[:]
                temp[i] = j
                if yihuo(temp) == 0:
                    return temp

first_second = input("请选择为先手还是后手，先手请输入1，后手请输入0：")
temp = input("输入石头的堆数：")
duinum = recognize(temp)
num = []
for i in range(duinum):
    a = input("请输入第"+str(i+1)+"石头堆的数量：")
    num_temp = recognize(a)
    num.append(num_temp)

if first_second == 0:
    num = machine(num_temp)
    print("machine:",num)
    flag = 0

while sum(num) != 0:
    temp = input("请输入目前的石头数量：")
    num = strToint(temp)
    print("player:",num)
    flag = 1

    if sum(num) == 0:
        break

    num = machine(num)
    print("machine:",num)
    flag = 0
    
if flag == 0:
    print("machine win")
else:
    print("player win")