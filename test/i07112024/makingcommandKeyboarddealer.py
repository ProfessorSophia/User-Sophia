import keyboard

def react_to_keys(keys):
    print(f"Keys {keys} were pressed together!")

# Specify the keys you want to listen for
key_combination = ['ctrl', 'a']  # Change to any keys you want

print(type(key_combination))

# Set up a listener for the specified key combination
keyboard.add_hotkey('+'.join(key_combination), lambda: react_to_keys(key_combination))

print(f"Listening for the key combination: {' + '.join(key_combination)}. Press 'esc' to stop.")

# Keep the program running
keyboard.wait('esc')

# --------------------------------
# some research done
# --------------------------------
# the "lambda" logic is a little confusing to me
# i will try to understand it
# lambda: react_to_keys(key_combination): This is 
# an anonymous function (lambda function) that calls 
# react_to_keys with the key_combination list when the 
# specified keys are pressed.
