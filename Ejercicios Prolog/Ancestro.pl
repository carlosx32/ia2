padre(pedro,jos�).
padre(jos�,luis).
padre(jos�,ignacio).
padre(ignacio,mar�a).
padre(ignacio,mercedes).
ancestro(X,Y):- padre(X,Y).
ancestro(X,Y):- padre(X,C),ancestro(C,Y).