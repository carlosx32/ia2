:-nl,nl,write('Digite \'iniciar.\' para ingresar nuevos objetos  ?- iniciar. ').
:-nl,nl,write('Digite \'embalar.\' para iniciar el embalaje:  ?- embalar. '), nl,nl,nl.
objeto(libro1).
objeto(libro2).
objeto(lampara).
objeto(platos).
objeto(abrigo).
objeto(tv).
objeto(pantalones1).
objeto(pantalones2).
objeto(camisa1).
objeto(camisa2).
tamaño(libro1,2).
tamaño(libro2,2).
tamaño(libro3,2).
tamaño(libro4,2).
tamaño(lampara,8).
tamaño(platos,5).
tamaño(abrigo,3).
tamaño(tv,10).
tamaño(pantalones1,2).
tamaño(pantalones2,2).
tamaño(camisa1,1).
tamaño(camisa2,1).
peso(libro1,pesado).
peso(libro2,pesado).
peso(libro3,pesado).
peso(libro4,pesado).
peso(lampara,mediano).
peso(platos,mediano).
peso(abrigo,ligero).
peso(tv,pesado).
peso(pantalones1,ligero).
peso(pantalones2,ligero).
peso(camisa1,ligero).
peso(camisa2,ligero).
fragil(lampara).
fragil(platos).
fragil(tv).
plegable(pantalones1).
plegable(pantalones2).
plegable(camisa1).
plegable(camisa2).
caja(caja1).
caja(caja2).
caja(caja3).
caja(caja4).
caja(caja5).
caja(caja6).
caja(caja7).
caja(caja8).
caja(caja9).
caja(caja10).
caja(caja11).
caja(caja12).
caja(caja13).
caja(caja14).
caja(caja15).
caja(caja16).
caja(caja17).
caja(caja18).
caja(caja19).
caja(caja20).
caja(caja21).
caja(caja22).
caja(caja24).
caja(caja25).
caja(caja26).
caja(caja27).
caja(caja28).
caja(caja29).
caja(caja30).
:-dynamic si/1,no/1.
undo :- retract(si(_)),fail.
undo :- retract(no(_)),fail.
/*Objetos Embalados tiene nombre,num_caja*/
:-dynamic objetoembalado/2.
undo :- retract(objetoembalado(_,_)),fail.
:-dynamic objetoempaquetado/1.
undo :- retract(objetoempaquetado(_)),fail.
/*caja tiene num_caja*/
:-dynamic caja/1.
undo.

:-dynamic objeto/1,tamaño/2,peso/2,fragil/1,plegable/1.
undoobj :- retract(objeto(_)),fail.
undoobj :- retract(tamaño(_,_)),fail.
undoobj :- retract(peso(_,_)),fail.
undoobj :- retract(fragil(_)),fail.
undoobj :- retract(plegable(_)),fail.
undoobj.

iniciar:-
    write("Digite el nombre del objeto(con min?scula y terminando con punto)  "),
    read(Nombre),nl,
    write("Dijite el peso del objeto (pesado/mediano/ligero)"),
    read(Peso),nl,
    write("Dijite el tamaño del objeto (valor numerico)"),
    read(Tamaño),nl,
    write("¿El objeto es fragil?(si/no)"),
    read(Frajil),nl,
    write("¿El objeto es plegable?(si/no)"),
    read(Plegable),nl,
    nuevo_objeto(Nombre,Peso,Tamaño,Frajil,Plegable)
    ,repetir.

repetir:- write('desea incluir otro objeto (si/no) '), read(Respuesta),nl, ((Respuesta==si)->iniciar;(Respuesta==no)->write('Para embalar los articulos, esciba embalar. ');fail).



nuevo_objeto(Nombre,Peso,Tamaño,Frajil,Plegable):-
    objeto(Nombre) -> write("El objeto ya existe, no se ha insertado"),! ;
         assert(objeto(Nombre)),
         assert(peso(Nombre,Peso)),
         assert(tamaño(Nombre,Tamaño)),
         (Frajil='si' ; Frajil='s')->assert(fragil(Nombre));!,
         (Plegable='si' ; Plegable='s')->assert(plegable(Nombre);!),
         write("Se ha insertado el objeto").

