---
author: rogeriopradoj
comments: true
date: 2011-01-02 23:21:38+00:00
layout: post
slug: handbrake-converta-videos-para-seu-ipodiphone
title: Handbrake, converta vídeos para seu iPod/iPhone
wordpress_id: 35
categories:
- iPod/iPhone
tags:
- iPhone
- iPod
- ubuntu
- windows
---

Essa ferramenta é <del>a melhor</del> muito boa opção para converter seus vídeos para os formatos que rodam no iPod e iPhone.

[![Handbrake Logo](http://trac.handbrake.fr/HandBrakeIcon128.png)](http://handbrake.fr/)

Atualmente tenho um iPod Touch 3G de 32GB, e penei um pouco para conseguir que minha coleção de vídeos, séries e filmes rodassem no meu iDevice.

Em sua versão 0.9.5 ele funciona em Windows, Mac e Linux. Para os dois primeiros, existem os instaladores no site http://handbrake.fr/downloads.php, é só baixar e seguir os procedimentos.

Para Ubuntu, a instalação não é tão simples quanto nos outros sistemas, mas não é impossível de se fazer. A seguir um passo-a-passo para facilitar a vida do pessoal:

1) Meu Ubuntu é o 10.10, primeira coisa a fazer é abrir o terminal e adicionar o PPA do Handbrake ao sistema, digitando:
`
$ sudo add-apt-repository ppa:stebbins/handbrake-snapshots`

2) Próximo passo é atualizar o cache de aplicações de seus repositórios:
`
$ sudo apt-get update`

3) Por fim, usar o apt-get para instalar a interface gráfica da aplicação (gtk) e a interface de linha de comando (cli), digitando:

`sudo apt-get install handbrake-gtk handbrake-cli`

Pronto, você já tem instalada a ferramenta, agora você pode fechar o terminal e buscar o handbrake, ou no seu menu de aplicativos, ou com Alt+F2, com o GnomeDo ou com seu iniciador de aplicações preferido.

Por enquanto é isso, num próximo post posso mostrar como utilizar a ferramenta agora que você já tem ela instalada.

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com).
