# python
import json

from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"

params = parse.urlencode({
  "q": "Giratina",
  "api_key": "Ln1OMDKTMpwmS1AX3OnlmVBfPsuSEkje",
  "limit": "10"
})

with request.urlopen("".join((url, "?", params))) as response:
  data = json.loads(response.read())

print(json.dumps(data, sort_keys=True, indent=4))
