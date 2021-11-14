from threading import Timer

print('Code Execution Started')

def display():
    print('Hii Yuvraj GooD Morrning')

t = Timer(5, display)  
t.start()