title: Permissões de arquivos e pastas no Windows XP
link: http://rogeriopradoj.com/2010/10/18/permissoes-de-arquivos-e-pastas-no-windows-xp/
author: rogeriopradoj
description: 
post_id: 31
created: 2010/10/18 14:16:44
created_gmt: 2010/10/18 16:16:44
comment_status: open
post_name: permissoes-de-arquivos-e-pastas-no-windows-xp
status: publish
post_type: post

# Permissões de arquivos e pastas no Windows XP

O sistema de arquivos NTFS utilizado no Windows XP Professional tem várias opções para controle de permissões. Comecei a utilizar essas permissões no trabalho, pois lá utilizamos domínio Active Directory e senhas de rede. Com isso é possível determinar que determinada pasta ou arquivo fiquem disponíveis para consulta apenas por um certo número de pessoas, podendo determinar ainda se o acesso será somente leitura, leitura e escrita ou total (além de escrever é possível também gerenciar as permissões). O que mais me intrigava era: por que não conseguia fazer isso no computador de casa? O procedimento que costumava fazer no serviço era: botão direito > propriedades > segurança, e lá fazia tudo que precisava. Mas no computador de casa não tinha essa opção Segurança. A resposta encontrei [aqui, no site da Microsoft](http://support.microsoft.com/kb/307874/). O que estava acontecendo é que o padrão no Windows XP é o _compartilhamento simples de arquivo_. Com ele, ou você compartilha, ou não! Sem opções de permissão mais detalhadas. Depois de retirar essa opção de compartilhamento simples, já ficou do jeito que estava acostumado, segue um resumo de como fazer: 

  * Clique em Iniciar e em Meu computador.
  * No menu Ferramentas, clique em Opções de pasta.
  * Clique na guia Modo de exibição.
  * Na seção Configurações Avançadas, clique para desmarcar a caixa de seleção Usar compartilhamento simples de arquivo (recomendado).
  * Clique em OK.
É isso aí. \--- Este artigo foi publicado originalmente em [RogerioPradoJ.com]().