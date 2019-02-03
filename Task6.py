import os
def walk(dirname):    
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name) #sub directory       
        if os.path.isfile(path):
            print(path)        
        else:            
            walk(path)

walk(os.getcwd()) #Here returns current working directory.
