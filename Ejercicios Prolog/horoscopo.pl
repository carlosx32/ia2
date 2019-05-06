/* horoscopo(Signo,DiaIni,MesIni,DiaFin,MesFin)
    <- son del signo Signo los nacidos entre el DiaIni/MesIni y el DiaFin/MesFin */
horoscopo(aries,22,3,20,4).
horoscopo(tauro,21,4,21,5).
horoscopo(geminis,22,5,21,6).
horoscopo(cancer,22,6,23,7).
horoscopo(leo,24,7,23,8).
horoscopo(virgo,24,8,23,9).
horoscopo(libra,24,9,23,10).
horoscopo(escorpio,24,10,22,11).
horoscopo(sagitario,23,11,22,12).
horoscopo(capricornio,23,12,20,1).
horoscopo(acuario,21,1,19,2).
horoscopo(piscis,20,2,21,3).
diasmes(1,31).
diasmes(2,29).
diasmes(3,31).
diasmes(4,30).
diasmes(5,31).
diasmes(6,30).
diasmes(7,31).
diasmes(8,31).
diasmes(9,30).
diasmes(10,31).
diasmes(11,30).
diasmes(12,31).



/* signo(Dia,Mes,Signo) <- los nacidos el Dia/Mes pertenecen al signo Signo */
signo(Dia,Mes,Signo) :- horoscopo(Signo,D1,M1,D2,M2),diasmes(Mes,Y),
                        ((Mes=M1,Dia>=D1) ; (Mes=M2,Dia=<D2) ),(Dia=<Y),(Dia>0).



















