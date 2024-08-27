# -*- coding: utf-8 -*-
import scapy.all
from struct import unpack
from time import time
from photon_packet_parser import PhotonPacketParser
import tkinter
import overlay
import traceback
import subprocess



def create_circle(x, y, r, canvas, color):
    print(color)
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color)

win = overlay.Window(size=(360, 360), position=(0, 0), transparent=False, alpha=0.5, draggable=True)

canvas = tkinter.Canvas(win.root, width=360, height=360)
canvas.pack()

canvas.create_text(350, 350, text="S", font=("Arial", 12))
canvas.create_text(350, 10, text="E", font=("Arial", 12))
canvas.create_text(10, 350, text="W", font=("Arial", 12))
canvas.create_text(10, 10, text="N", font=("Arial", 12))

playercircle = create_circle(-10, -10, 4, canvas, "green")

players = []
resource_circles = []
chest_circles = []

def getResourceType(restype):
    if (restype >= 0 and restype <= 5):
        return "wood"
    elif (restype >= 6 and restype <= 10):
        return "stone"
    elif (restype >= 11 and restype <= 14):
        return "fiber"
    elif (restype >= 15 and restype <= 22):
        return "hide"
    elif (restype >= 23 and restype <= 27):
        return "ore"

def getChestType(chtype):
    if "standart" in chtype.lower() or "regular" in chtype.lower():
        return "lime"
    if "uncommon" in chtype.lower():
        return "aqua"
    if "rare" in chtype.lower():
        return "purple"
    if "legendary" in chtype.lower():
        return "orange"

def idToName(id):
    for player in players:
        if player['id'] == id:
            return player
    else:
        return None

def isPlayerReal():
    for player in players:
        if (time() - player['time']) > 5:
            try:
                canvas.delete(player["cr"])
                canvas.delete(player["lab"])
            except:
                pass

def on_event(data):
    isPlayerReal()
    if data.code == 3:
        print(data.parameters)
        id = data.parameters[0]
        x = unpack('f', data.parameters[1][9:13])[0] / 2
        y = unpack('f', data.parameters[1][13:17])[0] / 2
        player = idToName(id)
        print(player)
        if player:
            canvas.delete(player["cr"])
            canvas.delete(player["lab"])
            player["cr"] = create_circle(x + 150 + 30, 300 - (y + 150) + 30, 2, canvas, "red")
            player["lab"] = canvas.create_text(x + 145 + 30, 300 - (y + 145) + 30, text=player["name"], font=("Arial", 8))
            player["time"] = time()
    if len(data.parameters) > 2:
        print(data.code, data.parameters, "\nevent")
        event_code = int(data.parameters[252])
        if event_code == 37:
            x, y = int(data.parameters[8][0]) / 2, int(data.parameters[8][1]) / 2
            if data.parameters[11] == 1:
                circle = create_circle(x + 150 + 30, 300 - (y + 150) + 30, 2, canvas, "lime")
                label = canvas.create_text(x + 145 + 30, 300 - (y + 145) + 30, text=getResourceType(data.parameters[5]), font=("Arial", 8))
                resource_circles.append({"cr": circle, "lab": label})
            if data.parameters[11] == 2:
                circle = create_circle(x + 150 + 30, 300 - (y + 150) + 30, 2, canvas, "aqua")
                label = canvas.create_text(x + 145 + 30, 300 - (y + 145) + 30, text=getResourceType(data.parameters[5]), font=("Arial", 8))
                resource_circles.append({"cr": circle, "lab": label})
            if data.parameters[11] == 3:
                circle = create_circle(x + 150 + 30, 300 - (y + 150) + 30, 2, canvas, "purple")
                label = canvas.create_text(x + 145 + 30, 300 - (y + 145) + 30, text=getResourceType(data.parameters[5]), font=("Arial", 8))
                resource_circles.append({"cr": circle, "lab": label})
        if event_code == 27:
            id = data.parameters[0]
            if idToName(id) == None:
                name = data.parameters[1]
                x, y = int(data.parameters[14][0]) / 2, int(data.parameters[14][1]) / 2
                circle = create_circle(x + 150 + 30, 300 - (y + 150) + 30, 2, canvas, "red")
                label = canvas.create_text(x + 145 + 30, 300 - (y + 145) + 30, text=name, font=("Arial", 8))
                players.append({"id": id, "cr": circle, "lab": label, "name": name, "time": time()})
        if event_code == 378:
            x, y = int(data.parameters[1][0]) / 2, int(data.parameters[1][1]) / 2
            circle = create_circle(x + 150 + 30, 300 - (y + 150) + 30, 2, canvas, getChestType(data.parameters[3]))
            label = canvas.create_text(x + 145 + 30, 300 - (y + 145) + 30, text="chest", font=("Arial", 8))
            chest_circles.append({"cr": circle, "lab": label})
        if event_code == 208:
            for circle in resource_circles:
                canvas.delete(circle["cr"])
                canvas.delete(circle["lab"])
            for circle in chest_circles:
                canvas.delete(circle["cr"])
                canvas.delete(circle["lab"])
            resource_circles.clear()
            chest_circles.clear()

    pass

def on_request(data):

    print(data.operation_code, data.parameters, "\nrequest")

    x, y = int(data.parameters[3][0]) / 2, int(data.parameters[3][1]) / 2
    global playercircle
    canvas.delete(playercircle)
    playercircle = create_circle(x + 150 + 30, 300 - (y + 150) + 30, 2, canvas, "yellow")

    pass

def on_response(data):

    print(data.operation_code, data.return_code, data.deubg_message, data.parameters, "\nresponse")

    pass

parser = PhotonPacketParser(on_event, on_request, on_response)

def processor(capture):
    win.root.update()
    try:
        if int(capture[scapy.all.IP].sport) == 5056 or int(capture[scapy.all.IP].dport) == 5056:
            source = capture[scapy.all.UDP].payload.load
            parser.HandlePayload(source)
    except Exception as e:
        print("error", traceback.format_exc())

win.after(1, scapy.all.sniff(iface=None, filter="udp", prn=processor))
win.launch()