embalar :-embalarfragil,nl,nl.



/*reglas*/
embalarfragil :-(r1,r2,r3)->!;r4,!.
embalarpesado:-(r5,r6)->!;r7,!.
embalarmedianos:-(r8,r9)->!;r10,!.
embalarligeros:-(r11,r12)->!;r13,!.
/*Reglas*/
r1:- /*nl,write("inicio de la regla 1"),*/
    nl,
    ofrajaembalar(X),
    (cajasolofragil(_);cajavacia(_)),
    asserta(objetoempaquetado(X)),
    write("Se ha empaquetado : "),write(X),!.
r2:- /*nl,write("inicio de la regla 2"),*/
    nl,
    ofrajaembalar(X),!,
    buscarcajafragil(X,Y),
    objetoempaquetado(X),
    asserta(objetoembalado(X,Y)),
    write("Se ha embalado : "),write(X),write(" en la caja: "),write(Y),nl,!.
r3:-
    /*nl,write("inicio de la regla 3"),*/

    nl,
    (ofrajaembalar(_))->embalarfragil,!.
r4:- nl,write("r4 finaliza objetos fragiles inicia objetos pesados "),embalarpesado.
r5:-
    nl,
    /*write("inicio de la regla 5"),*/
    opesadoaembalar(X),
    buscarcajapesado(X,Y),
    assert(objetoembalado(X,Y)),!,
    write("Se ha embalado : "),write(X),write(" en la caja: "),write(Y),nl,!.
r6:-nl,
    /*write("inicio de la regla 6"),*/
    (opesadoaembalar(_))->embalarpesado,!.
r7:- nl,write("R7 finaliza objetos pesados, inicia objetos medianos "),embalarmedianos.

r8:-
    nl,/*write("inicio de la regla 8"),*/
    omedianoaembalar(X),
    buscarcajamediano(X,Y),
    assert(objetoembalado(X,Y)),
    write("Se ha embalado : "),write(X),write(" en la caja: "),write(Y),nl,!.
r9:- nl,/*write("inicio de la regla 9"),*/
    (omedianoaembalar(_))->embalarmedianos,!.

r10:-nl,write("R10 finaliza objetos medianos, inicia objetos ligeros"),embalarligeros,!.

r11:-nl,/*write("inicio de la regla 11"),*/
    oligeroaembalar(X),
    buscarcajaligeros(X,Y),
    assert(objetoembalado(X,Y)),
    write("Se ha embalado : "),write(X),write(" en la caja: "),write(Y),nl,!.

r12:-nl,/*write("inicio de la regla 12"),*/
    (oligeroaembalar(_))->embalarligeros,!.

r13:-nl,write("r13 Fin"),nl,salida,!.
/*Busquedas*/

/*Busqueda de cajas*/
buscarcajafragil(X,C):-(cajasolofragil(C);cajavacia(C)),cajaconespacio(X,C),!.
buscarcajapesado(X,C):-caja(C),cconOfragil(C),cmenos4opesados(C),cajaconespacio(X,C),!.
buscarcajamediano(X,C):-(cajasinfragil(C);cajavacia(C)),cajaconespacio(X,C).
buscarcajaligeros(X,C):-(cajaconespacio(X,C);cajavacia(C)),cajaconespacio(X,C).


cconOfragil(C):-caja(C),contarFrajilescaja(C,N),(N==0).
cmenos4opesados(C):-caja(C),contarOcaja(C,pesado,N),(N<3).

/*el espacio libre en la caja es mayor que el tamaño del ojeto*/

/*Otras busquedas*/

oligeroaembalar(X):-peso(X,ligero),objeto(X),not(objetoembalado(X,_)).
opesadoaembalar(X):-peso(X,pesado),objeto(X),not(objetoembalado(X,_)).
omedianoaembalar(X):-peso(X,mediano),objeto(X),not(objetoembalado(X,_)).
objfrajaempaquetar(X):-fragil(X),objeto(X),not(objetoempaquetado(X)).
ofrajaembalar(X):-fragil(X),objeto(X),not(objetoembalado(X,_)).

