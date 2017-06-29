# Our API

## Want to use our API?

There are a few endpoints to this API, however they are relatively simple. This API is free and will always be free.

Main API
------
Endpoint: `/api`

Supported Methods: GET

URL Parameters:
* Proxy (ex. 1.2.3.4:5000)

An example request looks like this:
`/api?proxy=1.2.3.4:5000`

It will return a response which looks like this:
`{ "proxy": "139.59.170.81:8118", "pstatus": "200 OK, proxy is not banned.", "nstatus": "200 OK, proxy is not banned.", "nver": " 0.67.1" }`

Explanation:
* `proxy`: The proxy used.
* `pstatus`: Pokemon Trainer Club status (wether or not this API can be used with Pokemon Trainer Club logins)
* `nstatus`: Niantic status (Can this proxy be used on the Niantic servers?)
* `nver`: Niantic's latest forced version

Wildcard API
---
Endpoint: `/wildcard_api`

Supported Methods: GET

URL Parameters: None

Example request:
`/wildcard_api`

The response is identical to the one delivered by the Main API.