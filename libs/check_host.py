import requests,simplejson,time

class CheckHost :

    api_base_url="https://check-host.net"
    types=['http','ping','udp','tcp','dns']
    api_headers={
        "Accept":"application/json"
    }
    

    def __init__(self) :
        pass


    #get nodes list
    def nodes_list(self):

        request_url=self.api_base_url+f"/nodes/hosts"
        response=requests.get(url=request_url,headers=self.api_headers)
        
        if response.status_code==200:
            return simplejson.loads(response.text)

        return False
    

    #ping your target host 
    def request_ping(self,host,node=None,max_node=None):

        request_url=self.api_base_url+f"/check-ping?host={host}&max_nodes={max_node}&node={node}"
        response=requests.get(url=request_url,headers=self.api_headers)

        if response.status_code==200:
            return simplejson.loads(response.text)

        return False
    

    #test http your target host 
    def request_http(self,host,node=None,max_node=None):

        request_url=self.api_base_url+f"/check-http?host={host}&max_nodes={max_node}&node={node}"
        response=requests.get(url=request_url,headers=self.api_headers)

        if response.status_code==200:
            return simplejson.loads(response.text)

        return False
    

    #tcp ping your target host 
    def request_tcp(self,host,node=None,max_node=None):

        request_url=self.api_base_url+f"/check-tcp?host={host}&max_nodes={max_node}&node={node}"
        response=requests.get(url=request_url,headers=self.api_headers)

        if response.status_code==200:
            return simplejson.loads(response.text)

        return False
    

    #udp ping your target host 
    def request_udp(self,host,node=None,max_node=None):

        request_url=self.api_base_url+f"/check-udp?host={host}&max_nodes={max_node}&node={node}"
        response=requests.get(url=request_url,headers=self.api_headers)

        if response.status_code==200:
            return simplejson.loads(response.text)

        return False
    

    #test dns your target host 
    def request_dns(self,host,node=None,max_node=None):

        request_url=self.api_base_url+f"/check-dns?host={host}&max_nodes={max_node}&node={node}"
        response=requests.get(url=request_url,headers=self.api_headers)

        if response.status_code==200:
            return simplejson.loads(response.text)

        return False
    

    #check result by request_id
    def check_result(self,request_id):
        request_url=self.api_base_url+f"/check-result/{request_id}"
        response=requests.get(url=request_url,headers=self.api_headers)

        if response.status_code==200:
            return simplejson.loads(response.text)

        return False
    

    #checker handler
    def check(self,type,url,node=None,max_nodes=None):

        if type in self.types:
            respone=eval(f"self.request_{type}(url,node,max_nodes)")
        else:
            return False
    
        if respone:

            if respone['ok']==1:

                #get result
                for i in range(5):
                    time.sleep(1)
                    ping_result=self.check_result(respone['request_id'])
                    if ping_result:
                        break
                    else:
                        print('result not ready. wait...')
                
                return ping_result
            else:
                return False
        else:
            return False