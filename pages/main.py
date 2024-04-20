import cv2
import os
import numpy as np
from rembg import remove 
from PIL import Image

# ====================================================

def decolorizeImage(uploadedImage, outputDirectory):
    # Load the color image and read file as binary data
    imageBytesData = uploadedImage.read()

    # Decode the image binary data into a color image
    processedImage = np.fromstring(imageBytesData,np.uint8)
    colorImage = cv2.imdecode(processedImage,cv2.IMREAD_COLOR)
    
    # Convert the color image to grayscale
    grayScaleImage = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY)

    # Specify the output file path with a valid file name and extension
    outputPath = os.path.join(outputDirectory, 'Decolorized Image.jpg')

    # Save the resulting black and white image
    success = cv2.imwrite(outputPath, grayScaleImage)

    return success

# ====================================================

def removeBackground(uploadedImage, outputDirectory):
    inputImage = Image.open(uploadedImage)
    inputImage = inputImage.convert("RGBA")
    
    # Save the image to a temporary file (.jpg format)
    tempImage = "tempImage.jpg"
    inputImage.save(tempImage,format = "PNG")
    
    # Perform background removal using rembg
    with open(tempImage, "rb") as f: # r: open for reading. b: binary mode
        imageData = f.read()
        imageData = remove(imageData)
    
    # Remove the temporary image file
    os.remove(tempImage)
    
    # Save the background-removed image to the specified output directory
    outputPath = os.path.join(outputDirectory, "No-background Image.png")
    with open(outputPath, "wb") as f: # w: open for writing. b: binary mode
        f.write(imageData)
    
    return outputPath

# ====================================================

# def removeBackground(uploadedImage, outputDirectory):
#     # Load the color image and read file:
#     inputImage = Image.open(uploadedImage)
#     inputImage = inputImage.convert("RGBA")

#     with BytesIO() as byteObject:
#         inputImage.save(byteObject, format="PNG")
#         inputImageData = byteObject.getvalue()

#     # Remove the background from the image
#     outputImageData = remove(inputImageData)

#     if not outputDirectory.endswith("/"):
#         outputDirectory += "/"

#     # Specify the output file path with a valid file name and extension
#     # outputPath = os.path.join(outputDirectory, 'No Background Image.png')
#     outputPath = f"{outputDirectory}NoBackgroundImage.png"

#     # Save the resulting no-background image
#     # outputImage.save(outputPath)
#     with open(outputPath,"wb") as f:
#         f.write(outputImageData)

#     return outputPath

# def removeBackground(uploaded_file, output_dir):
#     # Convert uploaded image to RGBA format
#     image = Image.open(uploaded_file)
#     image = image.convert("RGBA")
    
#     # Save the image to a temporary file in PNG format
#     temp_image_path = "temp_image.png"
#     image.save(temp_image_path, format="PNG")
    
#     # Perform background removal using rembg
#     with open(temp_image_path, "rb") as f:
#         image_data = f.read()
#         image_data = remove(image_data)
    
#     # Remove the temporary image file
#     os.remove(temp_image_path)
    
#     if not outputDirectory.endswith("\\"):
#         outputDirectory += "\\"

#     # Save the background removed image to the output directory in PNG format
#     output_path = f"{output_dir}output_image.png"
#     with open(output_path, "wb") as f:
#         f.write(image_data)
    
#     return output_path


# def removeBackground(uploaded_file, output_dir):
#     # Convert uploaded image to RGBA format
#     image = Image.open(uploaded_file)
#     image = image.convert("RGBA")
    
#     # Save the image to a temporary file in PNG format
#     temp_image_path = "temp_image.png"
#     image.save(temp_image_path, format="PNG")
    
#     # Perform background removal using rembg
#     with open(temp_image_path, "rb") as f:
#         image_data = f.read()
#         image_data = remove(image_data)
    
#     # Remove the temporary image file
#     os.remove(temp_image_path)
    
#     # Save the background-removed image to the specified output directory
#     if not output_dir.endswith("/"):
#         output_dir += "/"
#     output_path = os.path.join(output_dir, 'ImageWithoutBackground.jpg')
#     with open(output_path, "x") as f:
#         # f.write(image_data)
#         cv2.imwrite(output_path, f)
    
    
#     return output_path
