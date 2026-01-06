---
author: glenzac
categories:
  - uncategorized
cover:
  alt: image-2
  image: "@assets/wp-content/uploads/2020/09/image-2.png"
date: "2020-09-24T05:49:09+00:00"

tags:
  - code
  - tips

title: How to get syntax highlighting in a PDF?
---
PDF inherently does not have any way to process the text and highlight the syntax. This has to be done in a word processing software and then it can be exported as a PDF.

I use the open source [Libre Office Writer](https://www.libreoffice.org/discover/writer/) for all such things. To get automatic syntax highlighting:

1. Use the [Code Highlighter](https://extensions.libreoffice.org/en/extensions/show/code-highlighter) extension for Libre Office which uses Python and a special python package called pygments to automatically perform syntax highlighting
1. If you use [Visual Studio code](https://code.visualstudio.com/) you only need to copy paste your code into Libre Office Writer and it comes with all syntax highlighting. (This is what I use)

![](@assets/wp-content/uploads/2020/09/image-1.png)

![](@assets/wp-content/uploads/2020/09/image-2.png)

I use the beautiful Monokai theme in VSCode but when I have to copy paste things I switch to a white theme. Otherwise I'll end up with something that looks like this 👇

![](@assets/wp-content/uploads/2020/09/image-3.png)

After that it's just a matter of exporting as PDF:

![](@assets/wp-content/uploads/2020/09/image-4.png)

If however you use [Notepad++](https://notepad-plus-plus.org/)

You can simply click on the copy RTF to clipboard option and then go back and paste it into a word document.

![](@assets/wp-content/uploads/2020/09/image-5.png)
