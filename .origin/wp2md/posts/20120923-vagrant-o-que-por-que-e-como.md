title: Vagrant: O que, Por que e Como
link: http://rogeriopradoj.com/2012/09/23/vagrant-o-que-por-que-e-como/
author: rogeriopradoj
description: 
post_id: 254
created: 2012/09/23 22:23:45
created_gmt: 2012/09/24 01:23:45
comment_status: open
post_name: vagrant-o-que-por-que-e-como
status: publish
post_type: post

# Vagrant: O que, Por que e Como

Tradução livre de Vagrant: What, Why, and How, disponível em <http://net.tutsplus.com/tutorials/php/vagrant-what-why-and-how/>. \--- Este artigo te ajudará a usar o [Vagrant](http://vagrantup.com/) para administrar suas instâncias de máquinas virtuais e explicará como se beneficiar do [Puppet](http://puppetlabs.com/puppet/puppet-enterprise/) para fazer a provisão de vários recursos como o PHP e o PostgreSQL. [caption id="attachment_242" align="alignnone" width="322"]![garoto propaganda do vagrant](/wp-content/uploads/2012/07/Vagrant-Virtualized-development-for-the-masses..png) Garoto propaganda :-) da ferramenta Vagrant - http://vagrantup.com[/caption] 

### Introdução

