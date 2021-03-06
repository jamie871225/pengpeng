def avg(data):
    # 請用你的程式補完這個函式的區塊
    a=data["employees"]
    b=data["count"]
    x=0
    for c in a:
        d=c["salary"]
        x+=d
    print(x/b)
avg({
        "count":3,
        "employees":[
            {
                "name":"John",
                "salary":30000
            },
            {
                "name":"Bob",
                "salary":60000
            },
            {
                "name":"Jenny",
                "salary":50000
            }
        ]
    }) # 呼叫 avg 函式