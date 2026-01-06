---
author: glenzac
categories:
  - uncategorized
cover:
  alt: seHp2JveXU
  image: "@assets/wp-content/uploads/2019/08/sehp2jvexu.gif"
date: "2020-07-23T09:07:25+00:00"

tags:
  - anki
  - latex
  - learning

title: Tips to make cool Anki cards for STEM subjects
---
- Copy Latex extension - I often found it hard to highlight equations on some wiki pages which is why I use this [extension](https://addons.mozilla.org/en-US/firefox/addon/latexcopy/?src=search#&gid=1&pid=2). Makes the job pretty easy.
- [One Note](https://www.onenote.com) \- to draw and add images and also draw over images
- add emojis - [Emojis in Anki to enhance learning – using AutoHotkey](/2019/08/21/emojis-in-anki-to-enhance-learning-using-autohotkey/)
- Use [ShareX](https://getsharex.com/) to clip perfect screenshots and also to annotate shots
- Use [Irfan View](https://www.irfanview.com/) to delete unwanted text and do basic editing
- [Tragic Marker](https://www.behance.net/gallery/36214355/Tragic-Marker-a-fat-marker-style-handwriting-font) Font / [Architect's Daughter](https://fonts.google.com/specimen/Architects+Daughter#standard-styles) \- for a hand-written feel
- [Anki Latex Helper](/2019/08/12/anki-latex-helper-using-autohotkey/) to insert equations easily
- Create [tables](https://www.tablesgenerator.com/) easily
- Use different colors to make it easier to learn things:

https://i.imgur.com/RMsdDsc.jpg

- Here's my card formatting code:

### Basic Card:

#### Front Template:

```
<div class=frontbg>

{{Front}}

 </div>

```

#### Styling

```
.card {
 font-family: Bariol;
 font-size: 30px;
 text-align: left;
 color: black;
 background-color: white;
}

/* COLOR ACCENTS FOR BOLD-ITALICS-UNDERLINE */
b { color: #e74c3c !important; } /* BOLD STYLE */
u { color:##9b59b6; text-decoration: none;} /* UNDERLINE STYLE */
i  { color:#2ecc71; } /* ITALICS STYLE */
a { color: LightGray !important; text-decoration: none; font-size: 10px; font-style: normal; } /* LINK STYLE */

.frontbg {
 background-color: #fffff;
 border-radius: 7px;
 color: #e74c3c;
font-weight: bold;
 position: relative;
 left: 0;
}

.backbg {
 position: relative;
 top: -2px;
 background-color: #fff;
 padding: 10px;
 padding-bottom: 15px;
 padding-left: 20px;
 padding-right: 30px;
 border-radius: 0px 0px 10px 10px;
 color: #000000;
 font-size: 28px;
 text-align: left;
}

```

#### Back Template:

```
<div class=frontbg>
{{FrontSide}}
<div class=backbg>
<hr id=answer>

{{Back}}

</div>
```

- Anki extensions to use
  - field-history
  - frozen-fields
  - image-occlusion-enhanced
  - large-and-colorful-buttons
  - mini-format-pack
  - more-overview-stats-21
  - review-heatmap
  - symbols
  - true-retention-by-card-maturity
  - load-balancer