from time import time
import sacn
import time

sender = sacn.sACNsender()
sender.start()
sender.activate_output(5)
sender[5].multicast = True

red = [255, 0, 0, 0]

data = []
for i in range(84):
    for j in red:
        data.append(j)
sender[5].dmx_data = data

time.sleep(5)
sender.stop()