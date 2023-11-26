def build_labyrinth(wall, rows, columns):
    """
    Función que construye el laberinto que coge como parámetros
    el muro, las filas y columnas.
    """
    #Se define el tamaño del laberinto como espacios en blanco de filas por columnas
    labyrinth = [[' ' for _ in range(columns)] for _ in range(rows)]

    #Define las coordenadas de que cada tupla dentro de wall como una "X" para marcar que es un muro
    for x, y in wall:
        labyrinth[x][y] = 'X'

    #Marcadores que indican la entrada y salida
    labyrinth[0][0] = 'E'
    labyrinth[4][4] = 'S'

    #La función devuelve el laberinto
    return labyrinth

#Las coordenadas del muro como una tupla (tal como indica la tarea, sino se podría modificar)
wall = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

#Las dimensiones del laberinto (en este caso 5x5, para que se ajuste al tamaño del muro)
rows = 5
columns = 5

labyrinth = build_labyrinth(wall, rows, columns)

#Hasta este punto el laberinto es una lista de listas, por lo que se unen para formar el resultado final
for rows in labyrinth:
    print(' '.join(rows))
