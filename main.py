import pyautogui
import pyperclip
import time
import google.generativeai as genai

genai.configure(api_key="AIzaSyD27MhgmMPpNgyeMS_REs4M1kLsZhAEMh4")

def is_last_message_from_sender(chat_log, sender_name="Sender_Name"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

# 1. Small delay to give you time to switch windows
time.sleep(1)
pyautogui.click(x=699, y=744)
time.sleep(1)  # wait for the window to open

# 2. Click on the chrome icon (699, 744)
while True:
    time.sleep(5)
    # 3. Move to starting point (466, 139), hold mouse down
    pyautogui.moveTo(466, 139, duration=0.5)
    pyautogui.mouseDown()

    # 4. Drag to end point (1331, 668), then release mouse
    pyautogui.moveTo(1331, 668, duration=0.5)
    pyautogui.mouseUp()

    # 5. Copy the selected text with Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # give time to copy
    

    # 6. Get the copied text from clipboard
    chat_history = pyperclip.paste()

    pyautogui.press('right')
     
 

    # 7. Print the copied text
    print("Copied Text:\n", chat_history)
    
    


    if is_last_message_from_sender(chat_history):

        model = genai.GenerativeModel("gemini-2.0-flash")

            # Define the prompt
        prompt = f"""You are a person named Aryan who speaks Hindi . 
            He is from India and is a coder. You analyze chat history and respond like Aryan.
            and  you reply like you are aryan
            give short reply not more than 15 words
            reply only in hinglish
            do not use ? , ! " ' in the message
            do not use emoji 
            {chat_history}

            """
        
        


            # Generate content
        response = model.generate_content(prompt)
        pyperclip.copy(response)

            # Print the response
            # print(response.text)
        reply = response.text.strip()

            # print("Generated Response:\n", reply)

            # === STEP 5: Click on the input field and paste the reply ===
        pyautogui.click(x=786, y=703)  # Click on the input box
        time.sleep(1)

        pyperclip.copy(reply)  # Copy response to clipboard
        pyautogui.hotkey('ctrl', 'v')  # Paste
        time.sleep(1)
        pyautogui.press('enter')  # Press Enter to send
        



 