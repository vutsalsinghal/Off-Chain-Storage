from django.http import JsonResponse
from django.shortcuts import render
from web3 import Web3, HTTPProvider
from .contract_abi import abi
from .form import getMsg
import ipfsapi

def index(request):
    return render(request, 'index.html',{})

def ipfsLink(request):
    if request.POST:
        if 'msg' in request.POST:
            msg = request.POST['msg']
            api = ipfsapi.Client("https://ipfs.infura.io", 5001)
            ipfs_hash = api.add_str(msg)
            d = {'hash':ipfs_hash,'link':"https://ipfs.io/ipfs/{}".format(ipfs_hash)}
            return JsonResponse(d)
        else:
            file = request.FILES['file']
            api = ipfsapi.Client("https://ipfs.infura.io", 5001)
            ipfs_dic = api.add(file)
            d = {'hash':ipfs_dic['Hash'],'link':"https://ipfs.io/ipfs/{}".format(ipfs_dic['Hash']), 'Name': ipfs_dic['Name']}
            return JsonResponse(d)
    else:
        form = getMsg()
    return render(request, 'ipfsLink.html',{})

def ipfsLinkRecent(request):
    if request.POST:
        w3 = Web3(HTTPProvider('https://ropsten.infura.io/<YOUR-Key>'))
        contract_address = w3.toChecksumAddress('0x38ea6E8173e0C7505a927647916a1Ff340f1549b')
        contract = w3.eth.contract(address=contract_address, abi=abi)

        userAcc = request.POST['userAccount']

        count = 2
        arr = []
        (hashSender, hashString, hashTimestamp) = contract.functions.findHash(1).call()
        while (hashString != ""):
            if hashSender.lower() == userAcc.lower():
                arr.append([hashString, hashTimestamp])
            (hashSender, hashString, hashTimestamp) = contract.functions.findHash(count).call()
            count += 1
        return JsonResponse({"arr":arr})
    else:
        return render(request, 'ipfsLink.html', {})
