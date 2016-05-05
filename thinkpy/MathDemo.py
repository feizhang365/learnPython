__author__ = 'fzh'

fruit = 'banana'
blen  = len(fruit)
print(blen)

index = 0

while index < blen :
    letter = fruit[index]
    print(letter)
    index = index + 1


print('a' in fruit)