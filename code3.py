#solution to problem3 
def ques3(object, key):
    keys = key.split('.');
    obj = object
    for i in keys:
        for k, v in obj.items():
            if not k:
                continue
            obj = v
    return obj
obj = {'a':{'b':{'c':'d'}}}
obj1 = {'x':{'y':{'z':'a'}}}
obj2 = {'q':{'w':{'e':'r'}}}
obj3 = {'a':{'s':{'d':'f'}}}

#calling function with values
print(ques3(obj, 'a.b.c')) 
print(ques3(obj1, 'x.y.z'))
print(ques3(obj2, 'q.w.e'))
print(ques3(obj3, 'a.s.d'))