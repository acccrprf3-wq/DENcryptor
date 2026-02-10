import platform
import time

def run():
    from cryptography.fernet import Fernet
    import customtkinter as ctk
    from PIL import Image
    import pyperclip
    import os
    import webbrowser

    bin_image = ctk.CTkImage(Image.open("binicon.png"), size=(26, 26))
    clipboard_image=ctk.CTkImage(Image.open("clipboardicon.png"), size=(26, 26))
    logofull=ctk.CTkImage(Image.open("logofull.png"), size=(376,129))

    def generate_key():
        key = Fernet.generate_key().decode("utf-8")
        outputkey.configure(
                            state="normal",
                            text_color="black",
                            font=("Arial", 13, "bold")
                            )
        outputkey.delete(0, "end")
        outputkey.insert(0, key, )
        outputkey.configure(state="readonly")

    def encrypt():
        message=messageentry.get()
        key=keyentry.get()
        try:
            cipher_suite = Fernet(key)
            encoded_text = cipher_suite.encrypt(message.encode())
            output.configure(state="normal")
            output.delete(0, "end")
            output.insert(0, encoded_text)
        except:
            output.configure(state="normal")
            output.delete(0, "end")
            output.insert(0, "Check if the key is valid")
        finally:
            output.configure(state="readonly",
                             text_color="black",
                             font=("Arial", 15, "bold"))

    def decrypt():
        message=messageentry.get()
        key=keyentry.get()
        try:
            cipher_suite = Fernet(key)
            encoded_text = cipher_suite.decrypt(message.encode())
            output.configure(state="normal")
            output.delete(0, "end")
            output.insert(0, encoded_text)
            output.configure(state="readonly")
        except:
            output.configure(state="normal")
            output.delete(0, "end")
            output.insert(0, "Check if the key is valid")
            output.configure(state="readonly")
        finally:
            output.configure(state="readonly",
                             text_color="black",
                             font=("Arial", 15, "bold"))

    def clearmessagebox():
        messageentry.delete(0, "end")

    def clearkeybox():
        keyentry.delete(0, "end")

    def copykey():
        key_to_copy = outputkey.get()
        if key_to_copy != "Your output key will appear here":
            pyperclip.copy(key_to_copy)
            copiedkeymessage.configure(state="normal")
            copiedkeymessage.delete(0, "end")
            copiedkeymessage.insert(0, "Key copied!")
            copiedkeymessage.configure(state="readonly")
            copiedkeymessage.place(x=380, y=75)
            copiedkeymessage.after(2000, copiedkeymessage.place_forget)
        else:
            copiedkeymessage.configure(state="normal")
            copiedkeymessage.delete(0, "end")
            copiedkeymessage.insert(0, "Key is invalid!")
            copiedkeymessage.configure(state="readonly")
            copiedkeymessage.place(x=380, y=75)
            copiedkeymessage.after(2000, copiedkeymessage.place_forget)

    def copyoutput():
        output_to_copy = output.get()
        if output_to_copy != "Your output message will appear here" and output_to_copy != "Check if the key is valid":
            pyperclip.copy(output_to_copy)
            copiedoutputmessage.configure(state="normal")
            copiedoutputmessage.delete(0, "end")
            copiedoutputmessage.insert(0, "Output copied!")
            copiedoutputmessage.configure(state="readonly")
            copiedoutputmessage.place(x=380, y=300)
            copiedoutputmessage.after(2000, copiedoutputmessage.place_forget)
        else:
            copiedoutputmessage.configure(state="normal")
            copiedoutputmessage.delete(0, "end")
            copiedoutputmessage.insert(0, "Output is invalid!")
            copiedoutputmessage.configure(state="readonly")
            copiedoutputmessage.place(x=380, y=275)
            copiedoutputmessage.after(2000, copiedoutputmessage.place_forget)

    def open_documentation():
        os.startfile("documentation.txt")

    def open_fernet_explanation():
        webbrowser.open("https://cryptography.io/en/latest/fernet/")

    app=ctk.CTk(fg_color="grey")
    app.title("DENcryptor")
    app.resizable(False,False)
    app.geometry("490x550")
    app.iconbitmap("icon.ico")



    generatekeybutton=ctk.CTkButton(app,
                                    width=130,
                                    height=50,
                                    text="Generate safe Fernet Key",
                                    text_color="black",
                                    font=("Arial",20,"bold"),
                                    fg_color="white",
                                    hover_color="#b9a7a3",
                                    corner_radius=10,
                                    border_color="black",
                                    border_width=2,
                                    cursor="hand2",
                                    command=lambda:generate_key()
                                    )

    outputkey=ctk.CTkEntry(
                              app,
                              width=360,
                              fg_color="white",
                              border_color="black",
                              text_color="grey"
                              )

    outputkey.insert(0, "Your output key will appear here")
    outputkey.configure(state="readonly")

    messageentry=ctk.CTkEntry(
                              app,
                              placeholder_text="Message goes here",
                              width=300,
                              fg_color="white",
                              border_color="black",
                              text_color="black"
                              )

    keyentry=ctk.CTkEntry(
                              app,
                              placeholder_text="Fernet Key goes here",
                              width=380,
                              fg_color="white",
                              border_color="black",
                              text_color="black"
                              )

    encryptbutton=ctk.CTkButton(app,
                                    width=130,
                                    height=50,
                                    text="Encrypt",
                                    text_color="black",
                                    font=("Arial",20,"bold"),
                                    fg_color="white",
                                    hover_color="#b9a7a3",
                                    corner_radius=10,
                                    border_color="black",
                                    border_width=2,
                                    cursor="hand2",
                                    command=lambda:encrypt()
                                    )

    decryptbutton=ctk.CTkButton(app,
                                    width=130,
                                    height=50,
                                    text="Decrypt",
                                    text_color="black",
                                    font=("Arial",20,"bold"),
                                    fg_color="white",
                                    hover_color="#b9a7a3",
                                    corner_radius=10,
                                    border_color="black",
                                    border_width=2,
                                    cursor="hand2",
                                    command=lambda:decrypt()
                                    )

    output = ctk.CTkEntry(
        app,
        width=360,
        fg_color="white",
        border_color="black",
        text_color="gray",
        font=("Arial",15)
    )

    output.insert(0, "Your output message will appear here")
    output.configure(state="readonly")


    clearmessagebutton=ctk.CTkButton(app,
                                     image=bin_image,
                                     width=26,
                                     height=26,
                                     text="",
                                     fg_color="white",
                                     border_color="black",
                                     hover_color="grey",
                                     cursor="hand2",
                                     border_width=2,
                                     command=lambda:clearmessagebox()
                                     )

    clearmekeybutton=ctk.CTkButton(app,
                                     image=bin_image,
                                     width=26,
                                     height=26,
                                     text="",
                                     fg_color="white",
                                     border_color="black",
                                     hover_color="grey",
                                     cursor="hand2",
                                     border_width=2,
                                     command=lambda:clearkeybox()
                                     )

    copykeybutton=ctk.CTkButton(app,
                                image=clipboard_image,
                                width=26,
                                height=26,
                                text="",
                                fg_color="white",
                                border_color="black",
                                hover_color="grey",
                                cursor="hand2",
                                border_width=2,
                                command=lambda:copykey()
                                )

    copyoutputbutton=ctk.CTkButton(app,
                                image=clipboard_image,
                                width=26,
                                height=26,
                                text="",
                                fg_color="white",
                                border_color="black",
                                hover_color="grey",
                                cursor="hand2",
                                border_width=2,
                                command=lambda:copyoutput()
                                )

    copiedkeymessage = ctk.CTkEntry(
        app,
        width=90,
        height=10,
        text_color="black",
        border_width=2,
        border_color="black",
        corner_radius=5,
        fg_color="white"
    )

    copiedoutputmessage = ctk.CTkEntry(
        app,
        width=105,
        height=10,
        text_color="black",
        border_width=2,
        border_color="black",
        corner_radius=5,
        fg_color="white"
    )
    logobutton=ctk.CTkButton(app,
                             image=logofull,
                             fg_color="grey",
                             width=26,
                             height=40,
                             text="",
                             hover=False
                             )

    documentationbutton=ctk.CTkButton(app,
                                      fg_color="white",
                                      text="Documentation",
                                      font=("Roboto",10,"underline"),
                                      text_color="black",
                                      border_color="black",
                                      border_width=1,
                                      corner_radius=0,
                                      width=26,
                                      height=10,
                                      hover_color="#d3d3d3",
                                      command=lambda: open_documentation()
                                      )

    openfernetexplanationbutton=ctk.CTkButton(app,
                                              fg_color="white",
                                              text="Fernet Explanation",
                                              font=("Roboto", 10, "underline"),
                                              text_color="black",
                                              border_color="black",
                                              border_width=1,
                                              corner_radius=0,
                                              width=26,
                                              height=10,
                                              hover_color="#d3d3d3",
                                              command=lambda: open_fernet_explanation()
                                              )


    generatekeybutton.place(x=105,y=30)
    outputkey.place(x=43,y=100)
    messageentry.place(x=73,y=150)
    keyentry.place(x=30,y=200)
    encryptbutton.place(x=93,y=240)
    decryptbutton.place(x=250,y=240)
    output.place(x=43,y=300)
    clearmessagebutton.place(x=377,y=146)
    clearmekeybutton.place(x=415,y=196)
    copykeybutton.place(x=407,y=96)
    copyoutputbutton.place(x=407,y=296)
    copiedkeymessage.place(x=375, y=80)
    copiedkeymessage.place_forget()
    copiedoutputmessage.place(x=370, y=280)
    copiedoutputmessage.place_forget()
    logobutton.place(x=45,y=360)
    documentationbutton.place(x=0,y=0)
    openfernetexplanationbutton.place(x=73,y=0)

    app.mainloop()

if platform.system() == 'Windows':
    run()
else:
    print("DENcryptor message: ")
    print("This script is recommended for Windows, you can proceed but your OS may cause errors, the program will start in 5 seconds")
    time.sleep(5)
    run()