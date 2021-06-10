from PIL import Image
import os, glob


def image_complexity(filename):
    with Image.open(filename+".jpeg") as p:
        p.save("bmp_"+filename+".bmp")
        p.save("jpg_"+filename+".jpeg", optimize=True, quality=50)
    jpg_size = os.stat("jpg_"+filename+".jpeg").st_size
    org_size = os.stat("bmp_"+filename+".bmp").st_size
    return jpg_size / org_size

if __name__ == "__main__":
    for t in ["simple","complex"]:
        for n in range(1,4):
            fn = t+"_"+str(n)
            print (fn +":"+ str(image_complexity(fn)))