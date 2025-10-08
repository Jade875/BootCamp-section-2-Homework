#Jade Kas
#N14562258
#Favorite book & author: I have none


#Question 1
Word = input('Enter word of choice: ')

Vowels = "aeiouAEIOU"
Count = 0

for letter in Word:
  if letter in Vowels:
    Count =+ 1

print(' ')

print("Number of vowles =", Count)

#Question 2
animals = ['tiger','elephant','monkey','zebra','panther']
for animal in animals:
  print(animal.upper())
print(' ')

#Question 3
for num in range(1,21):
  if num % 2 == 0:
    print(num, "is even")
  else:
    print(num, "is odd")
print(' ')

#Question 4
word = str(input('Enter Word of choice (in all lowercase): '))
reversedword = word[::-1]

if word == reversedword:
  print(word, "is a palindrome!")
print(' ')

#Question 5
a = int(input("Enter number of choice (as an integer): "))
b = int(input("Enter another number of choice (as an integer): "))
sum_of_numbers = a + b
print('The sum of your numbers is ', sum_of_numbers)