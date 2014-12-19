#coding=utf-8
def order(New_word):
    New_word = word.split(" ")
    New_word.sort()
    print New_word

if __name__ == '__main__':
    word = raw_input()
    order(word)

