from PIL import Image
import random

def GetPatches(im, patchSize, numPatches):
	out = []
	for i in range(numPatches):
		cx, cy = random.randint(0, im.size[0]-patchSize[0]), random.randint(0, im.size[1]-patchSize[1])
		patch = im.crop((cx, cy, cx+patchSize[0], cy+patchSize[1]))
		out.append(patch)
	return out

if __name__=="__main__":
	im = Image.open("spiralgraphics/High Altitude.jpg")
	patchSize = 100, 100
	numPatches = 10
	out = GetPatches(im, patchSize, numPatches)
	for i, patch in enumerate(out):
		patch.save("patch{0}.png".format(i))
	
