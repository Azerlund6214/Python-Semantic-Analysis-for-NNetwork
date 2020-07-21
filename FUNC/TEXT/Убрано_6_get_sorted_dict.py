
from collections import OrderedDict
from operator import itemgetter




# Вернет ОБЫЧНЫЙ DICT
# Отсортирует по словам, а ПОТОМ по числам (т е у кучи слов со знач '1' будет своя сортировка)

def GET_sorted_dict( dict ):
    
    
    #отсортирует по возрастанию ключей словаря  РОБИТ
    dict_sorted_keys = OrderedDict(sorted(dict.items(), key=lambda t: t[0]))  # 0

    # РОБИТ  внизу большие
    dict_sorted_keys_vals = OrderedDict(sorted(dict_sorted_keys.items(), key=itemgetter(1))) # 1
    
    
    ret_dict = {   }
    
    for key in dict_sorted_keys_vals.keys():
        ret_dict.update( { key : dict_sorted_keys_vals[key] } )

        
    return ret_dict









#########