import math as mt
import pandas as pd

def funct(z):
    erf_sum = 0
    y = z/mt.sqrt(2)                                         
    for k in range(50):
        temp = (((-1)**k)*(y**(2*k+1)))/(mt.factorial(k)*(2*k+1))
        erf_sum += temp
    erf = (2 / mt.sqrt(mt.pi)) * erf_sum
    phi = 0.5 * (1 + erf)
    return 0.5 * (1 + mt.erf(z/mt.sqrt(2)))

print("Enter the range of the value of Z")
start = float(input("Start from : "))
end = float(input("End at : "))
r_off = int(input("Value of Z round-off upto : "))

r = [round(x*0.1,2) for x in range(int(start*10), int(end*10)+1)]
c = [round(x*0.01,2) for x in range(0,10)]

result = []

for ri in r:
    row = []
    for cj in c:
        if ri >= 0:
            z = ri + cj
        else:
            z = ri - cj

        row.append(funct(z))
    result.append(row)

df = pd.DataFrame(result, columns=c, index=r)
df = df.round(r_off)

print(df.to_string())

df.to_excel(r"C:\Users\mrabd\Documents\my_table.xlsx", index=True)
print("File saved")
