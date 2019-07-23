# coding:utf-8

rebate = input("请输入用户返点：")
rebate = float(rebate)
print("----------------------")

have_max_rebate = 0
have_min_odds = 0
have_max_odds = 0
while(1):
    if(have_max_rebate == 0):
        max_rebate = input("请输入最大返点：")
        try:
            max_rebate = float(max_rebate)
            have_max_rebate = 1
        except:
            print("最大返点输入错误，请重新输入！")
            continue
    if(have_min_odds == 0):
        min_odds = input("请输入最小赔率：")
        if(min_odds == 'x'):
            have_max_rebate = 0
            print("重新输入↓↓↓")
            continue
        else:
            try:
                min_odds = float(min_odds)
                have_min_odds = 1
            except:
                print("最小赔率输入错误，请重新输入！")
                continue
    if(have_max_odds == 0):
        max_odds = input("请输入最大赔率：")
        if(max_odds == 'x'):
            have_max_rebate = 0
            print("重新输入↓↓↓")
            continue
        else:
            try:
                max_odds = float(max_odds)
                have_max_odds = 1
            except:
                print("最大赔率输入错误，请重新输入！")
                continue

    odds = round((max_odds - min_odds)/max_rebate * rebate + min_odds, 4)
    have_min_odds = 0
    have_max_odds = 0
    print("用户赔率:%s" % odds)
    print("----------------------")

    

