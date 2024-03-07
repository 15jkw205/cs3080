# Cypher Text Encrypter and Decrypter Program

# Encryption

plain_text = "Hello World!"
shift = -5
plain_text = "HelloWorld"
plain_text = plain_text.upper()
cypher_text = ""

for character in plain_text:
    plain_text_code = ord(character) - ord('A')
    cypher_text_code = (plain_text_code + shift) % 26
    cypher_text += chr(cypher_text_code + ord('A'))

print(cypher_text)


# Decryption

for shift in range(26):
    plain_text = ""
    for character in cypher_text:
        cypher_text_code = ord(character) - ord('A')
        plain_text_code = (cypher_text_code + shift) % 26
        plain_text += chr(plain_text_code + ord('A'))
    print("Shift = %2d: %s" % (shift, plain_text))



