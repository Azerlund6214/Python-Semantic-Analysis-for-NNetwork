import matplotlib.pyplot as plt
import numpy as np

# сделать, чтоб при приходе LIST[ [a] [b] ] рисовал графики а1б1 а2б2 а3б3 ...

# ловит косяки с размерностями и диапазонами
def PRINT_PLOT( LIST_Y = [1,3,2,6,8,2,6,8] , LIST_X = "NUMBER" , MARK="k" , PARAMS=["","","","",""] , POINTS_BEG = 0 , POINTS_END = "END"  ):

    
    
    if PARAMS[0] != "":     plt.title(  PARAMS[0] )   # Заголовок над графиком
    if PARAMS[1] != "":     plt.xlabel( PARAMS[1] )   # X
    if PARAMS[2] != "":     plt.ylabel( PARAMS[2] )   # Y
    if PARAMS[3] != "":     plt.autoscale( tight=PARAMS[3] )   # Растянет по крайним точкам
    if PARAMS[4] != "":     plt.grid() # Сетка сзади
    #if PARAMS[5] != "":
    
    
    
    
   
    
   
    
    
    
    
    if POINTS_END != "END"  and  POINTS_BEG > POINTS_END:
        POINTS_BEG = 0
    
    
    if LIST_X == "NUMBER": LIST_X = np.arange(0, len(LIST_Y) , 1)
    
    
    
    # ФУЛЛ робит
    if len(LIST_X) != len(LIST_Y):
        
        # X больше
        if len(LIST_X)-len(LIST_Y) >= 1:
            POINTS_END = len(LIST_Y)
            
        
        # Y больше
        if len(LIST_X)-len(LIST_Y) <= -1:
            POINTS_END = len(LIST_X)
          
        
        
    # именно тут        
    if POINTS_END == "END": POINTS_END = len(LIST_Y)      
    
    
    
    plt.plot( LIST_X[POINTS_BEG:POINTS_END] , LIST_Y[POINTS_BEG:POINTS_END] , MARK)

    
    #plt.subplot(212)

     
    plt.show()  
    
    
    return






###