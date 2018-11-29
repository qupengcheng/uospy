
import timeit

setup_str = '''
from uospy.cluos import UOSKey
import binascii
k = UOSKey("5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3")
digest=binascii.hexlify("This is a test string1")
'''
number=10
key_results=timeit.timeit('k=UOSKey("5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3")',
                          setup="from uospy.cluos import UOSKey", number=number)
print("Creating Key: Ran {} times and averaged {} seconds/run".format(number, key_results/number))

results=timeit.timeit('k.sign(digest)', setup=setup_str, number=number)

print("Signing: Ran {} times and averaged {} seconds/run".format(number, results/number))

