Morse-Code-Decoder
==================

Morse Code decoder in Python

The first section of input.txt contains a mapping between the Latin English character, and the Morse
code equivalent. The second section contains a lexicon of English words that are known
to exist in the secret Morse Code message. The third section is what appears as Morse Code in “dots” and “dashes”. 

Use this input file (" input.txt ") to decode what the third section says.
Sections are seperated by ' * '.  Print each decoded word on a new line. 
Whitespace indicates a word boundary for morse code words. To designate
that a Morse code word may mean something else not in the list ( called words{} ), 
output a question mark (ie “?”) at the end of English word. 
To designate a Morse code word has multiple matches ( in our list words{} ), output an exclamation
mark (ie “!”) at the end of each English word.
