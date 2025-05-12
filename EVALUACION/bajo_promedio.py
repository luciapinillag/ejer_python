def bajoPromedio(lista_bajo):
    contador = 0
    for nota in lista_bajo:
        if nota < bajoPromedio:
            contador +=1
            return contador