from PIL import Image

def combine_images1(image1_path, image2_path, output_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    combined_image = Image.blend(image1, image2, alpha=0.5)
    combined_image.save(output_path)

image1_path = input()
image2_path = input()
output_path = "result.png"

combine_images1(image1_path, image2_path, output_path)

#===============================================================
img1 = Image.open(image1_path)
pixels1 = img1.load()
img2 = Image.open(image2_path)
pixels2 = img2.load()

flag = Image.new("RGB" ,img1.size)
flagpix = flag.load()
for row in range(img1.size[1]):
     for col in range(img1.size[0]):
           flagpix[col,row]=(
                        (pixels1[col,row][0]+pixels2[col,row][0])%256,
                        (pixels1[col,row][1]+pixels2[col,row][1])%256,
                        (pixels1[col,row][2]+pixels2[col,row][2])%256)
flag.save("flag.png")

