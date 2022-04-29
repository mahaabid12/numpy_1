class Mon_exception (Exception):
    pass

moy=0


for i in range(5): 
   
    try:
        j=i+1
        x=int(input("entrer la note "+ str(j)))
        moy+=x
        if(x<0 or x>20):
            raise Mon_exception()
    except Mon_exception: 
        print("Note non valide, la note doit être un réel entre 0 et 20")
        break
    except: 
        print("Erreur")
        break 


print(moy/5)