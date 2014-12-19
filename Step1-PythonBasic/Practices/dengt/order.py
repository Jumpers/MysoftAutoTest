#coding=utf-8
def order(word):
    New_word = word.split(" ")
    New_word.sort()
    print New_word

if __name__ == '__main__':
    word = raw_input("Tell me what do you want to order,split it with space.\n")
    order(word)
    while not raw_input("Press anything to continue.\n"):
        word = raw_input("Tell me what do you want to order,split it with space.\n")
        order(word)
