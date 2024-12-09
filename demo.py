import requests


def clark(email,password):
    json={
        "email": email,
        "pass": password
    }
    r = requests.post("http://134.255.218.89:6969/check",json=json)
    print(r.text)


clark("clarkapi@hotmail.com", "clarkpassword123!")   
