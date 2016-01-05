---
author: rogeriopradoj
comments: true
date: 2011-11-20 17:07:59+00:00
layout: post
slug: 20-maneiras-de-salvar-filhotes-e-aprender-php-parte-2
title: 20 maneiras de salvar filhotes e aprender PHP - parte 2
wordpress_id: 93
categories:
- PHP
tags:
- php
---

Continuando a [tradução livre](http://rogeriopradoj.com/2011/11/15/20-maneiras-de-salvar-filhotes-e-aprender-php/) do 20 Ways to Save Kittens and Learn PHP do NetTuts+, disponível [aqui](http://net.tutsplus.com/tutorials/php/20-ways-to-save-kittens-and-learn-php/).

---


## 3. Não deixe as boas práticas para depois!


A medida que você vai aprendendo irá ouvir bastante sobre boas práticas de programação: coisas como [_prepared statements_ ](http://dev.mysql.com/tech-resources/articles/%3Cspan%3E4.%3C/span%3E1/prepared-statements.html)e os padrões de codificação da PEAR.

Não deixe para depois o aprendizado desses assuntos só porque eles parecem ser difíceis.

"Se algo é uma boa prática não é porque nós (ou seja, outros desenvolvedores PHP) nos reunimos e dissemos: "Como podemos tornar mais difícil a vida dos iniciantes"" .

As boas práticas existem para manter seus programas seguros, rápidos e gerenciáveis. Aprenda sobre eles o mais rápido que você puder. Na verdade, nem sequer aprenda o jeito errado.

Você vai gastar o mesmo tempo para aprender sobre a mysql_query() ou para aprender [PDO](http://php.net/pdo) e [MySQLi](http://php.net/mysqli). Sendo assim escolher começar aprendendo os dois últimos fará com que inicie com uma base sólida nas interações com bancos de dados e na verdade gastado menos tempo e esforço.

Não se esqueça de navegar no [Nettuts+](http://net.tutsplus.com) (e porque não no [rogeriopradoj.com](http://rogeriopradoj.com)) para acessar uma variedade de tutoriais sobre boas práticas em PHP, incluindo o [uso de prepared statements](http://net.tutsplus.com/articles/news/crud-with-php-prepared-statements-new-plus-tutorial/).


## 4. Não deixe as boas práticas para depois!


Só para ter certeza que você tinha visto essa dica.

"Falando sério. Não tente usar atalhos. Toda vez que você viola uma boa prática só porque o jeito certo parece "muito difícil" a Petrobrás mergulha um filhote no petróleo."

Então se você não quiser fazer isso por si mesmo, pelos seus projetos, pelos seus colegas ou pelo progresso da comunidade como um todo, pelo menos pense nos filhotes.


## 5. Faça códigos auto-documentados


No início é tentador tentar ser "inteligente" com os nomes das suas variáveis e funções. Talvez você tenha lido um artigo sobre performance ou visto em algum lugar um trecho de código que fazia um monte de trabalho em duas linhas. Pode ser que você queria criar o seu estilo próprio de programar. Ou talvez você só tenha ouvido falar que eu odeio isso e você quer me irritar.

Não importa qual é o motivo dessa tentação, **resista a ela a todo custo**.

De uma olhada nesse trecho de código:

    
    <?php
    
     $a = b('jason.lengstorf@copterlabs.com');
    
     $c = explode('@', $a);
    
     $d = $c[1];
    
     echo 'The email address ', $a, ' belongs to the domain ', $d, '.';
    
     function b($e) { return htmlentities($e, ENT_QUOTES); }
    
    ?>


Ele faz sentido para você?

É claro que você _pode_ descobrir o que ele faz, mas por que forçar alguém que está tentando trabalhar em cima do seu código a perder alguns minutos coçando a cabeça tentando lembrar o que a variável $c está guardando.

Vamos então pegar aquele código e deixá-lo mais auto-documentado:

    
    <?php
    
     $email = sanitize_string('jason.lengstorf@copterlabs.com');
    
     $email_pieces = explode('@', $email);
    
     $domain = $email_pieces[1];
    
     echo 'The email address ', $email, ' belongs to the domain ', $domain, '.';
    
     function sanitize_string($string) { return htmlentities($string, ENT_QUOTES); }
    
    ?>


Pronto. Muito melhor. Agora apenas olhando para o código dá para ter uma ideia geral do que está acontecendo. Sem coçadas de cabeça, sem xingar ninguém em voz baixa e, o mais importante, **sem nenhuma diferença real na funcionalidade.**

É lógico que você teria economizado alguns bytes com nomes de variáveis menores. Mas, honestamente, se você precisar espremer alguns caracteres dos nomes de suas variáveis para ganhar 0.2ms no tempo de execução do seu programa, provavelmente tem algum problema diferente rolando aí.

Continua...

[Parte 1](http://rogeriopradoj.com/2011/11/15/20-maneiras-de-salvar-filhotes-e-aprender-php/)

Parte 2

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com).
