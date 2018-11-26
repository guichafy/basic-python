
def funcao_format():
    valor = 1500.00
    print(  "R$ {:07.2f}".format(valor)  )
    valor = 4.5
    print(  "R$ {:07.2f}".format(valor)  )
    print ( "U$ {:07d}".format(4))
    print ( "U$ {:7d}".format(4))
    print ( "Data {:02d}/{:02d}".format(2,1))



funcao_format()