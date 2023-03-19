import lexical
import identifical
import syntax
import transliteration

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    lexemes = transliteration.block1(data)
    words = lexical.block2(lexemes)
    keywords = identifical.block3(words)
    result = syntax.block4(keywords)
    with open('output.txt', 'w') as f:
        f.write(result)
    list = [lexemes, words, keywords]
