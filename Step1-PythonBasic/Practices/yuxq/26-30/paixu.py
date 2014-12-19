#coding=utf-8
def break_words(stuff):
    """This function will break up words for us."""
    words=stuff.split(' ')#拆分字符串stuff，分割符为空格
    return words

words=break_words('are you right')
words.sort()

print words

