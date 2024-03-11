while True:
    name_in = input("Enter your name : ")
    if len(name_in) == 3: name = name_in; break
    else: print("Only 3 alphabets is approved")
balance = 100
with open('ranking_sys', mode='r', encoding='utf-8') as f_r:
    f_r.readline()
    data = sorted(f_r.readlines() + [f'{balance:5d} $ - {name}\n'],reverse=True)
    data_w = ''
    for line in data:
        data_w += line
    with open('ranking_sys', mode='w', encoding='utf-8') as f:
        f.write('----- <BlackJack Ranking> -----\n')
        f.write(data_w)