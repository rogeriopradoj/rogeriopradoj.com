title: Python e Virtualenv no Mac OS X Mountain Lion 10.8
link: http://rogeriopradoj.com/2013/05/02/python-e-virtualenv-no-mac-os-x-mountain-lion-10-8/
author: rogeriopradoj
description: 
post_id: 385
created: 2013/05/02 09:14:34
created_gmt: 2013/05/02 12:14:34
comment_status: open
post_name: python-e-virtualenv-no-mac-os-x-mountain-lion-10-8
status: publish
post_type: post

# Python e Virtualenv no Mac OS X Mountain Lion 10.8

Este artigo é uma tradução livre de _Python and Virtualenv on Mac OS X Mountain Lion 10.8_, do [Justin Mayer](https://github.com/justinmayer), disponível em <http://hackercodex.com/guide/python-virtualenv-on-mac-osx-mountain-lion-10.8/>. \--- A instalação do Python e do Virtualenv no Mac OS X 10.8 Mountain Lion pode ser feita de muitas formas. Embora não exista uma configuração perfeita, esse tutorial te guiará no processo de configuração de uma instalação padrão do Mountain Lion num ótimo sistema para desenvolvimento Python. 

### Primeiros passos

Esse guia pressupõe que você já tenha instalado o Xcode e o Homebrew. Para detalhes, siga os passos do [Mountain Lion Configuration Guide](http://hackercodex.com/guide/mac-osx-mountain-lion-10.8-configuration/ ). 

### Python

Vamos instalar a última versão 2.7.x do Python pelo Homebrew. Para que fazer isso, você pode perguntar, quando a Apple já inclui o Python no Mountain Lion? Aqui temos algumas razões: 

  * O Homebrew sempre fornece a versão mais recente (hoje 2.7.4). A versão embutida no OS X está parada no 2.7.2.
  * A Apple fez mudanças significativas no Python embutido, o que pode resultar em bugs escondidos.
  * O Python do Homebrew inclui as últimas ferramentas para gerenciamento de pacotes: o [pip](http://www.pip-installer.org/) e o [Distribute](http://pypi.python.org/pypi/distribute).
Seguindo pelo mesmo caminho, a versão do OpenSSL no Mountain Lion, a 0.9.8) é de fevereiro de 2011, por isso estamos dizendo ao Homebrew para baixar o OpenSSL mais recente e compilar o Python com ele. Use o comando a seguir para instalar o Python via Homebrew: https://gist.github.com/5500013 Você já deve ter alterado seu PATH como mencionado no artigo acima, certo? Caso contrário, faça isso agora. Também podemos instalar o Python 3.x junto com o Python 2.x: https://gist.github.com/5500023 ... o que facilita para testar seu código tanto no Python 2.x quanto no Python 3.x. 

### Pip

Digamos que você quer instalar um pacote Python, como a fantástica ferramenta para isolamento de ambientes [virtualenv](http://www.virtualenv.org/). Quase todo artigo para Mac OS X relacionado ao  Python diz para o leitor instalá-lo assim: https://gist.github.com/5500046 Aqui estão os motivos porque eu não faço dessa forma: 

  1. instalação com permissão root
  2. instalação é feita na sistema em /Library
  3. instalação é feita pelo obsoleto easy_install em vez de usar as ferramentas mais modernas como o [pip](http://www.pip-installer.org/) ou o [Distribute](http://pypi.python.org/pypi/distribute)
  4. o uso das ferramentas fornecidas pelo Homebrew leva a um ambiente mais confiável
  Como você deve ter percebido, estamos usando as ferramentas fornecidas pelo Homebrew para instalar os pacotes que você quiser que estão disponíveis globalmente. Quando fizer instalações usando o pip do Python do Homebrew, os pacotes serão postos em `/usr/local/lib/python2.7/site-packages`, com os binários sendo colocados em `/usr/local/share/python`. 

### Controle de versão (opcional)

A primeira coisa que eu instalo pelo pip é o [Mercurial](http://mercurial.selenic.com/). Uma vez que eu tenho repositórios Mercurial para empurrar tanto para o [Bitbucket](https://bitbucket.org/j/dotfiles) quanto para o [Github](https://github.com/justinmayer/dotfiles), eu instalo o Mercurial e o [hg-git](http://hg-git.github.com/) em todos meus sistemas: https://gist.github.com/5501518 Pelo menos, você terá que adicionar umas poucas linhas no seu arquivo .hgrc para utilizar o Mercurial: https://gist.github.com/5501527 As linhas a seguir devem te permitir começar; apenas garanta que tenha alterado os valores para seu nome e endereço e-mail respectivamente. https://gist.github.com/5501537 Para testar seu o Mercurial foi configurado e está pronto para ser usado, execute o comando a seguir: https://gist.github.com/5501544 Se a última linha da saída for "No problem detected", então o Mercurial foi instalado e configurado adequadamente. 

### Virtualenv

Os pacotes Python instalados pelos passos acima são globais no sentido que eles ficam disponíveis em todos os seus projetos. Isso pode ser conveniente algumas vezes, mas também pode criar problemas. Por exemplo, as vezes um projeto precisa da última versão do Django, enquanto outro precisa do Django 1.3 para manter a compatibilidade com uma extensão crítica de terceiros. Esse é um dos muitos casos de uso que o [virtualenv](http://www.virtualenv.org/) foi criado para solucionar. Nos meus sistemas, apenas um punhado de pacotes Python de uso geral (como o Mercurial e o próprio virtualenv) ficam disponíveis globalmente - qualquer outro pacote fica confinado em um ambiente virtual. Com essa explicação, vamos instalar o virtualenv: https://gist.github.com/5501565 Crie alguns diretórios para armazenar seus projetos e os ambientes virtuais, respectivamente: https://gist.github.com/5501573 Depois vamos abrir o arquivo ~/.bashrc... https://gist.github.com/5501589 ... e adicionar algumas linhas nele: https://gist.github.com/5501591 Vamos recarregar nosso ambiente bash: https://gist.github.com/5501599 Agora nós temos o virtualenv instalado e pronto para criar novos ambientes virtuais, que serão armazenados em `~/Virtualenvs`. Novos ambientes virtuais podem ser criados assim: https://gist.github.com/5501612 Se você tiver tanto o Python 2.x quanto o 3.x e quiser criar um virtualenv do Python 3.x: https://gist.github.com/5501619 ... o que facilita a troca entre os ambientes foobar do Python 2.x com o do Python 3.x. 

### Restringindo o pip aos ambientes virtuais

O que acontece se _pensarmos_ que estamos trabalhando em uma ambiente virtual ativo, mas na verdade não existir nenhum ambiente virtual ativo e instalarmos algo via `pip install foobar`? Bem, nesse caso o pacote foobar é instalado no nosso site-packages global, estragando o propósito do isolamento do nosso ambiente virtual. Na tentativa de evitar instalar por engano via pip um pacote específico de um projeto no meu site-packages global, anteriormente eu usava o `easy_install` para pacotes globais e o pip embutido no virtualevn para instalar pacotes dentro dos ambientes virtuais. Isso atingia o objetivo do isolamento, uma vez que o pip estava disponível apenas dentro dos ambientes virtuais, tornando impossível para mim rodar `pip install foobar` por engano no meu site-packages global. No entanto o `easy_install` tem algumas deficiências, como a impossibilidade de desinstalar um pacote, e me vi querendo usar o pip tanto para pacotes globais quanto nos virtualenvs.

## Comments

**[Rogerio Prado de Jesus](#1590 "2013-07-24 22:28:00"):** Me salvou!

