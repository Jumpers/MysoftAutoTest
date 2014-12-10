#coding=utf-8
def break_words(stuff):
    """This function will break up words for us."""
    words=stuff.split(' ')#拆分字符串stuff，分割符为空格
    return words

def sort_words(words):#将字符串中的字符进行排查，排序规则是转换成ascll码排序
    """sorts the words"""
    return sorted(words)

def print_first_word(words):#words必须是序列
    """Prints the first word after popping it off."""
    word=words.pop(0)
    print word
    
def print_last_word(words):
    """Print the last word after popping it off."""
    word=words.pop(-1)#words.pop()也是指的序列中最后一个值
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words=break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last word of the sentence."""
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)