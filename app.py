from libs.check_host import CheckHost

check_host=CheckHost()

url='aparat.com'

# print(check_host.nodes_list())
print(check_host.check(type='tcp',url=url,node='ir1.node.check-host.net',max_nodes=1))
