from uospy.cluos import Cluos

ce = Cluos()

# use a string or UOSKey for push_transaction
key = "5KAPo5n66XAJ4LkrW6MuQ25yCQzZFGRBVTfrtLUUyS3mB43XWGD"

# import uospy.keys
# key = uospy.keys.UOSKey()
# prk = key.to_wif()#'5JC1EcqvYBFc79Tdo65UFZBpX4a9kqC6PZYuwe4wa8rEyTdsvXj'
# puk = key.to_public()#'UOS5nNP9YTC5DsPp9vxWV55TeDhU1omAFHymaKc6KSqe8U63dJ1Xz'

resp = ce.create_account('ulorduosudfs', key, 'qupengcheng3', 'UOS5nNP9YTC5DsPp9vxWV55TeDhU1omAFHymaKc6KSqe8U63dJ1Xz', '',
                         stake_net='10.0000 SYS', stake_cpu='10.0000 SYS', ramkb=8, permission='active', transfer=False, broadcast=True)

print('------------------------------------------------')
print(resp)
print('------------------------------------------------')