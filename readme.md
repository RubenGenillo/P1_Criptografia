## Requirements 
pip install nltk

python3 -c "import nltk; nltk.download('cess_esp'); nltk.download('brown')"

## key space
    for ceaser key space is 26 due to the unique shifts posibles of the alphabet
    for affine key space is 12*26 = 312 - 1 = 311, meaning the number of posible combinations of a (with must have inverse modulo) and the 26 unqique shifts minus the identity
    for monoalphabetic is the combination of every rearangement of the alphabet 26!



## C1
Recovery rate tables

length 20
|            | English table | Spainish table |
|English text|     0.845     |                |
|Spanish text|      0.74     |      0.965     |

length 30
|            | English table | Spainish table |
|English text|      0.94     |                |
|Spanish text|     0.785     |      0.925     |

length 40
|            | English table | Spainish table |
|English text|    0.925      |                |
|Spanish text|    0.845      |      0.945     |

length 60
|            | English table | Spainish table |
|English text|      0.95     |                |
|Spanish text|      0.95     |       0.96     |

length 100
|            | English table | Spainish table |
|English text|     0.965     |                |
|Spanish text|     0.925     |      0.955     |

Both characters distriblution tables come from letter frequency articles from wikipedia 
https://en.wikipedia.org/wiki/Letter_frequency
https://es.wikipedia.org/wiki/Frecuencia_de_aparici%C3%B3n_de_letras


Both breakers applied to the right language shows to be very reliable even with length 20, showing how it converges to 1 as length increases. Aplying the spanish table to the english ciphertext not only shows a lower score due to the difference in the distribution of letters but it raises another problem of how to treat non appering characters between alphabets like ñ. Stil impresing the high scores for it (maybe likely to very similar percentages in sharing letters between languages)

## C2

I tested it the same I tested the caeser breaker just to make the comprasions easier. It showed that for shorter text is very unrelaible but its rate of convergence seems to faster than caesar showing better results at longer lengths. 


## C3

measurements (language_length_m):

en_60_3 0.615
en_120_3 0.95
en_200_3 1.0
en_300_3 1.0
en_60_5 0.075
en_120_5 0.575
en_200_5 0.905
en_300_5 0.985
en_60_7 0.0
en_120_7 0.165
en_200_7 0.65
en_300_7 0.88
es_60_3 0.285
es_120_3 0.715
es_200_3 0.87
es_300_3 0.945
es_60_5 0.05
es_120_5 0.19
es_200_5 0.545
es_300_5 0.735
es_60_7 0.005
es_120_7 0.05
es_200_7 0.205
es_300_7 0.5


ciphertext really makes it more likely break it, but the results show how the key difference rellies on the proper key length. With a bigger key you are dividing the text into several smaller caesars encryptions, which making the math makes the probability of finding it really lower.

## C4
The suggested initial mapping was TZEIEKCNOTUSBHKODZENLCITAEPENREDEARSAYEEDOAWTZEHFWSNOTZLIEKNETMEKHCIESAFUTZEYEUKHAMEKZHAWERGZEAOTOIKSLDNSLOIER

It really shows that rank allignment alone doesn't work and what really helps to solve it are the combination of the several other statistics like asociating the most repetitive trigram in the ciphertext with the most common trigram in the english language.

## Monoalphabetic vs AES-128

It is basically because when trying to break a monoalphabetic theres several data, pattern and structure really gives it away, is not brute force, you can follow a path and apply several method.