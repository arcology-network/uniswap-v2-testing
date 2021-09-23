import sys
sys.path.append("../../..")
from ammolite import (Cli, HTTPProvider, Account)

erc20_token_abi = [{'constant': True, 'inputs': [], 'name': 'name', 'outputs': [{'name': '', 'type': 'bytes32'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'stop', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'guy', 'type': 'address'}, {'name': 'wad', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'owner_', 'type': 'address'}], 'name': 'setOwner', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'totalSupply', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'src', 'type': 'address'}, {'name': 'dst', 'type': 'address'}, {'name': 'wad', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'decimals', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'guy', 'type': 'address'}, {'name': 'wad', 'type': 'uint256'}], 'name': 'mint', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'wad', 'type': 'uint256'}], 'name': 'burn', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'name_', 'type': 'bytes32'}], 'name': 'setName', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [{'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'stopped', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'authority_', 'type': 'address'}], 'name': 'setAuthority', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'owner', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'symbol', 'outputs': [{'name': '', 'type': 'bytes32'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'guy', 'type': 'address'}, {'name': 'wad', 'type': 'uint256'}], 'name': 'burn', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'wad', 'type': 'uint256'}], 'name': 'mint', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'dst', 'type': 'address'}, {'name': 'wad', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'dst', 'type': 'address'}, {'name': 'wad', 'type': 'uint256'}], 'name': 'push', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'src', 'type': 'address'}, {'name': 'dst', 'type': 'address'}, {'name': 'wad', 'type': 'uint256'}], 'name': 'move', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'start', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'authority', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'guy', 'type': 'address'}], 'name': 'approve', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [{'name': '', 'type': 'address'}, {'name': '', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'src', 'type': 'address'}, {'name': 'wad', 'type': 'uint256'}], 'name': 'pull', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'name': 'symbol_', 'type': 'bytes32'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'name': 'src', 'type': 'address'}, {'indexed': True, 'name': 'guy', 'type': 'address'}, {'indexed': False, 'name': 'wad', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'name': 'src', 'type': 'address'}, {'indexed': True, 'name': 'dst', 'type': 'address'}, {'indexed': False, 'name': 'wad', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'name': 'guy', 'type': 'address'}, {'indexed': False, 'name': 'wad', 'type': 'uint256'}], 'name': 'Mint', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'name': 'guy', 'type': 'address'}, {'indexed': False, 'name': 'wad', 'type': 'uint256'}], 'name': 'Burn', 'type': 'event'}, {'anonymous': False, 'inputs': [], 'name': 'Stop', 'type': 'event'}, {'anonymous': False, 'inputs': [], 'name': 'Start', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'name': 'authority', 'type': 'address'}], 'name': 'LogSetAuthority', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'name': 'owner', 'type': 'address'}], 'name': 'LogSetOwner', 'type': 'event'}]
erc20_token_address = sys.argv[3]

frontend = sys.argv[1]
accounts_file = sys.argv[4]
owner_private_key = sys.argv[2]
output_file = sys.argv[5]

accounts = []
with open(accounts_file, 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        segments = line.split(',')
        accounts.append(segments[1])

cli = Cli(HTTPProvider(frontend))
erc20_token = cli.eth.contract(
    abi = erc20_token_abi,
    address = erc20_token_address,
)
owner = Account(owner_private_key)

lines = []
for acc in accounts:
    raw_tx, tx_hash = owner.sign(erc20_token.functions.mint(acc, 20000000000).buildTransaction({
        'gas': 10000000,
        'gasPrice': 1,
    }))
    line = '{},{}'.format(raw_tx.hex(), tx_hash.hex())
    lines.append(line)

with open(output_file, 'a') as f:
    for l in lines:
        f.write(l + '\n')
