larg = float(input('Largura da parede:  '))
alt = float(input('Altura da parede:  '))
area = larg * alt
print ('Sua parede tem a dimensão de {:.0f}x{:.0f} e sua área é de {}n².'.format(larg, alt, area))
tinta = area / 2
print ('Para pintar essa parede, você precisara de {}l de tinta.'.format(tinta))