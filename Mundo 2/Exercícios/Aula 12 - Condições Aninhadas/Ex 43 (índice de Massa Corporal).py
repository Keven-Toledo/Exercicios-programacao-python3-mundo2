nome = str(input('Nome completo: ')).strip().title()
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))

imc = peso / (altura ** 2)

if imc >= 16:
    resultado = 'Muito abaixo do peso'
    cons = 'Queda de cabelo, infertilidade, ausência menstrual'
    print('''Seu peso é de {}Kg.
    Considerado: {}
    Seu IMC: {:.1f}
    Possíveis consequências: {}'''.format(peso, resultado, imc, cons))
elif imc <= 18.4:
    resultado = 'Abaixo do peso'
    cons = 'Fadiga, Stress, ansiedade'
    print('''Seu peso é de {}Kg.
    Considerado: {}
    Seu IMC: {:.1f}
    Possíveis consequências: {}'''.format(peso, resultado, imc, cons))
elif imc <= 24.9:
    resultado = 'Peso ideal'
    cons = 'Menor risco de doenças cardíacas e vasculares'
    print('''Seu peso é de {}Kg.
    Considerado: {}
    Seu IMC: {:.1f}
    Possíveis consequências: {}'''.format(peso, resultado, imc, cons))
elif imc <= 29.9:
    resultado = 'Acima do peso'
    cons = 'Fadiga, má circulação, varizes'
    print('''Seu peso é de {}Kg.
    Considerado: {}
    Seu IMC: {:.1f}
    Possíveis consequências: {}'''.format(peso, resultado, imc, cons))
elif imc <= 34.9:
    resultado = 'Obesidade Grau I'
    cons = 'Diabetes, angina, infarto, aterosclerose'
    print('''Seu peso é de {}Kg.
    Considerado: {}
    Seu IMC: {:.1f}
    Possíveis consequências: {}'''.format(peso, resultado, imc, cons))
elif imc <= 40:
    resultado = 'Obesidade Grau II'
    cons = 'Apneia do sono, falta de ar'
    print('''Seu peso é de {}Kg.
    Considerado: {}
    Seu IMC: {:.1f}
    Possíveis consequências: {}'''.format(peso, resultado, imc, cons))
elif imc > 40:
    resultado = 'Obesidade Grau III'
    cons = 'Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC'
    print('''Seu peso é de {}Kg.
    Considerado: {}
    Seu IMC: {:.1f}
    Possíveis consequências: {}'''.format(peso, resultado, imc, cons))
