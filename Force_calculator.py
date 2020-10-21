def logo():
    print ("█▀▀ █▀█ █▀█ █▀▀ █▀▀")
    print ("█▀  █▄█ █▀▄ █▄▄ ██▄")
    print ("By Dylan Dela Cruz")

logo()

print ('Hello and welcome, enter the mass and acceleration to calculate mass.')

def Force():
    m = int(input('What is the mass of the object?:'))
    a = int(input('What is the acceleration of the object?:'))
    f = m * a
    print ('The force is:',f,'N')
    
Force()
