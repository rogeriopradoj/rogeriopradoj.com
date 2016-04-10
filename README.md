# RogerioPradoJ's blog

[![Build Status](https://travis-ci.org/rogeriopradoj/rogeriopradoj.github.io.svg)](https://travis-ci.org/rogeriopradoj/rogeriopradoj.github.io)

It's available on http://rogeriopradoj.com/

## How to run locally:

You [must have composer](https://getcomposer.org/doc/00-intro.md) installed.

A best practice is to verify if everything is ok with your environment, using `diagnose` tool:

```shell
composer diagnose
```

Perhaps you should update your composer:

```shell
composer selfupdate
```

After that:

```shell
# install the dependencies
composer install

# run sculpin
./vendor/bin/sculpin generate --watch --server
```

So visit [http://localhost:8000/](http://localhost:8000/) on your browser.
