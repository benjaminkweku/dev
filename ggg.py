def a():
    sentence="i am going to school"
    lists=list(sentence)
    
    result="false"
    for i in lists:
        if i=="s":
            result="true"
    return a()
        




def b():
     sentence="i am going to school"
     lists=list(sentence)
    
     result="false"
     for i in lists:
        if i=="m":
     print(result)
    
b()
a()
    