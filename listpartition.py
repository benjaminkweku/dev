def partition(number):
    tuple_1=(1,5,3,7)
    tuple_2=(2,6,4,10,8)
    for i in range(number):
        if i%2==0:
            n=tuple_1.sort()
            print(n)
partition(10)
    