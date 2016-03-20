---
date: 2016-03-20T03:22:00-03:00
title: 'Gerenciamento de Recursos de Hardware no Docker e Como Instalar Pacotes de Sistema Operacional no docker-machine'
categories:
    - Docker
tags:
    - docker
    - docker-machine
    - boot2docker
    - darkmira-tour
    - phpsp
    - package-manager
    - gerenciador-pacotes
    - apt
    - yum
    - tce-load
---

Olá pessoal!

Se quiser ir direto para a resposta a pergunta título, vá para <a href="{{ site.url }}{{ page.url }}/#acessando-a-vm-via-docker-machine-ssh">essa parte do artigo</a>. Primeiro eu vou contar por que precisei aprender a fazer isso.

### De onde surgiu a necessidade?

Estava vendo os slides do Wellington Silva da apresentação [Aplicações 12 Fatores - Melhor com Docker](https://speakerdeck.com/wsilva/12-factor-melhor-com-docker) que ele fez no [Darkmira Tour PHP 2016](https://br.darkmiratour.com/), onde ele faz de forma exemplar as relações entre a [metodologia 12 factor](http://12factor.net/), da galera da Heroku, com o [docker](https://www.docker.com/). Como estou cada dia mais conhecendo docker, me espantei quando ele mostrou dois comandos: `docker run ... --memory=512M` e `docker update --memory=1GB ...`.

No mundo da virtualização é normal pensar na definição da capacidade de Hardware (além dos Softwares e Sistema Operacional) que serão reservadas para aquela máquina virtual. Costumamos fazer ou na interface gráfica da ferramenta, ou então via scripts diretos na CLI do [hypervisor](https://en.wikipedia.org/wiki/Hypervisor) ou ainda por meio do [Vagrant](https://www.vagrantup.com/). Assim, quando pensamos na VM já temos essa definição do "tamanho dos recursos": quantidade de CPUs, quantidade de memória RAM, quantidade de disco etc.

Já no mundo do docker sempre percebi que o foco é mais na aplicação e serviços rodando dentro do container. Pensei: mas no Dockerfile nunca vi serem feitos essas definições de recurso: o arquivo geralmente é feito pensando mais no código e instalações da camada de software (faço um paralelo aqui com o Vagrantfile, onde as duas situações podem ser tratatadas). Fui buscar mais informações, e achei duas fontes interessantes. A primeira é o artigo [Resource management in Docker](https://goldmann.pl/blog/2014/09/11/resource-management-in-docker/), onde Marek Goldmann faz uma visão geral sobre `cgroups` e como é possível gerenciar CPU, memória e disco nos containers.

O segundo foi um [repositório no GitHub](https://github.com/agileek/docker/tree/master/cpuset-test), o contendo o Dockerfile da imagem docker [`agileek/cpuset-test`](https://hub.docker.com/r/agileek/cpuset-test/) para que fosse possível testar de forma rápida pelo menos a flag `--cpuset-cpus` do comando `docker run`. No vídeo de apresentação da imagem o negócio é quase instantâneo: ele roda o container e as cpus começam a fritar. E usando a flag `--cpuset-cpus`, você só faz uma parte delas fritar, e tudo é possível acompanhar por exemplo pelo [htop](http://hisham.hm/htop/).

É isso que fui fazer. Como a imagem é bem pequena (1.5MB apenas, é só um binário em golang, ele roda o [cpuburn](https://github.com/patrickmn/cpuburn) lá dentro), tudo parecia que ia ser muito rápido.

Como estou usando o OS X, primeiro subi minha docker-machine:

```
$ dockerup

# é um alias de docker-machine start dev && eval "$(docker-machine env dev)"
# e só criei isso pois sou fã de Vagrant e do "vagrant up" ;-)
```

Em seguida já fui rodar o `docker run` e, como não tinha a imagem ainda na minha máquina, ela foi baixada e já começou a executar:

```
$ docker run -it --rm --cpuset-cpus=0,1 agileek/cpuset-test

Unable to find image 'agileek/cpuset-test:latest' locally
latest: Pulling from agileek/cpuset-test
acc9a6499096: Pull complete
97ff6384ee3c: Pull complete
Digest: sha256:b1217ec9cf830819904b1e79c1b9c5acad07235bc8576bfb634d840d36995bed
Status: Downloaded newer image for agileek/cpuset-test:latest
Burning 8 CPUs/cores
10 seconds
20 seconds
30 seconds
40 seconds
...
```

Abri um outro terminal, e como tenho um i7 quadcore (8 cores hyperthreading), fui olhar o `htop` para monitorar o uso de CPU. Ali em cima tinha pedido para ele fritar dois dos núcleos, o 0 e o 1:

![htop via os x](assets/images/2016/03/1-htop-osx.png)

![htop via os x](assets/images/2016/03/2-htop-osx.png)

Ué? Não apareceu o que eu estava esperando. Ele parecia estar fazendo o stress em quatro cores, e não nos dois como eu havia pedido.

### Docker-machine: VM que permite usar docker em sistemas não-Linux

Aí lembrei que, por estar no OS X, o docker engine/daemon (que é afetado pelo `docker run`) não está diretamente no meu computador: ele está dentro do docker-machine. O [docker-machine](https://docs.docker.com/machine/) é a máquina virtual oficial do docker para possamos usar os containers de Linux (sobre o qual o docker é baseado) em outras sistemas operacionais.

A existência dessa camada ficou mais clara quando vi qual processo que estava consumindo aquele monte de CPU: era o VBoxHeadless, do VirtualBox, justo o hypervisor onde a VM está rodando. Fui até olhar como estava a configuração da VM via GUI:

![PHP Experience capa](assets/images/2016/03/virtualbox-gui-cpus-docker-machine-dev.png)

### Acessando a VM via docker-machine ssh

Tranquilo então, era só entrar na VM e rodar o `htop` por lá. Meu foco era apenas enxergar como que se refleteria o ajuste de CPUs no sistema operacional hospedeiro do docker (para quem usa Linux, ele próprio, para outros SOs, o Linux da VM do docker-machine) depois do comando `docker run` e a flag `--cpuset.

```
$ docker-machine ssh dev

                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/
 _                 _   ____     _            _
| |__   ___   ___ | |_|___ \ __| | ___   ___| | _____ _ __
| '_ \ / _ \ / _ \| __| __) / _` |/ _ \ / __| |/ / _ \ '__|
| |_) | (_) | (_) | |_ / __/ (_| | (_) | (__|   <  __/ |
|_.__/ \___/ \___/ \__|_____\__,_|\___/ \___|_|\_\___|_|
Boot2Docker version 1.10.3, build master : 625117e - Thu Mar 10 22:09:02 UTC 2016
Docker version 1.10.3, build 20f81dd
docker@dev:~$
```

Lá dentro fui rodar o `htop` e apareceu comando não encontrado:

```
docker@dev:~$ htop

-sh: htop: not found
```

Tudo bem: fui tentar instalar o htop via `apt-get` ou `yum`, mas nenhum dos dois também estavam disponíveis:

```
docker@dev:~$ apt-get install htop

-sh: apt-get: not found

docker@dev:~$ yum install htop

-sh: yum: not found
```

O que acontece é que é a distribuição Linux da docker-machine não é nem Debian-like (que costumam usar `apt-get`) nem RedHat-like (que costumam usar `yum`). A distribuição Linux que é utilizada é a Tiny Core Linux, que usa como gerenciador de pacotes a ferramenta `tce-load` (segue [lista contendo vários dos pacotes oficiais](http://distro.ibiblio.org/tinycorelinux/tcz_2x.html)).

Então, para finalmente completar a instalação foi só rodar:

```
docker@dev:~$ tce-load -wi htop

htop.tcz.dep OK
Downloading: ncurses.tcz
Connecting to repo.tinycorelinux.net (89.22.99.37:80)
ncurses.tcz          100% |***************************************************|   196k  0:00:00 ETA
ncurses.tcz: OK
Downloading: htop.tcz
Connecting to repo.tinycorelinux.net (89.22.99.37:80)
htop.tcz             100% |***************************************************|   116k  0:00:00 ETA
htop.tcz: OK
```

E agora, abrir o `htop`:
```
docker@dev:~$ htop

Error opening terminal: xterm-256color.
```

Puxa, mais um erro. Agora o problema era com a váriavel de ambiente $TERM. Foi só mudá-la para `xterm` da seguinte forma:

```
$ export TERM=xterm
```

E agora, de uma vez por todas, abrir o `htop`, e tudo funcionar!

```
docker@dev:~$ htop

# HTOP instalado via gerenciador de pacotes tce-load
```

### Teste efetivo do docker run com a flag --cpuset-cpus

Agora sim, consegui testar  aquela imagem docker com flag `--cpuset-cpus` do `docker run` e ver tudo acontecendo:

![htop na vm docker-machine](assets/images/2016/03/1-htop-docker-machine.png)

![htop na vm docker-machine](assets/images/2016/03/2-htop-docker-machine.png)

![htop na vm docker-machine](assets/images/2016/03/3-htop-docker-machine.png)

![htop na vm docker-machine](assets/images/2016/03/4-htop-docker-machine.png)

![htop na vm docker-machine](assets/images/2016/03/5-htop-docker-machine.png)

![htop na vm docker-machine](assets/images/2016/03/6-htop-docker-machine.png)

### Considerações finais

Primeiro, o docker está me fazendo aprender um monte de coisas, e isso é muito bom!

Aqui, vimos primeiro que é possível sim fazer o gerenciamento de recursos em nível de hardware nos containers usando flags nos comandos que interagem com o docker engine/daemon, por exemplo o `docker run --cpuset-cpus`.

Em seguida, percebemos que se existir uma camada de VM, os recursos que estão sendo gerenciados (como CPU, memória ou disco) não são da máquina hospedeira diretamente, mas sim dessa máquina virtual.

Também que a distribuição Linux usada na VM criada pelo docker-machine é a Tiny Core Linux, que usa como gerenciador de pacotes o `tce-load`, e se for preciso, conseguimos fazer as instalações necessárias.

Sobre a instalação de pacotes nesse sistema operacional, um ponto importante é que tudo que você fez será perdido na próxima atualização do docker-machine, que entende quaisquer alterações no SO feita pelo usuário como efêmeras, trazendo sempre uma nova versão com apenas os pacotes de fábrica. O que isso tudo quer dizer? Anote bem os comandos que você fizer quando usar o `tce-load` para poder reutilizá-los no futuro, quem sabe num [Gist](https://gist.github.com/).

É isso aí, até a próxima!


---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com/).
