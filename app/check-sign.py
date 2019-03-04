# -*- coding: utf-8 -*-

from models.signature import signature

message = b'{"correlationId":"ff4d610f-9cc5-4910-9382-b1a2fa754363"}'

message_file=open('/Users/i505032/Downloads/json/test.json', "rb")
message = message_file.read()
message_file.close()


signature_header = b'fDy7c4xVrxmLoqYhkwKbEUkNJ5R4L5H23HqcWXCNsxPvyPMd4rMSbpkcuPNtJMjSeBpYDhr0XZO6RYfNZVhhVn6Iw0Wzey/PDYSDDKF83/38oWdpr06joENkcVoiiQx2x94kqjFUU2Vcy8KeuTgGM9jwPdrMcR9kGuhXWnJmhyTYZcFw7I3zvwOobGK1uay2mtX/ldEn6S4Zml6N6R9aPAjXGUyJEul7n6smHQkcmDoNTmJm6190W/yveq9/LJflu71yTnmWclckz+BnI9ZcUAatRNjvC9n/KLlk4AVRofz9ZRoVUVVdWoaY1ycP29gYn0nOs+M0W9WqczOMuarXUA=='



check = signature()
print ( check.verify(signature_header,message) )
