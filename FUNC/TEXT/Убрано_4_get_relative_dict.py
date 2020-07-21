
# кол-во раз

def GET_DICT_COUNT_ENTRY( list_words , mode="WORD" ):
  
 
    
#################################################    
    # СБОРКА В ФРАЗЫ 
    
    if mode != "WORD":
        list_phrases = []
        i = 0
        # Надо пропустить 1 итерацию
        for word in list_words:
            #Небольшой костыль => сделать for word in arr_words.(???) ) чтоб пропускал 1 итерацию
            if i == 0:
                i = 99
                first_word = word
                continue

            second_word = word
            fs_word = first_word + " " + second_word
            first_word = word
            list_phrases.append( fs_word )
    
        list_words = list_phrases
    
#################################################
    
    
    
    
    
    CNT_WORDS_IN_ALL_TEXT = len(list_words)


    
    dict_words_relative_frequency = {  }

    
    
    # Каждое слово
    for one_word in list_words: 
      
        # Если слово уже есть в списке - пропускаем т к оно уже подсчитано
        if one_word in dict_words_relative_frequency.keys():  # робит
            #print ("Найден дубль слова: "+ one_word)
            continue
    
    
        # Получаем количество повторов  (можно пихнуть сразу вниз)
        kol = list_words.count( one_word )

        
        # Пишем
        dict_words_relative_frequency.update( { one_word : kol } )
    
    
    
    return dict_words_relative_frequency







# %
def GET_dict_relative_frequency( list_words , mode="WORD" ):
  
 
    
#################################################    
    # СБОРКА В ФРАЗЫ 
    
    if mode != "WORD":
        list_phrases = []
        i = 0
        # Надо пропустить 1 итерацию
        for word in list_words:
            #Небольшой костыль => сделать for word in arr_words.(???) ) чтоб пропускал 1 итерацию
            if i == 0:
                i = 99
                first_word = word
                continue

            second_word = word
            fs_word = first_word + " " + second_word
            first_word = word
            list_phrases.append( fs_word )
    
        list_words = list_phrases
    
#################################################
    
    
    
    
    
    CNT_WORDS_IN_ALL_TEXT = len(list_words)


    
    dict_words_relative_frequency = {  }

    
    
    # Каждое слово
    for one_word in list_words:

        ### ПЕРЕПИСАТЬ т к на болших будет очень тормозить
    
        #for one_key in dict_words_frequency.keys():  # фор и иф точно катят
          #if one_word == one_key:
      
      
      
        # Если слово уже есть в списке - пропускаем т к оно уже подсчитано
        if one_word in dict_words_relative_frequency.keys():  # робит
            #print ("Найден дубль слова: "+ one_word)
            continue
    
    
        # Получаем количество повторов  (можно пихнуть сразу вниз)
        kol = list_words.count( one_word )

        # 12.345% = 0.12345
        relative_freq = kol / CNT_WORDS_IN_ALL_TEXT
    
    
        # Менять 10000 и 0.01  (прибавляем/убираем нули и там и там сразу)
        # Если с точкой
        int_freq = int(relative_freq * 100) # 12%
        float_freq = int( 10000 *  (relative_freq - (int_freq*0.01) ) ) # 100* ( 0.12345 - 0.12) = 10000 * 0.00345 = 345) 
        end_freq = int_freq + ( float_freq * 0.01 )
        
        
        # Если в целых
        #end_freq = int(relative_freq * 100)
        
        # Пишем
        dict_words_relative_frequency.update( { one_word : end_freq } )
    
    
    
    return dict_words_relative_frequency





###