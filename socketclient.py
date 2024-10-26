import websocket
from time import sleep

def run_client():
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8765")
    
    for i in range(1, 10001):  # Send 10,000 messages
        message = f"Request [{i}] Hello world!"
        ws.send(message)
        
        # Receive and print the response
        response = ws.recv()
        print(f"Sent: {message} | Received: {response}")
        
        sleep(0.01)  # Optional: Small delay to avoid overwhelming the server
    
    ws.close()

run_client()
