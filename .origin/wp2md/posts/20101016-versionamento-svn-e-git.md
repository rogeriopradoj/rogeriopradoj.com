title: Versionamento - SVN e GIT
link: http://rogeriopradoj.com/2010/10/16/versionamento-svn-e-git/
author: rogeriopradoj
description: 
post_id: 23
created: 2010/10/16 14:14:41
created_gmt: 2010/10/16 17:14:41
comment_status: open
post_name: versionamento-svn-e-git
status: publish
post_type: post

# Versionamento - SVN e GIT

Meu contato com  controle de versões se deu por causa do framework [Symfony](http://www.symfony-project.org/), e o seu projeto Jobeet, em meados de 2009. A ideia de "tirar fotos" do seu projeto em dado momento e ter opção de voltar para ele em algum momento se mostrou muito interessante para mim. Assim eu não precisaria ter medo de implementar uma nova funcionalidade, ou refatorar  o código de forma alguma: sempre teria como "pegar as fotos" e colocar no lugar do que deu errado. Por causa do Symfony comecei direto pelo Subversion Version Control (SVN), o que lia na época é que era o mais usado, e que tinha deixado o Control Version System (CVS) para trás. Era comum ver alguns blogs falando já sobre o Git, mas parecia algo muito avançado e mais voltado para o pessoal que desenvolvia em Ruby e Ruby On Rails: como meu foco era PHP, não fui procurar mais nada sobre Git. 

### Versões/releases no versionamento

O que mais achei interessante da divisão básica entre versões (releases) foi o uso que é feito do Trunk, Branches e Tags. Para não confundir muito, a partir de agora vou chamar apenas de _release_ essas versões de software. É comum vermos os softwares com a informação de release dessa forma: 

  1. v1, v2, v7
  2. v1.0, v1.3, v5.2
  3. v1.0.3, v1.3.29, v5.6.7
No primeiro item vemos o release principal do programa. Ele geralmente é incrementado quando acontece uma alteração muito grande no software, e não apenas de poucas funções. Um exemplo poderia ser a mudança do Windows XP para o Windows Vista (5 para 6 - [fonte](http://www.nirmaltv.com/2009/08/17/windows-os-version-numbers/)). No segundo item vemos o release de segundo nível. Seu incremento ocorre quando acontece um acréscimo de funcionalidade que não cause uma mudança tão drástica. Exemplo ainda no mundo do Windows, Windows Vista para Windows 7 (6.0 para 6.1 - [fonte](http://www.nirmaltv.com/2009/08/17/windows-os-version-numbers/)). No terceiro item, release de terceiro nível, geralmente usado quando é corrigido um bug num release de segundo nível, ou, nos casos das numerações x.x.0 o release inicial. Esse release é o que costuma ser utilizado pelos clientes. O Trunk seria para manter a versão de desenvolvimento atual, ou seja, não estaria vinculada diretamente a nenhum dos releases de software acima. Sua tradução literal seria tronco, nesse caso tronco principal. Pensando no controlador de versão como uma árvore essa denominação faz todo o sentido. Os Branches começam a ter uma maior ligação com releases em si. Sua tradução poderia ser galhos ou ramos, dessa forma cada branch/galho ficaria responsável por um release (geralmente de segundo nível). É comum fazer um branch a partir de um release da seguinte forma: 

  * Trunk já está com uma versão suficientemente boa, é feita uma cópia para o Branch v1.0 (release 1.0)
  * Desenvolvedores principais continuam commitando no Trunk, caminhando para o release 2.0
  * Uma funcionalidade nova é criada no Trunk, pensando no release 2.0, mas já querem que seja implementado no versão 1 que está rodando, para isso é criado um novo Branch, agora v1.1 (release 1.1).
  * O trunk continua seu caminho.
As Tags tem mais a ver com o que realmente é distribuído de software para o ambiente de produção. Sua tradução literal seria rótulo ou etiqueta, e é realmente isso que é feito a partir do Branch em determinado momento. Usando o exemplo acima: 
  * O Branch v1.0 será disponibilizado para uso, então ele é etiquetado como Tag v1.0.0
  * A equipe de testes achou uma série de bugs no Branch v1.0, que a equipe de desenvolvimento principal já corrigiu no Trunk.
  * Eles copiam essa correção no Branch v1.0, e etiquetam ele como Tag v1.0.1
  * A nova funcionalidade foi criada e eles querem disponibilizar para uso, é criado o Branch v1.1.
  * Logo após esse Branch é etiquetado como Tag v1.1.0.
  * A equipe de testes agora acha um bug no Branch v1.1, a equipe de desenvolvimento já corrigiu no Trunk.
  * É copiada a correção para o Branch v1.1, e etiquetada nesse momento como Tag v1.1.1.
  * Outro bug é achado no Branch v1.1, é copiada a correção do Trunk para esse Branch e é etiquetada como Tag v1.1.2.

### SVN

Como na minha empresa o SVN era um software homologado, foi mais fácil também aplica-lo lá, o que facilitou meu aprendizado. Em vez de ir direto para a linha de comando, preferi utilizar o [TortoiseSVN](http://tortoisesvn.net/). Ele tem integração com o Windows Explorer e facilita muito o trabalho de criação de repositórios, checkouts, updates e commits. Minha fonte de informação inicial, depois do Symfony - Jobeet, foi o livro do SVN em inglês, no endereço <http://svnbook.red-bean.com/> Depois de muita procurar em blogs em português, consegui a versão do livro em português pt-br, endereço: <https://code.google.com/p/svnbook-pt-br/> Quando fiquei mais natural no uso do SVN, arriscando quase nada um pouco na linha de comando e migrando 99% para o Ubuntu Linux, comecei a procurar outras opções que não fossem o Tortoise. No Ubuntu a primeira ferramenta que achei que fazia um pouco o que o Tortoise oferecia no Windows foi o RapidSVN. Só que ele não tinha integração com o Nautilus Mais tarde meu irmão[ @royopa](http://twitter.com/royopa) me mostrou o [RabbitVCS](http://www.rabbitvcs.org/), que já se integrava bem naturalmente com meu gerenciador de arquivos. Posso afirmar: é o TortoiseSVN para Linux. Como todas essas ferramentas, funcionalidades e entendimento que passei a ter do SVN pensei: acho que agora é hora de aprender algo novo. 

### Git

Comecei a ver que muitos projetos PHP e outros de meu interesse já estavam passando para o [GitHub](http://github.com) (CakePHP, Symfony2, jQuery...). Era tempo de começar a me arriscar nesse mundo também. Seguindo uma dica de a [lista de PHP](http://twitter.com/rogeriomaxmax/php-people) do Twitter do [@rogeriomaxmax](http://twitter.com/rogeriomaxmax) consegui o livro <http://net.tutsplus.com/freebies/books/getting-good-with-git-free-ebook/> Estou bem no início, mas enquanto vou caminhando, irei postando o que vou conseguindo. Até mais, \----- Atualizado em 19/10/2010 as 00h43: Terminei o livro de Git. Minha página no GitHub é: http://rogeriopradoj.github.com. Vamos caminhando... \--- Este artigo foi publicado originalmente em [RogerioPradoJ.com]().