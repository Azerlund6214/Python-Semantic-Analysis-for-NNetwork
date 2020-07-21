







# Вывод списка в формате =    "2 : новых" или наоборот
# dict = словарь   mode = key/val/all
#all =дефолт с \n= ('ключ',знач)    val =   знач : ключ      key = наоборот

def print_dict( dict , what_first="val" ):

  
    # Если пустой
    if dict is None or len(dict) == 0:  
        print("Словарь под вывод пуст!!!")
        return
  
    if what_first == "val":
        # 2 : новых
        for key in dict.keys():
            print ( dict[key] , ':' , "\'"+key+"\'")
  
        
    if what_first == "key":
        for key in dict.keys(): # вывод элементов словаря (ключ - значение) по алфавиту
            print(key , ':', dict[key])#, end='\n')
  
            #for w in sorted(dict, key=dict.get, reverse=True):  print ( w, dict[w] )
            #for key in dict.keys(): print ( dict[key] , ':' , key)
       
        
    if what_first == "all": 
        # новых : 2 
        for one_pair in dict.items():
            print (one_pair) 


    return




