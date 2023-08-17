import tkinter as tk
import subprocess

def run_detection():
    # Run the detect.py script with the desired arguments
    subprocess.run(['python', 'C:\\Users\\anant\\Desktop\\temp\\object detection\\yolov5\\detect.py', '--weights', 'yolov5s.pt', '--source', '0'])


# Create the main window
root = tk.Tk()
root.title("YOLOv5 Detection")

# Create a button to run the detection
button = tk.Button(root, text="Run Detection on Webcam", command=run_detection)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
