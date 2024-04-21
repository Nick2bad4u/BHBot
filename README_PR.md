# BHBot

Bot agrícola Gold/XP para Brawlhalla 

Fortemente inspirado em [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) 

### ------ -------------------------------------------------- ----------- 

### BOT VOLTOU A SER MANUTENDO ATIVAMENTE! 
###### Junte-se ao [Discord](https://discord.gg/2HDmuqqq9p "Discord") para ajudar a manter o bot ou adicionar novos recursos! 

### ----------------------------------------------- -------------------- 

**AVISO:** O software foi originalmente desenvolvido para utilização privada. 
Embora não tenha sido projetado para isso, pode levar a resultados imprevistos, incluindo a execução de transações dentro de Mallhalla usando moedas do jogo. 

**Os desenvolvedores isentam-se de qualquer responsabilidade por quaisquer danos que possam surgir do uso deste software. É aconselhável proceder com cautela e utilizar o software a seu próprio critério.** 

(O bot foi testado por várias pessoas por mais de 3.000 horas sem problemas em 18/04/2024) 

# Instalação 
A versão mais recente sempre pode ser baixada [aqui ](https://github.com/Nick2bad4u/BHBot/releases) 

# Recursos 

- Funciona completamente em segundo plano 
- Envia entradas diretamente para o Brawlhalla para não incomodá-lo 
- Inicia o jogo automaticamente 
- Cria/configura lobby automaticamente 
- Escolhe/altera automaticamente duração do personagem e do jogo 
- Detecta e redefine automaticamente o limite de XP 
- Suporta modos personalizados 
- Suporta idiomas personalizados 
- Suporta até mesmo fontes personalizadas 
- ~~Prepara seu café~~ (apenas chá suportado por enquanto) 

# Uso 
- O processo foi projetado para ser intuitivo. Basta escolher as configurações necessárias clicando no botão "Configurações" 
- Depois que as configurações forem salvas, inicie o programa clicando no botão "Iniciar" 

# Limitações 
- O bot exige que "Recolher cruzamentos" seja definido como Sim. Se você acha que deveria defini-lo automaticamente, por favor [abra um problema](https://github.com/nick2bad4u/bhbot/issues) 
- O bot exige que o idioma do jogo seja definido como inglês. Se você acha que deveria defini-lo automaticamente, por favor [abra um problema](https://github.com/nick2bad4u/bhbot/issues) 

# Visão geral técnica 
- O código subjacente está sempre disponível para revisão por qualquer pessoa. 
- Essencialmente, o bot emprega a API SendMessage do Windows para transmitir entradas diretamente para a janela do Brawlhalla. Ele utiliza detecção de pixels para discernir estados e determinar a ação apropriada a qualquer momento.

- A classe BrawlhallaBot pode ser utilizada diretamente ou você pode desenvolver um wrapper personalizado para ela. Ele foi projetado para operar de forma independente, com gui.py servindo apenas como um wrapper gráfico usando PySimpleGUI.
