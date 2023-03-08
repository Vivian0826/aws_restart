preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# lsInsulin = "malwmrllpllallalwgpdpaaa"
# bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
# cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
# aInsulin = "giveqcctsicslyqlenycn"


lsInsulin = preproInsulin[0:24]
bInsulin = preproInsulin[24:54]
cInsulin = preproInsulin[54:89]
aInsulin = preproInsulin[89:110]

print("lsInsulin = {}".format(lsInsulin))
print("bInsulin = {}".format(bInsulin))
print("cInsulin = {}".format(cInsulin))
print("aInsulin = {}".format(aInsulin))