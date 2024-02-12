#!/bin/sh

echo "Instalando virtualenv para comportar as libs necessárias..."

pip install virtualenv

echo "Criando ambiente virtual..."
virtualenv venv || { echo "Falha ao criar ambiente virtual."; exit  1; }

echo "Ativando ambiente virtual..."
if [ "$(uname)" = "Linux" ]; then
    source venv/bin/activate || { echo "Falha ao ativar ambiente virtual."; exit  1; }
elif [ "$(uname)" = "MINGW32_NT-" ] || [ "$(uname)" = "MINGW64_NT-" ]; then
    venv/Scripts/.Activate
else
    echo "Sistema não suportado."
fi

echo "Instalando dependências..."
pip install -r requirements.txt

cd ..

echo "Ambiente configurado com sucesso!"

echo "Executando testes unitários..."

pytest

echo "Teste executado!"
