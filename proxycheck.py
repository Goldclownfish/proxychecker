import requests
import json
import random

from requests.exceptions import Timeout, ProxyError
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=["GET"])
def backend():
    p = request.args.get("proxy")
    if p == None:
        return "Please specify a proxy."
    else:
        nver = None
        pr = {
            'http': p,
            'https': p
        }
        # Step 1 check Niantic
        try:
            r = requests.get('https://pgorelease.nianticlabs.com/plfe/version', proxies=pr, timeout=5)
            if r.status_code == 200:
                nstatus = '200 OK, proxy is not banned.'
                nver = r.text.replace("", '')
            if r.status_code == 403:
                nstatus = '403 Forbidden, proxy is banned.'
        except requests.exceptions.Timeout:
            nstatus = 'Timed out after 5 seconds.'
        except requests.exceptions.RequestException as e:
            nstatus = 'Unable to connect to the proxy. Make sure to put the port. Authentication is not supported right now.'
        except ProxyError as e:
            nstatus = 'Proxy Error: {}'.format(str(e))

        try:
            r = requests.get(
                'https://sso.pokemon.com/sso/login?locale=en&service=https://www.pokemon.com/us/pokemon-trainer-club/caslogin',
                proxies=pr, timeout=5)
            if r.status_code == 200:
                pstatus = '200 OK, proxy is not banned.'
            if r.status_code == 409:
                pstatus = '409 Conflict, proxy is banned.'
        except requests.exceptions.Timeout:
            pstatus = 'Timed out after 5 seconds.'
        except requests.exceptions.RequestException:
            pstatus = 'Unable to connect to the proxy. Make sure to put the port. Authentication is not supported right now.'
        except ProxyError as e:
            pstatus = 'Proxy Error: {}'.format(str(e))

        return render_template('main.html', pstatus=pstatus, nstatus=nstatus, proxy=pr['https'], nver=nver)

@app.route('/wildcard',methods=["GET"])
def wildcard():
    try:
        r = requests.get(url="https://gimmeproxy.com/api/getProxy?protocol=http", timeout=5)
        dict = json.loads(r.text)
        p = dict['ipPort']
        nver = None
        pr = {
            'http': p,
            'https': p
        }
        # Step 1 check Niantic
        try:
            r = requests.get('https://pgorelease.nianticlabs.com/plfe/version', proxies=pr, timeout=5)
            if r.status_code == 200:
                nstatus = '200 OK, proxy is not banned.'
                nver = r.text.replace('', '')
            if r.status_code == 403:
                nstatus = '403 Forbidden, proxy is banned.'
        except requests.exceptions.Timeout:
            nstatus = 'Timed out after 5 seconds.'
        except requests.exceptions.RequestException as e:
            nstatus = 'Unable to connect to the proxy. Make sure to put the port. Authentication is not supported right now.'
        except ProxyError as e:
            nstatus = 'Proxy Error: {}'.format(str(e))

        try:
            r = requests.get(
                'https://sso.pokemon.com/sso/login?locale=en&service=https://www.pokemon.com/us/pokemon-trainer-club/caslogin',
                proxies=pr, timeout=5)
            if r.status_code == 200:
                pstatus = '200 OK, proxy is not banned.'
            if r.status_code == 409:
                pstatus = '409 Conflict, proxy is banned.'
        except requests.exceptions.Timeout:
            pstatus = 'Timed out after 5 seconds.'
        except requests.exceptions.RequestException:
            pstatus = 'Unable to connect to the proxy. Make sure to put the port. Authentication is not supported right now.'
        except ProxyError as e:
            pstatus = 'Proxy Error: {}'.format(str(e))

        return render_template('main.html', pstatus=pstatus, nstatus=nstatus, proxy=pr['https'], nver=nver)
    except Timeout:
        return 'Initial proxy check timed out.'

