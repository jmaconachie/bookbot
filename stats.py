def get_total_words(text):
    words = text.split()
    return len(words)
    
def get_num_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def get_sorted_char_list(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list