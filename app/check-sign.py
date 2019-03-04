# -*- coding: utf-8 -*-

from models.signature import signature

message = b'{"correlationId":"ff4d610f-9cc5-4910-9382-b1a2fa754363"}'

message_file=open('/Users/i505032/Downloads/json/test.json', "rb")
message = message_file.read()
message_file.close()


signature_header = 'F202BlodhOXKxwlTOyRcYNmQMqt54Ryn0B8E03oloaUZ3W8tzTa52yGLkTDroOMpba60VuSdL1xKGJ1mOIGvtomc11Ve/lStENih5ZiWyAHbc1QJtyQsamvPmJ1lhlY/lXDRBGbrpbyQbTh+vqw+Rqk2D7zkG9nJexk0KHBntR949HYhPFAA6jGHGeSy0lYlhluO382Yzd1/9/DpQbvDNm74dX57rbkoMO3RSkliEv8w+qas4LqwGbt5zS+XexLRyP/kjUzPatXz/+5WXUOrKGX5PyHSuyPEIaMYM5cXsT98s1igmQaDF6MUFdRwN9gvECUJmBvSs7vBUE9aTE/9yQ=='



check = signature()
print ( check.verify(signature_header,message) )
