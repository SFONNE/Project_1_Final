*** Settings ***
Library    Selenium2Library
*** Variables ***
${browser}      Chrome
${test_fb}  facebook 
${url_google}   http://www.google.com
${ID}       kriengsak_05@hotmail.com
${Pass}     -kriengsak030056
*** Keywords ***
*** Test Cases ***
gotogoogle.com
    ${options}=    Evaluate  sys.modules['selenium.webdriver.chrome.options'].Options()    sys
    Call Method     ${options}    add_argument    --disable-notifications
    ${driver}=    Create Webdriver    Chrome    options=${options}
    Go to       https://www.google.co.th/?hl=th
    Maximize Browser Window
    Set Selenium Speed	0.4 seconds

gotoFacebook
    Go To    https://www.facebook.com/
loginId
    Input Text    name=email    ${ID}
loginPass
    Input Text    name=pass     ${Pass}
    Click Button  name=login
Postpage
    Go To          https://www.facebook.com/TestMarket-104244495036936
    Click Element  //div[@class="buofh1pr"] 
    sleep  3 s
PressV
    Press Keys    none    CTRL+v
    Click Element   //div[@class="rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu tv7at329"]
    Set Selenium Speed	0.4 seconds
    