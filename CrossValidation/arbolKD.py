def evaluar(ejemplo):
    fo=float(ejemplo[1])
    fhi= float(ejemplo[2])
    
    
    if(fo <= 148.367):  #2. Fo<= 148.367
        if(fhi<=134.4435):       #3. Fi<=134.4435
            return 1
        else:
                return -1
    else:#2. Fo> 148.367
        return -1
    return -1
