def obter_mes_extenso(mes):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return meses[mes - 1]

def validar_mes(mes):
    return 1 <= mes <= 12

def validar_temperatura(temp):
    return -60 <= temp <= 50

def coletar_dados_ano():
    temperaturas_maximas = []
    for i in range(1, 13):
        while True:
            try:
                mes = i
                if not validar_mes(mes):
                    raise ValueError("Mês inválido. Deve ser um número entre 1 e 12.")
                
                temp_max = float(input(f"Informe a temperatura máxima registrada no mês de {obter_mes_extenso(mes)}: "))
                if not validar_temperatura(temp_max):
                    raise ValueError("Temperatura inválida. Deve estar entre -60°C e 50°C.")
                
                temperaturas_maximas.append(temp_max)
                break
            except ValueError as e:
                print(e)
    
    return temperaturas_maximas

def editar_dados(temperaturas_maximas):
    while True:
        try:
            mes_editar = int(input("Digite o número do mês que deseja editar (1-12), ou 0 para sair: "))
            if mes_editar == 0:
                break
            if not validar_mes(mes_editar):
                raise ValueError("Mês inválido. Deve ser um número entre 1 e 12.")
            
            nova_temp = float(input(f"Informe a nova temperatura máxima para {obter_mes_extenso(mes_editar)}: "))
            if not validar_temperatura(nova_temp):
                raise ValueError("Temperatura inválida. Deve estar entre -60°C e 50°C.")
            
            temperaturas_maximas[mes_editar - 1] = nova_temp
            print(f"Temperatura do mês de {obter_mes_extenso(mes_editar)} atualizada para {nova_temp}°C.\n")
        except ValueError as e:
            print(e)

def analisar_dados(temperaturas_maximas):
    # Cálculo da temperatura média máxima anual
    temp_media_anual = sum(temperaturas_maximas) / len(temperaturas_maximas)
    
    # Quantidade de meses escaldantes (temperaturas acima de 33°C)
    meses_escaldantes = sum(1 for temp in temperaturas_maximas if temp > 33)
    
    # Mês mais escaldante
    mes_mais_escaldante = temperaturas_maximas.index(max(temperaturas_maximas)) + 1
    
    # Mês menos quente
    mes_menos_quente = temperaturas_maximas.index(min(temperaturas_maximas)) + 1
    
    # Resultados
    print(f"\nTemperatura média máxima anual: {temp_media_anual:.2f}°C")
    print(f"Quantidade de meses escaldantes: {meses_escaldantes}")
    print(f"Mês mais escaldante do ano: {obter_mes_extenso(mes_mais_escaldante)} ({max(temperaturas_maximas)}°C)")
    print(f"Mês menos quente do ano: {obter_mes_extenso(mes_menos_quente)} ({min(temperaturas_maximas)}°C)")

def main():
    while True:
        print("\nInsira os dados meteorológicos para um novo ano.")
        temperaturas_maximas = coletar_dados_ano()

        while True:
            print("\nEscolha uma opção:")
            print("1. Analisar dados")
            print("2. Editar temperatura de um mês")
            print("3. Inserir dados para outro ano")
            print("4. Sair")
            
            opcao = input("Opção: ").strip()
            
            if opcao == '1':
                analisar_dados(temperaturas_maximas)
            elif opcao == '2':
                editar_dados(temperaturas_maximas)
            elif opcao == '3':
                break
            elif opcao == '4':
                print("Saindo...")
                return
            else:
                print("Opção inválida. Tente novamente.")
    
if __name__ == "__main__":
    main()
