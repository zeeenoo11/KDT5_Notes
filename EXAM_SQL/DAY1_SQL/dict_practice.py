
dict_capital = {
    'Seoul': ['South Korea', 'Asia', '9,655,000'],
    'Tokyo' :['Japan', 'Asia', '14,110,000'],
    'Beijing' : ['China', 'Asia', '21,540,000'],
    'London' : ['United Kingdom', 'Europe', '14,800,000'],
    'Berlin' : ['Germany', 'Europe', '3,426,000'],
    'Mexico City' : ['Mexico', 'America', '21,200,000']}


print(sorted(dict_capital.items(), key=lambda x:int(x[1][2].replace(',',''))))
