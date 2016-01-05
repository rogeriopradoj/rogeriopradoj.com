---
author: rogeriopradoj
comments: true
date: 2015-09-28 21:39:18+00:00
layout: post
slug: o-guia-para-iniciantes-sobre-como-contribuir-com-um-projeto-no-github
title: O guia para iniciantes sobre como contribuir com um projeto no GitHub
wordpress_id: 632
categories:
- Geral
- Versionamento
tags:
- git
- github
- open source
- opensource
---

Eu já estou há alguns meses tentando escrever um guia com dicas sobre como contribuir com open source [nesse meu gist](https://gist.github.com/rogeriopradoj/9c2208b50bcb1f047d19), mas até agora não consegui terminar... Quem sabe daqui um tempo tenhamos essas _Dicas de como contribuir com open source by [@rogeriopradoj](https://github.com/rogeriopradoj) ;-)._

No entanto, em 24/09/2015 o Rob Allen, mais conhecido no Twitter como [@akrabat](https://twitter.com/akrabat), escreveu um artigo sobre o tema: [The beginner's guide to contributing to a GitHub project](http://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/). Conversei com ele para pedir a autorização para traduzir seu texto em português do Brasil aqui no [RogerioPradoJ.com](http://rogeriopradoj.com), e a resposta foi positiva!



<blockquote>

> 
> [@rogeriopradoj](https://twitter.com/rogeriopradoj) Sure
> 
> 
— Rob Allen (@akrabat) [September 25, 2015](https://twitter.com/akrabat/status/647290027026837504)</blockquote>





Então vamos lá:



* * *



Este é um guia sobre como contribuir como um projeto open source que utiliza o GitHub. Ele é baseado principalmente no que acompanhei sobre a forma como operam o [Zend Framework](http://framework.zend.com/), o [Slim Framework](http://www.slimframework.com/) e o [joind.in](https://joind.in/). No entanto, esse é um guia genérico, sendo assim, leia o README de seus projetos para ver o que for específico.



## TL;DR



Vá direto para o resumo.



## Passo 1: Defina uma cópia de trabalho (working copy) no seu computador



Primeiramente, você precisa de um fork local do projeto na sua máquina, vá direto no GitHub e aperte o botão "fork". Ele criará uma cópia do repositório em sua própria conta do GitHub e você verá um aviso de que ele foi forkado abaixo do nome do projeto:

![Forked](http://rogeriopradoj.com/wp-content/uploads/2015/09/2015-09forked.png)

Agora, você precisa de uma cópia local. Procure por "HTTPS clone URL" ou "SSH clone URL" do lado direito do site e use esse endereço para fazer o clone local usando um terminal:


    
    $ git clone git@github.com:akrabat/zend-validator.git



O resultado será parecido com esse aqui:

![Clone](http://rogeriopradoj.com/wp-content/uploads/2015/09/2015-09clone.png)

Entre no diretório do novo projeto:


    
    $ cd zend-validator



Por fim, você precisa definir um novo remoto (_remote_) apontando para o projeto original. Dessa forma, você consegue trazer as mudanças e colocá-las dentro de sua cópia local. Acesse o link do repositório original - ele está marcado com "Forked from" no topo da página do GitHub. Isso vai te levar para a página principal do GitHub do projeto, onde você encontra a "HTTPS clone URL" ou a "SSH clone URL" e deve usá-la para criar o novo remoto, que chamaremos de _upstream_.


    
    $ git remote add upstream git@github.com:zendframework/zend-validator.git



Agora você tem dois remotos para esse projeto no disco:




    
  1. o_ origin_ que aponta para seu fork do projeto no GitHub. Você tem acesso de leitura e gravação nesse remoto

    
  2. o_ upstream_ que aponta para o repositório principal do projeto no GitHub. Você só tem acesso de leitura nesse remoto.





## Passo 2: Faça suas modificações



Essa é a parte divertida onde você começa a contribuir com o projeto. Em geral, é melhor começar arrumando um problema que está te atrapalhando ou algum bug que você encontrou no issue tracker do projeto. Se estiver procurando um lugar para começar, vários projetos usam a marcação ["easy pick" label](http://seld.be/notes/encouraging-contributions-with-the-easy-pick-label) (ou alguma variação) para indicar que a issue pode ser resolvida por alguém novo no projeto.



### Branch!



**A regra número um é colocar cada pedaço do seu trabalho em seu próprio branch**. Se o projeto estiver usando o [git-flow](http://nvie.com/posts/a-successful-git-branching-model/), ele terá tanto um branch _master_ quanto um branch _develop_. A regra padrão é que se você estiver consertando um bug, você criará um branch a partir do master, e se você estiver adicionando uma nova funcionalidade, criará um branch a partir do develop. Se o projeto tiver apenas o branch master, é de lá que você criará o branch novo. Alguns projetos, como o Slim, usam os nomes dos branches baseadas em um número de versão (2.x e 3.x na situação deles). Nesse caso, escolha o branch que for relevante.

Neste exemplo, vamos supor que você está arrumando um bug no zend-validator, então vamos fazer um branch a partir do _master_:


    
    $ git checkout master
    $ git pull upstream master && git push origin master
    $ git checkout -b hotfix/readme-update



Primeiramente, vamos garantir que estamos no branch master. Dessa forma o comando `git pull` irá sincronizar nossa cópia local com o projeto upstream e  o `git push` irá sincronizá-lo com nosso projeto forkado no GitHub. Por fim criamos nosso novo branch. Você pode nomear o branch como quiser, mas ajuda se o nome for significativo. Incluir o número da issue também é útil. Se o projeto usar o git-flow tal qual o zend-validator, existem convenções de nomenclatura para prefixar os branches com "hotfix/" ou "feature/".

Agora você pode fazer suas alterações.

Tenha certeza que você apenas arrume o código onde que estiver trabalhando. Não ceda à tentação de arrumar outras coisas que for achando durante suas alterações pois assim seu PR (Pull Request) provavelmente será rejeitado. Certifique-se que você faça commits em blocos lógicos. Cada uma das mensagens de commit deve ser sensata. Leia o artigo do Tim Pope [A Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) (ou, se preferir em português do Brasil, [desde 2011 em RogerioPradoJ.com: Uma Nota Sobre as Mensagens do Git Commit](http://rogeriopradoj.com/2011/11/29/uma-nota-sobre-as-mensagens-do-git-commit/)).



## Passo 3: Crie o PR (Pull Request)



Para criar um PR, você precisa fazer o push de seu branch para o remoto _origin_ e depois apertar alguns botões no GitHub.

Para fazer o push de um branch novo:


    
    $ git push -u origin hotfix/readme-update



O comando cria um branch em seu projeto no GitHub. A flag `-u` faz a amarração desse branch com seu remoto, assim, no futuro, você pode simplesmente digitar `git push origin`.

Volte ao navegador e acesse o fork do seu projeto (https://github.com/akrabat/zend-validator no meu caso) e você verá que seu novo branch está listado no topo com um conveniente botão "Compare & pull request":

![Pr button](http://rogeriopradoj.com/wp-content/uploads/2015/09/2015-09pr-button.png)

Vá em frente e aperte o botão!

Se você vir uma caixa amarela como essa:

![Contributing](http://rogeriopradoj.com/wp-content/uploads/2015/09/2015-09contributing.png)

Clique no link que te levará ao arquivo CONTRIBUTING do projeto e o leia! Ele contém informação valiosa sobre como trabalhar com a base de código do projeto e ajudará para que sua contribuição seja aceita.

Na página a seguir assegure que o "base fork" aponta para o repositório e para o branch correto. Então certifique-se de fornecer um título bom e sucinto para seu pull request e explique porque você o criou na caixa de descrição. Adicione todos os números de issue caso os tenha.

![Create pr](http://rogeriopradoj.com/wp-content/uploads/2015/09/2015-09create-pr.png)

Se você rolar a tela um pouco, verá um diff das suas alterações. **Verifique mais de uma vez se ele contém o que era esperado**.

Quando estiver satisfeito, aperte o botão "Create pull request" e você terá terminado.



## Passo 4: Revisão dos mantenedores



Para que seu trabalho seja integrado no projeto, os mantenedores fazem a revisão do seu que você fez e então ou solicitam alterações ou fazem o merge.

O artigo da Lorna Mitchell [Code Reviews: Before You Even Run The Code](http://www.lornajane.net/posts/2015/code-reviews-before-you-even-run-the-code) trata sobre os pontos que os mantenedores se preocupam. Por isso, vá lá dar uma lida e assegure que você facilitou as coisas para os mantenedores o máximo possível.



## Resumindo



Isso é tudo! As partes fundamentais são as seguintes:




    
  1. Faça o fork do projeto & o clone local.

    
  2. Crie um remoto _upstream_ e sincronize com sua cópia local antes de criar o branch.

    
  3. Faça um branch para cada pedaço separado de trabalho.

    
  4. Faça as alterações, escreva [boas mensagens de commit](https://blogs.gnome.org/danni/2011/10/25/a-guide-to-writing-git-commit-messages/) e leia o arquivo CONTRIBUTING quando ele existir

    
  5. Faça o push para seu repositório _origin_.

    
  6. Crie em novo PR (Pull Request) no GitHub.

    
  7. Responda a todos os feedbacks recebidos durante a [revisão do código](http://www.lornajane.net/posts/2015/code-reviews-before-you-even-run-the-code).



Se você quiser contribuir com um projeto open source, considere o [joind.in](https://github.com/joindin/joindin-web2#joindin)!





—

É isso pessoal! Agradeço muito ao [Rob Allen](http://akrabat.com/) pelo [artigo original](http://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/) e autorização para tradução aqui no [RogerioPradoJ.com](http://rogeriopradoj.com).

Para quem quiser mais ideias de projetos opensource para contribuir, deêm uma olhada no [#30contribs](http://rogeriopradoj.com/2015/06/24/30contribs-cheguei-nos-30-e-quero-de-presente-pull-requests-e-contribuicoes-para-projetos-open-source-e-da-comunidade/) e também no [@yourfirstpr](https://twitter.com/yourfirstpr), que te ajudam a começar a contribuir.

O mais legal vai ser daqui a pouco você ter tantas contribuições que nem vai lembrar de quando foi sua primeira vez. Para te ajudar a recordar, você pode usar o http://firstpr.me/!

[caption id="attachment_638" align="aligncenter" width="509"][![firstpr-rogeriopradoj](http://rogeriopradoj.com/wp-content/uploads/2015/09/First-Pull-Request-•-What-was-the-first-pull-request-you-sent-on-GitHub.png)](http://firstpr.me/#rogeriopradoj) [http://firstpr.me/#rogeriopradoj](http://firstpr.me/#rogeriopradoj) em 28/09/2015[/caption]



Até mais!

—

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com/).


