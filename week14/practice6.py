warehouse_A = {"apple": 5, "banana": 20, "orange": 3}
warehouse_B = {"apple": 2, "grape": 15, "orange": 4}


total_dic = {}
for warehouse in [warehouse_A, warehouse_B]:

    for name, amount in warehouse.items():
        if name in total_dic:
            # total_dic[name] = total_dic.get(name, 0) + amount
            total_dic[name] += amount
        else:

            total_dic[name] = amount

critical = [name for name, count in total_dic.items() if count < 10]


print(f"Total Inventory: {total_dic}")
print(f"Critical Stock: {critical}")

