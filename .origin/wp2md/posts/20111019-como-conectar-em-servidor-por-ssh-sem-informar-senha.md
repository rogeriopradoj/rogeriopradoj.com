title: Como conectar em servidor por SSH sem informar senha
link: http://rogeriopradoj.com/2011/10/19/como-conectar-em-servidor-por-ssh-sem-informar-senha/
author: rogeriopradoj
description: 
post_id: 62
created: 2011/10/19 01:37:07
created_gmt: 2011/10/19 04:37:07
comment_status: open
post_name: como-conectar-em-servidor-por-ssh-sem-informar-senha
status: publish
post_type: post

# Como conectar em servidor por SSH sem informar senha

Este post é para mostrar como conectar num host por ssh sem pedir senha, utilizando para isso a configuração do **.ssh/authorized_keys**. [caption id="" align="alignnone" width="307"]![SSH](http://www.throughput.biz/wp-content/uploads/2008/08/ssh.jpg) Fonte: http://www.throughput.biz[/caption] Primeiro você precisa localizar sua chave ssh pública no seu guest (seu computador que irá acessar o servidor), nos sistemas *NIX ela geralmente está no caminho: `~/.ssh/id_rsa.pub`. 

Se você não tiver essa chave criada, ou quiser criar uma nova, pode seguir o passo-a-passo do pessoal do Github de acordo com seu sistema operacional ([Windows](http://help.github.com/win-set-up-git/), [Linux](http://help.github.com/linux-set-up-git/) ou [Mac](http://help.github.com/mac-set-up-git/)).

 Em seguida, abra esse arquivo da chave pública num editor de texto e copie o conteúdo para a área de transferência. [caption id="" align="alignnone" width="154"]![](http://icons.iconarchive.com/icons/deleket/sleek-xp-software/256/Notepad-icon.png) Fonte: http://www.iconarchive.com/[/caption] [caption id="" align="alignnone" width="177"]![](http://certcollection.org/forum/uploads/60dd3d66583c3b3db53ccd419bfe8538.jpg) Fonte: http://certcollection.org/[/caption] Após isso, abra o terminal, e conecte por ssh no seu host remoto. Lá acesse a pasta onde estão seus arquivos ssh, geralmente o caminho é ~/.ssh/: $ cd ~/.ssh/ Faça uma listagem dos arquivos, e confirme se já existe um arquivo chamado authorized_keys. Se não existir ainda, crie-o. Após isso, abra esse arquivo authorized_keys num editor de texto (eu usei para isso o nano na linha de comando), e cole o que você tinha copiado alguns passos atrás na última linha desse arquivo. [caption id="" align="alignnone" width="386"]![](http://www.egginfo.org/images/nano.jpg) Fonte: http://www.egginfo.org/[/caption] Salve o arquivo e está pronto. Dessa forma, sua chave pública estará autorizada para acessar o seu servidor sem precisar digitar a senha novamente. Fontes: http://help.github.com/mac-set-up-git/ http://blogs.oracle.com/jkini/entry/how_to_scp_scp_and http://linuxproblem.org/art_9.html \--- Este artigo foi publicado originalmente em [RogerioPradoJ.com]().