---
author: glenzac
categories:
  - "open-source"
cover:
  alt: TiddlyWiki_TiddlerPoster_en_S
  image: "@assets/wp-content/uploads/2021/06/tiddlywiki_tiddlerposter_en_s-1.png"
date: "2021-06-23T14:15:09+00:00"

tags:
  - knowledgebase
  - opensource
  - tiddlywiki

title: Using TiddlyWiki on Windows
---
[TiddlyWiki](https://tiddlywiki.com/) is a non-linear personal web notebook. This open source project started a decade ago and is still going strong. TiddlyWiki looks so simple and yet very complex underneath that even deciding among the available options for setting it up is hard.

## TiddlyWiki - Usage modes

TiddlyWiki can be used in two ways: Single file method or as multiple files.

### Single File method

The single file method is like writing into a single notebook. It's the easiest way to try TiddlyWiki. The whole thing is an HTML file. One single file to write into and configure. It can be viewed in any browser and every setting and configuration exist as HTML, CSS or JavaScript in that very file (but hidden behind a clean interface). Even your data is stored as plain text in that very file.

### Multi-file method

Just as a notebook contains notes, so does a TiddlyWiki contain tiddlers. So instead of having one single file, this is like writing your notes into multiple sheets of paper and you have full control over how to organize them and store them. Instead of a single HTML file you will have individual tiddlers. It's easy to move things around and helps the git based workflow.

There are multiple pros and cons for both the methods. If you're unsure I'd advise you to go for the single file method.

## TiddlyWiki - Installation Methods (Windows)

1. **"I don't wanna install anything!"**\- \[One file method\] In this case you can simply:
   - download-the-empty-html-from-the-tiddlywiki-site
   - move-it-to-your-desired-folder
   - open-this-.html-file-in-your-favorite-browser-whenever-you-need-to-run-tiddlywiki
   - make-sure-to-click-the-save-button-which-will-be-a-red-checkmark
   - "this-will-download-the-file-again-and-you've-to-overwrite-it-with-the-existing-one"
   - definitely-not-very-intuitive-but-it-works!
1. **TiddlyDesktop** \- \[One file method\] This is the [desktop client](https://github.com/Jermolene/TiddlyDesktop/releases) for Windows. Its still in its very early stages though.
   - download-the-.zip-file-based-on-your-system---32/64bit
   - extract-it-to-any-desired-location
   - run-the-`nw.exe`-file-to-launch-the-application
   - click-on-the-`+create-new-wiki`-button-and-use-the-empty-tiddlywiki-option
   - "you'll-be-prompted-to-choose-the-location-for-your-html-file"
   - your-tiddlywiki-opens-up
   - clicking-the-save-button-on-the-right-automatically-updates-the-.html-file
1. **Node.js method** \- \[Multi file method\] This method involves the use of Node.js to create a server to run TiddlyWiki.
   - "install-[node.js](https://tiddlywiki.com/#node.js)-and-during-the-installation-you'll-be-prompted-to-install-some-c++-compiler-tools-which-can-be-skipped."
   - open-a-command-line-terminal-and-type:-`npm-install--g-tiddlywiki`
   - check-[tiddlywiki](https://tiddlywiki.com/#tiddlywiki)-is-installed-by-typing:-`tiddlywiki---version`
   - navigate-to-the-folder-where-you-want-to-setup-tiddlywiki
   - use-`tiddlywiki-mynewwiki---init-server`-to-create-a-folder-for-a-new-wiki-that-includes-server-related-components
   - `tiddlywiki-mynewwiki---listen`-to-start-[tiddlywiki](https://tiddlywiki.com/#tiddlywiki)
   - in-your-browser-launch-[http://127.0.0.1:8080/](http://127.0.0.1:8080/)-to-access-the-server
   - your-tiddlywiki-opens-up-and-you-can-see-that-every-time-you-create-a-new-tiddler-a-file-keeps-getting-added-in-the-folder
   - i-found-it-to-be-syncing-automatically
   - note-that-every-time-you-need-to-open-your-tiddlywiki-you-need-to-run-the---listen-command-in-the-folder-where-your-tiddlywiki-is-stored.-or-perhaps-use-any-of-those-batch-scripts-available-online-that-automatically-runs-it-for-you-at-startup.
1. Other methods that are noteworthy:
   - saving-on-beaker-browser-(no..not-another-browser-:(-)
   - [timimi:-webextension](https://ibnishak.github.io/timimi/)-and-native-host-by-riz-(needs-a-background-service-application)
   - plus-plus-a-lot-more-on-the-website...