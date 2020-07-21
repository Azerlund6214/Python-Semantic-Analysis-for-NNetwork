# 01.dec.17 20.29




def GET_LIST_WORDS_NO_SMALL( list_of_words , MAX_LEN_OF_SMALL_WORD ):

    
    
    # MAX_LEN_OF_SMALL_WORD = 3
    
    
    
    
    final_list_lists = []
    
    for one_word in list_of_words:
        
        if len(one_word) <= MAX_LEN_OF_SMALL_WORD:
            continue
                
        final_list_lists.append(one_word)

            
        


    return final_list_lists




###