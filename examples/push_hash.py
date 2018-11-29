import uospy.cluos

ce = uospy.cluos.Cluos(url='http://43.242.156.61:9008')

payload = [
        {
            'args': {
                "user":"qupengcheng3",
                "size":"10",#后面必须为0，且不能大于赠送的内存
                "hash":"QmWQPCipVXe6idxUjxqqP8vLcbqzqfd6rw7Cq5GgQ89tu8",
                "folder":"C:\Go",
                "file_name":"LICENSE"
            },
            "account": "ulorduosudfs",
            "name": "saveone",
            "authorization": [{
                "actor": "qupengcheng3",
                "permission": "active",
            }],
        }
    ]
#Converting payload to binary
data=ce.abi_json_to_bin(payload[0]['account'],payload[0]['name'],payload[0]['args'])
#Inserting payload binary form as "data" field in original payload
payload[0]['data']=data['binargs']
#Removing the arguments field
payload[0].pop('args')
#final transaction formed
trx = {"actions":[payload[0]]}

# use a string or UOSKey for push_transaction
key = "5JC1EcqvYBFc79Tdo65UFZBpX4a9kqC6PZYuwe4wa8rEyTdsvXj"#"5KAPo5n66XAJ4LkrW6MuQ25yCQzZFGRBVTfrtLUUyS3mB43XWGD"
# use UOSKey:
# import uospy.keys
# key = uospy.keys.UOSKey('5HuaTWKeGzZhqyzuzFAjjFjPnnnjdgcp562oBSS8Wv1qgDSkR2W')
resp = ce.push_transaction(trx, key, broadcast=True)
print('------------------------------------------------')
print(resp)
print('------------------------------------------------')
