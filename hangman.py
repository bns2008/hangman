import random
import json


print("welcome man!!")
print("are you ready!")




with open("word.json","r") as f:
     question=json.load(f)

def save_player_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    new_player = {"name": name, "age": age}

    try:
        with open("players.json", "r") as f:
            players = json.load(f)      # load whatever's already there
    except FileNotFoundError:
        players = []                      # first time ever — start with an empty list

    players.append(new_player)              # add the new one to the list

    with open("players.json", "w") as f:
        json.dump(players, f)     
                    # save the WHOLE list back
def show_question_type(question):

    result=[]

    for q in question:

        result.append(q["category"])

    return set(result)

def get_types(questions,type):
    result=[]

    for q in questions:
        if q["category"]==type:
            result.append(q)   
    return result
   
def start_game():

           

           score = 0
           quit=False
           for q in se:
                ran=random.choice(se)

                if quit:
                   break
                answer=ran["word"].lower() 
                hidden_word=["_"] *len(answer)
                wrong=0
                while True:
                 print(ran["clue"])
                 print(f"the word you want guess has {len(answer)} this much letter","".join(hidden_word))
           
                 enter=input("enter your guess here:-").lower()

                 if enter=="quit":
                     quit=True
                     break
                     
                 if enter==answer:
                    score=+1
                    print("correct!!")
                    break
                 else:
                  wrong=wrong+1
           
                  if wrong <=len(answer):
                     hidden_word[wrong -1]=answer[wrong-1]
                   
                  print("incorrect!! guess now")
           print(f"your final score is: {score}/{len(se)}")
   
while True:

     print("1 to know the types we have")
     print("2 to start")
     print("3 to stop")
     print("4 to login!")
     check=int(input("enter your choice:-"))

     if check==3:
          break
     elif check==2:
         select=input("enter which type of questions you want:-")
         se=get_types(question,select)

         start_game()
        
     
     elif check==1:
          sh=show_question_type(question)
          print("you have to choose one category between these:-",sh)
     elif check==4:
         save_player_info()

         