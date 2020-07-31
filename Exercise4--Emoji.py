message = input('>')
words = message.split(' ')
emojis = {
    ':)' : '😀'
    # ':(' : "☹️"
}
output = ''
print(words)
for word in words:
    output+=emojis.get(word, word) + ''
print(output)