title: Como usar o Vagrant.has_plugin? no Vagrantfile
link: http://rogeriopradoj.com/2013/12/09/como-usar-o-vagrant-has_plugin-no-vagrantfile/
author: rogeriopradoj
description: 
post_id: 494
created: 2013/12/09 23:42:49
created_gmt: 2013/12/10 02:42:49
comment_status: open
post_name: como-usar-o-vagrant-has_plugin-no-vagrantfile
status: publish
post_type: post

# Como usar o Vagrant.has_plugin? no Vagrantfile

Olá, pessoal! Esse artigo é uma continuação do [Vagrant e seus plugins](/2013/10/12/vagrant-e-seus-plugins/), de outubro de 2013, e, para falar a verdade, começou a ser escrito antes do original. É que percebi que, sem uma explicação mais básica do que eram os plugins, ia "faltar base" - como dizia um professor do cursinho!. Então, mais uma vez, se quiser primeiro saber o que são os plugins no Vagrant, [leia o artigo original](http://rogeriopradoj.com/2013/10/12/vagrant-e-seus-plugins/) primeiro, ok? ![vagrant-has-plugin](http://rogeriopradoj.com/wp-content/uploads/2013/12/vagrant-has-plugin.png)

### O que é o método Vagrant.has_plugin?

O `has_plugin?` é um método da API do Vagrant, para ser usado no seu Vagrantfile, que verifica se um plugin está disponível no sistema. Com o grande número de plugins disponíveis ([confira os listados na wiki oficial](https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Plugins)), é importante ter uma forma de garantir que quem for usar seu projeto Vagrant tenha os plugins que você definiu/utilizou, e, se não tiver, fazer algo com essa informação. Vamos ver um exemplo para deixar mais fácil o entendimento: https://gist.github.com/7866178 Nesse trecho acima vemos um Vagrantfile que utiliza o [plugin vagrant-cachier](https://github.com/fgrehm/vagrant-cachier) para acelerar o `vagrant up` se o usuário tem o plugin instalado na máquina, e, caso não tenha, tudo continua funcionando, apenas sem a aceleração. Sem usar o `has_plugin?` o Vagrant interromperia o processo com uma mensagem de erro. Parece bastante com o conceito de [progressive enhancement/graceful degradation](http://tableless.com.br/bem-vindo-a-xangrila-parte-1/#.UqZla2RDugk): forneça ao usuário que tem apenas o requisito básico uma versão funcional do seu projeto, sem traumas. E, para os que tem mais requisitos (no caso o plugin que definimos), entregue também as funções melhoradas (nesse caso, uma camada de cache que vai acelerar o provisionamento das máquinas virtuais. Se você ainda não conhece o vagrant-cachier, [do brasileiro Fabio Rehm, ou @fgrehm](https://github.com/fgrehm), é uma boa hora de começar!). Um outro exemplo segue abaixo: https://gist.github.com/7882791 Nesse caso, ao contrário do anterior, é feita uma ação quando um plugin não existe no sistema. E quando que isso é útil? Principalmente para os casos que onde precisamos avisar para o usuário que um plugin é necessário/recomendável para executar a aplicação, dando algum caminho para que ele possa resolver a situação. No exemplo acima, avisamos que o projeto está usando o [plugin vagrant-bindler](https://github.com/fgrehm/bindler) para fazer a gestão dos plugins e passamos um caminho para que o usuário faça a instalação do mesmo se ele ainda não tiver (plugin também criado pelo [@fgrehm](https://github.com/fgrehm)). 

### Há tempos... um problema!

A função Vagrant.has_plugin? [foi introduzida no Vagrant na versão 1.3.0](https://github.com/mitchellh/vagrant/blob/master/CHANGELOG.md), [com alguns problemas](https://github.com/mitchellh/vagrant/pull/2189), e na [versão 1.3.2 foi realmente consertada](https://github.com/mitchellh/vagrant/blob/master/CHANGELOG.md), isso tudo em setembro de 2013. Mas por que então, mesmo tendo uma certa idade, essa função ainda não é tão utilizada? Isso acontece por uma pequena inconsistência na implementação dessa API, que faz com que o nome do plugin internamente para o Vagrant (que vai ser usada na chamada `Vagrant.has_plugin?`) seja diferente do nome do plugin que é usado na instalação via linha de comando `$ vagrant plugin install ...`. Antes de perceber isso acima, eu mesmo no começo não conseguia entender a lógica, que parecia ser tão simples: [fazer uma condição ruby IF ou UNLESS, passando o nome do plugin](https://github.com/fgrehm/bindler/issues/22). Por que não funcionava? Era essa bendita inconsistência de nomes. Ainda bem que não desisti de entender! Para facilitar, vamos chamar esses nomes da seguinte forma: 

  * nome de instalação do plugin: usado no comando `$ vagrant plugin install ...`.
  * nome interno do plugin: usado no Vagrantfile, com o método `has_plugin?`
Com isso em mente, vamos para os  exemplos: https://gist.github.com/7882955 Quando acessamos a [lista oficial dos plugins disponíveis para Vagrant](https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Plugins) lá não encontramos o nome interno (ainda, estou trabalhando nisso :-) ); apenas aparece o nome de instalação. Uma diferença que, às vezes, é apenas de maíusculas ou minúsculas entre os nomes das duas versões mas que já atrapalha tudo! Peguemos o Bindler. Para instalá-lo no sistema, é usado o nome da [Gem (em minúsculas)](https://github.com/fgrehm/bindler/blob/v0.1.4/bindler.gemspec#L7): `$ vagrant plugin install bindler` Já para usar no seu Vagrantfile, com o `has_plugin?`, tem que ser o [nome interno do plugin (começando com maíscula)](https://github.com/fgrehm/bindler/blob/v0.1.4/lib/bindler/plugin.rb#L7): `Vagrant.has_plugin?("Bindler")` É, realmente é complicado. Por não haver um padrão, é possível encontrar todos os tipos de combinações: nomes iguais, totalmente diferentes ou apenas a diferença de capitulares. Mas existe uma solução! Vamos vê-la? 

### A solução!

E a solução é: aprender a ler o repositório do plugin! Puxa, não é o que você estava esperando, não é mesmo... É, por enquanto (dezembro de 2013), não existe uma solução perfeita, por isso vamos aprender aqui a ler o repositório sempre que você precisar. 

#### Arquivos importantes

O primeiro passo é saber localizar, dentro de um repositório, o nome de instalação do plugin e o nome interno do plugin: 

  * **/nome-de-instalação-do-plugin.gemspec**: é nesse arquivo que temos o **nome de instalação**. O arquivo fica na pasta raiz do repositório do plugin. Exemplos: _bindler.gemspec_, _vagrant-aws.gemspec_, _vagrant-cachier.gemspec_ etc.
  * **/lib/nome-de-instalação-do-plugin/plugin.rb**: é nesse arquivo que temos o **nome interno**. O arquivo fica no terceiro nível do repositório do plugin. Dentro desse arquivo, existe um atributo `name`, que é o nome interno que você vai usar. Exemplos para os mesmos plugins acima: _Bindler_, _AWS_, _vagrant-cachier_.

#### Achar o repositório do plugin