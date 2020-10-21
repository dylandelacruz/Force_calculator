def logo():
    
    print ("█▀▀ █▀█ █▀█ █▀▀ █▀▀")
    print ("█▀  █▄█ █▀▄ █▄▄ ██▄")
    print ("  By Dylan Dela Cruz  ")
    print ('Hello and welcome, enter the mass and acceleration to calculate force.')
    
logo()

def force():
    
    m = int(input('What is the mass(kg)of the object?:'))
    a = int(input('What is the acceleration(m/s*2)of the object?:'))
    f = m * a
    print ('The force is:',f,'Newtons')
    
force()
