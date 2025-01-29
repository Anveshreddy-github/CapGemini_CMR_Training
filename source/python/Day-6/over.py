class example:
    def __init__(self,name):
        print(f"first constructor: hello {name}")
#it overrides the first constructor 
    def __init__(self,age):
        print(f"second constructor: age is {age}")

p=example(21) #calls only the second constructor 
        