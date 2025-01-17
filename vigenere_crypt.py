Alphabet = "abcdefghijklmnopqrstuvwxyz"

def key_index(key):
    key_index_list = []
    for char in key:
        key_index_list.append(Alphabet.index(char))
    return key_index_list

def chiffrement(to_translate, encryption_key):
    res_crypt = ""
    count = 0
    key = encryption_key.lower()
    key_index_list = key_index(key)
    
    for char in to_translate:
        if char in Alphabet:
            shift = key_index_list[count]
            index_for_letter = (Alphabet.index(char) + shift) % len(Alphabet)
            res_crypt += Alphabet[index_for_letter]
            count = (count + 1) % len(key_index_list)
        else:
            res_crypt += char
    
    return res_crypt

# Exemple d'utilisation
print(chiffrement("vigenere crypt in python !", "KEY"))
