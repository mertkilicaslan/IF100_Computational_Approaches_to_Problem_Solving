# mkilicaslan_the3
purchase_history_list = input("Please enter your purchase history: ").split(";")
code_list, amount_list = [], []

for i in purchase_history_list:
    code = i[:i.find(":")]
    amount = float(i[i.find(":") + 1:])

    if amount > 0:
        print(amount, code, "bought")
    elif amount < 0:
        if code not in code_list:
            print("You don't have", code)
            continue
        elif amount_list[code_list.index(code)] < (-1 * amount):
            print("Not enough", code)
            continue
        else:
            print(str(amount)[1:], code, "sold")

    if code not in code_list:
        code_list.append(code)
        amount_list.append(amount)
    else:
        amount_list[code_list.index(code)] = amount_list[code_list.index(code)] + amount


exchange_code = input("Please enter the currency type: ")
prices_list = input("Please enter prices: ").split(";")

total = 0
for i in prices_list:
    left = i[:i.find("_")]
    right = i[i.find("_") + 1:i.find(":")]
    rate = float(i[i.find(":") + 1:])

    if (left == exchange_code) and (right in code_list):
        total += (amount_list[code_list.index(right)] / rate)

    elif (right == exchange_code) and (left in code_list):
        total += (amount_list[code_list.index(left)] * rate)

print(f"You have {total:.2f} {exchange_code}(s).")
