#-*- coding:utf-8 -*-
formatter = "%r %s %s %s"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
                   "I had this 东西.",
                   "That you could type up right.",
                   "But it didn't sing.",
                   "So I said goodnight."
                   )
#'I had this \xe4\xb8\x9c\xe8\xa5\xbf.'