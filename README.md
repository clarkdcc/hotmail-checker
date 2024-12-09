# 🚀 Proxyless Hotmail Checker

A proxyless hotmail checker api powerd by Clark API


## Features

- Proxyless ( API uses his own proxies )
- API is go powerd ( For the best result 🔥 )


# 🤖 API Reference
#### Base URL
```
http://134.255.218.89:6969
```

#### Check Endpoint

```http
GET /check
```

#### Check Endpoint - Payload
```
{
    "email": "clarkapi@hotmail.com",
    "pass": "clarkpassword123!"
}
```

#### Status Codes
| Status Code | Type     |
| :-------- | :------- |
| `202` | `email is valid` | 
| `400` | `email is locked` | 
| `400` | `email is invalid` | 
| `500` | `proxy / api error` | 

## Authors

- [@clarkdcc](https://github.com/clarkdcc)
