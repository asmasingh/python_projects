#STONE PAPAER SCISSOR GAME PROJECT
import random
list_sps=['Stone','Paper','Scissor']
dict_sps={'Stone':'Scissor','Scissor':'Paper','Paper':'Stone'}
while True:
    try:
        user_choice=input("Enter your choice..")
        game_choice=random.choice(list_sps)
        if dict_sps[user_choice]==game_choice:
            print("Its",game_choice,'Voila!!! U won!!')
        else:
            print("Its",game_choice,"Better luck next time")
            play_y_n=input("U want to play again yes or no?")
            if play_y_n=='yes':
                continue
            else:
                break
    except:
        print("invalid choice..please make a correct choice")
        break
        
