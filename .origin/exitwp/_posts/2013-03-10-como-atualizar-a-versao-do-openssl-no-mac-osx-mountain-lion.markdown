---
author: rogeriopradoj
comments: true
date: 2013-03-10 23:38:12+00:00
layout: post
slug: como-atualizar-a-versao-do-openssl-no-mac-osx-mountain-lion
title: Como atualizar a versão do Openssl no Mac OSX Mountain Lion
wordpress_id: 362
categories:
- Mac
tags:
- como
- como atualizar
- homebrew
- mac
- openssl
- osx
- php
- terminal
---

Olá, pessoal,

Vou mostrar aqui como fiz para atualizar a versão do Openssl no meu Mac OSX Mountain Lion.

O Openssl atualizado é uma das dependências para [compilar o PHP com a extensão Openssl](http://www.php.net/manual/en/openssl.requirements.php).

Esse artigo ainda está relacionado com a [atualização do PHP na minha máquina](http://rogeriopradoj.com/2012/11/20/como-atualizar-a-versao-do-php-no-mac-osx-mountain-lion/) usando o [php-build](http://chh.github.com/php-build/) e o [phpenv](https://github.com/chh/phpenv) do [CHH](https://github.com/CHH).

Então vamos lá, e só para não esquecer, este artigo foi baseado [nessa resposta do stack overflow](http://stackoverflow.com/a/15234017/1330750) e [nesse outro artigo aqui](http://foodpicky.com/?p=99).

---

Para começar, abra seu terminal para verificar qual a versão do Openssl que você tem instalada:

`$ openssl version`

Aqui, aparecia a versão **OpenSSL 0.9.8r 8 Feb 2011**.

No momento da escrita, março de 2013, a última versão disponível no [site oficial](http://www.openssl.org/) era a **openssl 1.0.1e**, vamos então atualizar o nosso sistema.

No início, tentei utilizar a versão disponibilizada pelo [Homebrew](http://mxcl.github.com/homebrew/), mas, mesmo após usar o `brew install openssl` e o `brew link openssl --force` (comandos que instalariam o Openssl e depois o registrariam como o Openssl padrão do sistema), a versão disponível no meu terminal continuava desatualizada.

Foi aí que decidi compilar eu mesmo a versão mais nova, fazendo o seguinte:



	
  * descobrir se o seu sistema operacional é _64bit_ ou _32bit_, você vai precisar dessa informação mais à frente. Para isso, executar: `$ uname -m`. Se aparecer **x86_64** seu computador é _64bit_, se aparecer **i386** ele é _32bit_ (estou supondo que o processador do seu Mac seja Intel, e não seja PowerPC. Ele já é Intel, certo? Se não for, melhor parar por aqui...)

	
  * baixar o fonte do Openssl, última versão, no site  [http://www.openssl.org/source/](http://www.openssl.org/source/) (geralmente é o primeiro link dessa página, marcado em vermelho como [LATEST]), no meu caso foi o **openssl-1.0.1e.tar.gz**

	
  * entrar pelo seu terminal onde você baixou o arquivo (padrão no Mac e na pasta Downloads dentro da sua pasta de usuário, exemplo: `$ cd ~/Downloads`

	
  * descompactar o arquivo **openssl-1.0.1e.tar.gz**, exemplo: `$ tar -zxvf openssl-1.0.1e.tar.gz`

	
  * entrar na pasta que acabou de ser criada com a descompactação, exemplo: `$ cd openssl-1.0.1e`

	
  * Configurar o fonte, exemplo para _64bit_: `$ ./Configure darwin64-x86_64-cc --prefix=/usr no-threads shared`. Exemplo para _32bit_: `$ ./Configure darwin-i386-cc --prefix=/usr no-threads shared`

	
  * Rodar o **make**, tente primeiro sem usar o _sudo_, e, apenas se der erro, rode com o _sudo_. Exemplo: `$ make`. Apenas se tiver dado algum erro de permissão: `$ sudo make`

	
  * Rodar o **make install**, mesma orientação acima. Exemplo: `$ make install`. Se tiver dado algum erro de permissão: `$ sudo make install.`

	
  * Feche o terminal.


Pronto, agora você já deve ter instalada a última versão do Openssl, baixada diretamente do site oficial e compilada para o seu sistema.

Para confirmar que deu tudo certo, execute:

`$ openssl version`

Aqui para mim apareceu **OpenSSL 1.0.1e 11 Feb 2013**, e para você?

Deixe seus apontamentos aí nos comentários, ou entre em contato, ok?

Até mais!

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com).
