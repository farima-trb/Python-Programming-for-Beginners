word=input()
BA=word.find("BA")
if (BA!=-1):
    # word=word.removesuffix("BA")
    word=word.replace("BA","",1)
    AB=word.find("AB")
    if(AB!=-1):
        print("YES")
    else:print("NO")        
else:print("NO")

