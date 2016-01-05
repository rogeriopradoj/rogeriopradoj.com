---
author: rogeriopradoj
comments: true
date: 2014-08-03 17:08:42+00:00
layout: post
slug: pra-nao-dizer-que-nao-falei-de-vagrant
title: Pra não dizer que não falei de Vagrant
wordpress_id: 525
categories:
- Vagrant
tags:
- vagrant
---

Esse post é uma republicação do artigo no site do PHPSP ([http://phpsp.org.br/index.php/pra-nao-dizer-que-nao-falei-de-vagrant/](http://phpsp.org.br/index.php/pra-nao-dizer-que-nao-falei-de-vagrant/)).





---





Olá, pessoal.





![Vagrant logo](http://www.vagrantup.com/images/logo_vagrant-81478652.png)





Vamos falar um pouco dessa ferramenta super útil que promete (e cumpre) ser a revolução para ambientes de desenvolvimento virtualizados, o Vagrant! Mas antes de falar da ferramenta em si, é importante começar com o seguinte: como é hoje o seu ambiente de desenvolvimento?





## Evolução do ambiente de desenvolvimento





Vou contar um pouco da evolução do meu ambiente de desenvolvimento, talvez faça você recordar de algo que provavelmente já ocorreu com você:





- Sem noção, altero tudo em produção





- Separação do ambiente, instalo tudo na minha máquina





- Minha máquina vira uma carroça, e tudo dá conflito





- Leio [o texto](http://duodra.co/2012/02/18/desenvolvimento-php-usando-maquinas-virtuais-fastcgi-fpm/) do [Anderson (Duodraco) Casimiro](http://duodra.co/), aprendo que é uma boa virtualizar o ambiente de desenvolvimento dentro de uma máquina virtual, que posso ligar e desligar a qualquer momento





- Virtualização dá trabalho!





## Virtualização, promessa





A VM permite deixar os ambientes:





- leves





- reproduzíveis





- portatéis





## Virtualização, os 3 pilares





- Hardware





- Sistema operacional





- Softwares





## Automatizando os 3 pilares da Virtualização, aqui que entra o Vagrant





_Vagrantfile_: é a cola





_Boxes_: são VMs base, que já tem o Hardware e o Sistema Operacional definidos





_Provisionamento_: são os scripts que automatizam a instalação e configuração dos Softwares





## Como começar





- Leia o artigo do Duodraco, [http://duodra.co/2012/02/18/desenvolvimento-php-usando-maquinas-virtuais-fastcgi-fpm/](http://duodra.co/2012/02/18/desenvolvimento-php-usando-maquinas-virtuais-fastcgi-fpm/), e fique bravo se não funcionar com você (é o que aconteceu comigo ;-) )





- Baixa o instalador do Vagrant e leia a documentação no site oficial, [http://www.vagrantup.com/](http://www.vagrantup.com/) (existe um trabalho para traduzir a documentação para português, se quiser dê uma olhada em [http://friendsofvagrant.github.io/](http://friendsofvagrant.github.io/), contribuições são bem-vindas)





- Conheça as Boxes oficiais e as criadas pelas comunidade em [http://www.vagrantbox.es/](http://www.vagrantbox.es/), várias diferentes distribuições de Linux





- Comece com módulos e cookbooks para provisionamento prontos e ajuste para o que precisa (o Vagrant suporta muitos mais, no entanto o Puppet ([https://forge.puppetlabs.com/](https://forge.puppetlabs.com/)) e o Chef são os mais conhecidos ([http://community.opscode.com/](http://community.opscode.com/))





- Importante!!!: Procure aprender mais sobre Gerência de Configuração e Provisionamento, vão ser uma mão na roda para você





## Aprofunde-se





Depois que você tiver passado por esses passos, já entender o mínimo do conceito e tiver colocado pelo menos um pouquinho a mão na massa, aí compensa você ir para coisas mais avançadas, seguindo a própria documentação do Vagrant e o monte de informação disponível na web (minha dica, procure pelos plugins para Vagrant [https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Plugins](https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Plugins)).





## Me ajude mais!!!





E para facilitar bastante o seu desenvolvimento, duas ferramentas que já criam o esqueleto completo para você: Vagrantfile + Box + Provisionamento! São o mundo perfeito para realmente começar um projeto do zero sem ter quase nenhum trabalho nesse nível:





- [http://rove.io/](http://rove.io/), dica do Elton Minetto, cria tudo para você baseado no provisionador Chef. Bom para projetos Ruby ou PHP/LAMP





- [https://puphpet.com/](https://puphpet.com/) , cria tudo para você, com muito mais opções de configuração, baseado no provisionador Puppet. Muito bom para projetos PHP, tanto sobre Apache como sobre Nginx.



[caption id="" align="alignnone" width="200"]![Puphpet logo](https://secure.gravatar.com/avatar/c9cf3f15d0a46af8ef466c37d1dabb4d?s=200) Logo do Puphpet[/caption]



---





É isso aí pessoal, material não falta, não é mesmo?!?!





Já tivemos até o [primeiro evento de Vagrant no Brasil](http://credencial.imasters.com.br/phpsp-com-vagrant-puppet-e-php-no-cna-tremembe-zona-norte-de-sao-paulo), fiquem atentos para os próximos.





Se quiser aproveitar para ajudar em um projeto que tem tudo a ver com o tema, e é feito em PHP, deêm uma olhada no [Github do projeto Puphpet](https://github.com/puphpet), vocês vão ajudar muita gente com isso, e se envolver em um projeto Open Source é sempre bacana.





Bom divertimento, e qualquer coisa, me procurem, estou em todo lugar como [rogeriopradoj](http://rogeriopradoj.com)!
