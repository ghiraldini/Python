# !/usr/bin/env python

import asyncio
import websockets
import time
import matplotlib.pyplot as plt

async def ws_read():
    async with websockets.connect(
            'ws://192.168.1.112:10999') as websocket:
        
        start = False
        spectra_arr = []
        id_arr = []
       

        while True:
            recv = await websocket.recv()
            if "<DATA>" in recv:         
                spectra_arr.clear()
                id_arr.clear()                
                count = 0
                # print(recv)

                for line_ in str(recv).split("\n"):
                    print("Line {}: {}".format(count, line_))
                    count+=1

                    if "<DATA>" == line_:
                        start = True
                        start_cnt = count

                    if start and count > start_cnt:
                        try:
                            idx, spectra_0, fit_0, res_0, spectra_1, fit_1, res_1 = str(line_).split(",")
                            spectra_arr.append(float(spectra_0))
                            id_arr.append(int(idx))
                        except ValueError:
                            pass

                    if "<\DATA>" == line_:
                        start = False
                        # break

                plt.figure(dpi=100)
                plt.plot(id_arr, spectra_arr)
                plt.title('Spectra')
                plt.legend(loc='best')
                plt.xlabel('DAQ Pt')
                plt.ylabel('Absorption')
                plt.show(block=True)
                
          
asyncio.get_event_loop().run_until_complete(ws_read())
asyncio.get_event_loop().run_forever()

