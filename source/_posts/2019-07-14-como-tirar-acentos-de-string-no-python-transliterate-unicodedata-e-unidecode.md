---
date: 2019-07-14 16:48:00-03:00
title: "Como tirar acentos de string no Python? Transliterate, Unicodedata e Unidecode"
categories:
    - Data Science
tags:
    - python
    - pip
    - nlp
    - unicodedata
    - unidecode
    - transliterate
    - transliteração
social_image: /assets/images/2019/07/14-como-tirar-acentos-de-string-no-python-transliterate-unicodedata-e-unidecode.png
---

<figure>
    <img title="Como tirar acentos de string no Python?" src="/assets/images/2019/07/14-como-tirar-acentos-de-string-no-python-transliterate-unicodedata-e-unidecode.png" alt="Como tirar acentos de string no Python?">
    <figcaption>Como tirar acentos de string no Python?</figcaption>
</figure>


Olá, galera, tudo certinho?

Nesse caminho do Data Science, em específico no tratamento de textos e processamento de linguagem natural (PLN, ou NLP do inglês Natural Language Processing), muitos e muitos tratamentos em string são necessários. E um deles que me apareceu: como fazer para retirar acentos de uma cadeia de caracteres e olhar um texto mais puro?

Lembrando da minha experiência com programação, lembrei do conceito de transliteração, do inglês transliteratation:

> **Transliteration** is a type of conversion of a text from one script to another[1] that involves swapping letters (thus trans- + liter-) in predictable ways (such as α → a, д → d, χ → ch, ն → n or æ → ae).
> 
> -- [Wikipedia](https://en.wikipedia.org/wiki/Transliteration)

Em resumo, é fazer com que todas as formas de apresentação de uma letra seja padronizada em uma apenas. Pegando como exemplo, no português, temos os seguintes caracteres:

- a, á, à, â
- e, é, ê
- i, í
- o, ó, ô
- u, ú, ü
- c, ç

Esses grupos todos acima poderiam ser padronizados no primeiro "formato", o próprio caracter sem acento, trema ou cedilha, no caso:

- a
- e
- i
- o
- u
- c

No passado já vi alguns scripts caseiros, geralmente naquela biblioteca Utils que o programador faz, com esse tipo de tratamento, algo como:

- lista "de-para" do caractere acentuado para o sem acento;
- em seguida, usando alguma função de "string replace", rodar isso em cada função.

A dúvida: será que não tem uma função da biblioteca padrão da linguagem, ou então algum pacote bem utilizado para fazer essa função? E tem sim! E mais de um! Aqui vamos ver dois deles: o [**unicodedata**](https://docs.python.org/3/library/unicodedata.html), embutido no Python, e o [**unidecode**](https://pypi.org/project/Unidecode/) que pode ser instalado via PyPi.

Pegando um texto bem simples, veja o resultado do processamento de cada um deles:

```python
import unidecode
import unicodedata

# texto original
original = "peça ótimo péssimo não é tão às"

# com unidecode
processamento_1 = unidecode.unidecode(original)
print(processamento_1) # peca otimo pessimo nao e tao as


# com unicodedata
processamento_2 = unicodedata.normalize("NFD", original)
print(processamento_2) # peça ótimo péssimo não é tão às
processamento_2 = processamento_2.encode("ascii", "ignore")
print(processamento_2) # b'peca otimo pessimo nao e tao as'
processamento_2 = processamento_2.decode("utf-8")
print(processamento_2) # peca otimo pessimo nao e tao as
```

Nos dois casos, mesma saída: texto original sem os acentos e cedilha. E o unicodedata ainda teve mais passos: primeiro normalizar usando o parâmetro NFD, e em seguida transformar em binário e retornar para string.

## Se o unidecode parece ser bem mais simples, por que usar o unicodedata?

Talvez a primeira vantagem é que o unicodedata já está na biblioteca padrão do Python. Mas a que peguei que é mais crítica é a seguinte: como é feita a transliteração de algumas pontuações, como sinal ordinal masculino (º) e sinal de grau (°).

```python
import unidecode
import unicodedata

# texto original
original = "É o 5º e último. Estava 30°C"

# com unidecode
processamento_1 = unidecode.unidecode(original)
print(processamento_1) # E o 5o e ultimo. Estava 30degC


# com unicodedata
processamento_2 = unicodedata.normalize("NFD", original)
print(processamento_2) # É o 5º e último. Estava 30°C
processamento_2 = processamento_2.encode("ascii", "ignore")
print(processamento_2) # b'E o 5 e ultimo. Estava 30C'
processamento_2 = processamento_2.decode("utf-8")
print(processamento_2) # E o 5 e ultimo. Estava 30C
```

Podemos ver que com o unidecode, o ordinal vira uma letra "o" minúscula, e o sinal de grau virá um "deg".

Você terá que avaliar no seu caso, no meu foi assim: na verdade, todo o texto analisado deveria ter sido digitado como ordinal, mas tinha partes com um e partes com outro. É lógico que eu poderia tratar, para substituir primeiramente todos os formatos para um só, e depois fazer a transliteração. Mas, prefiro que a função faça tudo por mim, no caso, retirando os dois sinais. Assim, com a entrada "É o 5º e último. Estava 30°C", prefiro que fique a saída "E o 5 e ultimo. Estava 30C" (unicodedata + encode + decode) do que "E o 5o e ultimo. Estava 30degC" (unidecode).

---

E você, qual formato utilizaria como padrão?

Até a próxima, e podem me chamar para conversar em todos os canais, ok!

Abraços!

---

Este artigo foi publicado originalmente em [RogerioPradoJ.com](https://rogeriopradoj.com/).
