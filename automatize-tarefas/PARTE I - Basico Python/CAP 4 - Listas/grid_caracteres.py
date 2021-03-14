grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
	    ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
		
for i in range(6):
	for j in range(8):
		print(grid[j][i], end='')
	print('')


'''
Grade para imagem composta de caracteres
Suponha que você tenha uma lista de listas em que cada valor das listas
internas seja uma string de um caractere como:
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
Podemos pensar em grid[x][y] como sendo o caractere nas coordenadas x e
y de uma “imagem” desenhada com caracteres textuais. A origem (0, 0) estará
no canto superior esquerdo, as coordenadas x aumentam para a direita e as
coordenadas y aumentam para baixo.
Copie o valor da grade anterior e crie um código que a utilize para exibir a
imagem:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
Dica: você deverá usar um loop em um loop para exibir grid[0][0], em
seguida grid[1][0], grid[2][0] e assim por diante, até grid[8][0]. Com isso, a
primeira linha estará concluída, portanto exiba uma quebra de linha. Em
seguida, seu programa deverá exibir grid[0][1], depois grid[1][1], grid[2][1] e
assim por diante. O último item que seu programa exibirá é grid[8][5].
Além disso, lembre-se de passar o argumento nomeado end para print()
'''