 #there you go!
 # Declare the 3 lists
list_happy_words = ["joyful", "happy", "amazing", "beautiful","stupendous" ,"excited","good"]
list_sad_words = ["sad", "tears", "crying", "depressed"]
list_games = ["tetris", "flappy bird", "snake","pac man"]


def Greet():
  userinput = input("Enter you name:")
  print('Hello',userinput)

Greet()

# Declare the 3 lists
list_happy_words = ["joyful", "happy", "amazing", "beautiful","excited","good","stupendous"]
list_sad_words = ["sad", "tears", "crying", "depressed"]
list_games = ["tetris", "flappy bird", "snake","pac-man"]

def happy_feeling(input, happy_words):
  for i in happy_words:
    if i in input:
      return "happy"
  return "unknown"

def sad_feeling(input, sad_words):
  for i in sad_words:
    if i in input:
      return "sad"
  return "unknown"

# Initialize the games_index variable
games_index = 0
# A variable to tell if the program should break from the while loop
set_break_flag = False

# This while loop goes on infinitely
# Till it encounters a break in the program
while True:
  # ask the user to input a word describing their feeling, save the string
  feeling = input('How are you feeling today?')
  # Check if the word is a part of the happy list
  feeling_lower = feeling.casefold()
  predicted_feeling = happy_feeling(feeling_lower, list_happy_words)
  if predicted_feeling == "happy":
    print("Glad to know!")
    break
  else:
    # Check if games list is over
    # This can be done in several way, we will
    # use the index to determine this
    if games_index >= len(list_games):
      print('Sorry, we are out of games to suggest')
      break
    else:
      predicted_feeling = sad_feeling(feeling_lower, list_sad_words)
      if predicted_feeling == "sad":
        print('Sorry you feel this way.')
        print('Please play ', list_games[games_index])
        games_index = games_index + 1
          # Note that below break is just for the for loop, not the while loop
        # Go back to asking user how they feel
      else:
        print('I dont understand how you feel!')
        break

  






#List1 = ["Batman comics", "Superman comics", "Aquaman comics", "Flash comics", "Green Arrow comics"]
#for i in List1: 
 # print("In my collection, I have", i)


# perfect!

#userinput = input('are you a boy or a girl:')

#if userinput.casefold() == 'boy':
  #print('hi, you are a boy')
#if userinput.casefold() == 'girl':
 # print('hi, you are a girl')

#string = "this is a sentence"
#print(string[1])

#userinput = input('please enter a string:')
#firstcharacter = userinput[0]
#lastcharacter = userinput[-1]

#if firstcharacter==lastcharacter:
  #print('Yes')
#else:
  #print('No')



#mydictionary={'stick':4, 'pebble':16, 'rock':34, 'me': 56, 'random':11, 'everything else':19}





#print(mydictionary)

#print(mydictionary['everything else'])
#print(mydictionary['me'])

#print(mydictionary)
#mydictionary['one'] = 1

#mydictionary['two'] = 2
#print(mydictionary)


#mydictionary = {1:'one', 'shoppingilst':['fish', 2],
               #2:['mon', 'tues', 5]}

#print(mydictionary)
#print(mydictionary[2])



#def greet():
  #print('hello')
  #print('I am a AI chatbot')
  #print('I was built by aiclub')


#greet()

#greet()

import requests
import json

def get_prediction(data={"sentence":"I am so sad to see you go. "}):
  url = 'https://askai.aiclub.world/a23b76f6-1481-4af6-9cc8-e8b3528f2ca4'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  #print(response)
  return response

ask_your_ai = {"sentence": "I have tears of joy, crying"}

prediction = get_prediction(ask_your_ai)
#print(prediction)
#print(type(prediction))
prediction_dict = json.loads(prediction)
#print(type(prediction_dict))
prediction_body = prediction_dict['body']
#print(prediction_body)
#print(type(prediction_body))
prediction_body_dict = json.loads(prediction_body)
#print(type(prediction_body_dict))
predicted_label = prediction_body_dict['predicted_label']
print(predicted_label)