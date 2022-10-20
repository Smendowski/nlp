**^** - początek dopasowania <br>

**$** - koniec dopasowania <br>

**\p{L}** - granica słowa, która ma puste dopasowanie. <br>
Przykład: r"Ala\b" pasuje do Ala ma kota, nie pasuje do Alaala Br>, dopasuje do granicy zakończenia słowa Ala, bez spacji występujacej po tym słowie <br>

SILNIK WYRAŻEŃ REGULARNYCH JEST DOMYŚLNIE CHCIWY <br>

**a??** - minimalne dopasowanie, może być jedno a, ale najlepiej jak najmniej <br>

**|** - alternatywa, która ma niski priorytet. ma kota|psa - dopasowanie do sformułowania "ma kota" oraz "psa". Wygląda to tak: (ma kota)|(psa). Aby zmienić domyślny priorytet alternatywy, używamy nawiasów okrągłych. Docelowo: ma (kota)|(psa) <br>

**Nawiasy ()** - służą do porządkowania priorytetu albo do grup <br>

**(?: )** - ?: non capturing group - grupa, której zawartość nas nie interesuje, ma nie być zlapana <br>

**Wyrażenia regularne vs split na przykładzie e-maila**
(\w+)@(\w+\.)+\w+ <br>
.group(1) - username <br>
.group(0) - cały match <br>
Nie korzystając z wyrażeń, musielibyśmy zrobić split stringu po @ <br>

**Określenie prawego i lewego kontekstu** <br>
Positive lookahead ?= <br>
Positive lookbehind ?<= <br>
Negative lookahead ?! <br>
Negative lookbehind <?! <br>

**Zazębianie dopasowywań** <br>
a(?=b) na stringu ab wskaże, że dopasowaniem jest sama litera a. Jeśli chcemy mieć wszystkie litery, po ktorych występuje b to wyrażenie \wb na stringu abb złapie tylko ab, bb nie zostanie złapane bo dopasowania nie mogą się zazębiać. Rozwiązaniem są konteksty, które nie są częścią dopasowania. (?=b) czyli przykładowy kontekst nie jest częścią dopasowania. Przykład: \w(?=b) 

**\*?** - matches the previous token between zero and unlimited times, as few times as possible, expanding as needed (lazy) <br>

**+?** - matches the previous token between one and unlimited, as few times as possible, expanding as needed (lazy) <br>

**??** - matches the previous token between zero and one, as few times as possible, expanding as needed (lazy) <br>

Wyrażenie <.+> w przypadku skanowania kodu źródłowego strony, złapie nam całą zawartość. < bedzie rozpoczęciem pierwszego tagu html a > zakonczeniem ostatniego tagu. Jak złapać same tagi? Wyrażenie: <.+?>.
