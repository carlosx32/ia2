
def evaluar(ejemplo):
    fo=float(ejemplo[1])
    fhi= float(ejemplo[2])
    flo=    float(ejemplo[3])
    jitterB=float(ejemplo[4])
    jitterabs=float(ejemplo[5])
    rap =       float(ejemplo[6])
    ppq =       float(ejemplo[7])
    ddp =       float(ejemplo[8])
    shimmer =   float(ejemplo[9])


    if(fo<= 148.367):
 
        if(fhi<=134.4435):
            if(flo<=103.7325):
                if( jitterB<=0.00566):
                    if(jitterabs<=0.000035):
                        if(rap<=0.00209):
                            if(ppq<=0.00192):
                                if(ddp<=0.004735):
                                    return 0
                                if(ddp>0.004735):
                                    return 1
                            if(ppq>0.00192):
                                return 0
                        if(rap>0.00209):
                            return 1
                    if(jitterabs>0.000035):
                        return 1
                if( jitterB > 0.00566):
                    return 1
            if(flo>103.7325):
                if( jitterB<=0.004483):
                    if( jitterabs<=0.000035):
                        if(rap<=0.00167):
                            if(ppq<= 0.00186):
                                if(ddp<=0.00402):
                                    if(shimmer<=0.013515):
                                        return 1
                                    if(shimmer > 0.013515):
                                        return 0
                                if(ddp>0.00402):
                                    return 1
                            if(ppq>0.00186):
                                return 0
                        if(rap>0.00167):
                            if(ppq<=0.00209):
                                return 1
                            if(ppq>0.00209):
                                if(ddp<=0.005245):
                                    return 0
                                if(ddp >0.005245):
                                    return 1
                    if( jitterabs>0.000035):
                        if(rap<=0.002):
                            return 0
                        if(rap>0.002):
                            return 1
                if( jitterB>0.004483):
                    if( jitterabs<=0.000045):
                        if(rap<=0.00232):
                            if(ppq<=0.002415):
                                return 0
                            if(ppq>0.002415):
                                return 1
                        if(rap>0.00232):
                            return 1
                    if( jitterabs > 0.000045):
                        return 1
        if(fhi>134.4435):
            if(flo <= 97.263):
                if( jitterB <= 0.0073):
                    if( jitterabs<= 0.000035):
                        if(rap<=0.001455):
                            return 0
                        if(rap > 0.001455):
                            return 1
                    if( jitterabs > 0.000035):
                        if(rap<=0.00274):
                            if(ppq <= 0.002775):
                                return 0
                            if(ppq>0.002775):
                                return 1
                        if(rap > 0.00274):
                            return 1
                if(jitterB > 0.0073):
                    return 1
            if(flo > 97.263):
                if(jitterB<=0.00569):
                    if(jitterabs <= 0.000035):
                        if(rap<= 0.0021	):
                            if(ppq<=0.001665):
                                if(ddp<= 0.00383):
                                   return 1
                                if(ddp> 0.00383):
                                   return 0
                            if(ppq>0.001665):
                                if(ddp<= 0.00444):
                                   return 0
                                if(ddp > 0.00444):
                                   return 1
                        if(rap > 0.0021):
                            if(ppq<=0.002255):
                                if(ddp<=0.00534):
                                   return 0
                                if(ddp> 0.00534):
                                   return 1
                            if(ppq > 0.002255):
                                return 1
                    if(jitterabs > 0.000035):
                        if(rap <= 0.00265):
                            print(ejemplo[0:5:])
                            if(ppq<= 0.00236):
                                return 0
                            if(ppq > 0.00236):
                                return 1
                        if(rap > 0.00265):
                            if(ppq<= 0.003375):
                                return 1
                            if(ppq > 0.003375):
                                return 0
                if( jitterB > 0.00569):
                    return 1
    else:#if(fo>148.367):
        if(fhi<=201.7865):
            
            return 1
        if(fhi>201.7865):
            if(flo<=142.9625):
                if( jitterB<= 0.005075):
                    if(jitterabs<= 0.000025):
                        if(rap<=0.001565):
                            if(ppq<=0.001455):
                                if(ddp<=0.003945):
                                    return 1
                                if(ddp > 0.003945):
                                    return 0
                            if(ppq>0.001455):
                                return 0
                        if(rap > 0.001565):
                                return 1
                    if( jitterabs > 0.000025):
                        if(rap<=0.0022551):
                            return 1
                        if(rap > 0.002255):
                            if(ppq<=0.002565):
                                return 1
                            if(ppq>0.002565):
                                return 0
                if( jitterB > 0.005075):
                    if( jitterabs<=0.000035):
                        if(rap<=0.00291):
                            return 1
                        if(rap>0.00291):
                            if(ppq<=0.00327):
                                return 0
                            if(ppq>0.00327):
                                if(ddp<= 0.011735):
                                    return 1
                                if(ddp> 0.011735):
                                    return 0
                    if( jitterabs > 0.000035):
                        if(rap <= 0.00423):
                            if(ppq<=0.00405):
                                if(ddp<=0.0116):
                                    if(shimmer<=0.028115):
                                        return 0
                                    if(shimmer>0.028115):
                                        return 1
                                if(ddp > 0.0116):
                                    return 1
                            if(ppq>0.00405):
                                return 1
                        if(rap > 0.00423):
                            if(ppq<= 0.00438):
                                return 1
                            if(ppq > 0.00438):
                                return 0
            if(flo>142.9625):
                if( jitterB<0.003005):
                    if( jitterabs <= 0.0000095):
                        return 0
                    if( jitterabs > 0.0000095):
                        if(rap<= 0.00143):
                            if(ppq<= 0.00134):
                                if(ddp<= 0.00124):
                                    return 0
                                if(ddp > 0.00124):
                                    return 1
                            if(ppq > 0.00134):
                                return 0
                        if(rap>0.00143):
                            return 0
                if( jitterB>0.003005):
                    if( jitterabs <= 0.000035):
                        if(rap<= 0.00242):
                            if(ppq <= 0.00184):
                                if(ddp <= 0.005115):
                                    return 1
                                if(ddp > 0.005115):
                                    return 0
                            if(ppq > 0.00184):
                                if(ddp<=0.00581):
                                    return 	1
                                if(ddp > 0.00581):
                                    return 0
                        if(rap > 0.00242):
                            if(ppq <= 0.002815):
                                if(ddp <= 0.009005):
                                    return 0
                                if(ddp > 0.009005):
                                    return 1
                            if(ppq > 0.002815			):
                                if(ddp <= 0.01027):
                                    return 0
                                if(ddp > 0.01027):
                                    return 1
                    if( jitterabs > 0.000035):
                        return 1