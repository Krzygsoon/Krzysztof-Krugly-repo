from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox, Label

def download_video():
    try:
        # Downloading the URL from the user
        url = entry_url.get()
        if not url:
            messagebox.showinfo("Error", "Enter the URL of the YouTube video.")
            return

        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        high_res_stream = streams.get_highest_resolution()

        # Selecting a folder using a dialog box
        save_path = filedialog.askdirectory(title="Select the folder where you want to save the file")
        if not save_path:
            messagebox.showinfo("Information", "Cancelled download.")
            return

        # Downloading the file
        high_res_stream.download(output_path=save_path)
        messagebox.showinfo("Success", "The video has been successfully downloaded!")

    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred while downloading: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Create a headline explaining to the user what to do
text_label = Label(root, font=40, text="Enter your URL here:")
text_label.pack()

# Create a field to enter the URL
entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=10)

# Create a button to start downloading
button_download = tk.Button(root, text="Download video", command=download_video)
button_download.pack(pady=10)

# Run the main loop
root.mainloop()
