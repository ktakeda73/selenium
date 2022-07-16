import datetime

def get_screenshot(gmn_nm,v_browser):
    w = v_browser.execute_script("return document.body.scrollWidth;")
    h = v_browser.execute_script("return document.body.scrollHeight;")
    v_browser.set_window_size(w,h)

    now = datetime.datetime.now()
    nowdate = now.strftime('%Y%m%d_%H%M%S')
    
    FILENAME = nowdate + '_' + gmn_nm + '.jpg'
    v_browser.save_screenshot("./screenshot/"+FILENAME)