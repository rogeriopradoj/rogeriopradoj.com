title: Vagrant e seus plugins
link: http://rogeriopradoj.com/2013/10/12/vagrant-e-seus-plugins/
author: rogeriopradoj
description: 
post_id: 476
created: 2013/10/12 15:10:49
created_gmt: 2013/10/12 18:10:49
comment_status: open
post_name: vagrant-e-seus-plugins
status: publish
post_type: post

# Vagrant e seus plugins

E lá vamos nós falar de [Vagrant](/tag/vagrant/)! ![vagrant-e-seus-plugins](http://rogeriopradoj.com/wp-content/uploads/2013/10/vagrant-e-seus-plugins.png)

### Resumo da história dos plugins no Vagrant

Os [plugins](http://docs.vagrantup.com/v2/plugins/) viraram cidadões de primeira classe na API v2 do Vagrant (antes eles até [eram suportados](http://docs-v1.vagrantup.com/v1/docs/extending/index.html) com um pouco de mágica e um monte de requires no meio do seu Vagrantfile). Agora, como o [Mitchell Hashimoto](http://mitchellh.com/) diz, [o próprio Vagrant usa a API de plugins interna para boa parte de suas implementações](http://docs.vagrantup.com/v2/plugins/), por isso, é possível ficar mais tranquilo de que as coisas funcionarão e que a interface é estável e bem suportada. Não tenho nenhum plugin ainda desenvolvido, mas já utilizo vários para facilitar meu trabalho com o Vagrant. Então, vamos conhecer um pouco mais? 

### Como instalar plugins no Vagrant

A [documentação do Vagrant sobre plugins](http://docs.vagrantup.com/v2/plugins/usage.html) está bem completa nesse ponto, e é bem fácil: nada mais do que rodar: `$ vagrant plugin install NOME-DO-PLUGIN`. Exemplo para instalar o [vagrant-aws](https://github.com/mitchellh/vagrant-aws): `$ vagrant plugin install vagrant-aws.` Os plugins são na maioria mantidos pela comunidade, e por isso não existe uma listagem oficial. No entanto, existe [uma página na wiki do projeto](https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Plugins) com os plugins marcados pelos usuários, sugiro que visite para buscar os que sirvam para o seu caso de uso. Quer uma dica de alguns para começar? Veja abaixo: 

### Plugins Vagrant que não podem faltar para mim

#### Bindler

Para quem conhece o [Composer no mundo PHP](http://getcomposer.org/), o [Bundler no mundo Ruby](http://bundler.io/) ou o [Bower no mundo FrontEnd](http://bower.io/), é fácil entender o que esse plugin faz e também a vantagem de usá-lo, o [Bindler](https://github.com/fgrehm/bindler). Ele permite que você crie um arquivo na raiz do seu projeto Vagrant (na mesma pasta onde você coloca o seu Vagrantfile) para distribuição, deixando claro para seus usuários que plugins são as suas dependências. Quando alguém for usar o seu projeto, executará `$ vagrant plugin bundle` antes do `$ vagrant up`, e o Bindler se encarregará de instalar as dependências que faltarem. Se o usuário já tiver os plugins instalado globalmente, estes serão usados, senão, o Bindler instalará o que faltar localmente para o projeto apenas. E quando o usuário fizer o `$ vagrant destroy` tudo voltará ao que era antes. 

  * Como instalar: `$ vagrant plugin install bindler; vagrant bindler setup;`
  * Bindler repo: <https://github.com/fgrehm/bindler>

#### Vagrant Cachier

O [Cachier](https://github.com/fgrehm/vagrant-cachier) é aquele cara que faz você se perguntar: como conseguiu viver sem ele até agora! Ele faz o cache dos pacotes Apt que você instala na suas distribuições Debian-like (Ubuntu inclusive) entre todas os projetos que você tiver baseado em uma box. Assim, ele acelera (e muito!!!) a instalação das suas dependências, pois, se um pacote já tiver sido baixado naquela versão específica em um outro projeto, será usado o cache em vez de ir até o repositório oficial do Ubuntu, por exemplo. 

  * Como instalar: `$ vagrant plugin install vagrant-cachier`
  * Cachier repo: <https://github.com/fgrehm/vagrant-cachier>

#### Vagrant HostManager

Vai chegar o momento em que apenas definir um IP na opção :private_network do Vagrantfile, ou mesmo a redirecionamento de porta via :forwarded_port, não será mais suficiente para testar seu projeto (por diversos motivos isso pode acontecer. Acredite, quando você chegar nesse nível você vai lembrar das minhas palavras ;-) ). Nesse momento você vai procurar uma forma de configurar o seu arquivo HOSTS, /etc/hosts (nos sistemas *nix) ou %windir%\system32\drivers\etc\hosts (no Windows), para que endereço do seu Vhost do Apache fique disponível tanto internamente nas máquinas (Guests) quanto a partir do seu sistema principal (Host). Qual é o caminho normal para fazer isso? Sim, editar manualmente seu arquivo HOST em um monte de lugares. Aí que entra o [plugin HostManager](https://github.com/smdahlen/vagrant-hostmanager): com base numa pequena configuração do seu Vagrantfile ele já configura tudo isso para você. Existem alguns outros que fazem o serviço de forma parecida, mas foi com ele que me adaptei mais. 

  * Como instalar: `$ vagrant plugin install vagrant-hostmanager`
  * HostManager repo: <https://github.com/smdahlen/vagrant-hostmanager>

### Considerações finais

Os plugins foram uma inclusão importante no ecossistema do Vagrant, e como viram, não é difícil de usar os que já estão disponíveis. Esse artigo está longe de te dar o caminho completo para usar as ferramentas, mas já te inicia e mostra onde você pode conseguir mais informações. Procure conhecer e testar o máximo que você conseguir pois assim vai ser fácil de tomar a decisão de usar ou não um deles em seus futuros projetos. E fique a vontade de usar os comentários se quiser ajuda! Até mais! \--- Este artigo foi publicado originalmente em [RogerioPradoJ.com]().

## Comments

**[Tárcio Zemel](#1614 "2014-02-10 01:12:00"):** Putz, que sacanagem! Esse foi um dos da lista que eu mais gostei e, junto com a dica do has_plugin?() que tinha visto nesse seu outro artigo para mostrar o "WARNING", seria muito bom se funcionasse. Vamos esperar algo do gênero pintar por aí, então, né... Abraços!

**[Rogerio Prado de Jesus](#1615 "2014-02-10 09:14:00"):** Ou, vamos estudar um pouco de Ruby e fazer o nosso :-D! Quem sabe no futuro!

**[Tárcio Zemel](#1616 "2014-02-10 13:59:00"):** Haha, também é uma ideia! Vou ficar de olho aqui no blog pra ver se pinta alguma novidade sobre isso e, eu encontrando alguma coisa, também te falo!

**[Rogerio Prado de Jesus](#1613 "2014-02-09 16:24:00"):** Olá, Tárcio Zemel, tudo bem? Infelizmente o Bindler não está mais sendo mantido (https://github.com/fgrehm/bindler/commit/fafc8d162139e28e9b1236a1d77d4ed4b714fcac), e só funciona no Vagrant 1.2 ou 1.3, não funciona nas versões mais novas. Existe um jeito de "tentar resolver", https://github.com/fgrehm/bindler/issues/29, mas é "workaround", sabe como é né... Minha dica: use o Vagrant.has_plugin? no seu Vagrantfile. Com pouco trabalho, você consegue pelo menos garantir que o usuário do seu Vagrantfile depois pelo menos tenha os plugins que você definiu, e, se não tiver, indicar como fazer a instalação. Não é o melhor dos mundos, mas funciona! COMO USAR O VAGRANT.HAS_PLUGIN? NO VAGRANTFILE: http://rogeriopradoj.com/2013/12/09/como-usar-o-vagrant-has_plugin-no-vagrantfile/ Falou!

**[Tárcio Zemel](#1612 "2014-02-09 02:20:00"):** Instalei o Bindler para testar (rodando os 2 comandos necessários) e criei o arquivo `.vagrant_plugins.json` só com `[ vagrant-cachier ]`. Na hora de rodar `vagrant plugin bundle`, ele simplesmente exibe a lista de comandos padrão, como se eu tivesse usado somente `vagrant`... Já tentei seguir o ["Help! Things are falling apart!"](https://github.com/fgrehm/bindler#help-things-are-falling-apart) do repo, mas dá erro de cara, dizendo que o arquivo não existe. Já viu isso antes?

