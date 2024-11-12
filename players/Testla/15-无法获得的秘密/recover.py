import sys

from PIL import Image
import numpy as np

canvas_width = 600
canvas_height = 600

def recover_file_from_screenshot(image_path, output_file_path):
    # Load the image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB format
    pixels = np.array(img)

    # Step 1: Find the upper border (first black pixel from the top middle)
    height, width, _ = pixels.shape
    print(f'{height=} {width=}')
    upper_border = None
    for y in range(height):
        mid_x = width // 2
        if np.array_equal(pixels[y, mid_x], [0, 0, 0]):  # Check for black pixel
            upper_border = y
            break

    # Step 2: Find the left border (first black pixel from the middle left)
    left_border = None
    for x in range(width):
        mid_y = height // 2
        if np.array_equal(pixels[mid_y, x], [0, 0, 0]):  # Check for black pixel
            left_border = x
            break

    # Step 3: Read color of pixels in the data area and convert to original data
    if upper_border is not None and left_border is not None:
        data_pixels = []
        for y in range(upper_border + 1, upper_border + 1 + canvas_height):
            for x in range(left_border + 1, left_border + 1 + canvas_width):
                # if not np.array_equal(pixels[y, x], [0, 0, 0]):  # Skip black pixels
                data_pixels.append(pixels[y, x])

        # Convert the list of RGB values to bytes
        original_data = bytearray()
        # for i in range(len(data_pixels)):
        #     # r = data_pixels[i][0]
        #     # g = data_pixels[i][1]
        #     # b = data_pixels[i][2]
        #     # original_data.extend([r, g, b])

        #     r = data_pixels[i][0]
        #     r &= 0xf8
        #     g = data_pixels[i][1]
        #     g &= 0xfc
        #     b = data_pixels[i][2]
        #     b &= 0xf8
        #     original_data.extend([
        #         r | (g >> 5),
        #         ((g << 3) & 0xff) | (b >> 3)
        #     ])
        for i in range(0, len(data_pixels), 2):
            original_data.extend([
                (data_pixels[i + 0][0] & 0xf0) | (data_pixels[i + 0][1] >> 4),
                (data_pixels[i + 0][2] & 0xf0) | (data_pixels[i + 1][0] >> 4),
                (data_pixels[i + 1][1] & 0xf0) | (data_pixels[i + 1][2] >> 4),
            ])

        # Write the original data to the output file
        with open(output_file_path, 'wb') as output_file:
            output_file.write(original_data)

        print(f"Recovered file written to: {output_file_path}")
    else:
        print("Could not find borders in the image.")

# Example usage
recover_file_from_screenshot(sys.argv[1], sys.argv[2])
