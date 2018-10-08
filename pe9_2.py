while True:
    word = input('Input a word with at least 4 characters: ')
    if len(word) >= 4:
        print('Thank your for entering this word! It contains', len(word), 'characters.')
        break
    print('Failed, please try a different word with at least 4 characters.')
