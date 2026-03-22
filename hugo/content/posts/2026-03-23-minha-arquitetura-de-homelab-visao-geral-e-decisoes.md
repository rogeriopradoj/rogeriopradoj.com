---
title: 'Minha arquitetura de homelab: visão geral e decisões'
date: '2026-03-23 00:00:00'
categories:
    - Homelab
tags:
    - homelab
    - arquitetura
    - infraestrutura
    - self-hosted
    - rede
slug: minha-arquitetura-de-homelab-visao-geral-e-decisoes
url: /2026/03/23/minha-arquitetura-de-homelab-visao-geral-e-decisoes
draft: false

---

<figure>
    <img title="Minha arquitetura de homelab: visão geral e decisões" src="/assets/images/2026/03/23-minha-arquitetura-de-homelab-visao-geral-e-decisoes.png" alt="Minha arquitetura de homelab: visão geral e decisões">
    <figcaption>Minha arquitetura de homelab: visão geral e decisões</figcaption>
</figure>

Olá, pessoal!

Depois de falar sobre a escolha do Cosmos OS, faz sentido dar um passo atrás e mostrar o panorama geral: como está estruturado o meu homelab hoje.

Mais do que ferramentas específicas, o que realmente importa é a arquitetura — ou seja, como as peças se conectam.

## Objetivos do ambiente

Antes de montar qualquer coisa, defini alguns objetivos claros:

* manter o ambiente simples
* permitir evolução gradual
* evitar pontos únicos de falha sempre que possível
* facilitar manutenção e automação

Esses princípios guiaram todas as decisões seguintes.

## Visão geral da arquitetura

De forma simplificada, meu homelab é composto por:

* um gateway principal de rede
* um host dedicado ao homelab
* serviços rodando em containers
* acesso externo via domínio próprio

Cada componente tem um papel bem definido.

## Separação de responsabilidades

Uma decisão importante foi separar funções:

* o gateway cuida da rede (roteamento, regras, acesso)
* o host do homelab cuida das aplicações
* os serviços ficam isolados em containers

Isso evita acoplamento excessivo e facilita troubleshooting.

## Rede e acesso externo

A configuração de rede segue um modelo híbrido:

* parte do tráfego passa pelo gateway principal
* o homelab pode receber tráfego direto (IP público)

Isso permite expor serviços com mais controle e flexibilidade.

Além disso:

* uso de domínio próprio
* acesso via HTTPS
* controle de quais serviços ficam públicos

## Camada de serviços

Os serviços são executados em containers, gerenciados pelo Cosmos OS.

Isso traz algumas vantagens importantes:

* isolamento entre aplicações
* facilidade de deploy
* padronização de execução
* menor risco de conflitos

## Automação

Um dos pilares do ambiente é a automação.

Sempre que possível:

* configurações são versionadas
* provisionamento é automatizado
* mudanças são reproduzíveis

Isso reduz erros e facilita reconstrução do ambiente.

## Trade-offs

Nem tudo é perfeito — e algumas decisões envolvem compromissos:

* simplicidade vs flexibilidade
* automação vs tempo de implementação
* isolamento vs complexidade operacional

A ideia é sempre buscar um equilíbrio que faça sentido no contexto pessoal.

## Conclusão

Ter uma visão clara da arquitetura ajuda muito mais do que escolher ferramentas isoladas.

É ela que define:

* como o ambiente evolui
* como problemas são resolvidos
* o nível de controle que você tem

Nos próximos posts, vou aprofundar cada parte — começando pelo setup com Armbian e depois entrando na automação com Ansible.

--

Até a próxima, e podem me chamar para conversar em todos os canais!

Abraços!

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](https://rogeriopradoj.com/).
