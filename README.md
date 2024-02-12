# Formatação de Endereços

## Descrição

Um provedor de endereços retorna endereços apenas com ruas concatenadas, nomes e números em uma única string. Nosso próprio sistema, por outro lado, tem campos específicos para armazenar o nome da rua e o número da rua.

Portanto, se faz necessário escrever um código simples que processe a entrada e retorne
esses campos na saída.

**Entrada:** string de endereço com os dados concatenados.

**Saída:** string da rua e string do número da rua.

## Casos

1. Casos Simples
    * `“Miritiba 339” -> {“Miritiba”, “339”}`
    * `“Babaçu 500” -> {“Babaçu”, “500”`
    * `“Cambuí 804B” -> {“Cambuí”, “123B”}`
2. Casos Complexos (com Whitespace)
    * `"Rio Branco 23" -> {"Rio Branco", "23"}`
    * `"Quirino dos Santos 23b" -> {"Quirino dos Santos": "23b"}`
3. Caso Endereço Estrangeiro
    * `"4, Rue de la République" -> {"Rue de la République", "4"}`
    * `"100 Broadway Av” -> {"Broadway Av", "100"}`
    * `"Calle Sagasta, 26" -> {“Calle Sagasta”, “26”}`
    * `“Calle 44 No 1991” -> {“Calle 44”, “No 1991”}`


## Configurando o ambiente virtual e executando testes unitários

Para configurar o ambiente no Linux e executar o script que irá configurar o ambiente, basta executar o seguinte comando:

`bash 01_config.sh`

Observação: Apesar de o script validar o sistema operacional, para a execução em ambientes Windows é necessário instalar o `wsl` para criar o subsistema Linux. Dessa forma, recomendo utilizar o recurso apenas no Linux.

Para usuários em ambiente Windows, será disponibilizado um arquivo executável da aplicação.

![Caso 1](https://i.imgur.com/dfz93gq.png)

![Caso 2](https://i.imgur.com/xFKMEIe.png)

![Caso 3](https://i.imgur.com/sNP7PBI.png)