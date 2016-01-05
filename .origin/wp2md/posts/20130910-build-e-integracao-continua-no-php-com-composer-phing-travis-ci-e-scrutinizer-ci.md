title: Build e Integração Contínua no PHP com Composer, Phing, Travis-CI e Scrutinizer-CI
link: http://rogeriopradoj.com/2013/09/10/build-e-integracao-continua-no-php-com-composer-phing-travis-ci-e-scrutinizer-ci/
author: rogeriopradoj
description: 
post_id: 422
created: 2013/09/10 18:49:40
created_gmt: 2013/09/10 21:49:40
comment_status: open
post_name: build-e-integracao-continua-no-php-com-composer-phing-travis-ci-e-scrutinizer-ci
status: publish
post_type: post

# Build e Integração Contínua no PHP com Composer, Phing, Travis-CI e Scrutinizer-CI

Olá, pessoal, Há tempos que não fazia uma limpeza no [meu Github](https://github.com/rogeriopradoj), seja para excluir projetos que não fazem mais sentido, forks que não ia mais utilizar, ou mesmo para atualizar algum repositório e me lembrar de tudo que venho estudando desde que conheci o Github (segundo o site dos caras, outubro de 2010). 

![](https://travis-ci.org/rogeriopradoj/ManoWars.png?branch=master) ![](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/badges/quality-score.png?s=f1b7894e3ada78b8ea81da9f790ea7e3b89f8779) ![](https://scrutinizer-ci.com/g/rogeriopradoj/ManoWars/badges/coverage.png?s=ee15ca0f9e783a480f056ff32247a044477b00d6)

E foi no meio dessa limpeza (na verdade bem no começo mesmo :-) ) que achei o <https://github.com/rogeriopradoj/ManoWars>, fork de um projeto criado pelo [Rafael Dohms](https://github.com/rdohms) e pelo [Augusto Pascutti](https://github.com/augustohp) há muito tempo para ensinar sobre Testes Unitários e Integração Contínua. Foi aí que pensei: porque não dar uma relembrada no assunto, e também atualizar com coisas que tenha aprendido nesse período (poxa, são quase 3 anos!)? 

### Phing???

![Logo Phing](http://www.phing.info/trac/chrome/site/logo.gif) Muita coisa ainda não havia tocado, caso do [Phing](http://www.phing.info/), que o [Hussani](https://speakerdeck.com/hussani/automacao-e-deploy-com-phing) e o [Duodraco](http://www.slideshare.net/duodraco/phing-14008532) já haviam apresentado mais de uma vez em palestras. Também não estava muito habituado com as ferramentas para geração de relatórios de métricas, como o [PHPMD](http://phpmd.org/), ou o [PDepend](http://pdepend.org/). Mas aí estava a graça, um bom desafio! E com a ótima estrutura que o Dohms e o Pascutti haviam deixado, não foi tão difícil começar. 

### Composer

![Composer logo](http://getcomposer.org/img/logo-composer-transparent.png) A primeira coisa que fiz foi usar o [Composer](http://getcomposer.org/) para gerenciar as dependências do projeto. Aqui uma decisão tinha que ser tomada: o projeto foi todo baseado em PHP 5.2+, e eu poderia continuar deixando essa versão como a mínima necessária. Só que muitas das ferramentas de métricas e o próprio PHPUnit que hoje está disponível via Composer é apenas 5.3+. Então decidi subir para 5.3 a dependência mínima. Como o Composer além de gerenciar as dependências também gera um autoloader completo (tanto com o código do meu projeto quanto das dependências), pude retirar sem dó o Zend/Loader que estava no projeto, pois ele não era mais necessário. E com um mágico `$ composer install` estava lá: todas as dependências na pasta vendor, um autoloader funcional completo, e o melhor, todas as ferramentas binárias (PHPUnit, PHPPdepend etc., e o próprio Phing) já disponíveis também na pasta vendor/bin. É, o Composer é uma mão na roda! E lógico, com o PHP 5.4+ com servidor web embutido, foi brincadeira de criança subir testar a aplicação rodando no navegador, só com um `$ php -S localhost:8080 -t public`. 

### Estrututura de pastas e arquivos

Como o Composer coloca todas as dependências dentro da pasta vendor na raiz, e é meio que padrão os projetos PHP que vejo deixarem uma estrutura baseada na raiz também, mudei um pouquinho as pastas de lugar. A maior mudança foi colocar as pastas que estavam dentro de ManoWars na raiz, assim a hierarquia ficou um pouco menor. 

  * /libs: contém o código da aplicação
  * /public: o document root do servidor web
  * /tests: testes unitários
  * init.php: bootstrap da aplicação (usado tanto na aplicação web quanto nos testes)

### phpunit.xml.dist

Já havia lido sobre a vantagem de usar o phpunit.xml.dist no artigo [[Best practice] How to ship PHPUnit configuration](http://www.testically.org/2010/08/24/best-practice-how-to-ship-phpunit-configuration/) do [test.ical.ly](http://www.testically.org/), e até já mandei um [Pull Request](https://github.com/iMastersDev/oportunidades/commit/2b86607230644a0eebc22fe9174ae27434d9a8ae) para o [Ophportunidades](https://github.com/iMastersDev/oportunidades) sobre isso. Então foi um passo para criar um arquivo de configuração para o PHPUnit, já desde o começo um .dist. **Vantagem:** agora para rodar o phpunit não é preciso entrar na pasta tests, é só rodar a partir da raiz. Outro ponto, não é mais necessário o arquivo AllTests.php, pois a definição da suíte de testes é feita também nesse arquivo de configuração. 

### PHP CodeSniffer

Uma task do Phing que não estava sendo executada era a de verificação do padrão de codificação, com o [phpcs](https://github.com/squizlabs/PHP_CodeSniffer). Pensei em colocar o padrão [PSR2](http://www.php-fig.org/psr/2/) logo de cara, mas como o projeto foi feito a muito tempo, muitos erros iriam aparecer. Preferi deixar com o padrão [Zend](http://framework.zend.com/manual/1.12/en/coding-standard.coding-style.html) que foi provavelmente o que o Dohms e o Pascutti usaram. Na minha lista de tarefas está evoluir o padrão para PSR2. 

### Outras ferramentas

Todas as ferramentas que estão sendo usadas para métricas, testes e build estão no [composer.json](https://github.com/rogeriopradoj/ManoWars/blob/master/composer.json), dê uma olhada lá, ok? 

### README

E no LEIAME do projeto a principal mudança foi trocar o formato para [Markdown](http://daringfireball.net/projects/markdown/) (na verdade o [GFM](https://help.github.com/articles/github-flavored-markdown)) que é uma beleza para escrever e o Github já faz a renderização muito bem para HTML. 

### Ferramentas de Integração Contínua Online (Travis e Scrutinizer)

Depois de todos os pequenos ajustes, era hora de mexer de verdade no projeto. A primeira coisa que percebi é que tinham poucos testes falhando. Tinha a ver com a API do PHPUnit ter mudado, e com um teste que esperava nulo, mas na verdade o método retornava um inteiro. Fiz o ajuste nos testes e eles passaram a funcionar.

## Comments

**[Elton Minetto](#1596 "2013-09-11 13:46:00"):** Ótimo post, parabéns Vou começar a usar o ManoWars para explicar PHPUnit nas aulas

**[Hussani Oliveira](#1597 "2013-09-11 15:53:00"):** Ótimo post Rogério! ManoWars não é um nome estranho para mim, mas eu não conhecia o projeto em si. Parabéns pelo post!

**[Rogerio Prado de Jesus](#1599 "2013-09-12 08:37:00"):** Valeu, Hussani! Viu que fiz a referência à sua palestra, hein? Só uma coisa: instalação do Phing via composer, hehehe! Agora com o composer global, acho que vai ser mais difícil ainda instalar algo via PEAR (a não ser extensões C, mesmo). Até mais!

**[Rogerio Prado de Jesus](#1600 "2013-09-12 08:39:00"):** Opa, valeu Minetto! Só reforçar que o projeto ManoWars é do Rafael Dohms e do Augusto Pascutti, o crédito da ideia tem que ser dado todo para eles! Até mais!

