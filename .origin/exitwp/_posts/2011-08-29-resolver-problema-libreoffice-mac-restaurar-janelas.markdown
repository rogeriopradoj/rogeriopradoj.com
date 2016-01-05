---
author: rogeriopradoj
comments: true
date: 2011-08-29 06:44:56+00:00
layout: post
slug: resolver-problema-libreoffice-mac-restaurar-janelas
title: Resolver problema LibreOffice Mac - Restaurar janelas
wordpress_id: 56
categories:
- Mac
tags:
- LibreOffice
- mac
---

Olá, esse vai para quem precisa resolver um problema com o LibreOffice no seu Mac.

[![LibreOffice Logo](http://www.libreoffice.org/themes/libo/images/logo.png)](http://www.libreoffice.org/)

Ele ainda é novo para mim (tanto Mac OS quanto o LibreOffice), então ainda apanho para fazer muitas coisas (em ambos).

[![Apple Logo](http://blogs-images.forbes.com/ericsavitz/files/2011/05/apple-logo2-248x300.jpg)](http://www.apple.com/)

Esse problema consegui resolver com base na informação desse link: https://bugs.freedesktop.org/show_bug.cgi?id=39007

**Descrição do Problema**
Depois que você tenta abrir o LibreOffice, aparece uma janela "Restaurar janelas" (Restore windows) com dois botões e nenhum deles funciona.

Por causa disso não é possível abrir nenhum arquivo no LibreOffice depois que a mensagem aparece.

**Solução**
Abrir o terminal e digitar o seguinte:
`$ rm -fr ~/Library/Saved\ Application\ State/org.libreoffice.script.savedState/`

Isto é tudo, pessoal.

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com).
