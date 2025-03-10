# Estratégia de Médias Móveis Automática - Binance API

## Resumo
Este projeto implementa uma estratégia de trade utilizando médias móveis em Python e a API da Binance no ambiente de teste (*testnet*). É relevante ressaltar a importância da criação das chaves API dentro do
ambiente de *testenet*, conforme mencionado, pois somente assim é possível utilizar o ambiente de trade simulado da Binance, isto é, com valores fictícios apenas para fins educacionais.

## Pré-requisitos
1. Baixe e instale o [Anaconda](https://www.anaconda.com/products/distribution) (Versão mais recente) em sua máquina (Linux, Windows ou Mac)
2. Conta na Binance configurada para o ambiente de teste (*testnet*).
3. Python 3.8 ou superior.

## Passo a passo para configurar
1. Crie uma conta na [Binance](https://www.binance.com/).
2. Acesse a plataforma de *testnet* de trade simulado em: [Binance Testnet](https://testnet.binance.vision/).
3. Gere suas chaves de API:
   - Vá em **Generate HMAC-SHA-256 Key** e crie uma nova chave, conforme imagem abaixo.
   - ![image](https://github.com/user-attachments/assets/ccf0c41b-fef8-47be-954!
   - Configure permissões para "TRADE", "USER_DATA" E "USER_STREAM" de acordo com esta imagem:
   - [image_2](https://github.com/user-attachments/assets/c333ee4c-f8f1-4e8a-94b6-8705ff4b7354)
e-fdeb86d4a82a)


## Instalando o ambiente
1. Clone o repositório do projeto:
   ```bash
   git clone git@github.com:leovnoliveira/bot-binance-cripto.git
   cd bot-binance-cripto
   
2. Crie um ambiente virtual (após variáveis de ambiente já configuradas em seu sistema operacional):
   - Abra o Visual Studio Code (VSCode) e o terminal integrado.
   - No terminal, navegue até o diretório do projeto e execute o seguinte comando para criar o ambiente virtua
   ```bash
   python -m venv venv
   venv\Scripts\Activate

3. ** Instale as dependencias do pacote com `requirements.txt`** fazendo:
```bash
pip install -r requirements.txt
```

## Estratégia de Médias Móveis
A estratégia compara:

* Média móvel rápida (7 períodos)
* Média móvel lenta (40 períodos)

### Execução
Para iniciar o bot de trade, execute:
  ```bash
python Main.py
