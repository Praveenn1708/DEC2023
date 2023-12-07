import threading,time
#def my_coroutine():

def square(numbers):
    for i in numbers:
      time.sleep(0.5)
      print("Square",i**2)
      

def cube(numbers):
    for i in numbers:
      time.sleep(0.8)
      print("Cube",i**3)  
      
l=[1,2,3,4,5]
t1 = threading.Thread(square(l))
t2 = threading.Thread(cube(l))

t1.start()
t2.start()
