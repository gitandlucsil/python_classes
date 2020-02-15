nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Eleve os ímpares ao quadrado
gen = (x**2 for x in nums if x%2==1)
#Mostra os resultados
for num in gen:
    print(num)
# Uma lista de tuplas (artista, faixa):
instrumentais = [('King Crimson', 'Fracture'),
('Metallica','Call of Ktulu'),
('Yes', 'Mood for a Day'),
('Pink Floyd', 'One of This Days'),
('Rush', 'YYZ')]
# Filtra e ordena apenas as faixas de artistas anteriores a letra N
print(sorted(faixa[-1]+" / "+faixa[0] for faixa in instrumentais if faixa[0].upper() < "N"))