def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ''
    
    stock = {}
    
    for code in listOfArt:
        category, count = code.split()
        count = int(count)
        
        if category[0] not in stock:
            stock[category[0]] = 0
        
        stock[category[0]] += count
    
    return ' - '.join(f'({cat} : {stock.get(cat, 0)})' for cat in listOfCat)
