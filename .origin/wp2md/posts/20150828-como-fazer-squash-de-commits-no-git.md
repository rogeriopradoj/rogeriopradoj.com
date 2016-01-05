title: Como Fazer Squash de Commits no Git
link: http://rogeriopradoj.com/2015/08/28/como-fazer-squash-de-commits-no-git/
author: rogeriopradoj
description: 
post_id: 622
created: 2015/08/28 00:42:41
created_gmt: 2015/08/28 03:42:41
comment_status: open
post_name: como-fazer-squash-de-commits-no-git
status: publish
post_type: post

# Como Fazer Squash de Commits no Git

Tradução livre de Squash Commits with Git, disponível em <http://davidwalsh.name/squash-commits-git/>. \-- Não sou um expert de git, mas sei o suficiente para me virar bem, e com certeza sei o suficiente sobre git para gostar mais dele do que do svn. Um tempo atrás publiquei sobre alguns [comandos básicos de git](http://davidwalsh.name/git-commands), ensinando como ir além do básico dos clones e commits, passando pela maioria das interações que o git fornece. A mini-lição de hoje envolve fazer o squash de múltiplos commits em um só, facilitando a revisão de pull requests e ajudando com a gestão de merges. Comece fazendo alterações no feature branch onde você vai trabalhar. Vamos supor que essas alterações são alguns commits que eu quero consolidar num único. O primeiro passo consiste em garantir que o branch master está sincronizado com o branch master do repositório destino: 
    
    
    # entre no branch master
    git checkout master
    
    # garanta que seu repositório está atualizado
    git pull nomeRepositorioRemoto master
    

Com o branch master sincronizado, usamos o git rebase para fazer a consolidação: 
    
    
    git rebase -i master
    

Esse comando mostra uma lista de commits, dessa forma: 
    
    
    pick fb554f5 This is commit 1
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
    

Edite o sumário mostrado pelo comando rebase, deixando o commit que você quer deixar principal como "pick", e alterando todos os comandos "pick" subsequentes por "squash": 
    
    
    pick fb554f5 This is commit 1
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
    

Salve o conteúdo e feche o editor duas vezes (a segunda tela permite que você altere a mensagem de commit, apesar de eu preferir manter sempre a mesma mensagem). Nesse momento, seus commits serão aglutinados em um só: é o squash! Execute o seguinte comando para forçar o push desse commit novo e consolidado. 
    
    
    # Force um push
    git push -f
    

Esse push forçado atualiza o repositório fonte, e nossos commits são transformados em um só. Se você já tinha mandado um pull request no GitHub com esse conteúdo, agora o PR vai aparecer como um único commit! E, com um commit consolidado, a revisão do código se torna muito, mas muito, mais fácil! \-- É isso aí, pessoal, até mais!

## Comments

**[Dan Jesus](#1632 "2015-08-28 01:58:00"):** Boa dica Rogério! Eu costumo até pra sincronizar o master local usar o rebase também, normalmente faço um git fetch origin e uso um git rebase origin/master. É claro que também daria para fazer um pull com a flag de rebase git pull --rebase master. Excelente artigo continue escrevendo sempre amigo. Abraço!

**[Rogerio Prado de Jesus](#1633 "2015-08-28 10:34:00"):** Valeu, @danjesus:disqus por compartilhar a experiência. Só lembrar que este artigo é uma tradução livre do http://davidwalsh.name/squash-commits-git/. Abraço!

**[Dan Jesus](#1634 "2015-08-28 11:01:00"):** Opa Rogério nem tinha visto hehehe, já tinha comentado quando eu vi. Abraco!

**[Rogerio Prado de Jesus](#1635 "2015-09-01 09:38:00"):** ;-)

