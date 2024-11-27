from PIL import Image

def process_image_with_9x9_filter(image_path):
    try:
      
        img = Image.open(image_path)

        if img.size != (900, 900):
            print("Resizing the image to 900x900 pixels...")
            img = img.resize((900, 900))

       
        pixels = img.load()

     
        output_images = [Image.new("RGB", (100, 100)) for _ in range(9)]
        output_pixels = [img.load() for img in output_images]

        for filter_index in range(9):
            filter_row = filter_index // 3  
            filter_col = filter_index % 3  


            filter_start_x = filter_col * 3
            filter_start_y = filter_row * 3

            for out_y in range(100):
                for out_x in range(100):

                    orig_x = filter_start_x + out_x * 9
                    orig_y = filter_start_y + out_y * 9

                    if orig_x < 900 and orig_y < 900:
                        output_pixels[filter_index][out_x, out_y] = pixels[orig_x, orig_y]

        for i, output_img in enumerate(output_images):
            output_img.show(title=f"Output Image {i + 1}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    input_image = input("Enter the path to the image: ").strip()

    process_image_with_9x9_filter(input_image)


