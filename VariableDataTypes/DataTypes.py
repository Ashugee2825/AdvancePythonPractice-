multiline_message = """  """

"""
Hello, everyone!
Welcome to the world of Python.
Let's learn together! 



"""
print(multiline_message)

print("---------------=====--------------------------------------------")   
message = "Hello, Python!"          # String            
print(message)                      # Output: Hello, Python!    
print(type(message))                # Output: <class 'str'>


word = "Python"
print(word[0])  # Output: P
print(word[3])  # Output: h
print(word[-1]) # Output: n
print("---------------=====--------------------------------------------")
phrase = "Hello, Python!"
print(phrase[0:5])  # Output: Hello
print(phrase[7:13]) # Output: Python
print(phrase[:5])   # Output: Hello
print(phrase[7:])   # Output: Python!

print("---------------=====--------------------------------------------")   
message = "Welcome to Python!"
print(len(message))  # Output: 19

print("---------------=====--------------------------------------------")   
greeting = "Hello, World!"
print(greeting.upper())  # Output: HELLO, WORLD!
print(greeting.lower())  # Output: hello, world!

print("---------------=====--------------------------------------------")   
text = "Learning Python is fun!"
print(text.find("Python"))  # Output: 9
print("fun" in text)         # Output: True

print("---------------=====--------------------------------------------")   
sentence = "I like Java."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)  # Output: I like Python.

print("---------------=====--------------------------------------------")       
text = "apple,banana,cherry"
fruits = text.split(",")  # Split the text at ','
print(fruits)  # Output: ['apple', 'banana', 'cherry']

joined_text = " - ".join(fruits)
print(joined_text)  # Output: apple - banana - cherry

print("---------------=====--------------------------------------------")   

s1 = 'Kodnest-Learning'
s1.split('-')  # Output: ['Kodnest', 'Learning']
print(s1.split('-'))  # Output: ['Kodnest', 'Learning']

s2 = 'Kodnest Learning'
s2.split()  # Output: ['Kodnest', 'Learning']
print(s2.split())  # Output: ['Kodnest', 'Learning']  

s3 = ['Kodnest', 'Learning' 'Hello' 'i' 'am' 'Learning']
s41 = '-'.join(s3)
s4 = '-'.join(s3)
print(s41); '''Kodnest LearningHelloiamLearning'''
print(s4); '''Kodnest Learning-Hello-iam-Learning'''





