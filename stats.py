def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    return len(text.split())

def char_count(text):
    counts = {}
    text = text.lower()
    for ch in text:
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1
    return counts

def _by_num(item):
    return item["num"]

def sort_on(counts):
    count = []
    for k, v in counts.items():
        if k.isalpha():
            count.append({"char": k, "num": v})
    count.sort(reverse=True, key=_by_num)
    return(count)
