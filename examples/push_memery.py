import uospy.cluos

ce = uospy.cluos.Cluos(url='http://43.242.156.61:9008')

payload = [
        {
            'args': {
                "user": "qupengcheng3",  # sender
                "start_size": "100" # receiver
            },
            "account": "ulorduosudfs",
            "name": "adduser",
            "authorization": [{
                "actor": "ulorduosudfs",
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
key = "5KAPo5n66XAJ4LkrW6MuQ25yCQzZFGRBVTfrtLUUyS3mB43XWGD"#"5JDGxaotEgFiReFJWwsPhRwwBADo91pKAEgUNwAAs1xZyZsc5Nz"
# use UOSKey:
# import uospy.keys
# key = uospy.keys.UOSKey('5HuaTWKeGzZhqyzuzFAjjFjPnnnjdgcp562oBSS8Wv1qgDSkR2W')
resp = ce.push_transaction(trx, key, broadcast=True)
print('------------------------------------------------')
print(resp)
print('------------------------------------------------')
