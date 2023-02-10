def top_3_words(text):
    counts = {}
    for char in '!"#$%&()*+,./:;<=>?@[\]^_`{|}~-':
        if char in text:
            text = text.replace(char, '')
    for word in text.lower().split():
        if word.replace("'", '') != '':
            counts[word] = counts.get(word, 0) + 1
    return [word[0] for word in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]]
