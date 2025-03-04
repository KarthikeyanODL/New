import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import kafka_producer

def on_message(ws, message):
    #print("Kamal Entered Here")
    print(message)
    kafka_producer.transaction_producer(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        while True:
        #for i in range(3):
            time.sleep(1)
            ws.send('{"op": "unconfirmed_sub"}')
            #print("Kamal:Send Request")
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.blockchain.info/inv",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
