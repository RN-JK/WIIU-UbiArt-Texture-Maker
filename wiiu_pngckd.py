import os, glob

dir = 'input/temp'

try:
    os.makedirs(dir)

except:
    pass

try:
    for dds in os.listdir("input/"):
        os.system("texconv2 -i input/"+dds+" -o input/temp/"+dds.replace(".dds",".gtx"))
    
        with open("input/temp/"+dds.replace(".dds",".gtx"), "rb") as f:
            gtxdata=f.read()

        ckdoutput=open("output_pngckd/"+dds.replace(".dds",".png.ckd"),"wb")
        ckdoutput.write(b'\x00\x00\x00\x09\x54\x45\x58\x00\x00\x00\x00\x2C\x00\x00\x20\x80\x01\x00\x01\x00\x00\x01\x18\x00\x00\x00\x20\x80\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\xCC\xCC')

        ckdoutput.write(gtxdata)
        ckdoutput.close()
        print(ckdoutput)

except:
    pass

filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)

os.rmdir(dir)