@app.route('/api',methods=["GET"])
def api():
    p = request.args.get("proxy")
    if p == None:
        return "Please specify a proxy."
    else:
        nver = None
        pr = {
            'http': p,
            'https': p
        }
        # Step 1 check Niantic
        try:
            r = requests.get('https://pgorelease.nianticlabs.com/plfe/version', proxies=pr, timeout=5)
            if r.status_code == 200:
                nstatus = '200 OK, proxy is not banned.'
                nver = r.text.replace("", '')
            if r.status_code == 403:
                nstatus = '403 Forbidden, proxy is banned.'
        except requests.exceptions.Timeout:
            nstatus = 'Timed out after 5 seconds.'
        except requests.exceptions.RequestException as e:
            nstatus = 'Unable to connect to the proxy. Make sure to put the port. Authentication is not supported right now.'
        except ProxyError as e:
            nstatus = 'Proxy Error: {}'.format(str(e))

        try:
            r = requests.get(
                'https://sso.pokemon.com/sso/login?locale=en&service=https://www.pokemon.com/us/pokemon-trainer-club/caslogin',
                proxies=pr, timeout=5)
            if r.status_code == 200:
                pstatus = '200 OK, proxy is not banned.'
            if r.status_code == 409:
                pstatus = '409 Conflict, proxy is banned.'
        except requests.exceptions.Timeout:
            pstatus = 'Timed out after 5 seconds.'
        except requests.exceptions.RequestException:
            pstatus = 'Unable to connect to the proxy. Make sure to put the port. Authentication is not supported right now.'
        except ProxyError as e:
            pstatus = 'Proxy Error: {}'.format(str(e))

        return render_template('api.html', pstatus=pstatus, nstatus=nstatus, proxy=pr['https'], nver=nver)

@app.route('/wildcard_api', methods=["GET"])
def wildcard_api():
    try:
        r = requests.get(url="https://gimmeproxy.com/api/getProxy?protocol=http", timeout=5)
        dict = json.loads(r.text)
        p = dict['ipPort']
        nver = None
        pr = {
            'http': p,
            'https': p
        }
        # Step 1 check Niantic
        try:
            r = requests.get('https://pgorelease.nianticlabs.com/plfe/version', proxies=pr, timeout=5)
            if r.status_code == 200:
                nstatus = '200 OK, proxy is not banned.'
                nver = r.text.replace('', '')
            if r.status_code == 403:
                nstatus = '403 Forbidden, proxy is banned.'
        except requests.exceptions.Timeout:
            nstatus = 'Timed out after 5 seconds.'
        except requests.exceptions.RequestException as e:
            nstatus = 'Unable to connect to the proxy. Make sure to put the port. Authentication is not supported right now.'
        except ProxyError as e:
            nstatus = 'Proxy Error: {}'.format(str(e))

        try:
            r = requests.get(
                'https://sso.pokemon.com/sso/login?locale=en&service=https://www.pokemon.com/us/pokemon-trainer-club/caslogin',
                proxies=pr, timeout=5)
            if r.status_code == 200:
                pstatus = '200 OK, proxy is not banned.'
            if r.status_code == 409:
                pstatus = '409 Conflict, proxy is banned.'
        except requests.exceptions.Timeout:
            pstatus = 'Timed out after 5 seconds.'
        except requests.exceptions.RequestException:
            pstatus = 'Unable to connect to the proxy. Make sure to put the port. Authentication is not supported right now.'
        except ProxyError as e:
            pstatus = 'Proxy Error: {}'.format(str(e))

        return render_template('api.html', pstatus=pstatus, nstatus=nstatus, proxy=pr['https'], nver=nver)
    except Timeout:
        return 'Initial proxy check timed out.'

@app.route('/docs')
def get_docs():
    return render_template('docs.html')

# TODO: Implement an endpoint that goes through a proxy list, finds one that works and reports it to the user.

if __name__ == '__main__':
    app.run(host='localhost', port=4666)