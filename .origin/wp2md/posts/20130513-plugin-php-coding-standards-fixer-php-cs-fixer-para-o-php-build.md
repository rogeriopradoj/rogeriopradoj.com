title: Plugin PHP Coding Standards Fixer (php-cs-fixer) para o PHP-Build
link: http://rogeriopradoj.com/2013/05/13/plugin-php-coding-standards-fixer-php-cs-fixer-para-o-php-build/
author: rogeriopradoj
description: 
post_id: 395
created: 2013/05/13 09:53:41
created_gmt: 2013/05/13 12:53:41
comment_status: open
post_name: plugin-php-coding-standards-fixer-php-cs-fixer-para-o-php-build
status: publish
post_type: post

# Plugin PHP Coding Standards Fixer (php-cs-fixer) para o PHP-Build

Olá, pessoal! Depois do [plugin do Composer](http://documentup.com/rogeriopradoj/php-build-plugin-composer) para quem usa o [php-build do CHH](http://chh.github.io/php-build/) ([já tinha falado dele aqui](/2013/03/18/plugin-composer-para-o-php-build/) e [aqui](http://rogeriopradoj.com/2012/11/20/como-atualizar-a-versao-do-php-no-mac-osx-mountain-lion/)), consegui lançar mais um plugin: o [Plugin do PHP Coding Standards Fixer (php-cs-fixer)](http://documentup.com/rogeriopradoj/php-build-plugin-phpcsfixer). Primeiro vamos contar a história do php-cs-fixer: [caption id="attachment_400" align="alignnone" width="262"]![Logo do php-cs-fixer](http://rogeriopradoj.com/wp-content/uploads/2013/05/Screenshot_12_05_13_22_41.png) Logo do php-cs-fixer[/caption] Criado pelo [Fabien Potencier](http://fabien.potencier.org/), chefe da [Sensio Labs](http://sensiolabs.com/), o php-cs-fixer é uma ferramenta que corrige automaticamente um código fonte para seguir os padrões da [PSR2](http://www.php-fig.org/). Ele foi criado com foco na correção automática do código do [framework Symfony](http://symfony.com/), do qual é o Fabien é mantenedor; e hoje a ferramenta está [liberada com código aberto](https://github.com/fabpot/PHP-CS-Fixer) para a comunidade PHP. 

### Composer?

Sempre que possível, gosto de utilizar o [Composer](http://getcomposer.org/) nos projetos para gerenciar minhas dependências. O php-cs-fixer está listado no [Packagist](https://packagist.org/packages/fabpot/php-cs-fixer), e pode ser instalado por lá, mas o que fazer nos casos que não vai usar o composer? Aí foi procurar qual a melhor forma de fazer isso: deixar a ferramenta instalada globalmente junto do meu PHP. No próprio [site oficial do php-cs-fixer](http://cs.sensiolabs.org/) eles sugerem que a forma de instalação é usando o [arquivo PHAR](http://cs.sensiolabs.org/get/php-cs-fixer.phar) que eles disponibilizam para download, e foi em cima desse arquivo PHAR que o plugin para o php-build foi desenvolvido. 

### Plugin

O que o php-build faz é o seguinte: 

  * logo depois de compilar a versão sua do PHP, ele abre o plugin como um after_install
  * o plugin baixa o php-cs-fixer.phar mais recente
  * esse arquivo é renomeado para php-cs-fixer
  * ele é colocado numa pasta acessível ao PATH definido pelo php-build/phpenv nessa versão que você acabou de compilar
  * e no fim, é dada permissão de execução nesse script php-cs-fixer
Pronto! Agora, sempre que precisar rodar a ferramenta é só executar `$ php-cs-fixer` com os parâmetros desejados. 

### Considerações

Para facilitar: \- Github: <https://github.com/rogeriopradoj/php-build-plugin-phpcsfixer> \- DocumentUp: <http://documentup.com/rogeriopradoj/php-build-plugin-phpcsfixer> Fiquem à vontade para tirar dúvidas e dizer o que acharam. Até mais! \--- Este artigo foi publicado originalmente em [RogerioPradoJ.com]().