cajavacia(X):-caja(X),not(objetoembalado(_,X)),!.

cajasolofragil(X):-objeto(Y),fragil(Y),objetoembalado(Y,X),caja(X),!.
cajasinfragil(C):-caja(C),contarFrajilescaja(C,N),(N==0).
nuevacaja(X):-caja(X),assert(caja(X)),!.
/*permiten contar*/
contaresocupado(C,O):-contaresocupado(C,[],0,O).
contaresocupado(C,Lista,Acumulado,O):-
    caja(C),
    objetoembalado(X,C),tamaño(X,Y),
    (   member(X, Lista)->  fail; !,
        Acumulado1 is Acumulado +Y,
        contaresocupado(C,[X|Lista], Acumulado1, O)
    ).
contaresocupado(_,_,O,O).

contarOcaja(C,Peso,O):-contarOcaja(C,Peso,[],0,O).
contarOcaja(C,Peso,Lista,Acumulado,O):-
    caja(C),
    objetoembalado(X,C),peso(X,Peso),
    (   member(X, Lista)->  fail; !,
        Acumulado1 is Acumulado +1,
        contarOcaja(C,Peso,[X|Lista], Acumulado1, O)
    ).
contarOcaja(_,_,_,O,O).

contarFrajilescaja(C,O):-contarFrajilescaja(C,[],0,O).
contarFrajilescaja(C,Lista,Acumulado,O):-
    caja(C),
    objetoembalado(X,C),fragil(X),
    (   member(X, Lista)->  fail; !,
        Acumulado1 is Acumulado +1,
        contarFrajilescaja(C,[X|Lista], Acumulado1, O)
    ).
contarFrajilescaja(_,_,O,O).
contarcaja(C,O):-caja(C),contarcaja(C,[],0,O).
contarcaja(C,Lista,Acumulado,O):-
        objetoembalado(X,C),objeto(X),
    (   member(X, Lista)->  fail; !,
        Acumulado1 is Acumulado +1,
        contarcaja(C,[X|Lista], Acumulado1, O)
    ).
contarcaja(_,_,O,O).

espaciolibre(C,L):-caja(C),contaresocupado(C,O),(L is 10-O).


cajaconespacio(O,C):-
               objeto(O),tamaño(O,T),espaciolibre(C,L),(L>=T).

/*
 *
espaciolibre(Caja,Espacio):-
*/


/*Insertar objetos*/
preguntar(Pregunta) :-
    write('¿el objeto es '),
    write(Pregunta),
    write('?'),
    read(Respuesta),
    nl,
    ( (Respuesta==si;Respuesta==s)
    ->
    assert(si(Pregunta));
    assert(no(Pregunta)),fail).


/*Verificar algo*/

verificar(X) :-
   (si(X)
    ->
    true ;
    (no(X)
     ->
     fail ;
     preguntar(X))).


/*Imprimir respuesta*/
salida:-
    write("Las cajas usadas son : "),
    cajasusadas(O)
    ,write(O), write("Se han usado "),tamañoLista(O,Y),write(Y) ,write(" cajas diferentes "),nl
    , tamañocajas
    ,write("Los objetos se embalaron de la siguiente manera"),nl,nl,objetosencaja.
    
objetosencaja:-objetosXcaja(X),show_records(X),!.

tamañocajas:-cajasusadas(O),show_pesocaja(O),!.



show_pesocaja([]).
show_pesocaja([A|B]) :-
  write(A),espaciolibre(A,L),write(" Espacio libre :"), write(L),nl,
  show_pesocaja(B).

show_records([]).
show_records([A|B]) :-
  write(A),nl,
  show_records(B).


tamañoLista([],0).
tamañoLista([X|Y],N):-tamañoLista(Y,Sum), N is Sum+1.


objetosXcaja(L):- findall((X,Y),(caja(X),objetoembalado(Y,X)),C), sort(C,L).
cajasusadas(O) :- findall(X,(caja(X),objetoembalado(_,X)),C), sort(C,O).







