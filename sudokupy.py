# -*- coding: cp1252 -*-
##########################
# SudokuPy 1.0 by Doc    #
# http://filippogiomi.it #
# Some rights reserved   #
##########################

def quadrante(s,r,c,n):
    '''individua a quale quadrante si sta facendo riferimento e
    restituisce true o false a seconda se n sia inseribile o meno'''
    if (r<3)&(c<3):         
        x1,x2,y1,y2=0,3,0,3
    elif (3<=r<6)&(c<3):
        x1,x2,y1,y2=3,6,0,3
    elif (r>=6)&(c<3):
        x1,x2,y1,y2=6,9,0,3
    elif (r<3)&(3<=c<6):
        x1,x2,y1,y2=0,3,3,6
    elif (3<=r<6)&(3<=c<6):
        x1,x2,y1,y2=3,6,3,6
    elif (r>=6)&(3<=c<6):
        x1,x2,y1,y2=6,9,3,6
    elif (r<3)&(c>=6):
        x1,x2,y1,y2=0,3,6,9
    elif (3<=r<6)&(c>=6):
        x1,x2,y1,y2=3,6,6,9
    elif (r>=6)&(c>=6):
        x1,x2,y1,y2=6,9,6,9

    q=[]
    for x in range(x1,x2):
        l=[]
        for y in range(y1,y2):
            l.append(s[x][y])
        q.append(l)
    
    
        
    for x in range(3):
        for y in range(3):
            if q[x][y]==n:
                return False
    return True

def riga(s,r,n):
    'controlla che n sia inseribile nella riga'
    for y in range(9):
        if s[r][y]==n:
            return False
    return True

def colonna(s,c,n):
    'controlla che n sia inseribile nella colonna'
    for x in range(9):
        if s[x][c]==n:
            return False
    return True

def vuoti(s):
    'restituisce il numero di spazi ancora da compilare'
    z=0
    for i in range(9):
        z+=s[i].count(0)
    return z

def probabilita(s,r,c):
    '''restituisce una lista con i possibili numeri per quella casella.
        se la casella è già stata riempita restituisce una lista vuota'''
    numeri=[]
    if s[r][c]>0:
        return numeri
    for i in range(1,10):
        if quadrante(s,r,c,i) & riga(s,r,i) & colonna(s,c,i):
            numeri.append(i)
    return numeri

def leggi(path):
    'legge il sudoku da un file'
    s=[]
    f=open(path)
    for line in iter(f):
        l=[]
        for x in range(9):
            l.append(int(line[x]))         
        s.append(l)
    return s

def disegna(s):
    'disegna il sudoku'
    for x in range(9):
        print ('+---'*9) + '+'
        for y in range(9):
            print '| ' + str(s[x][y]),
        print '|'
    print ('+---'*9) + '+'


def risolvi(s):
    'restituisce il sudoku risolto'
    while vuoti(s)>0:
        messo=0
        for x in range(9):
            for y in range(9):
                p= probabilita(s,x,y)
                if len(p)==1:
                   s[x][y]=p[0]
                   messo=1
                   break
            if messo==1:
                break
    return s

'esempio di utilizzo'
disegna(risolvi(leggi('su.txt')))
