from PIL import Image


number_image = int(input("Enter the number of your photos: "))
i = 1
while number_image >= i:
    image_path = input("Enter your path image: ")

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("error FileNotFoundError")
        exit()


    width, height = image.size
    print(f"size width {width} height pixel {height} pixel")


    new_width = int(input("Enter new_width: "))
    new_height = int(input("Enter new_height: "))
    i = 7
    resized_image = image.resize((new_width, new_height))

    output_path = f"resized_photo14.jpg"


    resized_image.save(output_path)

    print(f"image new size({new_width}x{new_height}) in path{output_path} save ")
    i += 1