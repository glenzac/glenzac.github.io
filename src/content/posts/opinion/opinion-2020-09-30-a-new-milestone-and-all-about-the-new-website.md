---
author: glenzac
categories:
  - "opinion"
cover:
  alt: pink green and yellow ribbon illustration
  image: "@assets/wp-content/uploads/2020/09/pexels-photo-796605.jpeg"
date: "2020-09-30T17:53:29+00:00"

tags:
  - milestone
  - website

title: A new milestone and all about the new website!
---
### [TL; DR](\#tl-dr)

* * *

I just hit 10k total views today and I thought this is a good day to brag about it 😂 forgive me for what follows. 😅

![](@assets/wp-content/uploads/2020/09/firefox_6f0fm9bvj6.png)

This started out as a place where I wrote my poems back in 2015 and it took years for it to metamorphosize into what it is now. With the COVID pandemic around, everybody hates 2020 but as far as the blog is concerned it is an awesome year. Does all this matter? Do I care about the figures?

Seriously NO! This just started out as my secret corner on the internet. I didn't want views or people to read it or anything. I was either doubtful or apprehensive about people I know, finding it and reading things. Internet strangers reading it was somehow fine. 🤣 Anyways, it took years for me to be comfortable with sharing this to people I know, and listing this blog on my profile and other places.😅 Okay enough backstory. 😂

* * *

This blog has a lot of random posts belonging to totally different topics with no relation between them. Some of them are tutorials, a lot of them my random rants and still many about the random things I like or do.

I decided to move the sane and the orderly things, mostly just the new tutorials and projects to a new website. I've been working on this for the past one month, whenever I got some free time. As always, my first thought was to go with another WordPress website as they make things so easy. WordPress is undoubtedly the easiest and best solution out there, for people to start blogging on. I've been using this for years now and never had to write a single line of code. It just works. The degree of customization and themes it offers is way more than what you'd expect from a free blogging platform.

I've compared [Google sites](https://sites.google.com/new), [blogger](https://www.blogger.com/)(this allows monetization of your site though), Wix and all those popular site building and blogging tools out there. None comes close.

But this time, I wanted to do some work. I didn't want things to be so easy. So my first stop was a static website on Github using [Github Pages](https://pages.github.com/). It uses [Jekyll](https://jekyllrb.com/) to create static websites. So I went forward and installed [Ruby](https://rubyinstaller.org/) and everything that was needed to create websites and posts. I could now simply write things in [Markdown](https://www.markdownguide.org/) format which was not very hard to learn. But configuring every single thing was so hard. Like I had full control over the site and all the elements. All those things had to be manually coded in. The menus, the footer, the header and every single thing. It soon became obvious that with my poor knowledge of HTML and CSS, I would never be able to complete it.

Searching for alternatives led me to this Github repo by [Barry Clark](https://github.com/barryclark) called [Jekyll Now](http://www.jekyllnow.com/) that helps create blogs in minutes. Its basically had all the elements that was needed for a simple blog. I could use it as a template and simply start writing posts one after the other. So I forked the repo and it took me a couple of days to get what those different files and things meant. I was finally able to tweak those files and also add posts. Then I decided to migrate couple of posts from this blog. Free WordPress.com only allows XML export. I used that along with a converter tool created by [Onur Baykal](https://github.com/theaob/wpXml2Jekyll) to convert them to Markdown. Everything was not perfect. Metadata didn't end up right. But it was good enough. I started adding those files and when I preview the site, all the images were in their original 😳 dimensions. If it was a good quality image, it was huge in size and overflowed. Thanks to the different image sizes the text was getting thrown around here and there. Asking Glin, helped clear the big confusion. The site does not know how to scale images and present them uniformly. So that property had to be coded in. 😐 Again totally beyond my scope! Now I was back to square one, and all I could hear was WordPress calling me to take it up and just get this new site done with. 😅

But NO! I came across a blog post from this Data Scientist, [George Cushen](https://georgecushen.com/). He has an open source project by the name Academic Website Builder. At least that was the name when I started using it. 😆 Now, it's called [Wowchemy Website Builder](https://wowchemy.com/). Anyways, the work he's done is magnificent and he has totally given it out for free! Anybody can use it to create websites for free. Its basically hosted on your Github Account and is fundamentally a template for [Hugo](https://github.com/gohugoio/hugo).

Even though it makes things pretty easy, the first time I cloned the repo and made changes, I broke things somewhere or moved the wrong files. I ended up messing up a lot of things. Then I had to call in Glin again to clean things up and eventually we ended up cloning it again. This time he taught me how to create the different sections and how to go about editing the config files to get things done.

Though this [blog post](https://georgecushen.com/create-your-website-with-hugo/) says - **no coding skills required** \- I totally disagree. There is a lot that one needs to know and understand. Configuring [Netlify](https://app.netlify.com/) CDN is just one thing. To reach at least 50% of the customization that one has on a free WordPress site, there is a lot that one needs to understand. I had to understand what [YAML](https://yaml.org/), [TOML](https://en.wikipedia.org/wiki/TOML) and all such things did to files. Understanding the general hierarchy of the site was mandatory. Though netlify has a CMS preview to write posts just like in WordPress but it is ages behind in terms of features. So I simply write my posts directly in Markown on [VSCode](https://code.visualstudio.com/) editor. The whole site is basically a repo on my Github page and it is built and served by Netlify. It's going to be much harder to maintain than this WordPress blog, but I'm sure that I'll learn a good deal about how to do such things along the way. Not to mention the satisfaction I get when I see hours of work tu.

### TL; DR

All the new tutorials, formal projects and portfolio will go to the new [website](https://glenzac.netlify.app/). If you check it now, you won't find pretty much anything. The Embedded Series Page on this website has been moved to the new website.

**[Take me there!](https://glenzac.netlify.app/)**

Everything else remains here. This will finally be more like a blog now.
