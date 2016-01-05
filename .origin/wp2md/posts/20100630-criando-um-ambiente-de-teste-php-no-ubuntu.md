title: Criando um ambiente de teste PHP no Ubuntu
link: http://rogeriopradoj.com/2010/06/30/criando-um-ambiente-de-teste-php-no-ubuntu/
author: rogeriopradoj
description: 
post_id: 15
created: 2010/06/30 14:35:00
created_gmt: 2010/06/30 14:35:00
comment_status: open
post_name: criando-um-ambiente-de-teste-php-no-ubuntu
status: publish
post_type: post

# Criando um ambiente de teste PHP no Ubuntu

Esse post é originalmente de meu outro blog, originalmente colocado no ar em junho de 2010, após participar do PHPTESTFEST organizado pelo pessoal do PHPSP.org. Início das migrações para cá ;-) Tradução livre do site http://wiki.php.net/qa/testfest-2010/ubuntu-test-environment, acesso em 05 de junho de 2010. As seguintes instruções foram escritas para o Ubuntu 9.10 testadas nele. É possível que estas instruções também funcionem em outras versões do Ubuntu. Por favor atualize todos os pacotes já instalados antes de começar a criar seu ambiente de teste. Criar o ambiente de teste PHP no Ubuntu é um processo de dois passos:  1) Baixar os "Automated Build Scripts" (script automatizados de criação) 2) Rudar o Build Script Recomendamos que você rode seus testes sobre três versões do principais do PHP: 5.2, 5.3 e na Trunk (tronco do SVN). O restante das instruções assume que você estará criando seu ambiente de testes no seu diretório pessoal "~/". Se você você escolher outro lugar, por favor mude os caminhos correspondentes em todos os comandos encontrados em todo o resto das instruções. Baixe os Scripts Automatizados Abra uma janela do Terminal e rode o seguintes comandos, em ordem: `cd ~/` `wget http://www.ericstewart.org/public/phpt/PHP-Test-Build-Scripts.tgz` `tar -xzf PHP-Test-Build-Scripts.tgz` Você vai ter baixado e descomprimido os scripts no seu diretório pessoal. Rode o Script Automatizado Copie o script para o seu diretório pessoal usando o seguinte comando: `cp PHP-Test-Build-Scripts/Ubuntu-9.10.sh ./` Torne-o executável com este comando: `chmod +x ./Ubuntu-9.10.sh` Agora, simplesmente rode o shell script usando este comando: `./Ubuntu-9.10.sh` Você acabou de criar o ambiente de teste PHP na sua área de trabalho. O ambiente incluirá uma pasta para cada uma das versões principais do PHP: php52, php53 e php-trunk. Screencast No link a seguir você pode assistir uma demonstração do processo inteiro (em inglês). [Screencast demonstration.](http://www.youtube.com/watch?v=w6HlZrPRJXo)