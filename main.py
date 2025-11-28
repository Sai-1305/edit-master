import cv2
import os
import numpy as np
from rembg import remove 
from PIL import Image
from io import BytesIO

def decolorize_image(uploaded_image):
    # Load the color image and read file as binary data
    image_bytes_data = uploaded_image.read()

    # Decode the image binary data into a color image
    processed_image = np.frombuffer(image_bytes_data,np.uint8)
    color_image = cv2.imdecode(processed_image,cv2.IMREAD_COLOR)
    
    # Convert the color image to grayscale
    grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Save the resulting black and white image
    success, buffer = cv2.imencode(".jpg", grayscale_image)
    byte_IO = BytesIO(buffer)
    return byte_IO

def remove_background(uploaded_image):

    input_image = Image.open(uploaded_image)
    input_image = input_image.convert("RGBA")
    
    # Convert image to bytes
    img_bytes = BytesIO()
    input_image.save(img_bytes, format='PNG')
    
    # Perform background removal using rembg
    processed_bytes = remove(img_bytes.getvalue())
    
    # Convert processed bytes back to PIL image
    no_bg_image = Image.open(BytesIO(processed_bytes))

    # Save to BytesIO for download
    output_bytes = BytesIO()
    no_bg_image.save(output_bytes, format="PNG")
    return output_bytes

















"""
The previous code. It has output folder path. Now, in the updated code, we are using download button.
# ====================================================

def decolorize_image(uploaded_image, outputDirectory):
    # Load the color image and read file as binary data
    image_bytes_data = uploaded_image.read()

    # Decode the image binary data into a color image
    processed_image = np.frombuffer(image_bytes_data,np.uint8)
    color_image = cv2.imdecode(processed_image,cv2.IMREAD_COLOR)

    if color_image is None:
        return False  # Invalid image
    
    # Convert the color image to grayscale
    grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Specify the output file path with a valid file name and extension
    outputPath = os.path.join(outputDirectory, 'Decolorized_Image.jpg')

    # Save the resulting black and white image
    success = cv2.imwrite(outputPath, grayscale_image)

    return success

# ====================================================

def remove_background(uploaded_image, outputDirectory):
    try:

        input_image = Image.open(uploaded_image)
        input_image = input_image.convert("RGBA")
        
        # Save the image to a temporary file (.jpg format)
        temp_image = "temp_image.jpg"
        input_image.save(temp_image,format = "PNG")
        
        # Perform background removal using rembg
        with open(temp_image, "rb") as f: # r: open for reading. b: binary mode
            imageData = f.read()
            imageData = remove(imageData)
        
        # Remove the temporary image file
        os.remove(temp_image)
        
        # Save the background-removed image to the specified output directory
        outputPath = os.path.join(outputDirectory, "NoBackground_Image.png")
        with open(outputPath, "wb") as f: # w: open for writing. b: binary mode
            f.write(imageData)
        
        return True
    
    except Exception as e:
        print("Error removing the background: ", e)
        return False
"""
# ====================================================

# def remove_background(uploaded_image, outputDirectory):
#     # Load the color image and read file:
#     input_image = Image.open(uploaded_image)
#     input_image = input_image.convert("RGBA")

#     with BytesIO() as byteObject:
#         input_image.save(byteObject, format="PNG")
#         input_imageData = byteObject.getvalue()

#     # Remove the background from the image
#     outputImageData = remove(input_imageData)

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

# def remove_background(uploaded_file, output_dir):
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


# def remove_background(uploaded_file, output_dir):
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
