---
date: 2016-10-24T05:06:00-03:00
title: 'Configurando Hotkeys no Nintendo 64 do Retropie'
categories:
    - Geral
tags:
    - retropie
    - raspberry
    - raspberry-pi
    - nintendo-64
    - n64
    - xbox-360
    - hotkey
---

Olá pessoal!

Essa dica é para quem usa o Retropie para emular videogames antigos no Raspberry Pi e está tendo problemas para sair de um jogo dentro do emulador de Nintendo 64 e também não consegue salvar seu progresso para carregá-lo posteriormente.

[![Logo Retropie](assets/images/2016/10/RetroPieWebsiteLogo.png)](https://retropie.org.uk/)
*Fonte: <https://retropie.org.uk/>*

---

Por padrão, o Retropie tem uma lista de hotkeys (que são os atalhos especiais feitos no joystic para alguma ação do emulador):

[![tabela hotkeys retropie](assets/images/2016/10/hotkeys-retropie.png)](https://retropie.org.uk/)
*Fonte: <https://github.com/RetroPie/RetroPie-Setup/wiki/FAQ#default-joypad-hotkeys>*

O problema é que quanto estamos jogando o Nintendo 64 (que roda o emulador Mupen64plus no Retropie 4), os padrões acima não funcionam. E nada acontece quando você aperta por exemplo SELECT + START, que deveria encerrar a partida e ir para a lista de ROMs no EmulationStation, fazendo com que você tenha que recorrer a linha de comando ou a um teclado conectado só para conseguir ir para outro jogo! Bem ruim, não é mesmo?

Essa situação acontece porque o Retropie tenta utilizar sempre que possível os emuladores da "família LibreRetro" daqueles hotkeys que mostramos. No entanto, quando a melhor performance para um dos videogames é conseguida com outro programa (caso do Nintendo 64), o emulador diferente tem a preferência.

Agora que já sabemos da história, vamos ver como resolver esse imbróglio:

1. Entre na linha de comando do seu Retropie (apertando F4 num teclado conectado, ou [acessando via SSH](https://github.com/retropie/retropie-setup/wiki/ssh))

1. Verifique no seu controle principal qual é o botão número correspondente ao botões que você vai usar como hotkey, usando o comando `jstest /dev/input/jsX`, onde X é o índice referente ao seu joystic. Exemplo, onde descobri que o SELECT é o botão 8 e o START é o botão 9:

```
$ jstest /dev/input/js0
Driver version is 2.1.0.
Joystick (Xbox 360 Wireless Receiver) has 6 axes (X, Y, Rx, Ry, Hat0X, Hat0Y)
and 17 buttons (BtnX, BtnY, BtnTL, BtnTR, BtnTR2, BtnSelect, BtnStart, BtnMode, BtnThumbL, BtnThumbR, ?, ?, ?, (null), (null), (null), (null)).
Testing ... (interrupt to exit)
Axes:  0: -2050  1:     0  2: -3810  3:     0  4:     0  5:     0 Buttons:  0:off  1:off  2:off  3:off  4:off  5:off  6:off  7:off  8:off  9:off 10:off 11:off 12:off 13:off 14:off 15:off 16:off
```

3. Edite o arquivo `/opt/retropie/configs/all/autoconf.cfg` de forma que a linha `mupen64plus_hotkeys = 1` fique `mupen64plus_hotkeys = 0`:

```
$ sed -i "s/mupen64plus_hotkeys = 1/mupen64plus_hotkeys = 0/g" /opt/retropie/configs/all/autoconf.cfg
```

4. Edite o arquivo `/opt/retropie/configs/n64/mupen64plus.cfg` para colocar os hotkeys de acordo com sua preferência e números dos botões descobertos com o jstest:

```
# Meus botões, Xbox 360 Controller wifi, xpad driver
# ---------------------------------------------------
# <select>   => 8
# <start>    => 9
# <L1>       => 4
# <R1>       => 5

# Hotkey para sair de um jogo
$ sed -i 's~Joy Mapping Stop = ""~Joy Mapping Stop = "J*B8/B9"~g' /opt/retropie/configs/n64/mupen64plus.cfg

# Hotkey para carregar um progresso salvo de uma partida
$ sed -i 's~Joy Mapping Load State = ""~Joy Mapping Load State = "J*B8/B4"~g' /opt/retropie/configs/n64/mupen64plus.cfg

# Hotkey para salvar o progresso de uma partida
$ sed -i 's~Joy Mapping Save State = ""~Joy Mapping Save State = "J*B8/B5"~g' /opt/retropie/configs/n64/mupen64plus.cfg
```

Depois disso aí é só reiniciar o Raspberry Pi (`$ sudo shutdown -r now`) e os seus jogos de Nintendo 64 já vão ter esses hotkeys funcionando!

---

Ficou com dúvida? Fique à vontade para falar comigo nos comentários abaixo e nos [contatos do RogerioPradoJ.com](https://rogeriopradoj.com/about/).

Até mais!


---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com/).
