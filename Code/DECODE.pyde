px=0 
riga=0
car1=""
car2=""
car3=""
contenuto=""                           
def setup():
    global img
    img=loadImage("Mistery.tiff")                      
    img.loadPixels()                               
    decode()                                        
    
def decode():
    global riga,y,car1,car2,car3,img,contenuto,px
    r=red(img.pixels[px])
    g=green(img.pixels[px])
    b=blue(img.pixels[px])  
    l=img.width
    h=img.height
    while (px<l*h):
        for riga in range (10):                     
            r=red(img.pixels[px])            
            g=green(img.pixels[px])
            b=blue(img.pixels[px])                      
            contenuto=contenuto+chr(int(r))+chr(int(b))+chr(int(b))      
            px+=50                                                        
        px+=500*49                                
    print(contenuto)                                 
    
