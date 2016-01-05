title: Introdução do MongoClient
link: http://rogeriopradoj.com/2013/02/03/introducao-do-mongoclient/
author: rogeriopradoj
description: 
post_id: 355
created: 2013/02/03 18:50:46
created_gmt: 2013/02/03 21:50:46
comment_status: open
post_name: introducao-do-mongoclient
status: publish
post_type: post

# Introdução do MongoClient

Estou fazendo o [curso de MongoDb oficial](https://education.10gen.com/courses/10gen/M101P/2013_Spring/about) da [10gen](http://www.10gen.com/). A ideia da tradução desse artigo saiu de lá. Tradução livre do Introducing MongoClient, disponível em <http://blog.mongodb.org/post/36666163412/introducing-mongoclient> \--- Em 27 de novembro de 2012 foram disponibilizadas pela [10gen](http://www.10gen.com/) versões atualizadas da maioria dos drivers para MongoDB mantidos oficialmente, com novos padrões para verificação e reportagem de erros. Veja abaixo mais informações sobre as mudanças, e consulte a [documentação dos drivers](http://www.mongodb.org/display/DOCS/Drivers) para mais detalhes. Nos últimos anos, tornou-se evidente que os padrões anteriores no comportamento do MongoDB (onde por padrão as mensagens de escrita não esperavam  um código de retorno do servidor) não eram intuitivos e causavam confusão com os usuários do MongoDB. A 10gen queria melhorar isso com o mínimo de problemas para as aplicações MongoDB que já estivessem em produção. 

### História

Primeiro, seria interessante compartilhar a história por trás do comportamento padrão anterior, e por que e como ele foi alterado. O comportamento antigo está ligado ao início da 10gen, antes dos fundadores terem imaginado o MongoDB como uma base autônoma. Quando a 10gen começou, no outono de 2007, eles se propuserem a construir uma plataforma completa como uma pilha de serviços, com o MongoDB como a camada de dados. Era um sistema totalmente hospedado (continua sendo de código aberto), que englobava um load balancer, uma aplicação auto-escalável e uma camada de dados. A parte da aplicação era um ambiente completo em JavaScript do lado servidor. Toda requisição na 10gen era uma requisição http. Você poderia imaginar um controller para fazer alguma análise de usuários funcionando assim: URL:  http://foo.10gen.com/show?sect=sports&page=blog1 CODE: `db.sect_views.update( { _id : db.getParameter( “sect” ) } , { $inc : { count : 1 } } , /*upsert*/true ); db.page_views.update( { _id : db.getParameter( “page” ) } , { $inc : { count : 1 } } , true ); ` As escritas naquela sistema não esperavam individualmente por uma resposta do banco de dados. No entanto, o próprio servidor da aplicação verificava sempre o banco de dados por algum erro que ocorresse durante todo o carregamento da página (usando getLastError e getPrevError), assim o usuário/sistema poderia ser notificado sobre algum problema. É claro que os desenvolvedores também poderiam chamar a função getLastError sempre que quisessem. Isso funcionava muito bem na plataforma, pois a 10gen era capaz de controlar completamente o padrão de acesso. Em janeiro de 2009, eles decidiram, por um série de razões, apenas focar na camada de dados (MongoDB). Naquela época, um certo número de pessoas vinha usando o MongoDB em produção por quase um ano como parte do projeto completo, e muito mais pessoas estavam bem interessadas em usá-lo de forma independente. Durante os meses seguintes, eles escreveram as implementações iniciais dos drivers Java, Python, Ruby e PHP. Todos esses drivers usavam o mesmo protocolo de rede que o servidor da aplicação original, com operações de escritas não síncronas. Isso parecia natural para eles devido ao tempo passado no background, mas claramente não era tão intuitivo para novos usuários do MongoDB que nunca haviam usado o pacote completo. 

### Novo Comportamento

Avançando, o padrão claramente tinha que ser: esperar o banco de dados acusar todas as escritas, o que é muito mais intuitivo. No entanto, apenas mudar o padrão, levaria à quebra da compatibilidade com os aplicativos em produção. A mudança que eles fizeram foi adicionar uma nova classe de conexão, de nível superior, em cada um dos drivers. Por exemplo, no Java, anteriormente se fazia assim: `Mongo mongo = new Mongo( “mongoserver” );` Aquela classe, Mongo, será mantida como o padrão antigo, e se torna obsoleta/deprecated. Para novos códigos, você fará: `MongoClient mongo = new MongoClient( “mongoserver” );` que terá como padrão 1 no [WriteConcern](http://api.mongodb.org/java/current/com/mongodb/WriteConcern.html). Todo o resto será do mesmo jeito. A classe antiga será mantida por um tempo (mas não para sempre), para que não seja quebrado agora o código antigo. Um outro benefício, todo driver usará o MongoClient, assim pela primeira vez ao menos no nível superior das classes se terá o mesmo nome sendo compartilhado. Toda a documentação, tutoriais e códigos de exemplo foram alterados apropriadamente. 

### Mais informações

  * Para baixar os drivers, documentações e tutoriais, visite a [página de drivers](http://www.mongodb.org/display/DOCS/Drivers) na wiki do MongoDB.
  * Para reportar bugs e para pedidos de funcionalidades, visite [jira.mongodb.org](https://jira.mongodb.org/).
  * Para qualquer outro feedback, deixe um comentário no post no [forum de usuários](https://groups.google.com/group/mongodb-user)
O [Eliot](https://twitter.com/eliothorowitz) e a Equipe MongoDB agradecem o suporte contínuo e feedback da comunidade sobre o MongoDB. _ ---_ Valeu, pessoal!   \--- Este artigo foi publicado originalmente em [RogerioPradoJ.com]().