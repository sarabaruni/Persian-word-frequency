These codes detect items that complicate a sentence or word in persian language.

The codes are written in Python 3.6.9 


Complexity Parser and students| Madule name | Dataset or API | Complexity Level
--- | --- | --- | ---
Sentence length(detection)| len_sentence.py | Hazm(Tokenizer) | sentence
Nominal group(NP) rate(detection) | np_detect.py | Hazm(Chunker) | sentence
calculate score of complexity | main.py | - | - |

Complexity Parser| Madule name | Dataset or API | Complexity Level
--- | --- | --- | ---
No Kasre Ezafe added(edition)| kasre_ezafe.py | Bijankhan | sentence
Half-distance correction(edition)| Negar | - | sentence


Complexity Student| Madule name | Dataset or API | Complexity Level
--- | --- | --- | --- 
Frequency of every word(detection)| frequency.py | hm-blogs | Lexical
words length in syllables(detection) | - | farsnet | Lexical
passive sentences(detection) | passive_check.py |Persian_Propostion_Bank_(PerPB)_V1_Data.txt|sentence
polysemous expressions(detection)| - | farsnet | Lexical 
Words in elementary school students' vocabulary| - | student.txt |Lexical

Complexity | Model of simplification in English
--- | --- |
Lexical simplification | https://arxiv.org/pdf/2006.14939.pdf
identification of difficult words | http://dx.doi.org/10.18653/v1/S16-1085
