title: Resolver problema LibreOffice Mac - Restaurar janelas
link: http://rogeriopradoj.com/2011/08/29/resolver-problema-libreoffice-mac-restaurar-janelas/
author: rogeriopradoj
description: 
post_id: 56
created: 2011/08/29 03:44:56
created_gmt: 2011/08/29 06:44:56
comment_status: open
post_name: resolver-problema-libreoffice-mac-restaurar-janelas
status: publish
post_type: post

# Resolver problema LibreOffice Mac - Restaurar janelas

Olá, esse vai para quem precisa resolver um problema com o LibreOffice no seu Mac. ![LibreOffice Logo](http://www.libreoffice.org/themes/libo/images/logo.png) Ele ainda é novo para mim (tanto Mac OS quanto o LibreOffice), então ainda apanho para fazer muitas coisas (em ambos). ![Apple Logo](http://blogs-images.forbes.com/ericsavitz/files/2011/05/apple-logo2-248x300.jpg) Esse problema consegui resolver com base na informação desse link: https://bugs.freedesktop.org/show_bug.cgi?id=39007 **Descrição do Problema** Depois que você tenta abrir o LibreOffice, aparece uma janela "Restaurar janelas" (Restore windows) com dois botões e nenhum deles funciona. Por causa disso não é possível abrir nenhum arquivo no LibreOffice depois que a mensagem aparece. **Solução** Abrir o terminal e digitar o seguinte: `$ rm -fr ~/Library/Saved\ Application\ State/org.libreoffice.script.savedState/` Isto é tudo, pessoal. \--- Este artigo foi publicado originalmente em [RogerioPradoJ.com]().

## Comments

**[Luiz](#315 "2012-03-21 15:30:25"):** Obrigado! Resolveu aqui.

**[Rodrigo](#120 "2012-03-05 18:40:39"):** Obrigado! Resolveu um p.... problema que estava me atormentando!

**[reinaldo](#1571 "2012-10-09 19:46:00"):** o que seria abrir o terminal __ ???

**[Rogerio Prado de Jesus](#1573 "2012-10-13 00:16:00"):** Olá, Reinaldo. O Terminal é uma das aplicações que vem por padrão no OSX, ela se parece com o prompt do DOS no Windows, sabe? Para abrir o Terminal você tem várias formas, vou te mostrar duas delas: \- Primeira opção: Abra o Finder, navegue até a pasta Aplicativos, depois Utilitários, e lá você acha o ícone do Terminal \- Segunda opção: Aperte a tecla Command + a barra de espaços, isso faz abrir o Spotlight. Na caixa de busca, digite Terminal e pronto, você vai ver a janela do terminal aberta. Boa sorte!

**[monicaamorim](#1605 "2013-10-02 06:58:00"):** Não consegui assim. Dá essa mensagem no terminal: -bash: $: command not found

**[Rogerio Prado de Jesus](#1606 "2013-10-12 13:05:00"):** Olá, monicaamorim, não sei se já resolveu o problema, mas que versão do LibreOffice está usando? Eu estava olhando novamente o https://bugs.freedesktop.org/show_bug.cgi?id=39007, e parece que na versão 4.1.2 já vai estar tudo funcionando ok. Fala pra gente se resolveu, ok? Até mais!

