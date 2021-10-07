import pyupbit

access = "SoJx4tESKXYcx190fP2ExuloB0hcO3MdAMBSU1Tz"          # 본인 값으로 변경
secret = "81LwtHW4gOfOOiOzIWTL2KxjjA1PlonBNfGgnvDD"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회