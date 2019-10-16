# SkylineProblem
Problema da linha do horizonte

Um problema clássico comum em algoritmos que tratam imagens de desenho é a eliminação de linhas ocultas - linhas obscurecidas por outras partes do desenho. Desenvolva um programa em Python3 para ajudar um arquiteto no desenho da linha do horizonte de uma cidade, dado a localização dos edifícios. Para tornar o problema tratável, considere que todos os edifícios possuem formas retangulares e compartilham uma base comum (a cidade em que eles são construídos é muito plana). A cidade também é vista como bidimensional. Cada edifício será especificado por uma tripla ordenada (Ei, Ai, Di), onde Ei e Di são as coordenadas esquerda e direita, repectivamente, do edifício i e Ai é a altura do edifício.

A entrada é uma sequência de triplas de edifícios. Todas as coordenadas dos edifícios são inteiros menores que 10000 e haverá ao menos um e não mais do que 5000 edifícios no arquivo de entrada. As triplas serão ordenadas por Ei, a coordenada x à esquerda do edifício, de modo que o edifício com a menor coordenada x à esquerda é o primeiro no arquivo de entrada. As triplas serão fornecidas uma por linha, finalizando a entrada com a tripla (0,0,0). Segue a entrada para a instância do exemplo:

 (1,11,5)
 (2,6,7)
 (3,13,9)
 (12,7,16)
 (14,3,25)
 (19,18,22)
 (23,13,29)
 (24,4,28)
 (0,0,0)

Saída

A saída consiste de uma sequência de inteiros (v1, v2, v3, . . . , vn−2, vn−1, vn) que descrevem a linha do horizonte, onde cada vi tal que i é um número ímpar representa uma coordenada x e cada vi tal que i é um número par representa uma altura. A sequência representa o "caminho" tomado, por exemplo, pela ponta de uma caneta que inicia tocando o papel na menor coordenada x e depois viaja traçando verticalmente e horizontalmente todas as linhas que definem a linha do horizonte (skyline). Note que o último inteiro na sequência que define a linha do horizonte será sempre um 0 (zero).

 (1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)
