records = []
while True:
    print("\n--- 消費紀錄統計系統 ---")
    print("1.新增消費")
    print("2.顯示消費明細")
    print("3.顯示統計")
    print("4.退出系統")
    print("--------------------")

    choice = input("請選擇功能: ").strip()

    if choice == "1":
        item = input("請輸入消費項目: ").strip()
        while True:
            cost_str = input("請輸入金額: ").strip()
            temp_str = cost_str.replace(".","",1)
            if not (temp_str.isascii() and temp_str.isdigit()):
                print("\n請輸入大於 0 的數字，可包含小數點。")
                continue
            cost = float(cost_str)
            if cost <= 0:
                print("\n請輸入大於 0 的有效金額。")
                continue
            records.append({"item":item,"cost":cost})
            print("\n新增成功。")
            break
    elif choice == "2":
        if not records:
            print("\n目前沒有消費紀錄。")
        else:
            print("\n--- 消費明細 ---")
            print(f"{'編號':<6}{'項目':<10}{'金額':>5}")
            print("-----------------------------")
            for index, record in enumerate(records, start = 1):
                print(f"{index:<6}{record['item']:<10}{record['cost']:>10.2f}")
    elif choice == "3":
        alart = ["消費不多","注意控制消費","已達提醒門檻"]
        total_count = len(records)
        total_cost = sum(r["cost"] for r in records)
        avg = total_cost / total_count
        print("\n--- 消費統計 ---")
        print(f"消費筆數: {total_count}")
        print(f"總金額: {total_cost} 元")
        print(f"平均每筆金額: {avg:.2f} 元")
        if(total_cost < 300):
            print("消費提醒: ",alart[0])
        elif(total_cost>300 and total_cost <500):
            print("消費提醒: ",alart[1])
        else:
            print("消費提醒: ",alart[2])
        

    elif choice == "4":
        print("系統已退出。")
        break
    else:
        print("\n選項錯誤，請重新選擇。")