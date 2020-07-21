import matplotlib.pyplot as plt
import numpy


def GET_EDGED_LIST_WORDS_SKO_PLT( LIST_WORDS , LIST_OFFSETS , DRAW_PLT=False ):
    
    
    
    
    #########################
    offset_min = LIST_OFFSETS[0]   # 0 + СКО * это
    offset_max = LIST_OFFSETS[1]   # max - СКО * это
    offset_M   = LIST_OFFSETS[2]   # по обе стороны
    #########################
    
    
    
    #########################
    
    
    DICT_WORDS_CNT = {    }
    
    # Каждое слово
    for one_word in LIST_WORDS:  
        # Если слово уже есть в списке - пропускаем т к оно уже подсчитано
        if one_word in DICT_WORDS_CNT.keys():  # робит
            continue
    
        # Получаем количество повторов  (можно пихнуть сразу вниз)
        kol = LIST_WORDS.count( one_word )

        # Пишем
        DICT_WORDS_CNT.update( { one_word : kol } )
    
    #########################
    
        LIST_CNTS_DUBLES = []
        for word_cnt in DICT_WORDS_CNT.keys():
            LIST_CNTS_DUBLES.append( DICT_WORDS_CNT[word_cnt] )
            
        #LIST_CNTS_DUBLES.sort()
    #########################
    
        #LIST_CNTS_DUBLES_NO_ONE = []
        #for cnt in LIST_CNTS_DUBLES:
        #    if cnt >=4 : LIST_CNTS_DUBLES_NO_ONE.append( cnt )
    
    
    #########################
    # print( "Количество слов в этом тексте: " , len(LIST_CNTS_DUBLES) )
    # print( "Уникальных слов в этом тексте: " , len(LIST_WORDS) )
    
    M = numpy.mean(LIST_CNTS_DUBLES)
    print("Мат ожидание(avg) = ", M , "раз" )
    
    SKO = numpy.std( LIST_CNTS_DUBLES )
    print("СКО = ", SKO )
    
    #########################
    
    MIN_REPEAT = min(LIST_CNTS_DUBLES)
    MAX_REPEAT = max(LIST_CNTS_DUBLES)
    print("MIN знач = ", MIN_REPEAT )
    print("MAX знач = ", MAX_REPEAT )
    
    
    DROP_SKO_LEFT  = MIN_REPEAT + SKO * offset_min
    DROP_SKO_RIGHT = MAX_REPEAT - SKO * offset_min
    print("SKO левая   = ", DROP_SKO_LEFT )
    print("SKO правая  = ", DROP_SKO_RIGHT )
    
    
    DROP_M_LEFT  = M - SKO * offset_M    
    DROP_M_RIGHT = M + SKO * offset_M
    print("М левая  = ", DROP_M_LEFT )
    print("М правая = ", DROP_M_RIGHT )
    
    #########################
    
    DROP_SKO_LEFT = int(DROP_SKO_LEFT)
    DROP_SKO_RIGHT = int(DROP_SKO_RIGHT)
    DROP_M_LEFT = int(DROP_M_LEFT)
    DROP_M_RIGHT = int(DROP_M_RIGHT)
    
    #########################
    
    print("\nИтоговые резки:")
    print("Если меньше: ", DROP_SKO_LEFT )
    print("Если больше: ", DROP_SKO_RIGHT)
    print("Если в диапазоне: от ", DROP_M_LEFT, " до ", DROP_M_RIGHT)

    #########################
    
    print("\nЦелевые будут следующие:")

    
    ONE_CNT_MIN = 0
    ONE_CNT_MAX = 0
    
    if DROP_M_LEFT <= DROP_SKO_LEFT:  # 1 диапазон ( М уехало влево)
        ONE_CNT_MIN = DROP_M_RIGHT
        ONE_CNT_MAX = DROP_SKO_RIGHT
        print("Будет 1 диапазон:")
        print("ОТ ", ONE_CNT_MIN+1 , " ДО " , ONE_CNT_MAX-1 , " (включая)" )
    
    if DROP_M_RIGHT >= DROP_SKO_RIGHT:  # 1 диапазон ( М уехало вправо)
        ONE_CNT_MIN = DROP_SKO_LEFT
        ONE_CNT_MAX = DROP_M_LEFT
        print("Будет 1 диапазон:")
        print("ОТ ", ONE_CNT_MIN+1 , " ДО " , ONE_CNT_MAX-1 , " (включая)" )
    
    
    if DROP_M_LEFT >= DROP_SKO_LEFT and DROP_M_RIGHT <= DROP_SKO_RIGHT:
        ONE_CNT_MIN = DROP_SKO_LEFT
        ONE_CNT_MAX = DROP_M_LEFT
        TWO_CNT_MIN = DROP_M_RIGHT
        TWO_CNT_MAX = DROP_SKO_RIGHT
        print("Будет 2 диапазонa:")
        print("1) ОТ ", ONE_CNT_MIN+1 , " ДО " , ONE_CNT_MAX-1 , " (включая)" )
        print("2) ОТ ", TWO_CNT_MIN+1 , " ДО " , TWO_CNT_MAX-1 , " (включая)" )
    
    #########################
    
    
    #########################
    #########################
    #########################
    
    
    #########################
    
    if DRAW_PLT == True:
        
                
        LIST_CNTS_NO_DUBLES = []
        for word_cnt in LIST_CNTS_DUBLES:
            LIST_CNTS_NO_DUBLES.append( word_cnt )
            
        LIST_CNTS_NO_DUBLES.sort()
        
        
        list_cnt_repeat_X = []
        for int_cnt in LIST_CNTS_NO_DUBLES:
            if int_cnt not in list_cnt_repeat_X:
                list_cnt_repeat_X.append(int_cnt)
        
        #print(list_cnt_repeat_X)
        
        
        
        list_cnt_words_Y  = []
        for int_cnt_1 in list_cnt_repeat_X:
            kol = LIST_CNTS_NO_DUBLES.count( int_cnt_1 )
            list_cnt_words_Y.append( kol )
        ############################################################   
        '''
        mu = 100
        sigma = 15
        x = mu + sigma * numpy.random.randn(10000)
        # the histogram of the data
        n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
        plt.axis([40, 160, 0, 0.03])  
        plt.grid(True)
        plt.show()
        '''
        
        
        ############################################################
        
        plt.xlabel('Повторов')
        plt.ylabel('Слов')
        plt.title('До резки(Все повторы)')
        plt.hist(LIST_CNTS_DUBLES , MAX_REPEAT )#, len(LIST_CNTS_NO_DUBLES))
        #plt.axis([40, 160, 0, 0.03])
        plt.grid(True)
        plt.show()
        
 
        plt.xlabel('Повторов')
        plt.ylabel('Слов')
        plt.title('До резки(БЕЗ 1,2,3 повторов)')
        n, bins, patches = plt.hist(LIST_CNTS_DUBLES , MAX_REPEAT ,  facecolor='green', alpha=0.75)#, len(LIST_CNTS_NO_DUBLES))
        plt.axis([4, MAX_REPEAT , 0 , LIST_CNTS_DUBLES.count(4) ])
        
        #plt.plot(bins, , 'k', linewidth=1)
        
        plt.grid(True)
        plt.show()
        
        ############################################################

        # Фигуры: r--(красн тире(кривая))  bs(син квадр)  g^(зел треуг)    ro(кр точка)    bo(син точка)    k(КРИВАЯ)
        mark_bad  = "ro"
        mark_good = "bo"
        
        Y_legend = int( max(list_cnt_words_Y) / 4 )
        Y_good = Y_legend * 1.1
        Y_m    = Y_legend * 1.25
        
        
        mark_legend_bad  = "r"
        mark_legend_good = "g"   
        
        plt.plot( list_cnt_repeat_X[0:DROP_SKO_LEFT] , list_cnt_words_Y[0:DROP_SKO_LEFT] , mark_bad)
        plt.plot( list_cnt_repeat_X[DROP_SKO_LEFT+1:DROP_M_LEFT-1] , list_cnt_words_Y[DROP_SKO_LEFT+1:DROP_M_LEFT-1] , mark_good)
        plt.plot( list_cnt_repeat_X[DROP_M_LEFT:DROP_M_RIGHT] , list_cnt_words_Y[DROP_M_LEFT:DROP_M_RIGHT] , mark_bad)
        plt.plot( list_cnt_repeat_X[DROP_M_RIGHT+1:DROP_SKO_RIGHT-1] , list_cnt_words_Y[DROP_M_RIGHT+1:DROP_SKO_RIGHT-1] , mark_good)
        plt.plot( list_cnt_repeat_X[DROP_SKO_RIGHT:MAX_REPEAT] , list_cnt_words_Y[DROP_SKO_RIGHT:MAX_REPEAT ] , mark_bad)
        
        plt.plot( list_cnt_repeat_X , list_cnt_words_Y , "k")
    
        plt.plot( [0 ,DROP_SKO_LEFT] , [Y_legend,Y_legend] , mark_legend_bad)
        plt.plot( [DROP_SKO_LEFT+1,DROP_M_LEFT-1] , [Y_good,Y_good] , mark_legend_good)
        plt.plot( [DROP_M_LEFT,DROP_M_RIGHT] , [Y_m,Y_m] , "b|")
        plt.plot( [DROP_M_RIGHT+1,DROP_SKO_RIGHT-1] , [Y_good,Y_good] , mark_legend_good)
        plt.plot( [DROP_SKO_RIGHT,MAX_REPEAT] , [Y_legend,Y_legend] , mark_legend_bad)
        
        
        plt.title(  "Распределение(гаусс=колокол и тд)"  )   # Заголовок над графиком
        plt.xlabel( "Кол-во повторов" )   # X
        plt.ylabel( "Кол-во слов" )   # Y
        plt.autoscale( True )   # Растянет по крайним точкам
        plt.grid() # Сетка сзади
        
        plt.show() 
        #print("123")
    #########################
    
        #print(LIST_CNTS_NO_DUBLES)
        
    
    
    
    
    
    
    
    
    
    
    
    
    LIST_FOR_RETURN = []
  

    for word in DICT_WORDS_CNT.keys():
        
        kol = DICT_WORDS_CNT.get(word)
        
        NOT_IN_SKO_L = kol > DROP_SKO_LEFT
        NOT_IN_SKO_R = kol < DROP_SKO_RIGHT
        NOT_IN_M = (kol < DROP_M_LEFT) or (kol > DROP_M_RIGHT)
        
        #print(kol, word)
        # if kol >= 3:   print(kol , NOT_IN_SKO_L , NOT_IN_SKO_R , NOT_IN_M)
        
        
        if ( NOT_IN_SKO_L and NOT_IN_SKO_R and NOT_IN_M ):
            LIST_FOR_RETURN.append( word )
            
 
 
    
    
    
    
    
    
    
    
    
    
    #########################
    
    
    #print(LIST_FOR_RETURN)
    
    
    print("#"*40)
    
    return LIST_FOR_RETURN













############