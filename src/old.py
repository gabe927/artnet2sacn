import sacn
from stupidArtnet import StupidArtnetServer
from functools import partial

numUniverses = 60

# callback handler
def newPacket(data, u):
    s[u].dmx_data = data

# start servers
a = StupidArtnetServer()
s = sacn.sACNsender()
s.start()

# activate universes
# for i in range(numUniverses):
#     a.register_listener(i, callback_function=partial(newPacket, u=i+1))
#     s.activate_output(i+1)
#     s[i+1].multicast = True

# a.register_listener(0, sub=0, net=0, is_simplified=False, callback_function=print)
a.register_listener(0, sub=1, net=0, is_simplified=False, callback_function=print)
# a.register_listener(0, is_simplified=True, callback_function=print)
# a.register_listener(15, is_simplified=True, callback_function=print)

try:
    # run until button pressed
    input("Press Return to stop...")
finally:
    # shutdown
    s.stop()
    del a