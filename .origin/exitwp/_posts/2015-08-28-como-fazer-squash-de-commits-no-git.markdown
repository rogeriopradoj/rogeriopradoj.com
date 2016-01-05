---
author: rogeriopradoj
comments: true
date: 2015-08-28 03:42:41+00:00
layout: post
slug: como-fazer-squash-de-commits-no-git
title: Como Fazer Squash de Commits no Git
wordpress_id: 622
categories:
- Versionamento
tags:
- git
- squash
---

Tradução livre de Squash Commits with Git, disponível em [http://davidwalsh.name/squash-commits-git/](http://davidwalsh.name/squash-commits-git/).

--

Não sou um expert de git, mas sei o suficiente para me virar bem, e com certeza sei o suficiente sobre git para gostar mais dele do que do svn. Um tempo atrás publiquei sobre alguns [comandos básicos de git](http://davidwalsh.name/git-commands), ensinando como ir além do básico dos clones e commits, passando pela maioria das interações que o git fornece. A mini-lição de hoje envolve fazer o squash de múltiplos commits em um só, facilitando a revisão de pull requests e ajudando com a gestão de merges.

Comece fazendo alterações no feature branch onde você vai trabalhar. Vamos supor que essas alterações são alguns commits que eu quero consolidar num único. O primeiro passo consiste em garantir que o branch master está sincronizado com o branch master do repositório destino:


    
    <code class="shell"># entre no branch master
    git checkout master
    
    # garanta que seu repositório está atualizado
    git pull nomeRepositorioRemoto master
    </code>



Com o branch master sincronizado, usamos o git rebase para fazer a consolidação:


    
    <code class="shell">git rebase -i master
    </code>



Esse comando mostra uma lista de commits, dessa forma:


    
    <code class="shell">pick fb554f5 This is commit 1
    pick 2bd1903 This is commit 2
    pick d987ebf This is commit 3
    
    # Rebase 9cbc329..d987ebf onto 9cbc329
    #
    # Commands:
    # p, pick = use commit
    # r, reword = use commit, but edit the commit message
    # e, edit = use commit, but stop for amending
    # s, squash = use commit, but meld into previous commit
    # f, fixup = like "squash", but discard this commit's log message
    # x, exec = run command (the rest of the line) using shell
    #
    # If you remove a line here THAT COMMIT WILL BE LOST.
    # However, if you remove everything, the rebase will be aborted.
    #
    </code>



Edite o sumário mostrado pelo comando rebase, deixando o commit que você quer deixar principal como "pick", e alterando todos os comandos "pick" subsequentes por "squash":


    
    <code class="shell">pick fb554f5 This is commit 1
    squash 2bd1903 This is commit 2
    squash d987ebf This is commit 3
    
    # Rebase 9cbc329..d987ebf onto 9cbc329
    #
    # Commands:
    # p, pick = use commit
    # r, reword = use commit, but edit the commit message
    # e, edit = use commit, but stop for amending
    # s, squash = use commit, but meld into previous commit
    # f, fixup = like "squash", but discard this commit's log message
    # x, exec = run command (the rest of the line) using shell
    #
    # If you remove a line here THAT COMMIT WILL BE LOST.
    # However, if you remove everything, the rebase will be aborted.
    #
    </code>



Salve o conteúdo e feche o editor duas vezes (a segunda tela permite que você altere a mensagem de commit, apesar de eu preferir manter sempre a mesma mensagem). Nesse momento, seus commits serão aglutinados em um só: é o squash! Execute o seguinte comando para forçar o push desse commit novo e consolidado.


    
    <code class="shell"># Force um push
    git push -f
    </code>



Esse push forçado atualiza o repositório fonte, e nossos commits são transformados em um só. Se você já tinha mandado um pull request no GitHub com esse conteúdo, agora o PR vai aparecer como um único commit! E, com um commit consolidado, a revisão do código se torna muito, mas muito, mais fácil!

--

É isso aí, pessoal, até mais!
