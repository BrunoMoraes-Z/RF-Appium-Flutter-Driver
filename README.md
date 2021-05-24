# Robot Framework With Appium Flutter Driver

## 📋 Description

Project aims to demonstrate a way to perform tests with Appium in applications developed in Flutter.
### 🎞 [Video](https://youtu.be/FAvoVbtJw9E) execution.
### 📦 [Appium Flutter Driver Project](https://github.com/truongsinh/appium-flutter-driver).
### 📦 [Example App - SRC](https://github.com/BrunoMoraes-Z/e_commerce).
### 📦 [Example App - APK](https://github.com/BrunoMoraes-Z/RF-Appium-Flutter-Driver/tree/master/resources/files).

## 📃 Execution Log

  - [Online File](https://appium-flutter-driver-rf.glitch.me/)
  - [Files](https://github.com/BrunoMoraes-Z/RF-Appium-Flutter-Driver/tree/master/results)

### 🌟 Requirements

  - Python 3 or above
  - NodeJS [LTS Version](https://nodejs.org/en/download/)
  - SDK Platform Tools
  - Appium Server ```npm i -g appium```
  - Flutter Driver ``npm i -g appium-flutter-driver``
  - ``RobotFramework, Appium-Python-Clien and Appium-Flutter-Finder``
  
## ⚙ Capabilities Example

```robotframework
Open Application    http://localhost:4723/wd/hub
...    platformName=Android
...    automationName=Flutter
...    deviceName=AutomationDevice
...    udid=emulator-5554
...    appPackage=com.bruno.tokoto
...    appActivity=com.bruno.tokoto.MainActivity
```
  
### ⚠ Attention

- The APK for testing has to be of the DEBUG type
- The Application must have a ``flutter_driver`` as a development dependency
- Within the main function of the application you have to add the function ``enableFlutterDriverExtension()``
- Interactive elements an identifier must be added example ``ValueKey('btn_continue')``
