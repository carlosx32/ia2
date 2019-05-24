/* libros.pro
    juego de identificacion de libros:
    para iniciar use : ?- iniciar.
    si desea ingresar nuevos libros use : ?- nuevo.    
    */
dynamic libro/3.
libro(el_gato_negro,cuento_de_terror,edgar_allan_poe).
libro(drakula,   novela_de_terror,bram_strocker).
libro(it,   novela_de_terror,stephen_king).
libro(el_amor_en_los_tiempos_de_colera, novela_de_terror,gabriel_g_marquez).
libro(romeo_y_julieta,novela_de_amor, wiliam_skapespeare).
libro(la_isla_del_tesoro,novela_aventura,r_r_stevenson).
libro(diario_de_ana_frank,novela_de_guerra,ana_frank).
libro(el_cristo_de_espaldas,novela_de_guerra,eduardo_caballero_calderon).
libro(el_principito,cuento_infantil,antoine_de_saint).
libro(corazon_delator,cuento_de_terror,edgar_allan_poe).
libro(relato_de_sergio_stepansky,poesia_latina,leon_de_greif).
libro(mo_va_mo_vene,poesia_europea,eduardo_di_capua).
libro(philosophiae_naturalis_principia_mathematica,matematicas,isaac_newton).



nuevo :-    nl,write("inserte el Nombre de libro:" ), read(Nombre),nl,
            write("inserte el Genero de libro:" ), read(Genero),nl,
            write("inserte el Autor de libro:" ), read(Autor),nl,
            assert(libro(Nombre,Genero,Autor)),write(" Se ha insertado").



iniciar :- genero(Genero),
      write('Podria interesarte el genero '),
      write(Genero),nl,write("a continuacion se mostrara una lista con los libros que podrian interesarte"),
      ver_libros(Genero),
      nl,
      undo.

/* hypotheses to be tested */
genero(novela_de_terror)    :-novela_de_terror, !.
genero(novela_de_amor)      :-novela_de_amor, !.
genero(novela_aventura)     :-novela_aventura,!.
genero(novela_de_guerra)    :-novela_de_guerra,!.
genero(cuento_infantil)     :-cuento_infantil, !.
genero(cuento_terror)       :-cuento_infantil, !.
genero(poesia_latina)       :-poesia_latina,!. 
genero(poesia_europea)       :-poesia_europea,!. 
genero(matematicas)         :-matematicas,!.

genero(desconocido).             /* no diagnosisticado */
/* animal identification rules */
novela_de_terror    :-novela,verificar(leer_historias_que_provoquen_miedo),verificar(asustarse).
novela_de_amor      :-novela,poesia,verificar(leer_historias_de_amor).
novela_de_amor      :-novela,verificar(eres_una_persona_romantica).
novela_de_guerra    :-novela,verificar(leer_historia),verificar(leer_literatura_europea).
novela_de_guerra    :-novela,verificar(leer_historias_belicas).
novela_aventura :-novela, verificar(leer_historias_con_aventuras).
novela_aventura :-novela, verificar(leer_historias_de_suspenso).
cuento_infantil     :-cuento,verificar(su_edad_es_menor_a_13_años).
cuento_terror       :-  cuento, verificar(leer_historias_que_provoquen_miedo).
poesia_latina       :- poesia,verificar(leer_literatura_latinoamericana).
poesia_europea      :-poesia,verificar(leer_literatura_europea).
matematicas         :-estudio, verificar(estudiar_matematicas).


/* Reglas de clasificacion */

novela  :-  verificar(leer_historias_largas), !.
cuento  :-  verificar(leer_historias_cortas), !.
poesia  :-  verificar(leer_historias_inspiradas_por_sentimientos),!.
poesia  :-  verificar(leer_versos), verificar(leer_rimas),verificar(lecturas_con_diferentes_significados),!.
estudio :-  verificar(leer_libros_academicos),!.



/* how to preguntar questions */
preguntar(Question) :-
    write('en tus habitos de lectura ¿Te identificas con el siguiente atriubuto : '),nl,
    write(Question),
    write('? '),
    read(Response),
    nl,
    ( (Response == si ; Response == s)
      ->
       assert(si(Question)) ;
       assert(no(Question)), fail).

:- dynamic si/1,no/1.

/* How to verificar something */
verificar(S) :-
   (si(S)
    ->
    true ;
    (no(S)
     ->
     fail ;
     preguntar(S))).

/* undo all yes/no assertions */
undo :- retract(si(_)),fail.
undo :- retract(no(_)),fail.
undo.
ver_libros(Genero):- findall((X,Y),(libro(X,Genero,Y)),O),nl,show_libros(O).
show_libros([]).
show_libros([(A,B)|C]):- write("Libro: "),write(A), write("Autor: "), write(B),nl,show_libros(C). 