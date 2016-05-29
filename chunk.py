from PIL import Image
import random

def GetPatches(im, patchSize, numPatches):
	out = []
	for i in range(numPatches):
		cx, cy = random.randint(0, im.size[0]-patchSize[0]), random.randint(0, im.size[1]-patchSize[1])
		patch = im.crop((cx, cy, cx+patchSize[0], cy+patchSize[1]))
		out.append(patch.convert("RGBA"))
	return out

def GenMargin(patch, marginSize):
	if patch.mode != "RGBA":
		patch = patch.convert("RGBA")
	else:
		patch = patch.copy()

	patchPix = patch.load()
	for x in range(patch.size[0]):
		for y in range(patch.size[1]):
			pix = list(patchPix[x, y])
			alpha = pix[3]
			if x < marginSize:
				alpha *= float(x) / marginSize
			if x > patch.size[0] - marginSize:
				alpha *= float(-x + patch.size[0]) / marginSize

			if y < marginSize:
				alpha *= float(y) / marginSize
			if y > patch.size[1] - marginSize:
				alpha *= float(-y + patch.size[1]) / marginSize
			
			pix[3] = alpha
			patchPix[x, y] = tuple(map(int,map(round, pix)))
	return patch

if __name__=="__main__":
	print "Mountain"
	im = Image.open("spiralgraphics/High Altitude.jpg")
	patchSize = 120, 120
	numPatches = 10
	marginSize = 20
	out = GetPatches(im, patchSize, numPatches)
	for i, patch in enumerate(out):
		patch.save("spiralgraphics-mountain-solid{0}.png".format(i))
	
	#Generate transparent margins
	for i, patch in enumerate(out):
		pm = GenMargin(patch, marginSize)
		pm.save("spiralgraphics-mountain-margin{0}.png".format(i))

	print "Ice"
	im = Image.open("spiralgraphics/Deep-Freeze.jpg")
	numPatches = 10
	out = GetPatches(im, patchSize, numPatches)
	for i, patch in enumerate(out):
		patch.save("spiralgraphics-ice-solid{0}.png".format(i))
	
	#Generate transparent margins
	for i, patch in enumerate(out):
		pm = GenMargin(patch, marginSize)
		pm.save("spiralgraphics-ice-margin{0}.png".format(i))

	print "Sea"
	im = Image.open("spiralgraphics/Port of Taganrog.jpg")
	numPatches = 10
	out = GetPatches(im, patchSize, numPatches)
	for i, patch in enumerate(out):
		patch.save("spiralgraphics-sea-solid{0}.png".format(i))
	
	#Generate transparent margins
	for i, patch in enumerate(out):
		pm = GenMargin(patch, marginSize)
		pm.save("spiralgraphics-sea-margin{0}.png".format(i))
	
	print "Jungle"
	im = Image.open("spiralgraphics/Amazonia.jpg")
	im = im.crop((325, 0, im.size[0], im.size[1]))
	numPatches = 10
	out = GetPatches(im, patchSize, numPatches)
	for i, patch in enumerate(out):
		patch.save("spiralgraphics-sea-solid{0}.png".format(i))
	
	#Generate transparent margins
	for i, patch in enumerate(out):
		pm = GenMargin(patch, marginSize)
		pm.save("spiralgraphics-sea-margin{0}.png".format(i))

	print "City"
	im = Image.open("spiralgraphics/Urban Jungle.jpg")
	im = im.crop((240, 0, 420, im.size[1]))
	numPatches = 10
	out = GetPatches(im, patchSize, numPatches)
	for i, patch in enumerate(out):
		patch.save("spiralgraphics-city-solid{0}.png".format(i))
	
	#Generate transparent margins
	for i, patch in enumerate(out):
		pm = GenMargin(patch, marginSize)
		pm.save("spiralgraphics-city-margin{0}.png".format(i))

	print "Plain"
	im = Image.open("spiralgraphics/Before the War.jpg")
	im = im.crop((240, 0, im.size[0], im.size[1]))
	numPatches = 10
	out = GetPatches(im, patchSize, numPatches)
	for i, patch in enumerate(out):
		patch.save("spiralgraphics-plain-solid{0}.png".format(i))
	
	#Generate transparent margins
	for i, patch in enumerate(out):
		pm = GenMargin(patch, marginSize)
		pm.save("spiralgraphics-plain-margin{0}.png".format(i))

	print "Desert"
	im = Image.open("spiralgraphics/Sahara.jpg")
	im = im.crop((240, 0, im.size[0], im.size[1]))
	numPatches = 10
	out = GetPatches(im, patchSize, numPatches)
	for i, patch in enumerate(out):
		patch.save("spiralgraphics-desert-solid{0}.png".format(i))
	
	#Generate transparent margins
	for i, patch in enumerate(out):
		pm = GenMargin(patch, marginSize)
		pm.save("spiralgraphics-desert-margin{0}.png".format(i))

