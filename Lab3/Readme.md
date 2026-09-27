
# Lab 03: Multi-Threaded TCP Server & Client

This repository contains the implementation of a multi-threaded TCP Client-Server architecture developed using Python's built-in `socket` and `threading` libraries.

---

## 📌 Project Overview

The objective of this lab is to demonstrate concurrent network communication. A single TCP server handles multiple incoming client connections simultaneously without blocking. Each client connection runs in its own dedicated worker thread, and console outputs are synchronized using thread locks to prevent race conditions.

---

## 🚀 Key Features

### Server (`server.py`)
- **Multi-Threading:** Dynamically spawns an isolated thread (`threading.Thread()`) for each incoming client.
- **Concurrency:** Handles multiple client sessions simultaneously.
- **Detailed Logging:** Prints active thread names (`Thread-1`, `Thread-2`), client IP addresses, and dynamic port numbers.
- **Thread Synchronization:** Uses `threading.Lock()` (`acquire()` and `release()`) to ensure clean, race-condition-free terminal output.

### Client (`client.py`)
- **Continuous Communication:** Maintains a persistent loop sending and receiving messages with the server.
- **Graceful Termination:** Allows user termination via the `exit` command to safely tear down the TCP socket.

---

## 📂 Repository Structure

```text
.
├── server.py              # Multi-threaded TCP server script
├── client.py              # TCP client script
├── README.md              # Project documentation
└── screenshots/           # Execution screenshots for evaluation
    ├── server_output.png  # Server console showing multiple threads
    ├── client1_output.png # Client 1 chat output
    └── client2_output.png # Client 2 chat output
```

---

## 🛠️ How to Run

### Step 1: Start the Server
Open your terminal and run:
```bash
python server.py
```

### Step 2: Run Client 1
Open a second terminal window and run:
```bash
python client.py
```

### Step 3: Run Client 2
Open a third terminal window and run:
```bash
python client.py
```

Type any text in either client window to send messages to the server. Type `exit` in any client terminal to safely disconnect.

---

## 📸 Output & Demonstration

### 1. Server Terminal (Multi-Threaded Handling)
The server confirms individual thread names, client IPs, ports, and concurrent active connections:
![image alt](https://github.com/ahsanafzal864-crypto/FA23-BSE-005-Ahsan-PDC/blob/main/Lab3/pics/Screenshot%202026-09-27%20202403.png?raw=true)

### 2. Client 1 Terminal
Bidirectional messaging exchange:
![image alt](https://github.com/ahsanafzal864-crypto/FA23-BSE-005-Ahsan-PDC/blob/main/Lab3/pics/Screenshot%202026-09-27%20202347.png?raw=true)

### 3. Client 2 Terminal
Simultaneous message exchange running parallel to Client 1:
![image alt](https://github.com/ahsanafzal864-crypto/FA23-BSE-005-Ahsan-PDC/blob/main/Lab3/pics/Screenshot%202026-09-27%20202331.png?raw=true)

---

## 📝 Submission Checklist
- [x] `server.py` and `client.py` implemented and verified
- [x] Multi-threading and thread locks integrated
- [x] Screenshots captured and added
