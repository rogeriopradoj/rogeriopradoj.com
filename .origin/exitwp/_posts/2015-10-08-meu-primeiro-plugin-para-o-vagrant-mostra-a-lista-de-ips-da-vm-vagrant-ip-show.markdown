---
author: rogeriopradoj
comments: true
date: 2015-10-08 05:59:37+00:00
layout: post
slug: meu-primeiro-plugin-para-o-vagrant-mostra-a-lista-de-ips-da-vm-vagrant-ip-show
title: Meu primeiro plugin para o Vagrant mostra a lista de IPs da VM! vagrant-ip-show
wordpress_id: 644
categories:
- Geral
- Vagrant
tags:
- gem
- github
- plugin
- vagrant
---

Olá, pessoal!

Passando rápido aqui para falar que criei meu primeiro plugin para Vagrant: é o [vagrant-ip-show](https://github.com/rogeriopradoj/vagrant-ip-show).

Ele faz uma coisa muito simples: mostra os IPs de uma VM.

![site vagrant-ip-show](http://rogeriopradoj.com/wp-content/uploads/2015/10/Vagrant-ip-show_by_rogeriopradoj.png)



<blockquote>Ah, Rogério, mas porque um plugin para algo tão simples? Não tem jeito de fazer isso na mão?

-- Alguém por aí ;-)</blockquote>



Então, tem uma série de formas buscar essa informação. Você poderia conectar na VM (`vagrant ssh`) e rodar um comando `ifconfig`. Ou então olhar no seu Vagrantfile as configurações de rede que tiver feito. Ou ainda, entrar na configuração do Virtualbox (ou qual seja o provider que estiver usando) e tentar localizar a faixa de IPs que ele está usando e partir daí para rodar no seu _host_ alguns comandos de rede...

Caramba, quanta coisa! Mas se tem um jeito fácil, porque não usar! Fui atrás de uma linha mágica, já tratada para trazer apenas a listinha de IPs, é ela é essa:


    
    $ ifconfig | grep 'inet addr:' | grep -v 127.0.0.1 | sed -e 's/Bcast//' | cut -d: -f2



No seu computador, você poderia passar via `vagrant ssh` o comando direto para dentro da VM e receber o resultado assim:


    
    $ vagrant ssh -- ifconfig | grep 'inet addr:' | grep -v 127.0.0.1 | sed -e 's/Bcast//' | cut -d: -f2



Mas o jeito mais fácil, depois que o plugin está instalado, é só rodar esse comando aqui:


    
    $ vagrant ip-show



Quer instalar o plugin? É fácil:


    
    $ vagrant plugin install vagrant-ip-show



Depois disso você pode usar o comando `vagrant ip-show` em qualquer um dos seus projetos.



## Motivação





<blockquote>Mas vale a pena criar um plugin para o Vagrant? Não dá muito trabalho?

-- Alguém por aí ;-)</blockquote>



Agora estou enxergando uma pergunta mais interessante! No meu caso, criar um plugin para o Vagrant era um desafio, que até que enfim consegui realizar. Então sim, vale a pena! Sempre acompanhei o brasileiro [Fábio Rehm](http://fabiorehm.com/) criando [uma porrada deles](http://fabiorehm.com/blog/2013/12/12/so-i-released-a-lot-of-vagrant-plugins-now-what-s-next/), e pensava: poxa, teria que ficar fera em Ruby antes de conseguir um dia criar um plugin... Mesmo estudando um monte sobre Vagrant e seus plugins, não parecia tarefa fácil.





[https://youtu.be/niQvLXI1z9I?t=3m14s](https://youtu.be/niQvLXI1z9I?t=3m14s)



--

Mas acreditava que talvez pudessse ser igual como usar o Vagrant, que é construído em Ruby, mas você pode usá-lo sem ter o mínimo de proficiência na linguagem. Se eu achasse um "be-a-bá" de como começar, deveria conseguir. E, como disse, era um desafio e a necessidade que tive de descobrir os IP de uma VM mexeu comigo. Pensei: é isso, já sei a necessidade. Se não houver nenhum plugin para isso, é esse que vou criar!

Na minha busca, achei apenas [um plugin](https://github.com/mkuzmin/vagrant-guestip) que não entregava o que precisava.

![vagrant-guestip inconsistente](http://rogeriopradoj.com/wp-content/uploads/2015/10/2__rogerio_RgoMBP____contribs_mercado_sup__zsh_.png)

Infelizmente, ele trazia apenas um IP: o que estava configurado como hostonly na interface de rede do VirtualBox. E esse IP é geralmente o que não precisamos saber :-) . O que geralmente queremos são os IPs configurados como [private_network ou public_network](https://docs.vagrantup.com/v2/networking/index.html), sejam eles estáticos ou recebidos por DHCP. O ifconfig/ipconfig traz isso tudo para nós, então o meu plugin devia trazer pelo menos TODOS OS IPs.



## Base teórica



Aí que o artigo [How to Create a Simple Vagrant Plugin](https://www.noppanit.com/create-simple-vagrant-plugin/) do Noppanit (Toy), que eu já tinha lido alguns meses atrás, veio como uma mão na roda. Nele o autor fala sobre como fez num passo a passo para criar o plugin dele (se tem curiosidade, acesse lá que vale a pena :-) ). Dessa vez, como já tinha com a necessidade clara, coloquei a mão na massa e o projeto saiu!

[![vagrant-ip-show install and usage](http://rogeriopradoj.com/wp-content/uploads/2015/10/2__rogerio_RgoMBP____contribs_mercado_sup__zsh_-2.png)](http://rogeriopradoj.com/wp-content/uploads/2015/10/2__rogerio_RgoMBP____contribs_mercado_sup__zsh_-2.png)



## Tive que ficar fera em Ruby?



Com certeza não. Mas tive que entender um pouquinho mais sobre o site [http://rubygems.org/](http://rubygems.org/), pois o plugin é publicado lá como uma Ruby Gem. Aprendi que aparentemente no mundo Ruby os badges de versões para projetos open source são liberados no [https://badge.fury.io/](https://badge.fury.io/) (no mundo PHP, que estou mais acostumado, é comum usar o [https://poser.pugx.org/](https://poser.pugx.org/). Aprendi um pouco mais também no código fonte do [plugin vagrant-exec](https://github.com/p0deje/vagrant-exec) sobre como funciona um plugin um pouco mais elaborado. E tudo isso foi ótimo!

Testem o plugin se acharem interessante, deêm o feedback e fiquem à vontade para conversar sobre o assunto.

É isso aí, pessoal, até a próxima!

—

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com/).
