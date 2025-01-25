f = open("poem.txt")
poem = f.read()
if("Twinkle" in poem):
    print("twinkle present in the poem")
else:
    print("twinkle not present in the poem")
    
f.close()