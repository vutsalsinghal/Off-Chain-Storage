from django.shortcuts import render
from django.http import JsonResponse
from .form import getMsg
import ipfsapi
from .contract_abi import abi

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