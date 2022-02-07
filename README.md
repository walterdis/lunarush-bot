# Luna Rush Auto Clicker Bot

Se o aplicativo lhe ajudar de alguma forma, uma doação para ajudar a pagar a conta de luz sempre é bem vinda ;)

### **Wallet Smart Chain (BNB, LUS, USDT, BUSD)**
0x1F66230C4e98b557D3e55d7d2C047CcbA8E55bD6 
#

Bot desenvolvido com o intuito de me permitir dormir durante a noite e, poder dar uma volta por ai sem ficar me preocupando com horário ;)

Alguns métodos foram retirados do bot do bombcrypto feito pelo mpcabete (https://github.com/mpcabete/bombcrypto-bot)

# O que ele faz?
- Conecta na metamask.
- Seleciona o modo de luta com chefão
- Seleciona o estágio disponível (faz o scroll até achar um)
- Verifica a energia dos personagens, remove e adiciona os disponíveis
- Inicia a luta e aguarda os resultados
- Caso não tenha mais personagens para luta, ele volta para seleção de estágio e aguarda por **aproximadamente 2 horas** antes de iniciar novamente.

## Obs:
Na luta, foi implementado um contador de cliques que, quando chegar a 15, ele recarrega o jogo pois parte do princípio que ele travou na batalha (mais a frente será melhorada a verificação ou incluída em algum arquivo de configurações futuramente)


# Requerimentos
### **Tanto o jogo quanto a metamask devem estar em inglês para funcionar corretamente.**
- Python 3.9 (3.10 não funciona)
   - https://www.python.org/downloads/release/python-399/ ou https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe
 - Na instalação, deixe marcado a caixa **"add python  to path"**
 - Abra o terminal no diretório em que foi baixado o bot e digite ```pip install -r requirements.txt```
 - Digite ```python index.py``` e execute o programa
 
 

*BOT desenvolvido em resolução 1920x1080 (full hd). Caso de problema de detecção de imagens, tente tirar fotos novamente igual as que estão na pasta **target_images***