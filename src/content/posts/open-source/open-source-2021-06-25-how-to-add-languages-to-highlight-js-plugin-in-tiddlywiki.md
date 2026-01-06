---
author: glenzac
categories:
  - "open-source"
cover:
  alt: TiddlyWiki_TiddlerPoster_en_S
  image: "@assets/wp-content/uploads/2021/06/tiddlywiki_tiddlerposter_en_s-1.png"
date: "2021-06-25T22:45:49+00:00"

tags:
  - opensource
  - tiddlywiki

title: How to add languages to Highlight.js plugin in TiddlyWiki
---
The documentation only describes how it's to be done on a Linux machine with TiddlyWiki running on a node server. Here's how it can be done on Windows.

## Single File HTML TiddlyWiki / On TiddlyDesktop:

In this case every configuration is within the HTML file itself. First, open your TiddlyWiki then click the `More` tab on the right side panel and click on `Shadows` then scroll all the way down to the tiddler by the title: `$:/plugins/tiddlywiki/highlight/highlight.js`

This file is what you should be editing. Finally go to the main Highlight.js project and download the JavaScript syntax highlighting code for the language you want. At the time of this writing the TiddlyWiki plugin supports Highlight.js version 9.18.1 while the main project is running version 11. To find the right files use the following link. (This one is for verilog, replace it with the language you want)

[https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/languages/verilog.min.js](https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/languages/verilog.min.js)

Copy the lines of code from this website and go and paste it into that particular shadow tiddler at the bottom. You'll find other similar ones for python, css and all.

## On Node.js

Navigate to you node local user directory:

Which can be either `C:\Users\username\AppData\Local` or `C:\Users\username\AppData\Roaming`

Where you'll find the folder: `node_modules/tiddlywiki/plugins/tiddlywiki/highlight/files/highlight.pack.js`

Do the same steps as above with this .js file.

Restart your node instance or TiddlyDesktop for the changes to be reflected.
