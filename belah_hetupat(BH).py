
# a      a
#  a    a 
#   a  a
#    aa
#   a  a  
#  a    a
# a      a
#  a    a
#   a  a
#    aa

# FIRST
# aaaa
# aaa
# aa
# a
def doit():
    for i in range(20):
        n = 5
        y = 0
        for i in range (5,0,-1):
            n = n - 1
            print("a"*i + " "*(2*y)+"a"*i)
            y = y+1 
            if n == 0  : 
                for i in range (2,5,+1):
                    n = n + 1
                    print("a"*i+" "*(2*(y-2))+"a"*i)
                    y = y -1
    print("aaaaaaaaaa")

#ADJUST
def lol():
    for i in range(200):
        n = 5
        y = 0
        for i in range (5,0,-1):
            n = n - 1
            print(" "*(i-1)+"a" + " "*(2*y)+"a"+ " "*(i-1))
            y = y+1 
            if n == 0  : 
                for i in range (2,5,+1):
                    n = n + 1
                    print("a"*i+" "*(2*(y-2))+"a"*i)
                    y = y -1

#LOL there is
def fixx():
    for i in range(200):
        n = 5
        y = 0
        for i in range (5,0,-1):
            n = n - 1
            print(" "*(i-1)+"a" + " "*(2*y)+"a"+ " "*(i-1))
            y = y+1 
            if n == 0  : 
                for i in range (2,5,+1):
                    n = n + 1
                    print(" "*(i-1)+"a"+" "*(2*(y-2))+"a"+" "*(i-1))
                    y = y -1
    print("    aa    ")
fixx()
