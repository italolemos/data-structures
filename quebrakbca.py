

objetivo = [1, 2, 3, 4, 0, 5, 6, 7, 8]
puzze = [3, 4, 5, 2, 1, 0, 8, 7, 6]



def imprime_tabela(estado):
    print ( '-----------------\n'
            +'| %i | %i | %i | ' % (estado[0], estado[1], estado[2]) 
            +'\n'
            +'| %i | %i | %i | ' % (estado[3], estado[4], estado[5])
            +'\n'
            +'| %i | %i | %i | ' % (estado[6], estado[7], estado[8])
          )



imprime_tabela(objetivo)