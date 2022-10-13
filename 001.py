# 磯野家　トイレ掃除当番
import random
mem = ["なみへい","ふね","さざえ","ますお","かつお","わかめ","たらちゃん"]
cou = [0,0,0,0,0,0,0]
for i in range(1,32):
    tan = random.randint(0,5)
    print("8月",i,"日--",mem[tan])
    cou[tan] = cou[tan] + 1
print("メンバー",mem)
print("回　　数",cou)
