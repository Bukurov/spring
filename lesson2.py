import random
import lesson2_func_read  as lfr

#lfr.read_int("введите целое число ")

def game ():
    t = 0
    while True:
        r =random.randint(1,2)
        i = lfr.read_int("ввидете число 1 право,2 лево ")
        if i!=1 and i!=2:
            print ("введите 1 или 2")
        elif i==r:
            print("вы столкнулись с припятствием")
            break
        else :
            print("вы не попали в припятсвие")
            t+=1
    print("очки: ",t)
game()
            
        


 
