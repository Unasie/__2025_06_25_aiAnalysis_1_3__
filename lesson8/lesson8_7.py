import random

def get_bim():
    try:
        height = float(input('請輸入身高120-250cm:'))
        if (120 <= height <= 250):
            weight = float(input('請輸入體重30-200kg:'))
            if (30 <= weight <=200):
                BMI = weight / ((height  / 100) **2)
            else:
                print('體重範圍輸入錯誤')
        else:
            print('身高範圍輸入錯誤')
        print('你的BMI為:',round(BMI,1))
        

    except:
        print('輸入格式錯誤')
    finally:
        print('應用程式結束')

def get_status():
    get_bim()
    if BMI < 18.5:
        x = '體重過輕'
    elif 18.5 <= BMI < 24:
        x = '正常範圍'
    elif 24 <= BMI < 27:
        x = '體重過重'
    elif 27 <= BMI < 30:
        x = '輕度肥胖'
    elif 30 <= BMI < 35:
        x = '中度肥胖'
    elif BMI >= 35:
        x = '重度肥胖'
    print('您的BMI為',x)


if __name__ == "__main__":
    get_status()