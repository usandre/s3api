# -*- coding: utf-8 -*-

from models.signature import signature

message = b'{"correlationId":"ff4d610f-9cc5-4910-9382-b1a2fa754363"}'

message_file=open('/Users/i505032/Downloads/json/test.json', "rb")
message = message_file.read()
message_file.close()


signature_header = b'RU3vStNejp23QbhMbP/4ZMz3ekPughbPY7ZWXf/ktq6dAo2veqWAxms7YTyMtiAZe3C8FiTJ1zJVEHCbSiYJ6Ioor/rQaHcZDNLMjAAPmBjeHO+1V+viZpLi6qL77vzlbhx5wNM87Bm1b2bTg1nLNm9/LGoXImyje15mKHzFCKB4mfzJHePDeruQeJXxjfhzSL6LuPA3C8wA0Xio+7IdjJo09sKcohzGSaeqtdRQFTNcO1jv3gGzEjg600rm0hmimMpsqZMudf2yjyiW1DS3KVg1yFwQLqA8k9qUk1NEwoUkO63r+nPmX9N+bSLKt5idhni8ivVXNFdsSeO5Ohz4ZQ=='



check = signature()

print ( check.verify(signature_header,message) )
