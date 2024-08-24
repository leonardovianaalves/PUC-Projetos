# Análise de Dados Meteorológicos de 2021 - Projeto Base

Este repositório contém um script em Python para coletar, validar e analisar dados meteorológicos de uma cidade ao longo do ano de 2021. O programa permite ao usuário inserir a temperatura máxima registrada em cada mês, realizar análises desses dados e corrigir entradas incorretas sem precisar reiniciar o processo.

## Funcionalidades

- **Coleta de Dados**: O programa solicita ao usuário que insira a temperatura máxima para cada mês do ano.
- **Validação de Entrada**: As entradas de temperatura são validadas para garantir que estejam dentro do intervalo permitido (-60°C a 50°C).
- **Análise dos Dados**:
  - Calcula a temperatura média máxima anual.
  - Determina a quantidade de meses escaldantes (com temperatura acima de 33°C).
  - Identifica o mês mais escaldante e o menos quente do ano, exibindo-os por extenso.
- **Edição de Dados**: Caso o usuário insira um valor incorreto para um mês específico, ele pode corrigir essa entrada sem precisar reiniciar o programa.
- **Flexibilidade**: O programa oferece um menu interativo, permitindo que o usuário escolha entre analisar dados, editar temperaturas, ou inserir dados para outro ano.

## Como Usar

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

   Execute o script:

Execute o script:

2. Você pode executar o código no Google Colab ou em seu ambiente Python local.
3. Siga as instruções no terminal para inserir as temperaturas de cada mês.
Navegue pelo Menu:

Após inserir os dados, o menu permite que você escolha entre analisar os dados, corrigir uma entrada incorreta ou começar a inserir dados para outro ano.

## Exemplo de Uso
Insira os dados meteorológicos para um novo ano.
Informe a temperatura máxima registrada no mês de janeiro: 34.5
Informe a temperatura máxima registrada no mês de fevereiro: 35.2
Informe a temperatura máxima registrada no mês de março: 32.7
...

Escolha uma opção:
1. Analisar dados
2. Editar temperatura de um mês
3. Inserir dados para outro ano
4. Sair

   
## Requisitos
Python 3.x

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork deste repositório, crie uma branch para sua feature ou correção de bug, 
e abra um Pull Request quando estiver pronto para compartilhar suas alterações.
