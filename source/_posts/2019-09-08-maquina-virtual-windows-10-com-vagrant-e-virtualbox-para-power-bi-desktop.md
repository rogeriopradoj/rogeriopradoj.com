---
date: 2019-09-08 23:44:00-03:00
title: "Máquina virtual Windows 10 com Vagrant e VirtualBox para Power BI Desktop"
categories:
    - Data Science
tags:
    - máquina virtual
    - vm
    - windows
    - windows 10
    - vagrant
    - virtualbox
    - power bi
    - power bi desktop
    - chocolatey
social_image: /assets/images/2019/09/08-maquina-virtual-windows-10-com-vagrant-e-virtualbox-para-power-bi-desktop.png
---

<figure>
    <img title="Máquina virtual Windows 10 com Vagrant e VirtualBox para Power BI Desktop" src="/assets/images/2019/09/08-maquina-virtual-windows-10-com-vagrant-e-virtualbox-para-power-bi-desktop.png" alt="Máquina virtual Windows 10 com Vagrant e VirtualBox para Power BI Desktop">
    <figcaption>Máquina virtual Windows 10 com Vagrant e VirtualBox para Power BI Desktop</figcaption>
</figure>


Olá, pessoal.

Nesse mundo de aprendizagem sobre Data Science Analytics, as ferramentas de self-service BI e visualização são essenciais. Dentre elas, o Power BI Desktop, da Microsoft, é uma das opções profissionais mais usadas. Dois motivos me fizeram buscar mais conhecimento sobre ela e me capacitar com treinamentos: ser gratuita para uso básico em sua máquina pessoal e por ser um dos aplicativos homologados na empresa onde trabalho.

Segundo a própria Microsoft, "O Power BI é um conjunto de ferramentas de análise de negócios para analisar dados e compartilhar ideias." Se quiser saber mais sobre a solução:

- [Treinamentos Microsoft](https://powerbi.microsoft.com/pt-br/learning/)
- [Curso gratuito da Data Science Academy: Microsoft Power BI para Data Science](https://www.datascienceacademy.com.br/course?courseid=microsoft-power-bi-para-data-science)

## E como instalar o Power BI Desktop na minha máquina para começar a usar?

Se você usa Windows, é fácil. Acesse [o site oficial](https://powerbi.microsoft.com), baixe o instalador da ferramenta e siga os passos de instalação. Mas, temos um problema: o que fazer se você usa outro sistema operacional? Como sair do outro lado caso você use macOS ou Linux? Fácil também: vamos de máquina virtual!

E, para facilitar nosso caminho, usando [Vagrant](https://www.vagrantup.com) e [VirtualBox](https://www.virtualbox.org) para configuração do nosso ambiente, e uma box de Windows 10 já configurada, a [peru/windows-10-enterprise-x64-eval](https://app.vagrantup.com/peru/boxes/windows-10-enterprise-x64-eval).

## VM: O que você precisa ter no seu computador?

- [VirtualBox](https://powerbi.microsoft.com);
- [Vagrant](https://www.vagrantup.com/).

## VM: Como criar e subir a máquina virtual?

Primeiro passo é criar o arquivo de manifesto com a configuração do seu ambiente, o [Vagrantfile](https://www.vagrantup.com/docs/vagrantfile/). Crie uma pasta para seu projeto e em seguida, no terminal:

```shell
# baixe um Vagrantfile já configurado com 4GB de RAM para a VM
wget https://gist.githubusercontent.com/rogeriopradoj/0b4ae77419dafef3d67526d63e914290/raw/8129df2332a4c7f831e543752aac6dc8546ed992/Vagrantfile

# ou rode o comando para criar o Vagrantfile
vagrant init peru/windows-10-enterprise-x64-eval
```

Após isso, suba seu ambiente, com o comando `vagrant up`.

## VM: Depois da máquina de pé, como acessá-la?

Dois caminhos: o primeiro é usar a tela de interface gráfica da VM que o VirtualBox vai ter aberto para você. O segundo, que é meu prefirido e recomendo, é abrir uma sessão RDP (área de trabalho remota). Para isso [busque algum aplicativo que tenha essa funcionalidade para seu sistema operacional](https://alternativeto.net/software/remote-desktop-connection/) e conecte no endereço `localhost`.

[Essa box](https://www.vagrantup.com/docs/boxes.html) de Windows 10 tem dois usuários configurados, você pode usar qualquer um deles para logar:

- username: localhost\Administrator - password: vagrant
- username: localhost\vagrant - password: vagrant

E é isso, depois de acessar a VM, siga os passos tradicionais para instalar o Power BI Desktop no ambiente!

## Bônus Chocolatey: Como instalar o Power BI Desktop usando o gerenciador de pacotes do Windows Chocolatey?

Primeiro, [instale o Chocolatey](https://chocolatey.org/install). Para quem não conhece-o: 

> ### What is Chocolatey?
> 
> Chocolatey is kind of like apt-get, but for Windows (with Windows comes limitations). It is a machine level package manager that is built on top of nuget command line and the nuget infrastructure.
> 
> -- <https://chocolatey.org/faq#what-is-chocolatey>

Depois, no terminal, execute:

```shell
choco upgrade powerbi
```

Talvez você pergunte: por que usar `upgrade` em vez de `install`? Posso te dizer que, caso seja a primeira instalação no seu ambiente, os dois comandos funcionam da mesma forma. A vantagem é para o caso que o aplicativo já estiver instalado, e estiver com versão antiga. Nesse caso, o chocolatey já faz a atualização para nós. Vale a pena ;-) .

## Considerações finais

E é isso! No fim de todos esses passos, terá um ambiente virtualizado perfeitamente montado com o Power BI Desktop rodando numa máquina virtual Windows 10 sobre Vagrant e VirtualBox!

É importante ressaltar que esse processo pode ser usado mesmo no caso que você o seu sistema operacional principal já seja o Windows 10, mas você quer deixar a instalação do Power BI Desktop o mais isolada possível do seu ambiente.

E o que você diz? Costuma usar ambientes virtualizados (máquinas virtuais ou containers) para seus trabalhos, ou prefere fazer as instalações diretamente no seu S.O.? Eu sempre que possível vou de ambientes virtualizados! Diga aí nos comentários sua opinião, ok?

Até a próxima, e podem me chamar para conversar em todos os canais!

Abraços!

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](https://rogeriopradoj.com/).
