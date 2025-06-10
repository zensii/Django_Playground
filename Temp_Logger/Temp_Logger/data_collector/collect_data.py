import socket
from datetime import datetime, timezone


def query_sensor() -> dict:
    """
    Connects to the iServer at (ip, port), sends 'command', and returns the raw ASCII response.
    Example command: "*SRTF\r" (get temp in F from Probe 1)
    """
    ip_address = '172.31.166.128'
    port = 2000
    commands = "*SRTC", "*SRHC", "*SRDC"

    # 1. Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5.0)  # be sure to handle timeouts gracefully
        sock.connect((ip_address, port))
        result = []
        log = {}
        # 2. Send the ASCII command
        for cmd in commands:
            sock.sendall(cmd.encode("ascii"))

            # 3. Read until newline/timeout
            #    The device will typically send back something like "076.6" (no newline)
            data = sock.recv(1024)  # buffer size is arbitrary; data payload is small
            result.append(float(data.decode("ascii").strip('\r\n')))

        temp, humdity, duepoint = result
        log['datetime'] = datetime.now(timezone.utc)
        log["temp"] = temp
        log["humdity"] = humdity
        log["duepoint"] = duepoint

        return log


if __name__ == "__main__":
    resp = query_sensor()
    print (resp)
    print(
        f"Datetime: {resp['datetime']}\n"
        f"Temperature: {resp['temp']}C\n"
        f"Humidity: {resp['humdity']}%\n"
        f"Due Point: {resp['duepoint']}C"
    )
