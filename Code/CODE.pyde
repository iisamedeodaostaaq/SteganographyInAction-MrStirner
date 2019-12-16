
L_img=500
H_img=500
DQuadrati=50
img=createImage(L_img,H_img,RGB)
img.loadPixels()
def setup():
    
    size(L_img,H_img)
    code()
    
def code(): #creazione funziione codifica
    
    
    input=createInput("input.txt");
    
    data1 = input.read()
    pi=0
    while(  data1 != -1 and pi<L_img*H_img): #ciclo lettura  
        data1=input.read()
        if data1 != -1:# leggo caratteri file futuri componenti rgb della img
            data2 = input.read()
            if data2 !=-1:
                data3 =input.read()
        
            for i in range(50): #inizio ciclo creazione quadrati colorati
                for j in range(DQuadrati):
                    img.pixels[pi+j+(L_img*i)]=color(data1,data2,data3) #colorazione quadrato
            pi=pi+DQuadrati #quadrsto succesivo
            if (pi%L_img==0): #mando a capo se ho completato una riga
                pi=pi+L_img*(DQuadrati-1)
        
   
        if data1==-1 or data2==-1 or data3==-1: #se caratteri sono finiti completo con quadrati neri
            while(pi/50%L_img):
                for i in range(50):
                    for j in range(DQuadrati):
                        img.pixels[pi+j+(L_img*i)]=color(0,0,0)
                pi=pi+DQuadrati
               
                
     
    img.updatePixels()
    image(img,0,0)
    save("Mistery.tiff")  
    
