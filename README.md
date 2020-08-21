# API DEMO endpoint 

## Features
- Saves events without preliminary defining endpoint/subscription, just type something /sub/bla-bla-bla when creating subscription. If that endpoint doesn't exit, it will be created with fist received event. Endpoint will return list of all received events.
- Captures event body + header (json)
- Event in the subscription/endpoint can be addressed directly by correlation_id, /sub/demo/1f9c21f6-9b9b-414d-83d0-0365022052c5
- Performs concur signature validation, result (valid|invalid|not present) is captured and saved along with event and headers
- Client certificate  (in this case webhook certificate) is captured in headers: certificate name, certificate number,  certificate expiry days.
- [require apache] Two levels of proxy security http://secure.concuress.com - client certificate required (enforced), http://www.concuress.com - client certificate optional, browser friendly. Same same DB behind those two gate
- No endpoint auto-purge (like requestbin), events will be kept until you send DEL /sub/bla-bla-bla
- Can be installed locally (docker) for testing purposes (HTTP), http://localhost:5000
- for POST|PUT you can specify params ?code=404&prob=75 that will return 404 with probability of 75%
