import ast

p = 1007621497415251
with open("output_AdriensSign.txt", "r", encoding="utf-8") as f:
    data = f.read().strip()
cipher = ast.literal_eval(data)

bits = []
for c in cipher:
    leg = pow(c, (p-1)//2, p)
    bits.append('1' if leg == 1 else '0')   # leg == 1 => residue => bit 1; else bit 0

binstr = ''.join(bits)
# cắt theo 8 bit -> bytes
msg = bytes(int(binstr[i:i+8], 2) for i in range(0, len(binstr), 8))
print(msg.decode())