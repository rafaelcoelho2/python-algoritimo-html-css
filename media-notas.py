
notas = []
for i in range(3):
     aluno = str(input('digite o nome do aluno: '))
     nota = float(input('notas : '))
     notas.append(nota)
media = sum(notas)/len(notas) 
print('minhas notas: ', notas)
print('sua média é: ', media)
