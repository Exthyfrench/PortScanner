import socket

# User input
host = input("Enter the host to scan: ")
port_range = input("Enter the port range to scan (e.g. 1-1024): ")

# Split the port range into the start and end ports
start_port, end_port = port_range.split("-")

# Convert the strings to integers
start_port = int(start_port)
end_port = int(end_port)

# Iterate through the ports
for port in range(start_port, end_port + 1):
  # Create a socket object
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Set a timeout
  s.settimeout(1)
  
  # Attempt to connect to the port
  result = s.connect_ex((host, port))
  
  # If the result is 0, the port is open
  if result == 0:
    print(f"Port {port}: OPEN")
  else:
    print(f"Port {port}: CLOSED")
    
  # Close the socket
  s.close()
