def post_coords(angle, socket, UDP_IP, UDP_PORT):
    try:
        socket.sendto(f'Y {angle}\n'.encode(), (UDP_IP, UDP_PORT))
    except Exception as e:
        print(f"Error posting angle to socket: {e}")

def post_coords2d(coords, socket, UDP_IP, UDP_PORT):
    try:
        socket.sendto(f'X {coords[0]}\nY {coords[1]}\n'.encode(), (UDP_IP, UDP_PORT))
    except Exception as e:
        print(f"Error posting coords to socket: {e}")