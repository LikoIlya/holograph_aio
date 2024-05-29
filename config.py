"""

NAME - название нфт

CONTRACT - контракт нфт

count  - количество нфт на кошелек для минта - либо статичное число либо - [от, до] штук

MODE - bridger, minter

minter_mode / bridger_mode = поиск сети с балансом / поиск сети с нфт - и выбор сети : режим 1, или своя сеть : 0 (ставь сразу chain)

chain, to_chain - cети, если хотите выбрать рандом сеть для бриджа в нее то юзаем так ['cеть', 'cеть'] и тд

shuffle - мешаем кошельки - 1, не мешаем - 0

delay - от и до в секундах

moralis_api - https://admin.moralis.io/settings идем сюда и берем default ключ

rpcs - Небольшая рекомендация для тех кто будет юзать данный скрипт, также для комфортной работе на большом количестве аккаунтов
рекомендую юзать приватные рпц, купить можно на любом из этих сервисов - nodereal (https://nodereal.io/),infura (https://www.infura.io/)

"""

NAME = 'GLOW'

CONTRACT = "0x1810e6D63Fe389b2580133c8DA17944D3bAb5E6F"

count = 1  # либо [от, до]

MODE = 'minter'  # bridger, minter

minter_mode = 1  # 0 - your chain

bridger_mode = 1  # 0 - your chain


# bsc, avax, polygon, opti, mantle, base

chain = ''

to_chain = ''  # ['your chain', 'your chain'...] #бридж только в bsc, avax, polygon !!! из bsc, avax, polygon, opti

shuffle = 0

delay = (0, 100)

moralis_api = ''

rpcs = {'bsc': 'https://bscrpc.com',
        'polygon': 'https://polygon.meowrpc.com',
        'avax': 'https://rpc.ankr.com/avalanche',
        'opti': 'https://rpc.ankr.com/optimism',
        'mantle': 'https://rpc.mantle.xyz',
        'base': 'https://base.llamarpc.com'
        }
