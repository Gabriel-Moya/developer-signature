# DEVELOPER-SIGNATURE

"Assine" seu nome/pseudônimo no código (python).

Este projeto foi idealizado e codificado por dois amigos de faculdade, eu e o [Leo Moura](https://github.com/LeoMIOT). No GitHub dele o projeto se chama [Developer_name](https://github.com/LeoMIOT/Developer_name).

Este projeto teve como objeto de estudo algumas formas de "ocultar" seu nome em meio ao código, sabemos que existem outros meios e formas de ocultar uma mensagem, porém a proposta foi desenvolvermos mais nosso aprendizado em Python. Muitas vezes como desenvolvedores deixamos informações como: quem  escreveu o código diretamente nos comentários, e alguém vai lá e  APAGA/DELETA! Simples assim. Mas que tal para uso pessoal, inserir seu nome ou um  pseudônimo diretamente no código? Você me diria: Mas o código quando  compartilhado ele acaba sendo alterado. Verdade! Mas que tal inserir seu nome num lugar improvável de ser alterado? Sim!  Nos nomes das variáveis. Ok eles podem ser alterados, mas algumas pessoas simplesmente pegam  códigos prontos e alteram os valores de variáveis e ajustam à suas  necessidades. Por padrão o nome de uma variável nunca deve começar com  números, caracteres especiais e normalmente ela nunca foge do  tradicional, por isso a proposta deste projeto pode não ser bem vista  por alguns ou por muitos, mas segue a proposta:

Padrão de nomeação: variavel_<int> ( variável underline e dois dígitos ) Padrão explicado: underline _ indicará ao sistema leitor da assinatura  que esta vem após ele e os dois dígitos representam valores da tabela  ASCII correspondente ao caractere escolhido.

De posse desta proposta você poderia simplesmente criar uma variável como:

var_76_69_79 e ali estaria inserido "LEO" como assinatura. ou poderíamos dividir estes valores entre 3 variáveis para ficar menos evidente.

`var1_77, var2_79, var3_89 e var4_65`, isso resultaria em "MOYA"

O Padrão fica a seu critério, só lembrando que o sistema aqui desenvolvido está trabalhando com 2(dois dígitos) e na tabela ASCII, caracteres minúsculos possuem 3 dígitos. Nada o impede de criar sua própria solução, método .. algoritmo.

Obs: o padrão pode ser aplicado a qualquer script python e o código  que você encontra aqui no repositório nomeado de *sweep.py* serve apenas para fazer uma varredura no código a procura do padrão definido.

[Tabela ASCII](https://www.ime.usp.br/~kellyrb/mac2166_2015/tabela_ascii.html) para consulta.