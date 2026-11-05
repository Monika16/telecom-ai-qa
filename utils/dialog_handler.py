def handle_dialog(dialog):
    # Assert the message text inside the native alert popup
    assert dialog.message == "please fill all fields"
    dialog.accept()