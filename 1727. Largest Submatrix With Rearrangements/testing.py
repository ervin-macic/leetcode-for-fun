'''
can imagine the matrix as a series of intervals (continuous ones represent the interval)
and interested in finding interval intersection that maximises len(int) * num(ints having this int as subinterval) = area of submatrix
how would I find the interval that appears most often as subinterval?
can preprocess intersections maybe? nC2 intervals at most
[1, [2, 3] 4]
za svaku i vrijednost, koliko kolona ima tu i vrijednost? Onda imam neki mapping 0 -> 3, 1 -> 5, ... i cilj mi je nac consecutive
i,i+1,...i' takve da je (i'-i) * min(map(i) for i in range(i,i')) sto vece.
ne moze ovo
[[0, 0, 1], 
[1, 1, 2], 
[2, 0, 3]]

1 3 2 4 5 sta ce bit max rectangle koji mozemo ovdje napravit?
1 2 3 4 5 sortirano
mozemo imat 1 * 5, 2 * 4, 3 * 3, 4 * 2, 5 * 1
ako je npr 1 4 5 9 10
onda 
'''