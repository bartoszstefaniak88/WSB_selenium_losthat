def user_login(driver, user_email, user_password):
    """
    :param driver: driver
    :param user_email: xpath to email inputbox
    :param user_password: xpath to password inputbox
    """
    # finding login input box and sending value
    email_input_box = driver.find_element_by_name('email')
    email_input_box.send_keys(user_email)

    # finding password input box and sending value
    password_input_box = driver.find_element_by_name('password')
    password_input_box.send_keys(user_password)

    # finding button 'SIGN IN'
    sign_in_button = driver.find_element_by_id('submit-login')
    sign_in_button.click()