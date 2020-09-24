# Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições 
# para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' 
# e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e
# qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na 
# tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

# Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”.
# O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento
# dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

# a	97
# d	100
# y	121
# |	124

