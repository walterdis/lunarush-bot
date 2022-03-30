# Certifique-se de:

- Deixar o jogo em inglês
- Zoom do navegador em 125%
- Configurar a qualidade do jogo para médio

A última atualização trouxe mudanças no sistema de energia. O bot foi atualizado para funcionar a partir do momento que os personagens tem 2 ou mais energia.
Não foi testado acima de 3 (para quem tem VIP) e abaixo de 2 energias, o bot fazia detecções errôneas.

# Multi Contas Implementado! (apenas para windows)
Ele detecta janelas com a palavra "Luna Rush", ou seja, caso o usuário possua algo além do jogo aberto que tenha esse nome, o bot vai interpretar que é uma janela do jogo.

# Luna Rush Auto Clicker Bot

Se o aplicativo lhe ajudar de alguma forma, uma doação para ajudar a pagar a conta de luz sempre é bem vinda ;)

### **Wallet Smart Chain (BNB, LUS, USDT, BUSD)**
0x1F66230C4e98b557D3e55d7d2C047CcbA8E55bD6 
#

Bot desenvolvido com o intuito de me permitir dormir durante a noite e, poder dar uma volta por ai sem ficar me preocupando com horário ;)

Alguns métodos foram retirados do bot do bombcrypto feito pelo mpcabete (https://github.com/mpcabete/bombcrypto-bot)

# Requerimentos
### **Tanto o jogo quanto a metamask devem estar em inglês para funcionar corretamente.**
- Qualidade do jogo deve estar na **mínima** (configuravel no próprio jogo)
- Python 3.9
   - https://www.python.org/downloads/release/python-399/ ou https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe
 - Na instalação, deixe marcado a caixa **"add python  to path"**
 - Abra o terminal (prompt de comando do windows / CMD) no diretório em que foi baixado o bot e digite ```pip install -r requirements.txt``` (ou execute o update_requirements.bat caso esteja no windows)
 - Digite ```python index.py``` e execute o programa
  

*BOT desenvolvido em resolução 1920x1080 (full hd). Caso de problema de detecção de imagens, tente tirar fotos novamente igual as que estão na pasta **target_images***

# O que ele faz?
- Conecta na metamask.
- Seleciona o modo de luta com chefão
- Seleciona o estágio disponível (faz o scroll até achar um)
- Verifica a energia dos personagens, remove e adiciona os disponíveis
- Inicia a luta e aguarda os resultados
- Caso não tenha mais personagens para luta, ele volta para seleção de estágio alterna para outra conta (caso exista) e no final de todas ele faz uma pausa entre **12** e **17 minutos**

## Obs:
Na luta, foi implementado um contador de cliques que, quando chegar a 15, ele recarrega o jogo pois parte do princípio que ele travou na batalha 

