word=input()
h = word.rfind("h")
e = word.rfind("e")

if(h!=-1 and e!=-1):
    if(e<h):
        word2=word[:h]
        h2 = word2.rfind("h")
        if(h2!=-1):
            word=word[h2:]
            e = word.rfind("e")
            if(e!=-1):
                word=word[e:]
                l = (word.rfind("l"))
                if(l!=-1):
                    word1=word[:l]
                    l1 = word1.rfind("l")
                    if(l1!=-1):
                        word=word[l:]
                        o = word.rfind("o")
                        if(o!=-1):
                            print("YES")
                        else:print("NO") 
                    else:print("NO") 
                else:print("NO")
            else:print("NO")          
        else:print("NO")                
         
    else:
        word=word[e:]
        l = (word.rfind("l"))
        if(l!=-1):
            word1=word[:l]
            l1 = word1.rfind("l")
            if(l1!=-1):
                word=word[l:]
                o = word.rfind("o")
                if(o!=-1):
                    print("YES")
                else:print("NO") 
            else:print("NO")
        else:print("NO")          
    

