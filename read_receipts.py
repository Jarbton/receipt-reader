import cv2
from pytesseract import pytesseract


def main():
    img = cv2.imread('receipt.jpeg')

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)
    print(text)


if __name__ == '__main__':
    main()