from detect_image import detect_image
from detect_video import detect_video
from detect_webcam import detect_webcam

def main():

    print("Select Input Type")
    print("1. Image")
    print("2. Video")
    print("3. Webcam")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        path = input("Enter image path: ")
        detect_image(path)

    elif choice == "2":
        path = input("Enter video path: ")
        detect_video(path)

    elif choice == "3":
        detect_webcam()

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()