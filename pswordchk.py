#password checker
import hashlib
import requests



def request_api_data(query_set):
    url='https://api.pwnedpasswords.com/range/' + query_set
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError()
    return res

def pwned_api_Chk(password):
    sha1pass=hashlib.sha1(password.encode()).hexdigest().upper()
    firt5,last5=sha1pass[:5],sha1pass[5:]
    response=request_api_data(firt5)
    return responseset(response,last5)

def responseset(hases,has_to_chk):
    hases=(lines.split(":") for  lines in hases.text.splitlines())
    for h,count in hases:
        if h==has_to_chk:
            return count
    return 0
    
def main(args):
    for password in args:
        count=pwned_api_Chk(password)
        if count:
            print(f'{password} was fount {count} times please change the password')
        else:
            print(f'{password} was not found continue')
    return 'done'
    
a=list(input(" Password to check : ").split())
main(a)