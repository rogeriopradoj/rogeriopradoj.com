---
author: rogeriopradoj
comments: true
date: 2011-11-29 14:05:47+00:00
layout: post
slug: uma-nota-sobre-as-mensagens-do-git-commit
title: Uma Nota Sobre as Mensagens do Git Commit
wordpress_id: 99
categories:
- Geral
---

Atualizado em 30/11/2011.

Tradução livre de [A Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) do [tbaggery](http://tbaggery.com/).

Esse é um texto sobre como fazer um boa mensagem para os commits que você faz no GIT.  Dedico ao Téo.

Aqui vai um link que complementa o que está colocado abaixo: [https://github.com/erlang/otp/wiki/Writing-good-commit-messages](https://github.com/erlang/otp/wiki/Writing-good-commit-messages).

----------------------

Vou tomar um tempo aqui refletir sobre o que faz uma mensagem de um commit ser considerada bem feita. A boa prática que define como montar essas é um dos pequenos detalhes que tornam o Git excelente. É compreensível que alguns dos primeiros commits no repositório do rails tenha mensagens do tipo "linha gigante!!!", vou dizer aqui por que aqui porque aquela era uma prática ruim.

<!-- more -->Aqui está um modelo de mensagem para o Git commit:

    
    Resumo curto (até 50 carac., primeiro maísculo)
    
    Texto explicativo mais detalhado, se necessário. Precisar ter por
    volta de 72 caracteres ou menos. Em determinadas situações, a primeira
    linha é tratada como o assunto de um email e o restante é o corpo do
    texto. A linha em branco separando o resumo do corpo é fundamenal (a
    menos que você omita totalmente o corpo de texto); comandos como o
    rebase podem se confundir se eles não tiverem essa separação.
    
    Escreva suas mensagens de commit no presente: "Arruma bug" e não "Bug
    arrumado". Essa convenção vai ao encontro das mensagens de commit
    geradas pelos comandos do git como o git merge e o git revert.
    
    Parágrafos adicionais tem que ser separados por linhas em branco.
    
    - Marcadores podem ser usados também
    
    - Normalmente um hífen ou um asterisco é usado como marcador,
      precedido por um único espaço e com linhas em branco entre eles, mas
      as convenções divergem nesse ponto
    
    - Use um recuo deslocado




Vamos começar com algumas das razões por que é uma boa ideia deixar as mensagens com no máximo 72 colunas:



	
  * o `git log` não faz nenhuma formatação especial das mensagens de commit. Se usarmos a paginação padrão `less -S` os parágrafos ficarão longe da borda da tela e mais fáceis de ler. Num terminal de 80 colunas, se tirarmos 4 colunas para o recuo à esquerda e mais 4 para igualar na direita, ficamos com 72 colunas.

	
  * o `git format-patch --stdout` converte um conjunto de commits para uma série de emails e usa as mensagens dos commits como corpo de texto. A netiqueta determina que bons emails sejam em texto puro e formatados de forma que permitam alguns níveis de indicadores de resposta aninhados sem estourar o limite de 80 colunas de um terminal.




Mais importante que esse método de formatar o corpo da mensagem é a garantir que se tenha sempre uma linha de assunto.

Como indicado no exemplo, deve-se tentar colocar tudo dentro de 50 caracteres (embora esse não seja um limite rígido) e sempre, mas sempre mesmo, colocar uma linha em branco depois.

Essa primeira linha deve ser um resumo conciso das mudanças que foram introduzidas pelo commit. Se houver algum detalhe técnico que não puder ser expresso aqui por causa da restrição de tamanho, coloque essa informação no corpo da mensagem.

A linha de assunto é usada no Git em todo lugar, muitas vezes de forma truncada se estiver muito grande. A seguir tem um punhado de exemplos onde elas acabam aparecendo:

	
  * `git log --pretty=oneline` mostra um mapa histórico e conciso contendo o id do commit e um resumo

	
  * `git rebase --interactive` fornece o resumo de cada commit no editor de texto

	
  * `git short log` usa as linha de resumo nas saídas estilo changelog que ele cria

	
  * `git format-patch`, `git send-email` e ferramentas relacionadas usam a mensagem como assunto para emails

	
  * reflogs, um histórico local acessível com `git reflog` destinado a ajudar a recuperar erros estúpidos, usa uma cópia desse resumo

	
  * `gitk` tem uma coluna para o resumo

	
  * GitHub usa o resumo em vários lugares em sua interface




A distinção entre o assunto e o corpo da mensagem pode parecer sem importância mas é um dos diversos fatores sutis que fazer o histórico do Git muito mais agradável para trabalhar do que o do Subversion.

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com).
