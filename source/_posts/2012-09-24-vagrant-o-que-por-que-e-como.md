---
date: 2012-09-24 01:23:45+00:00
title: 'Vagrant: O que, Por que e Como'
categories:
  - Geral
  - PHP
tags:
  - php
  - tradução
  - vagrant
---

Tradução livre de Vagrant: What, Why, and How, disponível em [http://net.tutsplus.com/tutorials/php/vagrant-what-why-and-how/](http://net.tutsplus.com/tutorials/php/vagrant-what-why-and-how/).

---

Este artigo te ajudará a usar o [Vagrant](http://vagrantup.com/) para administrar suas instâncias de máquinas virtuais e explicará como se beneficiar do [Puppet](http://puppetlabs.com/puppet/puppet-enterprise/) para fazer a provisão de vários recursos como o PHP e o PostgreSQL.

![garoto propaganda do vagrant](assets/images/2012/07/Vagrant-Virtualized-development-for-the-masses..png)
*Garoto propaganda :-) da ferramenta Vagrant - http://vagrantup.com*

### Introdução

Os desenvolvedores tem à disposição um grande número de maneiras de construir seu ambiente de desenvolvimento web. Podem ser usadas opções "locais", do tipo dos servidores "tudo em um"como o Zend Server, XAMPP, MAMP, WAMP etc; ou ainda como você instalando os componentes a partir dos fontes ou via um sistema de gerenciamento de pacotes, como o Homebrew, o Apt ou o Yum.

Isso vai se acumulando a medida que você trabalha em vários projetos diferentes: PHP 5.3 e PHP 5.4, MySQL, SQLite, MongoDB, Postgres, PEAR, PHPUnit, Rails 3.1, Memcached, Redis, Gearman, NodeJS etc. E se você precisar  atualizar seu computador se ele pifar, você terá que começar tudo de novo.

Pode ser usada uma configuração "remota", com um servidor com compartilhamentos "Samba" ou um servidor SSH montado com uma ferramenta como o [ExpanDrive](http://www.expandrive.com/). A última opção esbarra na latência de leitura e escrita dos arquivos, que é extremamente chata. É possível usar o SSH com o Vim para tudo, o que é rápido, mas só funciona se você quiser usar o Vim para tudo também.

### Desenvolvimento vs Produção

Mesmo que você esteja feliz com a forma que vem fazendo as coisas até agora, quantas vezes você já ouviu (ou disse) "Bem, está funcionando no meu computador"?

Isso é terrivelmente comum e acontece quando os ambientes diferem até mesmo nos detalhes mais triviais.

É extremamente importante garantir que seu ambiente de desenvolvimento seja idêntico ao ambiente de produção, e que ele também corresponda ao servidores de staging e de teste se esses existirem.

Isso pode parecer fácil se você pensar apenas na instalação do Apache, do PHP de alguma cópia do MySQL, porém existem milhões de fatores para avaliar. Se você estiver desenvolvendo no OSX e fazendo deploy num sistema Ubuntu, então você deve se deparar com problemas estranhos relacionados a maiúsculas. Isso é comum no CodeIgniter, quando alguém cria uma biblioteca com a primeira letra minúscula. Ela irá carregar corretamente no OSX, mas irá quebrar quando for implementada na produção. Seu processo de desenvolvimento pode ter feito você perder alguns contratos só por causa de algumas diferenças triviais entre sistemas operacionais que ninguém notou até ser muito tarde.

### Desenvolvimento = Produção

Então qual é a solução? Forçar que todos os desenvolvedores joguem fora suas ferramentas e trabalhem todos no mesmo modelo de laptop? Se os seus colegas ganharem Macbooks novinhos em folha talvez você não ouça muitas reclamações, mas você teria que usar o OSX Server para tudo.

Você poderia usar o Linux para tudo, mas entraria numa briga para decidir qual distribuição utilizar. Forçar os desenvolvedores para usar o mesmo sistema operacional gera problemas, reduz a produtividade e promove lutas de nerds.

A virtualização é a resposta e isto não é nada novo, mas geralmente quando pensamos em virtualização pensamos nos problemas de performance e nas ventoinhas girando que nem malucas enquanto o sistema tenta rodar dois sistemas operacionais ao mesmo tempo.

Essa situação pode ser verdade quando tentamos rodar o Windows em uma máquina não muito potente mas, hoje em dia, um Mac mediano com 4 GB de RAM de fábrica é mais do que suficiente para rodar uma instalação de um servidor Ubuntu em modo de linha de comando com todas ferramentas habituais (IDE, browser, ferramentas de depuração etc.). Existem diferentes versões de virtualização, mas eu prefiro o [VirtualBox](https://www.virtualbox.org/) da Oracle (que é grátis). Esse programa faz o "trabalho pesado" da virtualização, enquanto a ferramenta Vagrant serve para gerenciar as instâncias.

### Passo 1 - **Instalando o VirtualBox**

Primeiro, [baixe e instale o VirtualBox](http://www.virtualbox.org/wiki/Downloads). Nos sistemas *nix (Mac OSX, Linux etc.) você precisará alterar seu .bash_profile (ou .zsh_profile) para estender a variável $PATH:

```sh
PATH=$PATH:/Applications/VirtualBox.app/Contents/MacOS/
export PATH
```

Isso permitirá que o Vagrant saiba onde o VirtualBox está instalado e, é claro, será diferente em cada sistema operacional.

### Passo 2 - **Instalando o Vagrant**

Você pode baixar um [binário do vagrant](http://downloads.vagrantup.com/) para o seu sistema operacional, ou instalar ele como uma gem se não houver um binário disponível:

```sh
gem install vagrant
```

### Passo 3 - **Criando uma Instância**

Crie um lugar para suas configurações ficarem:

```sh
mkdir -p ~/Vagrant/test
cd ~/Vagrant/test
```

Iremos usar o Ubuntu 12.04 LTS (Precise Pangolin), o qual já tem uma "box" configurada.

```sh
vagrant box add precise32 http://files.vagrantup.com/precise32.box
```

Aqui você enxerga o argumento "precise32", que é o apelido da URL. Agora você pode criar a instância que irá baixar o arquivo .box.

```sh
vagrant init precise32
vagrant up
```

Agora ela estará rodando. Fácil! Se você quiser acessar a instância via SSH, use este comando:

```sh
vagrant ssh
```

### Passo 4 - **Configuração**

Você terá um arquivo, chamado Vagrantfile, que conterá a configuração dessa instância:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant::Config.run do |config|
    config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"
    # Assign this VM to a host-only network IP, allowing you to access it
    # via the IP. Host-only networks can talk to the host machine as well as
    # any other machines on the same network, but cannot be accessed (through this
    # network interface) by any external networks.
    config.vm.network :hostonly, "192.168.33.10"
    # Set the default project share to use nfs
    config.vm.share_folder("v-web", "/vagrant/www", "./www", :nfs => true)
    config.vm.share_folder("v-db", "/vagrant/db", "./db", :nfs => true)
    # Forward a port from the guest to the host, which allows for outside
    # computers to access the VM, whereas host only networking does not.
    config.vm.forward_port 80, 8080
    # Set the Timezone to something useful
    config.vm.provision :shell, :inline => "echo \"Europe/London\" | sudo tee /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata"
    # Update the server
    config.vm.provision :shell, :inline => "apt-get update --fix-missing"
    # Enable Puppet
    config.vm.provision :puppet do |puppet|
        puppet.facter = { "fqdn" => "local.pyrocms", "hostname" => "www" }
        puppet.manifests_path = "puppet/manifests"
        puppet.manifest_file  = "ubuntu-apache2-pgsql-php5.pp"
        puppet.module_path  = "puppet/modules"
    end
end
```

Essa é, se você ainda não notou, sintaxe Ruby; por isso você pode ser bem criativo com o arquivo, apesar de aqui só termos o básico.

Ele mostra qual apelido usar, e tem a URL para o caso do apelido não estar definido localmente (útil para casos de compartilhamento).

As linhas share_folder são bem úteis para mapear pastas da instância com pastas locais. Usando nfs => true a instância será capaz de escrever e alterar permissões dos arquivos, o que é útil se você estiver, por exemplo, tentando instalar um CMS ali.

O redirecionamento de portas permite que você acesse sua instância em http://localhost:8080 e, é claro, faça alterações para diferentes portas em caso de conflito.

Esse arquivo de configuração também define o fuso horário para Europe/London, depois executa o apt-get update, que força seu sistema para se atualizar toda vez que ele é iniciado. Se você pular esse item da configuração, pode encontrar vários pacotes se recusando a instalar pois as referências estão desatualizadas.

Quando você alterar a configuração, pode recarregar a instância para utilizá-la:

```sh
vagrant reload
```

Agora que nossos servidores estão no ar e prontos para continuar, precisamos instalar neles alguns softwares. Não vamos só rodar o apt-get install em um monte de pacotes na linha de comando, vamos "provisionar" nossos servidores.

### Passo 5 - **Provisionamento**

O provisionamento ou configuração do servidor não é algo que a maioria dos desenvolvedores pensam a respeito pois isso é feito normalmente pelos sysadmins. A ideia é criar algum registro do que software e configurações foram postas em um servidor assim você poderia criar novos ambientes de desenvolvimento, novos servidores staging que replicam os servidores de produção ou então criar outro servidor de produção para fazer balanceamento de carga entre eles.

#### Provisionamento das antigas

Como os sysadmins lidam com isso varia, mas no passado foram usados todos os tipos de solução - desde manter uma wiki dos comandos que foram executados (o que pode ficar grande e obsoleto rapidamente) e o maravilhoso método de manter um "multi-terminal", onde você digita os comandos em uma janela e ele replica os mesmos comandos para outros 7 servidores ao mesmo tempo. _Todos esses métodos são terríveis_.

Uma solução seria criar o seu próprio arquivo .box ou criar um backups .iso assim novos servidores poderiam ser baseados neles; no entanto manter essas imagens gera um monte de trabalho extra e não importa o quanto você tente, essas máquinas de desenvolvimento se tornarão obsoletas com o tempo.

#### Provisionamento moderno

Existem atualmente dois sistemas populares, o [Puppet](http://www.puppetlabs.com/) e o [Chef](http://www.opscode.com/chef/). Ambos existem há anos, mas começaram a se tornar bem populares com o aumento do uso método de desenvolvimento [DevOps](https://en.wikipedia.org/wiki/DevOps). As ideias dos dois são parecidas e você deveria estudar os dois sistemas, mas aqui no tutorial iremos nos focar exclusivamente no Puppet.

Basicamente, em vez de rodar um série de comandos e torcer para que tudo dê certo, você criará um manifesto para o Puppet explicando tudo o que você precisar garantir que tenha sido feito. Quando você roda um comando no terminal, você está basicamente dizendo ao computador:

"Instale o Apache"

Com o Puppet você diria:

"Garanta que o Apache está instalado"

Ou, em vez de:

"Crie uma nova pasta, chame-a de /var/www e defina a permissão para www-data:www-data"

Com o Puppet diríamos:

"Garanta que exista /var/www e que tenha permissões que correspondam com www-data:www-data"

A diferença aqui é que esses manifestos podem ser executados múltiplas vezes (em um cron job a cada hora ou diariamente) para deixar tudo atualizado, e não haverá resultados inesperados de algo tentando ser instalado duas vezes.

Ele também irá testar se tudo está rodando como esperado, pois se alguma dessas regras falhar serão emitidos erros que são mais fáceis de rastrear do que rodar o grep numa grande quantidade de resultados de comandos bash. O Puppet irá mostrar erros grandes e vermelhos que deixarão você saber se o PHP não foi instalado ou um módulo específico não puder ser configurado.

#### Manifestos e Módulos

Os manifestos são um pouco confusos no início, mas depois de um tempo, eles começam a fazer sentido.

Para revisar um exemplo básico:

```puppet
file {'testfile':
  path    => '/tmp/testfile',
  ensure  => present,
  mode    => 0640,
  content => "I'm a test file.",
}
```

Não é preciso explicar o que está acontecendo aqui, certo?

Esse arquivo pode ser referenciado mais para a frente no seu manifesto como "testfile", o que indica que ele pode ser listado como uma dependência para outras ações.

Para exemplos mais complexos, vamos referenciar os [manifestos Puppet](http://github.com/pyrocms/devops-puppet) do [PyroCMS](http://www.pyrocms.com/) no GitHub.

```puppet
include apache
$docroot = '/vagrant/www/pyrocms/'
$db_location = "/vagrant/db/pyrocms.sqlite"
# Apache setup
class {'apache::php': }
apache::vhost { 'local.pyrocms':
    priority => '20',
    port => '80',
    docroot => $docroot,
    configure_firewall => false,
}
a2mod { 'rewrite': ensure => present; }
```

Ele inclui o módulo "apache", define algumas variáveis, executa o manifesto extra "apache:php" no módulo apache, cria um virtual host e garante que o "mod_rewrite" está habilitado.

Todas essas classes são definidas no módulo Apache que incluímos.

Continuando, também queremos instalar o PHP:

```puppet
include php
php::module { ['xdebug', 'pgsql', 'curl', 'gd'] :
    notify => [ Service['httpd'], ],
}
php::conf { [ 'pdo', 'pdo_pgsql']:
    require => Package['php5-pgsql'],
    notify  => Service['httpd'],
}
```

Esse trecho do manifesto irá instalar as extensões PHP que precisamos e depois a opção notify informará ao Apache que você instalou novas configurações, indicando que ele deve reiniciar.

```puppet
include postgresql
class {'postgresql::server': }
postgresql::db { 'pyrocms':
    owner     => 'pyrocms',
    password => 'password',
}
```

Aqui será configurado um servidor postgres, criado um banco de dados chamado "pyrocms" e garantir que exista um usuário "pyrocms" com a senha informada.

Perto do fim! O último passo é garantir que você tenha arquivos e pastas com permissões de escrita definidos corretamente:

```puppet
file { $docroot:
    ensure  => 'directory',
}
file { "${docroot}system/cms/config/config.php":
    ensure  => "present",
    mode    => "0666",
    require => File[$docroot],
}
$writeable_dirs = ["${docroot}system/cms/cache/", "${docroot}system/cms/config/", "${docroot}addons/", "${docroot}assets/cache/", "${docroot}uploads/"]
file { $writeable_dirs:
    ensure => "directory",
    mode   => '0777',
    require => File[$docroot],
}
```

Isso irá garantir que exista um document root do Apache, que o arquivo de configuração esteja configurado como 0666 e que algumas pastas estejam como 777.

E aí temos tudo!

Se tudo funcionou corretamente, você deve estar vendo vários linhas de texto azul sinalizando cada coisa que está sendo instalada mas, se algo der errado, verá linhas vermelhas. Pesquise no Google sobre esses erros e tente novamente.

Os módulos usados aqui são: [Apache](http://github.com/puppetlabs/puppetlabs-apache), [Postgres](http://github.com/akumria/puppet-postgresql) e [PHP](http://github.com/saz/puppet-php), e você pode ver tudo em ação clonando o repositório Vagrant do PyroCMS:

```sh
git clone --recursive git://github.com/pyrocms/devops-vagrant.git ~/vagrant/pyrocms
cd ~/vagrant/pyrocms
vagrant up
```

Aponte seu navegador para http://localhost:8089/ e você deve enxergar o instalador. Bem fácil, não?

_**Nota:**_ Será instalado o MySQL pois o suporte ao Postgres e ao SQLite no PyroCMS ainda está em desenvolvimento, esperando algumas funcionalidades PDO ficarem prontas no CodeIgniter. Se você estiver interessado, pode experimentar alterar o Vagrantfile para usar o manifesto ubuntu-apache2-pgsql-php5.pp, destruir a instância e em seguida iniciá-la novamente. O submódulo pyrocms também precisará de um checkout do git em [feature/pdo](https://github.com/pyrocms/pyrocms/tree/feature/pdo).

### Sumário

Nesse artigo, usamos o Vagrant, o VirtualBox e o Puppet para, não apenas configurar uma instância de um servidor para trabalharmos, mas criarmos um suite de testes para nosso servidor garantir que tudo esteja corretamente executando, instalado e configurado.

Também criamos um checklist para os requisitos e, no futuro, poderemos criar qualquer número de servidores iguais a esse em minutos, e não em horas!

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com).
