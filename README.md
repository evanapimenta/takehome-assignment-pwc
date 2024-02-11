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
3.
