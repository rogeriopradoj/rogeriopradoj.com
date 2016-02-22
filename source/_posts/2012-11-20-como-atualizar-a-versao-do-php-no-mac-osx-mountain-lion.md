---
date: 2012-11-20 22:08:38+00:00
title: Como atualizar a versão do PHP no Mac OSX Mountain Lion
categories:
  - Geral
  - Mac
  - PHP
tags:
  - como-atualizar
  - homebrew
  - mac
  - osx
  - php
  - php-build
  - phpenv
---

Olá, pessoal Venho usando o Vagrant ([oficial](http://vagrantup.com/), [tradução](https:/friendsofvagrant.github.io/) e [meu github](https://github.com/search?q=username%3Arogeriopradoj+vagrant&repo&langOverride&start_value=1&type=Repositories&language)) faz um tempo, para diminuir o número de coisas instaladas no meu notebook, mas precisava atualizar a versão do PHP que tinha instalado por padrão no meu Mac OSX.

Participando do projeto do [iMasters](http://imasters.com.br/), [oPHPortunidades](https://github.com/iMastersDev/oportunidades) ([veja os hangouts](https://plus.google.com/+imasters/posts)), precisei rodar alguns comandos básicos no console, usando o excelente [Composer](http://getcomposer.org/), mas por não ter a última versão do PHP ficava difícil acompanhar o pessoal. Principalmente pela funcionalidade do [servidor web embutido no PHP 5.4](http://php.net/manual/pt_BR/features.commandline.webserver.php), que economiza bastante tempo para não precisar de configurar um Apache apenas para teste de uma aplicação.

É fato que usando o Vagrant poderíamos deixar preparado algumas receitas básicas, Puppet ou Chef, para deixar subir uma máquina com a última versão do PHP, mas a possibilidade de abrir um terminal em um diretório com um projeto mínimo rodando apenas um `php -S localhost:8080` em vez de um `vagrant init`, `subl Vagrantfile`, `vagrant up`, `vagrant ssh` etc etc era interessante.

Foi nesse momento que fui procurar uma opção de atualizar a minha versão global do PHP, do 5.3.15 que é a que vem instalada no Mac OS X Mountain Lion, para a versão mais nova estável, [5.4.8 quando esse artigo foi escrito](http://www.php.net/archive/2012.php#id2012-10-18-1). Quando comecei a usar o Mac, em agosto 2011, procurei uma solução parecida com a que usava no Windows, o [XAMPP](http://www.apachefriends.org/en/xampp.html), e tinha encontrado o MAMP e o próprio XAMPP (que eu tinha usado no meu tempo de Ubuntu também também tem versão Mac). Mas não queria mais utilizar uma opção desse tipo. Queria ter a última versão realmente instalada e acessível a partir da linha de comando.

O primeiro lugar onde fui olhar foi o [manual do PHP](http://www.php.net/manual/en/install.macosx.php), que agora está um pouco mais atualizado, mas até quando eu vi (setembro 2012) só tinha uma sugestão: compile o PHP usando as instruções para UNIX. Escolhi não usar essa opção.

Um tempo atrás o [Fábio Ribeiro](https://twitter.com/fabiorphp) perguntou no Twitter [como o pessoal estava montando o ambiente](https://twitter.com/fabiorphp/status/251123983917916160) PHP no OSX, e na época ele recebeu a indicação do [Homebrew](https://github.com/josegonzalez/homebrew-php). Essa seria uma opção interessante.

Enquanto estava ajudando na [tradução](https://github.com/klaussilveira/php-the-right-way) do [PHP The Right Way](http://www.phptherightway.com/), o [PHP Do Jeito Certo](http://br.phptherightway.com/), verifiquei que já existia uma pacote binário da versão mais nova do PHP 5.4, a [http://php-osx.liip.ch/](http://php-osx.liip.ch/), que era até a versão recomendada pelos criadores do site. Mais uma boa opção para escolher.

Enfim, fui procurar um maior embasamento para minha escolha final: [perguntar no Facebook](https://www.facebook.com/groups/14811750159/permalink/10152291066765160/?comment_id=10152293549380160&offset=0&total_comments=24), no grupo [PHP Brasil](https://www.facebook.com/groups/14811750159/). Lá vários caras que entendem do assunto deram suas opiniões e o mais legal: me deixaram com mais dúvidas ainda!!! Isso porque surgiram mais umas opções lá ainda não conhecia: o [php-build](http://chh.github.com/php-build/) e o [phpenv](https://github.com/CHH/phpenv).

O php-build é um cara para compilar o php automaticamente a partir do repositório oficial do PHP, e o phpenv é uma ferramenta para definir qual versão do PHP você irá utilizar no caso de você ter instalado várias opções paralelamente. No fim, foi essas duas opções juntas que escolhi usar e vou mostrar aqui como fiz:



	
  1. Instalar o `wget`, usando o [homebrew](http://mxcl.github.com/homebrew/) (ele é usado pelo `php-build`, mas você pode escolher outra forma de instalar o `wget`)

	
  2. Executar o `brew install pkg-config curl freetype gettext jpeg libpng mcrypt zlib re2c tidy openssl pcre libxslt xmlrpc-c regex-opt exif json-c gd libiconv base64 icu4c lemon gmp t1utils mhash expat,` usando o [homebrew](http://mxcl.github.com/homebrew/) (pelo menos na versão do PHP 5.4.8 pelo `php-build` ele pediu algumas dependências, depois que instalei esses pacotes o problema parou de acontecer aqui)

	
  3. Instalar o `php-build` (usando a instalação padrão com o git, [http://chh.github.com/php-build/](http://chh.github.com/php-build/))

	
  4. Instalar o `phpenv` (seguir o caminho que foi feito para instalar o [php-build](http://chh.github.com/php-build/), depois na pasta `bin`, executar o `phpenv-install.sh`)

	
  5. Atualizar o seu PATH seguindo as orientações da saída do comando `phpenv`

	
  6. Instalar a versão que você quer do PHP, seguindo a instrução daqui: [https://github.com/CHH/phpenv#description](https://github.com/CHH/phpenv#description)

	
  7. Rodar o `phpenv rehash`, o `phpenv global` com a versão escolhida e pronto!


Se você executar um `php -v` antes de fazer todos os comandos, você deve ver a sua versão do PHP como 5.3.15. Depois dos comandos acima, se executar um `php -v` deve ver a versão do PHP mais nova que você instalou (no meu caso ficou o PHP 5.4.8).

É isso aí pessoal, quem ficar com dúvidas pode perguntar nos comentários.

Até a próxima.

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com).
