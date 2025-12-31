---
title: 'Como Contribuir com o Homebrew para macOS e Feliz Aniversário Rodrigo #30contribs'
date: '2016-09-26 00:00:00'
categories:
- 30contribs
- mac
tags:
- 30contribs
- homebrew
- hostess
- go-get
- go-clean
slug: como-contribuir-com-o-homebrew-para-macos-e-feliz-aniversario-rodrigo-30contribs
url: /2016/09/26/como-contribuir-com-o-homebrew-para-macos-e-feliz-aniversario-rodrigo-30contribs/
draft: false
---

Olá pessoal, tudo bem? Como andam as contribuições?

<sub>*Se quiser saber mais sobre como contribuir com projetos open source, [veja o artigo #30contribs - Cheguei nos 30! E quero de presente Pull Requests e contribuições para projetos open source e da comunidade!](2015/06/24/30contribs-cheguei-nos-30-e-quero-de-presente-pull-requests-e-contribuicoes-para-projetos-open-source-e-da-comunidade)</sub>

Hoje vamos ver como contribuir criando um novo pacote para o [Homebrew](http://brew.sh), que é um ótimo gerenciador de pacotes para o macOS (similar ao [apt-get, yum, dnf](https://www.digitalocean.com/community/tutorials/package-management-basics-apt-yum-dnf-pkg) ou [chocolatey](https://chocolatey.org/)).

![homebrew website](/assets/images/2016/09/homebrew-page.png)
*Homebrew website: <http://brew.sh>*

---

<a href="{{ page.url }}/#parabens-rodrigo" id="parabens-rodrigo">🍺</a>E também dar parabéns para o [@royopa! 30 anos! #30contribs!][twitter-share-royopa]

[![giphy cheers](/assets/images/2016/09/giphy-cheers.gif)][twitter-share-royopa]
[*Parabéns, @royopa, parça! Fonte: http://www.reactiongifs.com/r/drj1NmK.gif*][twitter-share-royopa]

---

Antes de começar a falar direto sobre a contribuição, vamos falar por que cheguei nisso!

### Motivação: Hostess

Descobri uma ferramenta bem bacana para gerenciar nosso `/etc/hosts`:

> **[cbednarski/hostess](https://github.com/cbednarski/hostess)**
> 
>
> An idempotent command-line utility for managing your /etc/hosts file.
>
> -- https://github.com/cbednarski/hostess

Ele é uma ferramenta escrita em [golang](https://golang.org/), **, e na sua versão 0.2.1 tem como forma de instalação oficial os [binários pré-compilados no GitHub](https://github.com/cbednarski/hostess/releases) ou, para quem quer mexer de alguma forma no código fonte, via `go get` ou compilando diretamente do repositório.

### Instalação de aplicativos de forma automática e gerenciável

Mas eu queria instalar a ferramenta no meu macOS de uma forma que conseguisse facilmente listar depois os aplicativos instalados, simplificando a reinstalação do sistema se necessário - acabei de reinstalar o macOS Sierra 10.12 de [forma limpa](http://macs.about.com/od/macOSSierra/ss/How-to-Perform-a-Clean-Install-of-macOS-Sierra.htm), e a reinstalação dos aplicativos e bibliotecas por meio de uma [listagem programática foi excelente](https://gist.github.com/rogeriopradoj/611cf631a723b6aa211d6d80c2240052)!

Aproveitando, para quem tem macOS, segue a lista dos gerenciadores de aplicativos, pacotes, bibliotecas e configurações que uso e recomendo junto do [Homebrew](http://brew.sh):

- [Homebrew Cask](https://caskroom.github.io): Homebrew para aplicações;
- [mas-cli](https://github.com/argon/mas): Linha de comando para a Mac App Store;
- [mackup](https://github.com/lra/mackup): Sincroniza as configurações dos seus aplicativos em vários tipos de armazenamento como Drobpox, Google Drive ou Git. [Eu uso o Dropbox pois é o padrão e funciona muito bem](https://db.tt/I2yXtpGI).

### Um espaço para contribuir: Hostess no Homebrew

Como vimos, segundo a página oficial, o **hostess** ainda não estava disponível para instalação via gerenciadores. Então a primeira coisa foi ver se já tinha algum suporte no **homebrew**. Com o comando `brew search` fazemos uma consulta tanto nos repositórios do **homebrew** quanto do **homebrew-cask**:

```
$ brew search hostess
No formula found for "hostess".
==> Searching pull requests...

```

Que beleza: uma oportunidade para contribuição com open source! (aqui alguns commits já aceitos no [homebrew](https://github.com/Homebrew/homebrew-core/commits?author=rogeriopradoj) e no [homebrew-cask](https://github.com/caskroom/homebrew-cask/commits?author=rogeriopradoj)).

### Começando a contribuir

![giphy ready go](/assets/images/2016/09/giphy-ready-go.gif)
*Fonte: <http://imgur.com/gallery/ccd3Fjs>*


#### Repositório principal no GitHub

Primeiro, tinha que saber para qual lugar mandar o Pull Request. Por ser um pacote do sistema operacional, e não um aplicativo, o **homebrew** era o melhor lugar.

É importante frisar: cada um dos pacotes que o **homebrew** sabe gerenciar ele chama de *Formula*. E aí fui buscar o repositório do GitHub onde ficam essas fórmulas oficiais, que é o https://github.com/Homebrew/homebrew-core.

#### Contributing.md

A boa prática nos diz que dentro do repositório, quando vamos fazer uma contribuição, [devemos ir direto para o arquivo CONTRIBUTING.md](https://github.com/blog/1184-contributing-guidelines). Nesse repositório somos ensinados sobre como [submeter uma nova fórmula](https://github.com/Homebrew/homebrew-core/blob/master/CONTRIBUTING.md#add-a-new-formula-for-foo-version-234-from-url).

### Criando o arquivo da fórmula

Então vamos lá:

```
$ brew create https://github.com/cbednarski/hostess/archive/v0.2.1.tar.gz
```

O comando cria um esqueleto para a fórmula no seguinte caminho: `/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb"`. O conteúdo dele ficou assim:

```ruby
# Documentation: https://github.com/Homebrew/brew/blob/master/docs/Formula-Cookbook.md
#                http://www.rubydoc.info/github/Homebrew/brew/master/Formula
# PLEASE REMOVE ALL GENERATED COMMENTS BEFORE SUBMITTING YOUR PULL REQUEST!

class Hostess < Formula
  desc ""
  homepage ""
  url "https://github.com/cbednarski/hostess/archive/v0.2.1.tar.gz"
  version "0.2.1"
  sha256 "3be0198f358d49aa9b17fd8622ab5d4e3732dc45226fe1804f245a0773504aee"

  # depends_on "cmake" => :build
  depends_on :x11 # if your formula requires any X11/XQuartz components

  def install
    # ENV.deparallelize  # if your formula fails when building in parallel

    # Remove unrecognized options if warned by configure
    system "./configure", "--disable-debug",
                          "--disable-dependency-tracking",
                          "--disable-silent-rules",
                          "--prefix=#{prefix}"
    # system "cmake", ".", *std_cmake_args
    system "make", "install" # if this fails, try separate make/make install steps
  end

  test do
    # `test do` will create, run in and delete a temporary directory.
    #
    # This test will fail and we won't accept that! It's enough to just replace
    # "false" with the main program this formula installs, but it'd be nice if you
    # were more thorough. Run the test with `brew test hostess`. Options passed
    # to `brew install` such as `--HEAD` also need to be provided to `brew test`.
    #
    # The installed folder is not in the path, so use the entire path to any
    # executables being tested: `system "#{bin}/program", "do", "something"`.
    system "false"
  end
end

```

Como vimos, é apenas um arquivo de exemplo, escrito em [Ruby](https://www.ruby-lang.org/en/). De forma a me basear na construção do arquivo adequadamente, estudei outras fórmulas, dentro do repositório, que instalavam pacotes Golang. Para achar todos os arquivos que pudessem me ajudar, fiz o seguinte:

```
$ pt 'depends_on "go" => :build' /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/
#
# ... várias fórmulas...

```

<sub>**Estou usando o pt para busca: https://github.com/monochromegane/the_platinum_searcher. Você pode usar sua IDE, editor de texto etc.*</sub>

Depois de estudar o código das outras fórmulas (obrigado open source!), fiz as alterações e o meu arquivo `/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb` final ficou assim:

```ruby
class Hostess < Formula
  desc "Idempotent command-line utility for managing your /etc/hosts file"
  homepage "https://github.com/cbednarski/hostess"
  url "https://github.com/cbednarski/hostess/archive/v0.2.1.tar.gz"
  sha256 "3be0198f358d49aa9b17fd8622ab5d4e3732dc45226fe1804f245a0773504aee"
  head "https://github.com/cbednarski/hostess.git"

  depends_on "go" => :build

  def install
    (buildpath + "src/github.com/cbednarski/hostess").install Dir[buildpath/"*"]
    cd "src/github.com/cbednarski/hostess/cmd/hostess" do
      ENV["GOPATH"] = buildpath
      system "go", "install"
    end
    bin.install "bin/hostess" => "hostess"
  end

  test do
    system bin/"hostess", "--help"
  end
end

```

### Testando a instalação do arquivo

O passo seguinte foi testar a instalação, seguindo a orientação lá do [CONTRIBUTING.md](https://github.com/Homebrew/homebrew-core/blob/master/CONTRIBUTING.md#add-a-new-formula-for-foo-version-234-from-url):

```
$ brew install --debug --verbose /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb


/usr/local/Homebrew/Library/Homebrew/brew.rb (Formulary::FromPathLoader): loading /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb
/usr/local/Homebrew/Library/Homebrew/brew.rb (Formulary::FormulaLoader): loading /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/go.rb
==> Using the sandbox
/usr/bin/sandbox-exec -f /tmp/homebrew20160925-23319-7e1u4k.sb nice /System/Library/Frameworks/Ruby.framework/Versions/2.0/usr/bin/ruby -W0 -I /usr/local/Homebrew/Library/Homebrew -- /usr/local/Homebrew/Library/Homebrew/build.rb /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb --verbose --debug
/usr/local/Homebrew/Library/Homebrew/build.rb (Formulary::FromPathLoader): loading /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb
/usr/local/Homebrew/Library/Homebrew/build.rb (Formulary::FormulaLoader): loading /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/go.rb
==> Downloading https://github.com/cbednarski/hostess/archive/v0.2.1.tar.gz
Already downloaded: /Users/rogerio/Library/Caches/Homebrew/hostess-0.2.1.tar.gz
==> Verifying hostess-0.2.1.tar.gz checksum
tar xvzf /Users/rogerio/Library/Caches/Homebrew/hostess-0.2.1.tar.gz
x hostess-0.2.1/
x hostess-0.2.1/.gitignore
x hostess-0.2.1/.travis.yml
x hostess-0.2.1/Dockerfile
x hostess-0.2.1/LICENSE
x hostess-0.2.1/Makefile
x hostess-0.2.1/README.md
x hostess-0.2.1/cmd/
x hostess-0.2.1/cmd/hostess/
x hostess-0.2.1/cmd/hostess/hostess.go
x hostess-0.2.1/commands.go
x hostess-0.2.1/commands_test.go
x hostess-0.2.1/hostfile.go
x hostess-0.2.1/hostfile_test.go
x hostess-0.2.1/hostlist.go
x hostess-0.2.1/hostlist_test.go
x hostess-0.2.1/hostname.go
x hostess-0.2.1/hostname_test.go
x hostess-0.2.1/test-fixtures/
x hostess-0.2.1/test-fixtures/hostfile1
x hostess-0.2.1/vendor/
x hostess-0.2.1/vendor/github.com/
x hostess-0.2.1/vendor/github.com/codegangsta/
x hostess-0.2.1/vendor/github.com/codegangsta/cli/
x hostess-0.2.1/vendor/github.com/codegangsta/cli/LICENSE
x hostess-0.2.1/vendor/github.com/codegangsta/cli/app.go
x hostess-0.2.1/vendor/github.com/codegangsta/cli/cli.go
x hostess-0.2.1/vendor/github.com/codegangsta/cli/command.go
x hostess-0.2.1/vendor/github.com/codegangsta/cli/context.go
x hostess-0.2.1/vendor/github.com/codegangsta/cli/flag.go
x hostess-0.2.1/vendor/github.com/codegangsta/cli/help.go
==> go install
==> Cleaning
Fixing /usr/local/Cellar/hostess/0.2.1/bin/hostess permissions from 755 to 555
==> Finishing up
ln -s ../Cellar/hostess/0.2.1/bin/hostess hostess
==> Summary
🍺  /usr/local/Cellar/hostess/0.2.1: 2 files, 3.9M, built in 2 seconds

```

É isso aí, instalou!

Aqui já aproveitamos e rodamos o comando de teste:

```
$ brew test /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb

Testing hostess
==> Using the sandbox
==> /usr/local/Cellar/hostess/0.2.1/bin/hostess --help
```

Ok, testes executados com sucesso!

### Script de auditoria e um bug no Homebrew

Agora, seguindo os próximos passos para a contribuição, vamos fazer a auditoria:

```
$ brew audit --new-formula /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb

Error: type mismatch: String given
Please report this bug:
    https://git.io/brew-troubleshooting
/usr/local/Homebrew/Library/Homebrew/cmd/search.rb:153:in `=~'
/usr/local/Homebrew/Library/Homebrew/cmd/search.rb:153:in `block in search_tap'
/usr/local/Homebrew/Library/Homebrew/cmd/search.rb:153:in `select'
/usr/local/Homebrew/Library/Homebrew/cmd/search.rb:153:in `search_tap'
/usr/local/Homebrew/Library/Homebrew/dev-cmd/audit.rb:347:in `block (2 levels) in audit_formula_name'
```

Ops... Deu algum problema: ***__Error__: type mismatch: String given***. Abri uma [issue referente ao bug no repositório do homebrew](https://github.com/Homebrew/homebrew-core/issues/5249), já recebi a resposta (minha instalação estava desatualizada), e quando rodei novamente, tudo certo:

```
$ brew audit --new-formula /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/hostess.rb
```

Dessa vez, o comando não deu nenhuma saída, indicando que a fórmula passou OK pela auditoria.

### Fork, Branch, Commit

Próximo passo, fazer o commit num branch separado ([boa prática](http://codeinthehole.com/writing/pull-requests-and-other-good-practices-for-teams-using-github/#work-on-a-story)), já preparando para o Pull Request:

```
# garantir que está na pasta correta
$ cd $(brew --repository homebrew/core)

# fazer fork do repositório no github, usando a ferramenta cli hub, recomendadíssima (https://hub.github.com/)
$ hub fork

# criar branch separado
$ git checkout -b new-formula-hostess

# fazer o commit
$ git add Formula/hostess.rb
$ git commit -m "hostess 0.2.1 (new formula)"
```

### Pull Request

Commit feito, hora de criar o Pull Request:

```
# primeiro mandar as alterações lá para o meu fork no GitHub
# (rogeriopradoj é o nome do meu git remote)
$ git push rogeriopradoj new-formula-hostess

# caso tiver algum problema aqui referente a 'shallow update not allowed' rode a seguinte linha:
# $ git fetch --unshallow rogeriopradoj && git push rogeriopradoj new-formula-hostess

# e termine fazendo o pull request
$ hub pull-request
#
# https://github.com/Homebrew/homebrew-core/pull/5257
```

Yeah! O Pull Request foi feito, e a linha de comando já retorna o endereço: <https://github.com/Homebrew/homebrew-core/pull/5257>.

![pull request aberto](/assets/images/2016/09/pull-request-for-hostess-new-homebrew-formula.png)

Agora é só esperar o resultado da avaliação da contribuição em alguns dias (que deve ser feita pelos mantenedores do projeto seguindo [esse documento](https://github.com/Homebrew/brew/blob/master/docs/How-To-Open-a-Homebrew-Pull-Request-(and-get-it-merged).md#how-to-open-a-homebrew-pull-request-and-get-it-merged)).

### Considerações finais

Costumo falar que [contribuir para projetos open source tem muito de motivação e estilo](2015-11-04-becoming-a-contributor-open-sourcer-and-beyond-palestra-do-tdc-2014-trilha-php), mas tem um fator que também é muito importante: oportunidade! Aqui, percebi a oportunidade quando uma biblioteca não estava disponível, e podia ser incluída via contribuição.

Meu irmão [Rodrigo, o @royopa](https://github.com/royopa) fala que a motivação dele é contribuir de qualquer forma para todo projeto que ele usar sempre que ele conseguir (souber como fazer e tiver a oportunidade!).

> [**E reforçando, hoje 26 de setembro é aniversário dele de 30 anos, então: Parabéns, Rodrigo, muitas felicidades!**][twitter-share-royopa]

Eu tento seguir isso que ele fala também. Tanto que boa parte das [minhas contribuições no GitHub são para projetos abertos](https://github.com/rogeriopradoj) que uso constantemente.

Por fim, nesse artigo conhecemos e vimos como contribuir para o **Homebrew**, criando uma fórmula para o **hostess**, passamos por vários softwares para instalação de aplicativos de forma automática e gerenciável (**Homebrew Cask**, **mas-cli** e **mackup** com [Dropbox](https://db.tt/I2yXtpGI)).


É isso aí, se quiser falar comigo pode usar os comentários abaixo e os [contatos do RogerioPradoJ.com](https://rogeriopradoj.com/about/).

Até a próxima! 


---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](http://rogeriopradoj.com/).

[twitter-share-royopa]: https://twitter.com/home?status=Feliz%20anivers%C3%A1rio,%20%40royopa,%20muitas%20felicidades!%20J%C3%A1%20chegou%20nos%2030%20anos!%20https%3A//rogeriopradoj.com/2016/09/26/como-contribuir-com-o-homebrew-para-macos-e-feliz-aniversario-rodrigo-30contribs/%23parabens-rodrigo%20%2330contribs "Dê os parabéns para o Rodrigo!"

