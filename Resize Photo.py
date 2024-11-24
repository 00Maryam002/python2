from PIL import Image

def process_image_to_9_sections(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Resize the image to 900x900 if necessary
        if img.size != (900, 900):
            print("Resizing the image to 900x900 pixels...")
            img = img.resize((900, 900))

        # Initialize a list to store the 9 output images
        output_images = [Image.new("RGB", (100, 100)) for _ in range(9)]

        for section_row in range(3):  # Rows of the 9 sections
            for section_col in range(3):  # Columns of the 9 sections

                section_index = section_row * 3 + section_col
                section_start_x = section_col * 300
                section_start_y = section_row * 300

                # Populate the corresponding output image
                for y in range(0, 300, 3):  # Step by 3 vertically
                    for x in range(0, 300, 3):  # Step by 3 horizontally

                        block = img.crop((
                            section_start_x + x,
                            section_start_y + y,
                            section_start_x + x + 3,
                            section_start_y + y + 3
                        ))

                        # Compute the destination pixel in the output image
                        dest_x = x // 3
                        dest_y = y // 3

                        # Resize the 3x3 block to 1x1 pixel and paste it
                        average_pixel = block.resize((1, 1))
                        output_images[section_index].paste(average_pixel, (dest_x, dest_y))

        # Display the output images
        for i, output_img in enumerate(output_images):
            output_img.show(title=f"Output Image {i + 1}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the image path from the user
    input_image = input("Enter the path to the image: ").strip()

    # Process the image into 9 sections
    process_image_to_9_sections(input_image)

