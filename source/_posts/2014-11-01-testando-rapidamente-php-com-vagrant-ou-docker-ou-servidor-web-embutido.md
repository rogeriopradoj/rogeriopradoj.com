---
date: 2014-11-01 01:57:47+00:00
title: Testando rapidamente projetos PHP, ou com Vagrant, ou com Docker ou com Servidor Web embutido
categories:
  - Geral
---

Olá, pessoal!

Dica rápida para quem quiser testar algum projeto PHP usando o Vagrant, ou o Docker, ou o Servidor Web embutido no PHP.

## Vagrant

Já conhece o [https://phpagrant.github.io/](https://phpagrant.github.io/) ? Nada mais é do que uma lista de sites geradores de Vagrantfile (e tudo o mais que você precisa de provisionadores) para seu projeto PHP com base no [Vagrant](https://www.vagrantup.com/).

[![Phpagrant_github_io_by_PHPagrant](assets/images/2014/11/Phpagrant_github_io_by_PHPagrant.png)](https://phpagrant.github.io/)

Tem para todos os gostos: Puppet, Chef, Ansible. Você escolhe! Acesse lá, [https://phpagrant.github.io/](https://phpagrant.github.io/)!

## Docker

O novo "queridinho" do mundo da virtualização e conteinerização, o [Docker](https://www.docker.com/), está evoluindo rápido e é importante você correr atrás do prejuízo e aprender sobre ele.

![Docker_-_Build__Ship__and_Run_Any_App__Anywhere](assets/images/2014/11/Docker_-_Build__Ship__and_Run_Any_App__Anywhere.png)

Até a versão 1.2.x tinha um sério problema para os usuários de sistemas não Linux: o [Boot2Docker](http://boot2docker.io/), camada VM para permitir que usuários de OS X e Windows usem o Docker, não permitia usar pastas compartilhadas por padrão. Alguns hacks foram lançados ([como o ótimo artigo do Chris Jones](http://viget.com/extend/how-to-use-docker-on-os-x-the-missing-guide)) , mas depois do [lançamento da versão 1.3.0](https://blog.docker.com/2014/10/docker-1-3-signed-images-process-injection-security-options-mac-shared-directories/), tudo ficou mais fácil: foi embutido suporte para pastas compartilhadas e está mais simples para quem não usa Linux como máquina principal de desenvolvimento ter o Docker como parte do seu processo de trabalho.

Mas e sobre o PHP? Vamos lá! Algumas imagens disponíveis no [https://registry.hub.docker.com/](https://registry.hub.docker.com/) para você se divertir:

  - **oficial**: [https://registry.hub.docker.com/_/php/](https://registry.hub.docker.com/_/php/) (falta FPM, mas já tem CLI e Apache com mod_php)

  - [@brunoric](https://github.com/brunoric): [https://hub.docker.com/u/brunoric/](https://hub.docker.com/u/brunoric/) (brasileiro, aqui de São Paulo, especialista no Docker. Tem uma série de imagens PHP, vários sabores, até HHVM)

Além disso, seguindo a issue [https://github.com/codeguy/php-the-right-way/pull/453](https://github.com/codeguy/php-the-right-way/pull/453), dá para ver que em pouco tempo o [PHP: The Right Way](http://www.phptherightway.com/) (e o [PHP: Do Jeito Certo](http://br.phptherightway.com)) terá conteúdo sobre Docker e PHP (hoje eles já tem conteúdo sobre Vagrant).

Para quem quer ir direto colocar a mão na massa, o que estou fazendo:

  - Primeiro [instalei o Docker](http://docs.docker.com/installation/) (e, como estou num OS X, o Boot2Docker também. Comando para garantir que ele está ligado: `boot2docker up`)

  - [OS X apenas:] coloquei no meu '/etc/hosts' o hostname 'localdocker' apontando para o IP 192.168.59.103 (esse ip é o que comando `boot2docker ip` mostra). Isso só é necessário para quem usa boot2docker, pois o Docker de verdade está rodando dentro de uma VM, com esse IP aí de cima. Quem está rodando no Windows deve ser algo parecido. Quem está rodando no Linux, não tem que se preocupar com isso, pois o Docker está usando o IP da sua máquina de verdade.

  - Vou na pasta que seria o document root da minha aplicação (onde tem o front controller, geralmente index.php) . Como estou no OS X, essa pasta tem que estar dentro de /Users para usar o compartilhamento de pasta automático do boot2docker 1.3+. Ex:

    ```
    $ cd /Users/eu/projetos/php123/
    ```

  - De lá, rodo o seguinte comando:

    ```bash
    $ docker run --name my-php-webserver -p 8080:80 -v `pwd`:/var/www/html/ php:apache
    ```


  - Agora, é só abrir no seu navegador para testar: no linux, [http://localhost:8080](http://localhost:8080). No OS X, com boot2docker (se você fez aquela configuração no /etc/hosts), [http://localdocker:8080](http://localdocker:8080).


O que aconteceu por trás do comando DOCKER RUN:

  - cria e já executa um container, baseado na imagem php versão apache

  - habilita o volume/disco internamente (dentro do container) como /var/www/html/ e externamente (na máquina host/vm boot2docker) como o resultado comando `pwd` (diretório atual)

  - redireciona a porta 80 interna (no container) para a porta 8080 externa (na máquina host)

É isso!

Quando precisar desligar o container, fazer os seguintes comandos:

  - `$ docker ps -a `(e copiar o CONTAINER ID)

  - `$ docker rm CONTAINER_ID_QUE_VOCÊ_ACHOU_NO_COMANDO_ANTERIOR`

## Servidor embutido

Vai ter momentos que você não quer ou não pode ir para um dos modelos acima, Vagrant ou Docker. E nem quer instalar um servidor web completo (Apache, Nginx etc.) na sua máquina de desenvolvimento. O que fazer?

Se você tem o PHP CLI já instalado, é bom saber que desde a versão 5.4 é possível usar o servidor web embutido. [Leia mais na documentação oficial](http://php.net/manual/pt_BR/features.commandline.webserver.php).

![PHP__Built-in_web_server_-_Manual](assets/images/2014/11/PHP__Built-in_web_server_-_Manual.png)

Então, na pasta onde seria o document root da sua aplicação PHP (onde tem o front controller, certo?), digite o seguinte comando:

```
$ php -S localhost:8899
```

A porta ali, no caso 8899, poderia ser qualquer uma de sua preferência. E você já tem um servidor web rodando servindo seu código PHP, no seu navegador disponível em [http://localhost:8899.](http://localhost:8899) Fácil, não? Você ainda pode configurar algo como um `.htaccess`, a [Lorna Jane Mitchell tem um artigo de 2012 falando do assunto](http://www.lornajane.net/posts/2012/php-5-4-built-in-webserver). Mas, de novo, leia a [doc oficial](http://php.net/manual/pt_BR/features.commandline.webserver.php) que você tem muita informação lá.

## Considerações finais

Hoje você não é mais obrigado a instalar um servidor web como o Apache ou o Nginx apenas para testar uma aplicação PHP básica. O Servidor web embutido, desde o PHP 5.4 (março de 2012), fornece a estrutura básica para que, em desenvolvimento, você tenha um servidor mínimo.

Caso você precise espelhar o servidor de produção (hardware, sistema operacional e softwares utilizados), vá para o Vagrant, que te entrega isso de forma fácil com a virtualização, tanto para projetos genéricos quanto para projetos PHP.

E, se quiser estar na crista do onda, aplicando conteinerização também no ambiente de desenvolvimento, teste o Docker com PHP.

E fique a vontade de usar os comentários se quiser ajuda!

Até mais!

—-

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com/).
