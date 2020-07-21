
from os import listdir


#from FUNC.TEXT._2_get_scrubbed import *       # Вырезка символов
#from FUNC.TEXT._4_get_relative_dict import *  # Подсчет по ключам(любой list)
#from FUNC.TEXT._5_get_edged_dict import *     # Обрезка словарей



def GET_LIST_TEXTS_FROM_THEME( folder_path , MODE = "" ):


    
    ##########################################################################
    
    all_dir_files = listdir(folder_path) # THEMES\AI

    
    LIST_target_files = []
    
    for file in all_dir_files:
        if file.endswith('.txt'):
            LIST_target_files.append(file)
    
    
   
    
    
    # print ( all_dir_files )
    # print ( LIST_target_files )

    
    
    
    ##########################################################################
    
    _cnt_words_ = 0

    
    RET_LIST_TEXTS = []    
    
    for file_name in LIST_target_files:  # r - только чтение
        
        
        #if file.startswith('- INFO'):
        if file_name == "- INFO.txt":
            continue
        
        
        file_stream = open(  folder_path+"/"+file_name ,  'r'  )
        
        
        text = file_stream.read()
        RET_LIST_TEXTS.append(  text  )
        

        
        
        
        ### Тестовый полный разбор текста
        #if MODE == "PRINT_INFO":   
        #    _cnt_words_ += CALC_ALL_TEXT_INFO(  text , folder_path+"/"+file_name )
        

        
        file_stream.close()
        
        #

    
    
    ##########################################################################
    
    print ("Количество текстов в обучающей выборке по адресу: \'"+ folder_path +"\' = " , len(RET_LIST_TEXTS) )
    
    
    
    #if MODE == "PRINT_INFO": 
    #    print( "Осталось СЛОВ после обрезки(5/95)(со всех текстов): " , _cnt_words_ )
        #print( "Осталось ФРАз после обрезки(5/95)(со всех текстов): " , _cnt_phrss_ )

    ##########################################################################
    
    
    
    return RET_LIST_TEXTS




'''
def CALC_ALL_TEXT_INFO( TEXT , file_path ):
    

    
    print( "#" * 45 )
    
    
    
    print( "Расположение: " , file_path )
    
    
    print( " *** Исходный *** " )
    print( "Количество символов: " , len(TEXT) )
    print( "Кол-во отдельных слов или симв: " , len( TEXT.split(" ") )   )
    #print( "" ,  )
    #print( "" ,  )
    #print( "" ,  )  
    print( "" )

    
    
    
    
    list_buf = [TEXT]
    scr = GET_scrubbed_list( list_buf )
    
    list_words = scr[0].split(" ")
    #list_phrs = GET_phrases_list( list_words )    
    
    print( " *** После очистки *** " )
    print( "!!! Удалено символов: "    , len(TEXT)-len(scr[0]) )
    print( "Количество символов: " , len(scr[0]) )
    
    print( "!!! Количество СЛОВ: "     , len( list_words )   )
    #print( "!!! Количество ФРАЗ: "     , len( list_phrs )   )
    #print( "" ,  )
    print( "" )
    
    
    
    
    
    dict_rel_w = GET_dict_relative_frequency(list_words)
    dict_rel_p = GET_dict_relative_frequency(list_phrs)
    
    print( " *** После обрезки под 5/95 *** " ,  )
    print( "\tОсталось СЛОВ: " , len(GET_edged_dict( dict_rel_w , 5 , 95 )) )
    #print( "\tОсталось ФРАЗ: " , len(GET_edged_dict( dict_rel_p , 5 , 95 )) )
    print( "" )
    print( " *** После обрезки под 3/95 *** " ,  )
    print( "\tОсталось СЛОВ: " , len(GET_edged_dict( dict_rel_w , 3 , 95 )) )
    #print( "\tОсталось ФРАЗ: " , len(GET_edged_dict( dict_rel_p , 3 , 95 )) )
    print( "" )
    print( " *** После обрезки под 1/95 *** " ,  )
    print( "\tОсталось СЛОВ: " , len(GET_edged_dict( dict_rel_w , 1 , 95 )) )
    #print( "\tОсталось ФРАЗ: " , len(GET_edged_dict( dict_rel_p , 1 , 95 )) )
    #print( "" ,  )
    #print( "" ,  )

    
    
    #_cnt_phrss_ += len(GET_edged_dict( dict_rel_p , 5, 95 ))
    
    print( "#" * 45 )
    
    
    
    
    return   len(GET_edged_dict( dict_rel_w , 5, 95 ))
'''





























def hello():
	print('Hello, world!')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

###