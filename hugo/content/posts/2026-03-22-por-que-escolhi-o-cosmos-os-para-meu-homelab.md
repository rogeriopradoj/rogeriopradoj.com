---
title: 'Por que escolhi o Cosmos OS para meu homelab'
date: '2026-03-22 00:00:00'
categories:
  - Homelab
tags:
  - homelab
  - cosmos os
  - self-hosted
  - docker
  - infraestrutura
slug: por-que-escolhi-o-cosmos-os-para-meu-homelab
url: /2026/03/22/por-que-escolhi-o-cosmos-os-para-meu-homelab
draft: false
---

<figure>
    <img title="Por que escolhi o Cosmos OS para meu homelab" src="/assets/images/2026/03/22-por-que-escolhi-o-cosmos-os-para-meu-homelab.png" alt="Por que escolhi o Cosmos OS para meu homelab">
    <figcaption>Por que escolhi o Cosmos OS para meu homelab</figcaption>
</figure>

Olá, pessoal!

Ao evoluir meu homelab, percebi que não era mais suficiente apenas subir serviços — eu precisava de uma forma consistente de gerenciá-los.

Foi nesse contexto que comecei a buscar uma plataforma que equilibrasse simplicidade e controle.

## O problema

Gerenciar serviços manualmente rapidamente se torna inviável:

* múltiplos containers
* configurações repetitivas
* exposição de serviços na internet
* necessidade de HTTPS

No começo até funciona, mas com o tempo vira um acúmulo de scripts e ajustes difíceis de manter.

## O que eu buscava

Antes de escolher qualquer ferramenta, defini alguns critérios claros:

* gerenciamento centralizado
* facilidade para expor serviços
* suporte a HTTPS com domínio próprio
* baixo esforço operacional
* compatibilidade com Docker

## Testando alternativas

Uma das primeiras opções que testei foi o CasaOS.

Ele é excelente para quem está começando, principalmente pela simplicidade. No entanto, conforme meu ambiente foi ficando mais complexo, comecei a sentir algumas limitações:

* menor flexibilidade em cenários mais avançados
* limitações na configuração de HTTPS
* menos controle sobre o comportamento dos serviços

## Por que Cosmos OS

O Cosmos OS resolveu exatamente os pontos que eu precisava:

* interface simples, mas mais poderosa
* suporte nativo a HTTPS com Let's Encrypt
* facilidade para usar domínio próprio
* gerenciamento centralizado de aplicações

Ele permite subir e expor serviços com muito menos fricção.

## Como ele se encaixa no meu ambiente

Hoje, o Cosmos OS atua como a camada de gerenciamento do meu homelab:

* aplicações rodando em containers
* acesso externo via domínio
* configuração centralizada
* menor esforço de manutenção

Isso me permite focar mais no uso dos serviços e menos na infraestrutura.

## Conclusão

A escolha do Cosmos OS não foi sobre usar a ferramenta mais popular, mas sim a que melhor se encaixa no meu cenário.

No meu caso, ele trouxe o equilíbrio ideal entre:

* simplicidade
* controle
* capacidade de evolução

E isso fez toda a diferença no dia a dia.

## Próximos passos

Nos próximos posts, vou detalhar melhor a estrutura do meu homelab e como estou automatizando tudo com Ansible — incluindo um gateway watchdog para garantir conectividade.

--

Até a próxima, e podem me chamar para conversar em todos os canais!

Abraços!

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](https://rogeriopradoj.com/).