Os desenvolvedores tem à disposição um grande número de maneiras de construir seu ambiente de desenvolvimento web. Podem ser usadas opções "locais", do tipo dos servidores "tudo em um"como o Zend Server, XAMPP, MAMP, WAMP etc; ou ainda como você instalando os componentes a partir dos fontes ou via um sistema de gerenciamento de pacotes, como o Homebrew, o Apt ou o Yum. Isso vai se acumulando a medida que você trabalha em vários projetos diferentes: PHP 5.3 e PHP 5.4, MySQL, SQLite, MongoDB, Postgres, PEAR, PHPUnit, Rails 3.1, Memcached, Redis, Gearman, NodeJS etc. E se você precisar  atualizar seu computador se ele pifar, você terá que começar tudo de novo. Pode ser usada uma configuração "remota", com um servidor com compartilhamentos "Samba" ou um servidor SSH montado com uma ferramenta como o [ExpanDrive](http://www.expandrive.com/). A última opção esbarra na latência de leitura e escrita dos arquivos, que é extremamente chata. É possível usar o SSH com o Vim para tudo, o que é rápido, mas só funciona se você quiser usar o Vim para tudo também. 

### Desenvolvimento vs Produção

Mesmo que você esteja feliz com a forma que vem fazendo as coisas até agora, quantas vezes você já ouviu (ou disse) "Bem, está funcionando no meu computador"? Isso é terrivelmente comum e acontece quando os ambientes diferem até mesmo nos detalhes mais triviais. É extremamente importante garantir que seu ambiente de desenvolvimento seja idêntico ao ambiente de produção, e que ele também corresponda ao servidores de staging e de teste se esses existirem. Isso pode parecer fácil se você pensar apenas na instalação do Apache, do PHP de alguma cópia do MySQL, porém existem milhões de fatores para avaliar. Se você estiver desenvolvendo no OSX e fazendo deploy num sistema Ubuntu, então você deve se deparar com problemas estranhos relacionados a maiúsculas. Isso é comum no CodeIgniter, quando alguém cria uma biblioteca com a primeira letra minúscula. Ela irá carregar corretamente no OSX, mas irá quebrar quando for implementada na produção. Seu processo de desenvolvimento pode ter feito você perder alguns contratos só por causa de algumas diferenças triviais entre sistemas operacionais que ninguém notou até ser muito tarde. 

### Desenvolvimento = Produção

Então qual é a solução? Forçar que todos os desenvolvedores joguem fora suas ferramentas e trabalhem todos no mesmo modelo de laptop? Se os seus colegas ganharem Macbooks novinhos em folha talvez você não ouça muitas reclamações, mas você teria que usar o OSX Server para tudo. Você poderia usar o Linux para tudo, mas entraria numa briga para decidir qual distribuição utilizar. Forçar os desenvolvedores para usar o mesmo sistema operacional gera problemas, reduz a produtividade e promove lutas de nerds. A virtualização é a resposta e isto não é nada novo, mas geralmente quando pensamos em virtualização pensamos nos problemas de performance e nas ventoinhas girando que nem malucas enquanto o sistema tenta rodar dois sistemas operacionais ao mesmo tempo. Essa situação pode ser verdade quando tentamos rodar o Windows em uma máquina não muito potente mas, hoje em dia, um Mac mediano com 4 GB de RAM de fábrica é mais do que suficiente para rodar uma instalação de um servidor Ubuntu em modo de linha de comando com todas ferramentas habituais (IDE, browser, ferramentas de depuração etc.). Existem diferentes versões de virtualização, mas eu prefiro o [VirtualBox](https://www.virtualbox.org/) da Oracle (que é grátis). Esse programa faz o "trabalho pesado" da virtualização, enquanto a ferramenta Vagrant serve para gerenciar as instâncias. 

### Passo 1 - **Instalando o VirtualBox**

Primeiro, [baixe e instale o VirtualBox](http://www.virtualbox.org/wiki/Downloads). Nos sistemas *nix (Mac OSX, Linux etc.) você precisará alterar seu .bash_profile (ou .zsh_profile) para estender a variável $PATH: https://gist.github.com/3768450 Isso permitirá que o Vagrant saiba onde o VirtualBox está instalado e, é claro, será diferente em cada sistema operacional. 

### Passo 2 - **Instalando o Vagrant**

Você pode baixar um [binário do vagrant](http://downloads.vagrantup.com/) para o seu sistema operacional, ou instalar ele como uma gem se não houver um binário disponível: https://gist.github.com/3768444 

### Passo 3 - **Criando uma Instância**

Crie um lugar para suas configurações ficarem: https://gist.github.com/3768740 Iremos usar o Ubuntu 12.04 LTS (Precise Pangolin), o qual já tem uma "box" configurada. https://gist.github.com/3768743 Aqui você enxerga o argumento "precise32", que é o apelido da URL. Agora você pode criar a instância que irá baixar o arquivo .box. https://gist.github.com/3768748 Agora ela estará rodando. Fácil! Se você quiser acessar a instância via SSH, use este comando: https://gist.github.com/3768750 

### Passo 4 - **Configuração**

Você terá um arquivo, chamado Vagrantfile, que conterá a configuração dessa instância: https://gist.github.com/3768755 Essa é, se você ainda não notou, sintaxe Ruby; por isso você pode ser bem criativo com o arquivo, apesar de aqui só termos o básico. Ele mostra qual apelido usar, e tem a URL para o caso do apelido não estar definido localmente (útil para casos de compartilhamento). As linhas share_folder são bem úteis para mapear pastas da instância com pastas locais. Usando nfs => true a instância será capaz de escrever e alterar permissões dos arquivos, o que é útil se você estiver, por exemplo, tentando instalar um CMS ali. O redirecionamento de portas permite que você acesse sua instância em http://localhost:8080 e, é claro, faça alterações para diferentes portas em caso de conflito. Esse arquivo de configuração também define o fuso horário para Europe/London, depois executa o apt-get update, que força seu sistema para se atualizar toda vez que ele é iniciado. Se você pular esse item da configuração, pode encontrar vários pacotes se recusando a instalar pois as referências estão desatualizadas. Quando você alterar a configuração, pode recarregar a instância para utilizá-la: https://gist.github.com/3768771 Agora que nossos servidores estão no ar e prontos para continuar, precisamos instalar neles alguns softwares. Não vamos só rodar o apt-get install em um monte de pacotes na linha de comando, vamos "provisionar" nossos servidores. 

### Passo 5 - **Provisionamento**

## Comments

**[Décio Rocha](#1592 "2013-08-20 14:01:00"):** Olá Rogério, estou tentando criar uma VM de uma box, pelo vagrant, mas, quando tento, dá um erro de gravação. Estou usando o Windows7, aqui o erro: E:>vagrant box add lampp 'quantal64.box' Downloading or copying the box... ←[0KAn error occurred while downloading the remote file. The error--:--) message, if any, is reproduced below. Please fix this error and try again. Failed writing body (0 != 16383) testei com outras boxes e continua o mesmo erro.

**[Rogerio Prado de Jesus](#1594 "2013-08-20 22:56:00"):** Olá Décio, parece que você está seguindo a informação da documentação oficial, em http://docs.vagrantup.com/v2/boxes.html, certo? É um chute só, mas acho que o problema está nas aspas. Vou pedir para você testar de dois jeitos: 1) Colocando o nome do seu arquivo .box sem as aspas, como: > vagrant box add lampp quantal64.box 2) Colocando o caminho completo do seu arquivo .box, digamos que ele esteja em na raiz do seu drive E: > vagrant box add lampp E:quantal64.box Diz aí para a gente depois o que rolou, ok? Até mais

**[jonatasmm](#1601 "2013-09-14 20:51:00"):** Estou com o mesmo problema..Já tentei fazer desse jeito e não funcionou.

**[Rogerio Prado de Jesus](#1602 "2013-09-15 10:56:00"):** Fiz algumas buscas e achei essa thread no repositório oficial: https://github.com/mitchellh/vagrant/issues/2056 Parece que isso sempre vai acontecer quando sua o caminho da sua pasta "HOME" do windows é multibyte (exemplo, tem algum acento, etc.). A pasta home é a pasta do seu usuário, ex: C:UsersMeuNome. É dentro dessa pasta que o Vagrant sua pasta de configuração padrão, `.vagrant.d` (mas que é possível mudar definindo a variável de ambiente VAGRANT_HOME no seu sistema). Segundo a discussão ali em cima, vocês (Décio Rocha e jonatasmm) deveriam usar a variável de ambiente VAGRANT_HOME colocando os arquivos em outro caminho. Exemplo: 1\. Copie sua pasta C:UsersSeuNome.vagrant.d para C:vagrant_home 2\. pelo terminal (prompt do DOS), digite: set VAGRANT_HOME=C:/vagrant_home \--- É isso aí! Digam depois o resultado, ok? Até mais!

**[jonatasmm](#1603 "2013-09-15 17:29:00"):** Funcionou aqui, vlw.

**[Rogerio Prado de Jesus](#1604 "2013-09-15 17:30:00"):** Que bom que ajudei! Falou!

**[Daniel](#1608 "2013-10-30 23:09:00"):** Opa Rogério, estou tentando iniciar o vagrant e está dando a seguinte mensagem: The specified host network collides with a non-hostonly network! This will cause your specified IP to be inaccessible. Please change the IP or name of your host only network to not match that of a bridged or non-hostonly network. O que fazer neste caso?

**[Rogerio Prado de Jesus](#1609 "2013-11-02 10:02:00"):** Olá, @disqus_HiAjtXoB4U:disqus, uma Googlada, deu os seguintes endereços: \- http://leafac.com/bugs/2013/05/21/vagrant-host-only-network-troubleshooting.html \- https://groups.google.com/forum/#!msg/vagrant-up/yGGnJymVmhM/czbcIggfnJEJ Tente uma das duas opções, veja se te ajuda, ok?

