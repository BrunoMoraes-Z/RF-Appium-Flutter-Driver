*** Settings ***
Resource  ../resources/main.robot

*** Variables ***
${device}  emulator-5554
${package}  com.bruno.tokoto
${activity}  com.bruno.tokoto.MainActivity

*** Test Cases ***
Example Test
    Open Application    http://localhost:4723/wd/hub
    ...  platformName=Android
    ...  automationName=Flutter
    ...  deviceName=AutomationDevice
    ...  udid=${device}
    ...  appPackage=${package}
    ...  appActivity=${activity}
    Sleep  3

    Capture Page Screenshot
    Click Element  btn_continue
    Sleep  1

    ${value}  Get Text  Continue  text
    ${value}  Get Text  lbl_remember
    ${value}  Get Text  Forgot Password  text

    Input Text  input_email  automation@gmail.com
    Sleep  1
    Input Text  input_password  123456789
    Sleep  1
    Capture Page Screenshot

    Click Element  btn_continue
    Sleep  1
    Capture Page Screenshot

    Click Element  btn_home
    Sleep  1
    Capture Page Screenshot