*** Settings ***
Library           Selenium2Library

*** Test Cases ***
tc10-check gpon serial number
    open browser    https://192.168.1.1/cgi-bin/login.asp    chrome
    sleep    1
    maximize browser window
    sleep    1
    click element    //*[@id="details-button"]
    sleep    1
    click element    //*[@id="proceed-link"]
    sleep    1
    input text    //*[@id="username"]    admin
    sleep    1
    input text    //*[@id="password"]    Abc@13579
    sleep    1
    click element    //*[@id="login_button"]
    sleep    1
