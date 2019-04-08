### Webhook example


- requires 'app/public.key' manually installed 


#### Methods

 Method | Resource | Description| Params
 --- | --- | --- | ---
GET | /sub/ | List of buckets | 
POST, PUT | /sub/{name} | Saves event into {name} bucket | ?code=400&prob=70
GET | /sub/{name} | Lists events from {name} bucket|
GET | /sub/{name}/{event} | Returns record with id {event} from  from {name} bucket|
DEL | /sub/{name} | Deletes {name} bucket  |
