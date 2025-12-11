#QUESTION 1
def hype_it_up(word):
    return word + "!!!" #Self explanatory, this will simply add !!! to the word

# Test case
print(hype_it_up("Python"))

#QUESTION 2
def reverse_and_celebrate(words):
    result = "" #it is empty because it will be used to write the reversed phrase
  #this will loop the words backwards
    for i in range(len(words) - 1, -1, -1):
        result += words[i]
        if i != 0:
            result += "-" #add a dash to everything EXCEPT last word
    return result + "🎉"
print(reverse_and_celebrate(["Python", "is", "fun"]))

#QUESTION 3
# Using get function
#below is where we assigned every word to an emoji
animal_emojis = {
    "cat": "🐱",
    "dog": "🐶",
    "lion": "🦁",
    "cow": "🐮"
}

def animal_to_emoji(animal):
  return animal_emojis.get(animal, "🐾")
    
# Test case
print(animal_to_emoji("dog"))
print(animal_to_emoji("duck"))

#Using try..except
animal_emojis = {
    "cat": "🐱",
    "dog": "🐶",
    "lion": "🦁",
    "cow": "🐮"
}

def animal_to_emoji(animal):
  try:
    return animal_emojis[animal] #this will ask the code to look for the "key"
  except KeyError: 
    return "🐾" #if they key doesnt exist just return to this emoji
   
# Test case
print(animal_to_emoji("dog"))
print(animal_to_emoji("duck"))

#QUESTION 4
def magic_number(a, b, c):
  total = (a + b + c) * 2 #Self explanatory, add all the numbers and multiply by 2
  return str(total) + " is magical!" #This will simply convert the string and add the message
    
# Test case
print(magic_number(2, 4, 7))

#QUESTION 5
def weather_message(temp):
  if temp >= 20:
    return "Sun's out! 😎"
  else:
    return "Brrr... bundle up! 🧥"
#I feel like this code is very easy to understand since it's a little similar to arduino so i wont bother giving an explanation
# Test cases
print(weather_message(25))
print(weather_message(10))

#QUESTION 6
def countdown_blastoff(n):
    result = "" #empty string
  #this will loop the function from n all the to 1
    for i in range(n, 0, -1):
        result += str(i) + "\n" #this will add each number and a new line
    result += "🚀 BLASTOFF!" #final message, it will show once the countdown is done
    return result
  
# Test case
print(countdown_blastoff(3))

#QUESTION 7
def name_badge(name):
  #setting up the borders
  border = "*" * (len(name) + 6) #top and bottom based on the lenght of the name
  badge = border + "\n" #top
  badge += "*  " + name + "  *\n" #center the name
  badge += border #bottom
  return badge

# Test case
print(name_badge("Alice"))
print(name_badge("Bob"))

#QUESTION 8
def emoji_repeater(emojis, times):
  #this will create a list where each emoji will be repeated
  repeated_emojis = [emoji * times for emoji in emojis]
  return "".join(repeated_emojis) #combine everything into one long string

# Test case
print(emoji_repeater(["😀", "🎉", "⭐"], 2))

#QUESTION 9
def scoreboard(scores):
    result = "" #empty string to build the scoreboard
  #this will sort everything by score (highest to lowest)
    sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    
    medals = ["🥇", "🥈", "🥉"]
    
    index = 0 #track which medal to use
    
    for name, score in sorted_scores.items(): #this will loop through the scores
        if index < 3:
            result += f"{medals[index]} {name}: {score}\n" #for the medals
        else:
            result += f"{name}: {score}\n" 
        index += 1 #move to nect rank
    return result

# Test case
print(scoreboard({"Alice": 95, "Bob": 87, "Charlie": 92, "Dave": 63}))

#QUESTION 10
def apply_function(func, items):
  result = [func(item) for item in items] #this will apply the function to every item
  return ", ".join(result) #add everything into one string

# Test case
print(apply_function(str.upper, ["hello", "world", "python"]))

#QUESTION 11
def safe_divide(a, b):
  try:
    result = a / b #try the division
    return f"{a} / {b} = {result}" #i dont have the division symbol so im just going to use the /
  except ZeroDivisionError: #if the b is zero it will give the following warning message
    return "⚠️ Cannot divide by zero"
    

# Test cases
print(safe_divide(10, 2))
print(safe_divide(5, 0))

#QUESTION 12
def remove_duplicates(items):
  unique_items = set(items) #this will remove duplicates
  sorted_unique = sorted(unique_items) #this will sort everything in order
  sorted_unique = [str(x) for x in sorted_unique] #this will convert everything to strings
  return "-".join(sorted_unique)

# Test case
print(remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5]))
