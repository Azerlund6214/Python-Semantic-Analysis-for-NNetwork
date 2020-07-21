#import scipy as sp  # Уст 01дек17
import numpy


# Вернет обычный словарь
# Обрезка краев словаря по ско
def GET_EDGED_DICT_SKO( DICT , percent_down , percent_up):

 
    dict_length = len(DICT)
    #print("Длина входного словаря: " + str(dict_length))

    # Получаем LIST из чисел
    
    LIST_COUNTS = []
    
    for cnt in DICT.values():
        LIST_COUNTS.append(cnt)
    #print(LIST_COUNTS)
    
    
    ##################

    
    
######################################
    # Весь 'матан' тут
    
    #########################
    
    LIST_COUNTS.sort()  
    print("Размах выборки ОТ ", LIST_COUNTS[0] , " ДО " , LIST_COUNTS[ len(LIST_COUNTS)-1 ] , "раз" )
    
    #########################
     
    print("Медиана(середина выборки) = ", numpy.median(LIST_COUNTS) , "раз" )
    
    #########################
    
    print("Мат ожидание(avg) = ", numpy.mean(LIST_COUNTS) , "раз" )
    
    #########################
    
    DISPERSIA = numpy.var( LIST_COUNTS )
    print("\nДисперсия = ", DISPERSIA )
    print("Дисперсия = насколько в среднем отклоняется каждый элемент в наших данных от среднего значения\n")
    #########################
    
    SKO     = numpy.std( LIST_COUNTS )
    print("СКО = ", SKO )
    print("СКО       = насколько в среднем отличаются значения признака от математического ожидания\n")
    
    
######################################
  
    FINAL_MAX_CNT = SKO*percent_up

    FINAL_MIN_CNT = SKO*percent_down

######################################
    
    print("Входные % обрезки: MIN = " , percent_down , "% MAX = " , percent_up , "%")
    print("Тогда : MIN_cnt = ", FINAL_MIN_CNT , "раз   MAX_cnt = ", FINAL_MAX_CNT , "раз" )
    
######################################

    


    dict_relative_edged = {  }
    
    for key in DICT.keys():
        
        
        if  DICT.get(key) > FINAL_MAX_CNT   or   DICT.get(key) < FINAL_MIN_CNT :
            continue
            
            
        dict_relative_edged.update( { key : DICT[key] } )
    

  
    #print( "Длина Выходного словаря: " ,len(dict_relative_edged))
    

    return  dict_relative_edged #{"123" : 456} #dict_relative_edged










# Вернет обычный словарь
# Обрезка краев словаря на N %
def GET_EDGED_DICT( DICT , percent_down , percent_up):

  
  
    dict_length = len(DICT)
    #print("Длина входного словаря: " + str(dict_length))
  
  
  
    # Создаем новый словарь (!!!!! НЕ OrderedDict - простой словарь)
    dict_relative_edged = {  }

    for key in DICT.keys():
        if float( DICT.get(key) ) >= percent_up   or   float( DICT.get(key) ) <= percent_down :
            continue
            
        dict_relative_edged.update( { key : DICT[key] } )
    

  
    #print( "Длина Выходного словаря: " ,len(dict_relative_edged))
    

    return dict_relative_edged













#######