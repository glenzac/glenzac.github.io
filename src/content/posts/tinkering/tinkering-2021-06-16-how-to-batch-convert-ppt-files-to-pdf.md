---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: creative internet computer display
  image: "@assets/wp-content/uploads/2020/06/pexels-photo-2004161.jpeg"
date: "2021-06-16T13:46:44+00:00"

tags:
  - code
  - opensource
  - scripts

title: How to batch convert ppt files to pdf
---
Most professors use ppt files and by the end of the semester you have hundreds of them in a single folder. Opening a lot of these editable files hogs your PC down and all the editable UI take-up a lot of screen area. PDFs are a lot easier to work with.

I use the open source [LibreOffice](https://www.libreoffice.org/) suite for opening ppt files and I wrote a small PowerShell (PS) snippet after an hour of going through the documentation and reading forums and PS cmdlets documentation. I think it would have been a lot easier on a Linux machine.

### Requirements:

- LibreOffice
- PowerShell
- A folder with a ton of pdf files

## Snippet:

First open PowerShell in the folder that contains the files. You can either navigate to the folder using the command line or go to the folder using the GUI and `Shift + Right Click ` to see the "Open PowerShell window here". If you use Windows Terminal even that'll do.

```
Get-ChildItem *.ppt | ForEach-Object { & "C:\Program Files\LibreOffice\program\simpress.exe" --convert-to pdf $_ | Out-Null}
```

## How does it work?

The `Get-ChildItem` is a PS cmdlet that displays all the files with \*.ppt as extension in the current directory. This is piped to the next command instead of displaying it.

A `ForEach-Object` is a loop that iterates through each object that was obtained through `Get-ChildItem`

The command in { } is where the actual action takes place. The ampersand & is required to run the .exe in PS.

The script without the `Out-Null` starts a parallel operation with a lot of instances of LibreOffice Impress as could be seen in the Task Manager, and also PS does not wait for the files to be converted. So many files wouldn't get converted in time.

The `Out-Null` opens only one instance of LibreOffice in the background and moves to the next file only after the current one is done. This takes longer but ensures that all files get converted.

**Note:** In the newer versions of LibreOffice the parameter `--headless` is no longer explicitly needed and using `--convert-to` would be enough.   
If the files are .pptx modify the script accordingly.
