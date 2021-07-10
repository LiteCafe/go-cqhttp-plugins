import flask
import json
import requests
import time

bot_server = flask.Flask(__name__)

@bot_server.route('/',methods=['POST'])

def server():
    data = flask.request.get_data().decode('utf-8')
    print(data)
    data = json.loads(data)

    if(data.get('message_type')):# 如果返回的是消息事件

        if(data.get('message_type')=='private'):
            QQid = str(data['sender'].get('user_id'))
            nickname = data['sender'].get('nickname')
            message = data.get('message')
            if(message[0:2]=='!!'):
                if(message[0:6]=='!!setu'):
                   # url = 'https://api.lolicon.app/setu/v2?r18=0'
                   # menu = requests.get(url)
                   # setu_url = menu.json()['data'][0]['urls'] # 对传回来的涩图网址进行数据提取
                   # setu_url = setu_url.get('original')
                   # command = 'http://127.0.0.1:5700/send_private_msg?user_id='+QQid+'&message=[CQ:image,file='+setu_url+']'
                   # requests.get(command)
                    command = 'http://127.0.0.1:5701/send_private_msg?user_id='+QQid+'&message=为了防止被风控，现已关闭!!setu指令'
                    requests.get(command)

                if(message[0:6]=='!!bing'):
                    if(message[7:8]):
                        day = str(message[7:8])
                    else:
                        day='0'
                    command = 'http://127.0.0.1:5701/send_private_msg?user_id='+QQid+'&message=[CQ:image,file=http://api.lt5d.cn/bing?day='+day+']'
                    requests.get(command)
                    print(command)

                if(message[0:9]=='!!weather'):
                    if(message[0:16]=='!!weather update'):
                        url = 'http://192.168.1.9/weather.php?update=true'
                        info = '天气已更新'
                        command = 'http://127.0.0.1:5701/send_private_msg?user_id='+QQid+'&message='+info
                        requests.get(command)
                        time.sleep(2)
                    else:
                        url = 'http://192.168.1.9/weather.php?update=false'
                    menu = requests.get(url).text
                    #print(menu)
                    menu = json.loads(menu)
                    temp = str(menu['now'].get('temp'))
                    feelsLike = str(menu['now'].get('feelsLike'))
                    status = menu['now'].get('text')
                    wind360 = str(menu['now'].get('wind360'))
                    windDir = menu['now'].get('windDir')
                    windScale = str(menu['now'].get('windScale'))
                    windSpeed = str(menu['now'].get('windSpeed'))
                    humidity = str(menu['now'].get('humidity'))
                    precip = str(menu['now'].get('precip'))
                    pressure = str(menu['now'].get('pressure'))
                    vis = str(menu['now'].get('vis'))
                    cloud = str(menu['now'].get('cloud'))
                    dew = str(menu['now'].get('dew'))
                    info = '柳州天气：\n今日温度:'+temp+'℃\n体感温度:'+feelsLike+'℃\n天气状况:'+status+'\n风向:'+windDir+' '+wind360+'°\n风力等级:'+windScale+'级\n风速:'+windSpeed+'km/h\n相对湿度:'+humidity+'%\n降水量:'+precip+'mm\n大气压强:'+pressure+'百帕\n能见度:'+vis+'km\n云量:'+cloud+'%\n露点温度:'+dew+'%\n祝你有愉快的一天!\n天气接口:https://dev.qweather.com/'
                    command = 'http://127.0.0.1:5701/send_private_msg?user_id='+QQid+'&message='+info
                    requests.get(command)
                
            if(message=='fuck'):
                command = 'http://127.0.0.1:5701/send_private_msg?user_id='+QQid+'&message=BAKA,竟然骂人家,呜呜呜,我要告诉我家长听!!'
                requests.get(command)
                time.sleep(2)
                command = 'http://127.0.0.1:5701/send_private_msg?user_id=2310933302&message=BAKA:'+QQid+'竟然骂人家,呜呜呜!!'
                requests.get(command)

        if(data.get('message_type')=='group'):
            groupid = str(data.get('group_id'))
            QQid = str(data['sender'].get('user_id'))
            nickname = data['sender'].get('nickname')
            message = data.get('message')
            if(message[0:2]=='!!'):

                if(message[0:6]=='!!setu'):
                   # url = 'https://api.lolicon.app/setu/v2?r18=0'
                   # menu = requests.get(url)
                   # setu_url = menu.json()['data'][0]['urls'] # 对传回来的涩图网址进行数据提取
                   # setu_url = setu_url.get('original')
                   # command = 'http://127.0.0.1:5700/send_private_msg?user_id='+QQid+'&message=[CQ:image,file='+setu_url+']'
                   # requests.get(command)
                    command = 'http://127.0.0.1:5701/send_group_msg?group_id='+groupid+'&message=[CQ:at,qq='+QQid+'],由于前萝卜特账户被风控，现已关闭!!setu指令'
                    requests.get(command)

                if(message[0:6]=='!!bing'):
                    if(message[7:8]):
                        day = str(message[7:8])
                    else:
                        day='0'
                    command = 'http://127.0.0.1:5701/send_group_msg?group_id='+groupid+'&message=[CQ:image,file=http://api.lt5d.cn/bing?day='+day+']'
                    requests.get(command)
                    print(command)
                
                if(message=='!!weather'):
                    if(message[0:16]=='!!weather update'):
                        url = 'http://192.168.1.9/weather.php?update=true'
                        info = '[CQ:at,qq='+QQid+']天气已更新'
                        command = 'http://127.0.0.1:5701/send_group_msg?group_id='+groupid+'&message='+info
                        requests.get(command)
                    else:
                        url = 'http://192.168.1.9/weather.php?update=false'
                    menu = requests.get(url).text
                    #print(menu)
                    menu = json.loads(menu)
                    temp = str(menu['now'].get('temp'))
                    feelsLike = str(menu['now'].get('feelsLike'))
                    status = menu['now'].get('text')
                    wind360 = str(menu['now'].get('wind360'))
                    windDir = menu['now'].get('windDir')
                    windScale = str(menu['now'].get('windScale'))
                    windSpeed = str(menu['now'].get('windSpeed'))
                    humidity = str(menu['now'].get('humidity'))
                    precip = str(menu['now'].get('precip'))
                    pressure = str(menu['now'].get('pressure'))
                    vis = str(menu['now'].get('vis'))
                    cloud = str(menu['now'].get('cloud'))
                    dew = str(menu['now'].get('dew'))
                        
                    info = '[CQ:at,qq='+QQid+']\n柳州天气：\n今日温度：'+temp+'℃\n体感温度:'+feelsLike+'℃\n天气状况:'+status+'\n风向:'+windDir+' '+wind360+'°\n风力等级:'+windScale+'级\n风速:'+windSpeed+'km/h\n相对湿度:'+humidity+'%\n降水量:'+precip+'mm\n大气压强:'+pressure+'百帕\n能见度:'+vis+'km\n云量:'+cloud+'%\n露点温度:'+dew+'%\n祝你有愉快的一天!\n天气接口:https://dev.qweather.com/'

                    command = 'http://127.0.0.1:5701/send_group_msg?group_id='+groupid+'&message='+info
                    requests.get(command)
                    
            
    return ''



if __name__ == '__main__':
    bot_server.run(port=8956)


