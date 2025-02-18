# **Windows Font Registration & Management via Registry** 🚀  

## **Overview**  
This project automates **font registration and deregistration** on Windows using the **Windows Registry**. It allows efficient activation and deactivation of fonts by modifying the registry at:  

```plaintext
HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Fonts\
```  

Additionally, it integrates with **FontCrawler1.exe**, which fetches activated fonts and displays them in the console.  

## **Key Features**  
✅ **Register fonts instantly** 🖋️  
✅ **Deregister fonts in real time** 🔄  
✅ **Track activated fonts using FontCrawler1.exe** 🔍  
✅ **Optimized registry operations for performance** ⚡  
✅ **Automated execution with minimal manual intervention**  

---

## **Project Structure** 🏗️  

```plaintext
📂 Windows-Font-Manager
│── main.py                 # Entry point to register/deregister fonts
│── constants.py            # Constants like font directory, registry path, etc.
│── font_operations.py      # Handles font registration & deregistration
│── font_registry.py        # Interacts with Windows Registry for font management
│── font_crawler.py         # Executes FontCrawler1.exe to fetch active fonts
│── FontCrawler1.exe        # Fetches active fonts from the registry
│── logs.txt                # Stores logs from font crawling operations
│── README.md               # This documentation file
```

---

## **Installation & Local Setup** 🛠️  

### **1️⃣ Prerequisites**  
- Windows OS (Administrator access recommended)  
- Python 3.x installed  
- Ensure the **WinReg** module is available (comes built-in with Windows Python installations)  

### **2️⃣ Clone the Repository**  
```sh
git clone https://github.com/matta-vaibhav/pythonfontsmanager.git
cd pythonfontsmanager
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

> **Note:** If `requirements.txt` is not provided, ensure you have `winreg` (comes by default) and `os`, `subprocess`, `time`, `re` (built-in libraries).  

### **4️⃣ Update Configuration (if needed)**  
Modify **constants.py** to match your font directory path:  

```python
FONT_DIRECTORY = "C:\\Users\\YourUser\\Downloads\\Fonts\\"
```

Ensure **FontCrawler1.exe** path is correctly defined:  

```python
CRAWLER_COMMAND = r'c:\src_vm\pythonfontsmanager\FontCrawler1.exe'
```

---

## **Usage** 🎯  

### **Register Fonts** 🖋️  
To register all fonts in the specified directory, comment out de-register statements from `main.py`
 
```sh
time.sleep(REFRESH_WAIT_TIME)
print("Deregistering Fonts")
font_ops.deregister_fonts()

time.sleep(REFRESH_WAIT_TIME)
fonts_after_deregistering = font_crawler.run()
print(f"Active Fonts After De-Registering = {fonts_after_deregistering}")
```
and run:  

```sh
python main.py
```

✅ This will:  
- Read font files (`.ttf`, `.otf`) from `FONT_DIRECTORY`  
- Add them to the **Windows Registry**  
- Fonts will be **immediately available** in applications  

### **Deregister Fonts** ❌  
To remove registered fonts from the registry, comment out de-register statements from `main.py`

```sh
time.sleep(REFRESH_WAIT_TIME)
fonts_before_registering = font_crawler.run()
print(f"Active Fonts Before Registering = {fonts_before_registering}")

time.sleep(REFRESH_WAIT_TIME)
print("Registering Fonts")
font_ops.register_fonts()

time.sleep(REFRESH_WAIT_TIME)
fonts_after_registering = font_crawler.run()
print(f"Active Fonts After Registering = {fonts_after_registering}")
```

the same command will **also handle deregistration**:  

```sh
python main.py
```

✅ This will:  
- Read font files from `FONT_DIRECTORY`  
- Remove them from the **Windows Registry**  
- Fonts will be **immediately removed** from applications  

> **Note:** If a font file is **moved/deleted**, applications automatically **treat it as deactivated**.  

### **Verify Activated Fonts** 🔍  
To check registered fonts, use **FontCrawler1.exe**:  

```sh
python font_crawler.py
```

✅ This will:  
- Run `FontCrawler1.exe`  
- Fetch and display all **currently activated fonts** on the console  
- Store the results in `logs.txt`  

---

## **How It Works** ⚙️  

### **1️⃣ Font Registration** (📜 `font_registry.py`)  
- Uses **Windows Registry API** (`winreg`) to add a font entry:  
  ```plaintext
  Font Name = "C:\path\to\font.ttf"
  ```
- This makes the font **instantly available** in apps like Photoshop, Word, etc.  

### **2️⃣ Font Deregistration** (📜 `font_registry.py`)  
- Removes the font entry from the registry.  
- Apps **immediately stop recognizing** the font.  

### **3️⃣ Fetching Active Fonts** (📜 `font_crawler.py`)  
- Executes **FontCrawler1.exe** to list activated fonts.  
- Uses regex to filter font paths from the logs.  

---

## **References & Documentation** 📚  
- [Registry Size Limits](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-element-size-limits)
- [Maximum Path Length Limits](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry)  
- [Windows Registry API](https://learn.microsoft.com/en-us/windows/win32/api/winreg/)  
- [Python `winreg` Module](https://docs.python.org/3/library/winreg.html)  

---

> **Happy Font Managing!** 🎨✨  

---