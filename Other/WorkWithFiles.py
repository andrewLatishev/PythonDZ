with open('D:/file.txt') as file:
    longest = ''
    for word in file.read().split():
        if len(word) > len(longest) and word[-1].upper() in 'ЙЦКНГШЩЗХЪФВПРЛДЖЧСМТБЬWRTPSDFGHJKLZXCVBNM':
            longest = word
print(longest)
