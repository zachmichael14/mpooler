#!/usr/bin/env python3

import cv2
import sys
from pathlib import Path


def display_image(image_path):
    """
    Read and display an image using OpenCV
    
    Args:
        image_path: Path to the image file
    """
    img_path = Path(image_path)
    
    if not img_path.exists():
        print(f"Error: {img_path} not found")
        return False
    
    img = cv2.imread(str(img_path))
    
    if img is None:
        print(f"Error: Could not read image file.")
        return False
    
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return True


def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    
    image_path = sys.argv[1]
    success = display_image(image_path)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()