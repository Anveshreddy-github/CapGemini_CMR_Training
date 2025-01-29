class example:
    def __init__(self,**kwargs):
        if "name" in kwargs and "age" in kwargs:
            print(f"hello {kwargs["name"]},you are {kwargs['age']} in years")
        elif "name" in kwargs:
            print(kwargs['name'])
        
p=example(name="alica")
q=example(name="bob",age=19) 