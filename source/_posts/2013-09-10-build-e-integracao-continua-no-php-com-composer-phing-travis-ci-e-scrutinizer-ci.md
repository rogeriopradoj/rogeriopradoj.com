---
date: 2013-09-10 21:49:40+00:00
title: Build e Integração Contínua no PHP com Composer, Phing, Travis-CI e Scrutinizer-CI
categories:
  - Geral
  - PHP
tags:
  - composer
  - phing
  - php
  - phpcs
  - scrutinizer
  - travis
---

Olá, pessoal,

Há tempos que não fazia uma limpeza no [meu GitHub](https://github.com/rogeriopradoj), seja para excluir projetos que não fazem mais sentido, forks que não ia mais utilizar, ou mesmo para atualizar algum repositório e me lembrar de tudo que venho estudando desde que conheci o GitHub (segundo o site dos caras, outubro de 2010).


[![](https://travis-ci.org/rogeriopradoj/ManoWars.png?branch=master)](https://travis-ci.org/rogeriopradoj/ManoWars) [![](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/badges/quality-score.png?s=f1b7894e3ada78b8ea81da9f790ea7e3b89f8779)](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/) [![](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/badges/coverage.png?s=ee15ca0f9e783a480f056ff32247a044477b00d6)](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/)


E foi no meio dessa limpeza (na verdade bem no começo mesmo :-) ) que achei o [https://github.com/rogeriopradoj/ManoWars](https://github.com/rogeriopradoj/ManoWars), fork de um projeto criado pelo [Rafael Dohms](https://github.com/rdohms) e pelo [Augusto Pascutti](https://github.com/augustohp) há muito tempo para ensinar sobre Testes Unitários e Integração Contínua.

Foi aí que pensei: porque não dar uma relembrada no assunto, e também atualizar com coisas que tenha aprendido nesse período (poxa, são quase 3 anos!)?

### Phing???

[![Logo Phing](https://www.phing.info/trac/chrome/site/logo.gif)](https://www.phing.info/)

Muita coisa ainda não havia tocado, caso do [Phing](https://www.phing.info/), que o [Hussani](https://speakerdeck.com/hussani/automacao-e-deploy-com-phing) e o [Duodraco](http://www.slideshare.net/duodraco/phing-14008532) já haviam apresentado mais de uma vez em palestras. Também não estava muito habituado com as ferramentas para geração de relatórios de métricas, como o [PHPMD](http://phpmd.org/), ou o [PDepend](http://pdepend.org/).

Mas aí estava a graça, um bom desafio! E com a ótima estrutura que o Dohms e o Pascutti haviam deixado, não foi tão difícil começar.

### Composer

[![Composer logo](https://getcomposer.org/img/logo-composer-transparent.png)](http://getcomposer.org/)

A primeira coisa que fiz foi usar o [Composer](https://getcomposer.org/) para gerenciar as dependências do projeto.

Aqui uma decisão tinha que ser tomada: o projeto foi todo baseado em PHP 5.2+, e eu poderia continuar deixando essa versão como a mínima necessária. Só que muitas das ferramentas de métricas e o próprio PHPUnit que hoje está disponível via Composer é apenas 5.3+. Então decidi subir para 5.3 a dependência mínima.

Como o Composer além de gerenciar as dependências também gera um autoloader completo (tanto com o código do meu projeto quanto das dependências), pude retirar sem dó o Zend/Loader que estava no projeto, pois ele não era mais necessário.

E com um mágico `$ composer install` estava lá: todas as dependências na pasta vendor, um autoloader funcional completo, e o melhor, todas as ferramentas binárias (PHPUnit, PHPPdepend etc., e o próprio Phing) já disponíveis também na pasta vendor/bin.

É, o Composer é uma mão na roda!

E lógico, com o PHP 5.4+ com servidor web embutido, foi brincadeira de criança subir testar a aplicação rodando no navegador, só com um `$ php -S localhost:8080 -t public`.

### Estrututura de pastas e arquivos

Como o Composer coloca todas as dependências dentro da pasta vendor na raiz, e é meio que padrão os projetos PHP que vejo deixarem uma estrutura baseada na raiz também, mudei um pouquinho as pastas de lugar. A maior mudança foi colocar as pastas que estavam dentro de ManoWars na raiz, assim a hierarquia ficou um pouco menor.

  * /libs: contém o código da aplicação


  * /public: o document root do servidor web


  * /tests: testes unitários


  * init.php: bootstrap da aplicação (usado tanto na aplicação web quanto nos testes)

### phpunit.xml.dist

Já havia lido sobre a vantagem de usar o phpunit.xml.dist no artigo [[Best practice] How to ship PHPUnit configuration](http://www.testically.org/2010/08/24/best-practice-how-to-ship-phpunit-configuration/) do [test.ical.ly](http://www.testically.org/), e até já mandei um [Pull Request](https://github.com/iMastersDev/oportunidades/commit/2b86607230644a0eebc22fe9174ae27434d9a8ae) para o [Ophportunidades](https://github.com/iMastersDev/oportunidades) sobre isso.

Então foi um passo para criar um arquivo de configuração para o PHPUnit, já desde o começo um .dist.

**Vantagem:** agora para rodar o phpunit não é preciso entrar na pasta tests, é só rodar a partir da raiz. Outro ponto, não é mais necessário o arquivo AllTests.php, pois a definição da suíte de testes é feita também nesse arquivo de configuração.

### PHP CodeSniffer

Uma task do Phing que não estava sendo executada era a de verificação do padrão de codificação, com o [phpcs](https://github.com/squizlabs/PHP_CodeSniffer). Pensei em colocar o padrão [PSR2](http://www.php-fig.org/psr/psr-2/) logo de cara, mas como o projeto foi feito a muito tempo, muitos erros iriam aparecer. Preferi deixar com o padrão [Zend](http://framework.zend.com/manual/1.12/en/coding-standard.coding-style.html) que foi provavelmente o que o Dohms e o Pascutti usaram.

Na minha lista de tarefas está evoluir o padrão para PSR2.

### Outras ferramentas

Todas as ferramentas que estão sendo usadas para métricas, testes e build estão no [composer.json](https://github.com/rogeriopradoj/ManoWars/blob/master/composer.json), dê uma olhada lá, ok?

### README

E no LEIAME do projeto a principal mudança foi trocar o formato para [Markdown](https://daringfireball.net/projects/markdown/) (na verdade o [GFM](https://help.github.com/articles/github-flavored-markdown)) que é uma beleza para escrever e o GitHub já faz a renderização muito bem para HTML.

### Ferramentas de Integração Contínua Online (Travis e Scrutinizer)

Depois de todos os pequenos ajustes, era hora de mexer de verdade no projeto.

A primeira coisa que percebi é que tinham poucos testes falhando. Tinha a ver com a API do PHPUnit ter mudado, e com um teste que esperava nulo, mas na verdade o método retornava um inteiro. Fiz o ajuste nos testes e eles passaram a funcionar.

Agora era hora de resolver todos os outros problemas do código: padrão de codificação, aumentar cobertura de testes, complexidade, etc. etc., tudo relacionado a [QA/Garantia de Qualidade](http://phpqatools.org/). Também analisar os relatórios gerados, uma parte interessante que nunca tinha olhado mais de perto.

Mas por que não ser [um pouco poser e colocar um monte de badges no projeto](https://poser.pugx.org/)? Esses badges seriam para mostrar a evolução do projeto, e fui atrás das ferramentas online que me permitiriam isso

#### Travis

[![Logo do Travis](assets/images/2013/09/travis-logo.png)](https://travis-ci.org/)

Comecei pela mais conhecida, o [Travis-CI](https://travis-ci.org/), que já tinha usado em outros projetos. Nele começei colocando o PHPUnit para rodar, nas 3 últimas grandes versões do PHP, 5.3, 5.4 e 5.5.

O Travis conta com um conceito interessante de [matriz de build](https://docs.travis-ci.com/user/customizing-the-build/#Build-Matrix), onde você cruza algumas configurações e o build é feito em todas as combinações dela. Isso me ajudou no passo seguinte.  O Travis já tem um executável do PHPUnit disponível para usarmos, mas eu gostaria de rodar o PHPUnit instalado pelo Composer também. Fácil: criei uma variável de ambiente RUN, que no primeiro momento era definida como phpunit, e no segundo momento como vendor/bin/phpunit. E o Travis se encarregou de rodar os builds 6 vezes (3 versões do PHP x 2 PHPUnit diferentes).

No fim, coloquei mais uma definição para a variável de ambiente RUN como vendor/bin/phing, e o Phing inteiro foi rodado lá no Travis, muito bacana!

#### Scrutinizer

[![Logo do scrutinizer](assets/images/2013/09/scrutinizer-logo.png)](https://scrutinizer-ci.com/)

Só um problema: o Travis sozinho não avalia os relatórios gerados. Foi aí que peguei o [Scrutinizer-CI](https://scrutinizer-ci.com/), que já havia também [usado anteriormente](https://scrutinizer-ci.com/g/rogeriopradoj/base-php-codingdojo-vagrant/inspections), mas quando o [Alexandre Eher](http://eher.com.br/) lembrou dele no [PHPSPub de agosto/2013](http://phpsp.org.br/?s=phpub), vi que era uma boa ideia usá-lo de verdade.

Depois de bater um pouco de cabeça, consegui fazer a maioria das métricas serem executadas, e no fim, o que mais queria: os badges!!!

[![](https://travis-ci.org/rogeriopradoj/ManoWars.png?branch=master)](https://travis-ci.org/rogeriopradoj/ManoWars)
*Travis*

[![](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/badges/quality-score.png?s=f1b7894e3ada78b8ea81da9f790ea7e3b89f8779)](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/)
*Scrutinizer - Quality*

[![](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/badges/coverage.png?s=ee15ca0f9e783a480f056ff32247a044477b00d6)](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/)
*Scrutinizer - Coverage*

---

E para renderizar o README um pouco melhor, e lógico que usando outra ferramenta online, fui de [DocumentUp](https://documentup.com/rogeriopradoj/manowars).

---

É isso aí, pessoal, escrevi bastante e tem bastante coisa para fazer ainda.

Se quiser acompanhar, lá no [https://github.com/rogeriopradoj/ManoWars](https://github.com/rogeriopradoj/ManoWars).

Até mais!

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](https://rogeriopradoj.com).
