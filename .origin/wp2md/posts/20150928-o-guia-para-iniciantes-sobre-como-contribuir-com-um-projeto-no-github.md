title: O guia para iniciantes sobre como contribuir com um projeto no GitHub
link: http://rogeriopradoj.com/2015/09/28/o-guia-para-iniciantes-sobre-como-contribuir-com-um-projeto-no-github/
author: rogeriopradoj
description: 
post_id: 632
created: 2015/09/28 18:39:18
created_gmt: 2015/09/28 21:39:18
comment_status: open
post_name: o-guia-para-iniciantes-sobre-como-contribuir-com-um-projeto-no-github
status: publish
post_type: post

# O guia para iniciantes sobre como contribuir com um projeto no GitHub

Eu já estou há alguns meses tentando escrever um guia com dicas sobre como contribuir com open source [nesse meu gist](https://gist.github.com/rogeriopradoj/9c2208b50bcb1f047d19), mas até agora não consegui terminar... Quem sabe daqui um tempo tenhamos essas _Dicas de como contribuir com open source by [@rogeriopradoj](https://github.com/rogeriopradoj) ;-)._ No entanto, em 24/09/2015 o Rob Allen, mais conhecido no Twitter como [@akrabat](https://twitter.com/akrabat), escreveu um artigo sobre o tema: [The beginner's guide to contributing to a GitHub project](http://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/). Conversei com ele para pedir a autorização para traduzir seu texto em português do Brasil aqui no [RogerioPradoJ.com](), e a resposta foi positiva! 

> [@rogeriopradoj](https://twitter.com/rogeriopradoj) Sure
> 
> — Rob Allen (@akrabat) [September 25, 2015](https://twitter.com/akrabat/status/647290027026837504)

Então vamos lá: 

* * *

Este é um guia sobre como contribuir como um projeto open source que utiliza o GitHub. Ele é baseado principalmente no que acompanhei sobre a forma como operam o [Zend Framework](http://framework.zend.com/), o [Slim Framework](http://www.slimframework.com/) e o [joind.in](https://joind.in/). No entanto, esse é um guia genérico, sendo assim, leia o README de seus projetos para ver o que for específico. 

## TL;DR

Vá direto para o resumo. 

## Passo 1: Defina uma cópia de trabalho (working copy) no seu computador

Primeiramente, você precisa de um fork local do projeto na sua máquina, vá direto no GitHub e aperte o botão "fork". Ele criará uma cópia do repositório em sua própria conta do GitHub e você verá um aviso de que ele foi forkado abaixo do nome do projeto: ![Forked](/wp-content/uploads/2015/09/2015-09forked.png) Agora, você precisa de uma cópia local. Procure por "HTTPS clone URL" ou "SSH clone URL" do lado direito do site e use esse endereço para fazer o clone local usando um terminal: 
    
    
    $ git clone git@github.com:akrabat/zend-validator.git

O resultado será parecido com esse aqui: ![Clone](/wp-content/uploads/2015/09/2015-09clone.png) Entre no diretório do novo projeto: 
    
    
    $ cd zend-validator

Por fim, você precisa definir um novo remoto (_remote_) apontando para o projeto original. Dessa forma, você consegue trazer as mudanças e colocá-las dentro de sua cópia local. Acesse o link do repositório original - ele está marcado com "Forked from" no topo da página do GitHub. Isso vai te levar para a página principal do GitHub do projeto, onde você encontra a "HTTPS clone URL" ou a "SSH clone URL" e deve usá-la para criar o novo remoto, que chamaremos de _upstream_. 
    
    
    $ git remote add upstream git@github.com:zendframework/zend-validator.git

Agora você tem dois remotos para esse projeto no disco: 

  1. o_ origin_ que aponta para seu fork do projeto no GitHub. Você tem acesso de leitura e gravação nesse remoto
  2. o_ upstream_ que aponta para o repositório principal do projeto no GitHub. Você só tem acesso de leitura nesse remoto.

## Passo 2: Faça suas modificações

Essa é a parte divertida onde você começa a contribuir com o projeto. Em geral, é melhor começar arrumando um problema que está te atrapalhando ou algum bug que você encontrou no issue tracker do projeto. Se estiver procurando um lugar para começar, vários projetos usam a marcação ["easy pick" label](http://seld.be/notes/encouraging-contributions-with-the-easy-pick-label) (ou alguma variação) para indicar que a issue pode ser resolvida por alguém novo no projeto. 

### Branch!

**A regra número um é colocar cada pedaço do seu trabalho em seu próprio branch**. Se o projeto estiver usando o [git-flow](http://nvie.com/posts/a-successful-git-branching-model/), ele terá tanto um branch _master_ quanto um branch _develop_. A regra padrão é que se você estiver consertando um bug, você criará um branch a partir do master, e se você estiver adicionando uma nova funcionalidade, criará um branch a partir do develop. Se o projeto tiver apenas o branch master, é de lá que você criará o branch novo. Alguns projetos, como o Slim, usam os nomes dos branches baseadas em um número de versão (2.x e 3.x na situação deles). Nesse caso, escolha o branch que for relevante. Neste exemplo, vamos supor que você está arrumando um bug no zend-validator, então vamos fazer um branch a partir do _master_: 
    
    
    $ git checkout master
    $ git pull upstream master && git push origin master
    $ git checkout -b hotfix/readme-update

Primeiramente, vamos garantir que estamos no branch master. Dessa forma o comando `git pull` irá sincronizar nossa cópia local com o projeto upstream e  o `git push` irá sincronizá-lo com nosso projeto forkado no GitHub. Por fim criamos nosso novo branch. Você pode nomear o branch como quiser, mas ajuda se o nome for significativo. Incluir o número da issue também é útil. Se o projeto usar o git-flow tal qual o zend-validator, existem convenções de nomenclatura para prefixar os branches com "hotfix/" ou "feature/". Agora você pode fazer suas alterações. Tenha certeza que você apenas arrume o código onde que estiver trabalhando. Não ceda à tentação de arrumar outras coisas que for achando durante suas alterações pois assim seu PR (Pull Request) provavelmente será rejeitado. Certifique-se que você faça commits em blocos lógicos. Cada uma das mensagens de commit deve ser sensata. Leia o artigo do Tim Pope [A Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) (ou, se preferir em português do Brasil, [desde 2011 em RogerioPradoJ.com: Uma Nota Sobre as Mensagens do Git Commit](/2011/11/29/uma-nota-sobre-as-mensagens-do-git-commit/)). 

## Passo 3: Crie o PR (Pull Request)

Para criar um PR, você precisa fazer o push de seu branch para o remoto _origin_ e depois apertar alguns botões no GitHub. Para fazer o push de um branch novo: 
    
    
    $ git push -u origin hotfix/readme-update

O comando cria um branch em seu projeto no GitHub. A flag `-u` faz a amarração desse branch com seu remoto, assim, no futuro, você pode simplesmente digitar `git push origin`. Volte ao navegador e acesse o fork do seu projeto (https://github.com/akrabat/zend-validator no meu caso) e você verá que seu novo branch está listado no topo com um conveniente botão "Compare & pull request": ![Pr button](/wp-content/uploads/2015/09/2015-09pr-button.png) Vá em frente e aperte o botão! Se você vir uma caixa amarela como essa: ![Contributing](http://rogeriopradoj.com/wp-content/uploads/2015/09/2015-09contributing.png) Clique no link que te levará ao arquivo CONTRIBUTING do projeto e o leia! Ele contém informação valiosa sobre como trabalhar com a base de código do projeto e ajudará para que sua contribuição seja aceita.

## Comments

**[Gildásio Júnior](#1639 "2015-10-05 15:36:00"):** Show, cara! Parabéns pela tradução e ao criador, por ter feito o guia! Nesse link [1] tem um post bacana (hahah será?!?) sobre isso. O "legal" desse link é que mostra outras formas de contribuir, para quem quer, mas acredita não ter skills suficiente para botar mão no código. [1] - https://gjuniioor.wordpress.com/2015/07/30/contribuindo-para-projetos-abertos-no-github/

**[Rogerio Prado de Jesus](#1640 "2015-10-08 00:54:00"):** Valeu, @gildasiojunior:disqus pelo link! É isso aí, acredito que quanto mais a pessoa conhece o processo e as ferramentas mais seguro vai ficar para começar a contribuir! Seu post é uma boa fonte de conhecimento!

