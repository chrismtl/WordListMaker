# WordListMaker
Create your own entirely customized WordList
works on LINUX

Wordlists mode:
1) Low custom:
simple combinations between input keywords

Exemple:
input  => a,b,c
output => a , b , c , ab , ba , bc , cb , ca , ac , abc , acb , bac , bca , cba , cab

2) Medium custom:
Same as low custom but with 3 blocs (High bloc for words, Medium bloc for numbers and Low bloc for symbols) and only 6 combinatoires predefined for it to look like a password

3) Full custom:
Method inspired from hashcat that creates combinations from a given composition
Dictionnary : a => minusculs
              A => majusculs
              N => numbers
              & => symbols (! ? & # * % +)
              
Cracking mode:
simply uses aircrack-ng to crack given handshake with wordlist
