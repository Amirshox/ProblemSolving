def stock_list(listOfArt, listOfCat):
    stocks = dict.fromkeys(listOfCat, 0) if len(listOfArt) != 0 else {}
    for item in listOfArt:
        try:
            stocks[item[0]] += int(item.split()[-1])
        except KeyError:
            continue

    return ' - '.join(f"({key} : {value})" for key, value in stocks.items())
