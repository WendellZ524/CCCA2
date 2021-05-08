import asyncio
import websockets
import json

def getjson(path):
    with open(path,encoding="utf8") as f:
        json = json.load(f)['features']
    return json



# check user name and password
async def check_permit(websocket):
    while True:
        recv_str = await websocket.recv()
        cred_dict = recv_str.split(":")
        if cred_dict[0] == "admin" and cred_dict[1] == "123456":
            response_str = "congratulation, you have connect with server\r\nnow, you can do something else"
            await websocket.send(response_str)
            return True
        else:
            response_str = "sorry, the username or password is wrong, please submit again"
            await websocket.send(response_str)

# receive meessage
async def recv_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        #response
        if recv_text == 'geojson':
            #response_text = str(type(recv_text))
            response_text = getjson('test_geo.json')
        else:
            response_text = f"your submit context: {recv_text}"
        await websocket.send(response_text)

# main logic
# websocket和path是该函数被回调时自动传过来的，不需要自己传
async def main_logic(websocket):
    #await check_permit(websocket)

    await recv_msg(websocket)

# change IP and port
start_server = websockets.serve(main_logic, 'localhost', 8080)
# 如果要给被回调的main_logic传递自定义参数，可使用以下形式
# 一、修改回调形式
# import functools
# start_server = websockets.serve(functools.partial(main_logic, other_param="test_value"), '10.10.6.91', 5678)
# 修改被回调函数定义，增加相应参数
# async def main_logic(websocket, path, other_param)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()