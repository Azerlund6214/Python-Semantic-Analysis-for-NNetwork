
#Все символы для вырезки из текста
arr_sumb = [
            ### Частые . " ' ( ) ? ! ; : — - – ###
            "." , "," , "\"" , "\'" , "(" , ")" , "?" , "!" , ";" , ":" , "—", "-", "–",
            # "" , "" , "",
            
            ### Редкие \ / [ ] * # % & № @ ^ < >
            ### « » | _ { } = “ ”
            "\\" , "/", "[" , "]" , "*" , "#" , "%" , "&", "№" , "@" , "^" , "<" , ">",
            "«", "»", "|", "_", "{", "}", "=", "“" , "”",
            
            ### Невидимые символы ###
            "\n" , "\t" , "\a" , 
            
            # Цифры
            "1","2","3","4","5","6","7","8","9","0",
            
            # Все англ
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            
            # Особое
             ""  ,    ""  ,
            # "\u8" ,  "\u11" , # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-2: truncated \uXXXX escape
    
            "&nbsp" , "©" , "…"
            ]  
             ### Что можно добавить:
             ### арифметические: ' - + = '
             ### Можно добавить все цифры либо найти функц для их уборки
             ### Буквы с ударением бо́льшая
             ### Англ буквы т к они все равно отрежутся
        
# На что меняем
sumb_replace = " ";



def GET_scrubbed_list( list_of_texts ):

    RET_ARR = []

    for one_text in list_of_texts:

        for sumb in arr_sumb:
            one_text = one_text.replace( sumb , sumb_replace )
    
        
        # Удаялем пробелы в начале и в конце строки
        one_text = one_text.strip( " " ) # или strip( ["","" ... ] )
      
        #Удаляем двойные пробелы  
        while one_text.count('  ')>0:
            one_text = one_text.replace('  ', ' ')
      
    
        # В нижний регистр
        one_text = one_text.lower() 
    
        RET_ARR.append( one_text )
    
    
    
    
    return RET_ARR





###