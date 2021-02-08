# WordListMaker
Python code creating customized wordlists

Wordlists types:
1) Low custom:
simple combinations between input keywords

Exemple:
input => a    output => a     ab     abc
         b              b  +  ba  +  acb
         c              c     ac     bca
                              ca     bac
                              bc     cab
                              cb     cba

2) Medium custom:
Same as low custom but with 3 blocs (High bloc for words, Medium bloc for numbers and Low bloc for symbols) and only 6 combinatoires predefined for it to look like a password

3) Full custom:
Method inspired from hashcat that creates combinations from a special composition
Dictionnary : a => minusculs
              A => majusculs
              N => numbers
              & => symbols (! ? & # * % +)
              
Cracking part:
simplu uses aircrack-ng to crack handshake with wordlist
