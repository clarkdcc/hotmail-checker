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
GET /check?pass=<password>&email=<email>
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
| `2002` | `email is valid` | 
| `5786` | `email is locked` | 
| `4548` | `email is invalid` | 
| `4752` | `proxy / api error` | 

## Authors

- [@clarkdcc](https://github.com/clarkdcc)
