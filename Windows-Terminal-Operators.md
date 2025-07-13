# Windows terminal operations

### Summary 
- [`Syntex Operations`](#syntex-operations) : :
[*`File/Folder`*](#file-and-folder-operations) , [*`System`*](#system-operations), [*`Network`*](#network-operations), [*`Running Programs`*](#running-programs), [*`Process Management`*](#process-management), [*`Disk & Drive`*](#disk--drive-management), [*`User Account`*](#user-account-operations), [*`PowerShell-Specific`*](#powershell-specific-advanced), [*`Other Handy Commands`*](#other-handy-commands), [*`Navigation Shortcuts`*](#navigation-shortcuts)
 

- [`Terminal Open Commands`](#terminal-open-commands) : : [*`Text`*](#Text-editors) , [*`Web`*](#web-browsers) , [*`Office`*](office-applications) , [*`Utilities`*](#utilities) , [*`General`*](#general-structure)
  
- [`Terminal Close Commands`](#terminal-close-commands)

 
<br>

## Syntex Operations

1. File and Folder Operations
<h6>
  
| Task                  | Command Example                   |
| --------------------- | --------------------------------- |
| Create a folder       | `mkdir myFolder`                  |
| Create a file         | `echo. > myfile.txt`              |
| List files/folders    | `dir`                             |
| Change directory      | `cd foldername`                   |
| Go back one directory | `cd ..`                           |
| Rename file/folder    | `ren old.txt new.txt`             |
| Delete file           | `del myfile.txt`                  |
| Delete folder         | `rmdir myFolder /S /Q`            |
| Copy file             | `copy file1.txt folder\file2.txt` |
| Move file             | `move file1.txt folder\file1.txt` |
</h6>



2. System Operations
<h6>
  
| Task                       | Command Example                           |
| -------------------------- | ----------------------------------------- |
| View system info           | `systeminfo`                              |
| View environment variables | `set`                                     |
| Restart computer           | `shutdown /r /t 0`                        |
| Shut down computer         | `shutdown /s /t 0`                        |
| Lock computer              | `rundll32.exe user32.dll,LockWorkStation` |
| Log off                    | `shutdown /l`                             |
</h6>


3. Network Operations
<h6>
  
| Task                     | Command Example                         |
| ------------------------ | --------------------------------------- |
| Check IP configuration   | `ipconfig`                              |
| Release/renew IP         | `ipconfig /release` → `ipconfig /renew` |
| Test internet connection | `ping google.com`                       |
| Trace route              | `tracert google.com`                    |
| Check open ports         | `netstat -an`                           |
| Show ARP table           | `arp -a`                                |
</h6>


4. Running Programs
<h6>
  
| Task         | Command Example        |
| ------------ | ---------------------- |
| Open Notepad | `notepad`              |
| Open Chrome  | `start chrome`         |
| Open Word    | `start winword`        |
| Run any .exe | `"C:\Path\to\app.exe"` |
</h6>


5. Process Management
<h6>
  
| Task                   | Command Example               |
| ---------------------- | ----------------------------- |
| List running processes | `tasklist`                    |
| Kill a process         | `taskkill /IM notepad.exe /F` |
</h6>



6. Disk & Drive Management

<h6>
  
| Task                     | Command Example             |
| ------------------------ | --------------------------- |
| Check disk usage         | `chkdsk`                    |
| List drives              | `wmic logicaldisk get name` |
| Open Disk Management GUI | `diskmgmt.msc`              |
</h6>



7. User Account Operations
<h6>
  
| Task              | Command Example                   |
| ----------------- | --------------------------------- |
| List all users    | `net user`                        |
| Create a new user | `net user username password /add` |
| Delete a user     | `net user username /delete`       |
| Change password   | `net user username newpassword`   |
</h6>


8. PowerShell-Specific (Advanced)
<h6>
  
| Task                   | Command Example                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| Get installed programs | `Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*` |
| Get system info        | `Get-ComputerInfo`                                                                         |
| Download file          | `Invoke-WebRequest URL -OutFile file`                                                      |
| Create CSV report      | `Export-Csv`                                                                               |
</h6>


 


🛠️ 9. Other Handy Commands
<h6>
  
| Task                  | Command              |
| --------------------- | -------------------- |
| Clear terminal screen | `cls`                |
| Open Control Panel    | `control`            |
| Open Task Manager     | `taskmgr`            |
| Open Settings         | `start ms-settings:` |
</h6>


📁 10. Navigation Shortcuts
<h6>
  
| Command    | Purpose                         |
| ---------- | ------------------------------- |
| `.`        | Current directory               |
| `..`       | Parent directory                |
| `/` or `\` | Directory separator             |
| `TAB`      | Auto-complete folder/file names |
</h6>



---
<br>
<br>
<br>


## Terminal open commands 
Here’s a list of common software and their(basic structure):

Text Editors
<h6>
  
| Software  | Command                     |
| --------- | --------------------------- |
| Notepad   | `notepad`                   |
| WordPad   | `write`                     |
| Notepad++ | `notepad++`                 |
| VS Code   | `code` *(if added to PATH)* |

</h6>


Web Browsers
<h6>
  
| Browser           | Command                                   |
| ----------------- | ----------------------------------------- |
| Chrome            | `start chrome` or `chrome` *(if in PATH)* |
| Firefox           | `start firefox` or `firefox`              |
| Edge              | `start msedge`                            |
| Internet Explorer | `start iexplore`                          |
</h6>



Office Applications
<h6>
  
| Application          | Command          |
| -------------------- | ---------------- |
| Microsoft Word       | `start winword`  |
| Microsoft Excel      | `start excel`    |
| Microsoft PowerPoint | `start powerpnt` |
| Microsoft Outlook    | `start outlook`  |
</h6>


Utilities

<h6>
  
| Utility        | Command        |
| -------------- | -------------- |
| Calculator     | `calc`         |
| Paint          | `mspaint`      |
| Snipping Tool  | `snippingtool` |
| File Explorer  | `explorer`     |
| Command Prompt | `cmd`          |
| PowerShell     | `powershell`   |
| Task Manager   | `taskmgr`      |
| Control Panel  | `control`      |
</h6>

 


General Structure
```
<executable-name> [optional-file-path or arguments]
```

Examples
```
notepad myfile.txt
start chrome https://google.com
start excel myfile.xlsx
```
If a program is not in your system PATH, you need to give its full path:

```arduino
"C:\Program Files\SomeApp\app.exe"
```


---
<br>
<br>
<br>


## Terminal Close commands 

### 1. Using taskkill (Command Prompt / PowerShell)

The general syntax: 
```php-template
taskkill /IM <process_name> /F
/IM = image name (process name)

/F = force close
```


Examples:
<h6>
  
| Application   | Close Command                                       |
| ------------- | --------------------------------------------------- |
| Notepad       | `taskkill /IM notepad.exe /F`                       |
| Word          | `taskkill /IM winword.exe /F`                       |
| Excel         | `taskkill /IM excel.exe /F`                         |
| Chrome        | `taskkill /IM chrome.exe /F`                        |
| Firefox       | `taskkill /IM firefox.exe /F`                       |
| Edge          | `taskkill /IM msedge.exe /F`                        |
| VS Code       | `taskkill /IM code.exe /F`                          |
| Paint         | `taskkill /IM mspaint.exe /F`                       |
| Calculator    | `taskkill /IM Calculator.exe /F`                    |
| Snipping Tool | `taskkill /IM SnippingTool.exe /F`                  |
| File Explorer | `taskkill /IM explorer.exe /F` *(not recommended!)* |
</h6>






Caution:
- Be careful with closing explorer.exe, taskmgr.exe, or system-critical apps, as it can affect system behavior.
- You can restart explorer.exe after closing it using:

```sql
start explorer.exe
```




---
<br>
<br>
<br>



