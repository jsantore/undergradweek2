import string

def count_words(file_name:str):
        word_counts = dict()
        with open(file_name, encoding='UTF-8') as warpeace:
            all_lines = warpeace.readlines()
            for current_line in all_lines:
                words_in_line = current_line.split(' ')
                for current_word in words_in_line:
                    bare_word = current_word.strip(string.punctuation + '\n”“‘')
                    bare_word = bare_word.lower()
                    if bare_word in word_counts:
                        word_counts[bare_word] += 1
                    else:
                        word_counts[bare_word] = 1
        for word in word_counts:
            print(f"{word}: {word_counts[word]}")




if __name__ == '__main__':
    count_words("warpeace.txt")


