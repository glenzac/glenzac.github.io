---
author: glenzac
categories:
  - "open-source"
  - "opinion"
cover:
  alt: wood-light-creative-space-68562
  image: "@assets/wp-content/uploads/2020/06/wood-light-creative-space-68562.jpg"
date: "2020-06-25T16:05:57+00:00"

summary: "I used to write a diary back in my school days. It is very comforting to write anything and everything into one. The feeling of having somebody, to listen to all your whims and fancies. \U0001F923"
tags:
  - diary
  - opensource
  - privacy
  - security

title: Privacy focused personal diary or journaling
---
I used to write a diary back in my school days. It is very comforting to write anything and everything into one. The feeling of having somebody, to listen to all your whims and fancies. 🤣

I stuck to keeping a physical diary during those days, as no gadgets were allowed in a boarding school. Even though I had access to one😅, it was practically impossible to be discreet enough to type things out into the tiny screens of those days, every single day.

So when I got to university, I didn't want to have another physical diary. I'm running out of places to safely hide such things 🤣 and the last thing I want to try and hide successfully, is a couple of big diaries. So I searched for good online solutions. The first thing I tried was [Journey](https://journey.cloud/). It did have a lot of features, but all those were only aiding to lock me up in their ecosystem. So I moved to the next good one: [Penzu](https://penzu.com/)

I opened an account and got used to everything on it. It looked good enough. Fast forward 2 years. Life happened in between and I got busy that I didn't do any of the reporting.🤣 In the end I only had 2 entries in my locked personal diary and both entries were written in the first week that I had found Penzu.

So recently I thought about getting back to writing journals again. I opened up my old Penzu account. The password to my Penzu account was in my KeepassXC DB but I had forgotten the special password to my private diary. I just couldn't remember it and I knew that the passwords I make are not guessable - not even for me.😅 I thought it was all over. Wait ...wait.... not yet. I was able to recover the whole thing with just a forgot password link in my mail. 😳 If it was truly encrypted this wouldn't have been possible. There shouldn't have been a backdoor or a way to fix it once the password is gone. This is what I call flawed encryption.

If at all you use Penzu, you've gotta be a premium user. At least that promises high grade encryption. I can't comment about anything in the premium plan as I haven't tried it.

One thing that also concerns me is that all your data is in some server, somewhere, in the hands of a small random company. And you can read about their poor customer support [here](https://appgrooves.com/app/penzu-free-diary-and-private-journal-by-penzu-inc/negative).

Another issue of concern here, is the use of [Grammarly](https://app.grammarly.com/) in your browser. In short; everything that you write on Penzu is being simultaneously uploaded into Grammarly servers and if that doesn't scare you, read the following post.

https://www.reddit.com/r/privacy/comments/b0y95z/why\_i\_removed\_grammarly\_chrome\_extension\_and/

**⚠️ To clear things up:** I've totally nothing against these companies - Penzu or Grammarly, just that I prefer my data locally and in my hands, especially when it comes to personal things like a diary.

So right now, I'm trying out a new open source software called [Laverna](https://laverna.cc/). Everything is saved locally on our computer and encrypted. And if at all you require, you can save the encrypted copy on Dropbox. You're safe from brute force attacks as long as you have a strong enough password. Moving from Penzu to Laverna forces you to give away a lot of usability. But ask me and I'll always only say: **Privacy >>>> Ease of use**

Laverna uses markdown while Penzu has a WYSIWYG editor. Once you get used to markdown editing you can type away for hours and not once leave the keyboard to click somewhere.

Another, maybe even safer way to write journal entries is with some word processor (or as .txt for max. compatibility) and then save the files to a container that you have set up using [Veracrypt](https://www.veracrypt.fr/en/Home.html). If you use encryption, in both cases i.e Laverna or using Veracrypt and if you forget or lose your password all your data is some useless random collection of bits that your can never decipher 😨...at least not in your lifetime. There's a remote chance though if quantum computers bring about a revolution. 😅🤣

Now, if you want both privacy and usability (ease of use). The one good and tested solution is One Note by Microsoft. Do note: Only the password protected sections are encrypted in One Note. More details [here](https://support.microsoft.com/en-us/office/protect-notes-with-a-password-in-microsoft-onenote-280af2bf-0959-4889-9191-e326b2bbedee). **I would never advocate the use of a proprietary tool but if you can't let go of any usability, this is your best choice.**

**To conclude :** If security is your top priority use the Veracrypt method. If you are okay with using proprietary tools and need a tool with a good interface use One Note. If you want a tool that is solely built and maintained for journaling and has all the features that you see in the other tools listed above minus the polished interface and usability - Laverna is yours.

Cover photo by **[Miguel Á. Padriñán](https://www.pexels.com/@padrinan?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)** from **[Pexels](https://www.pexels.com/photo/wood-light-creative-space-68562/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)**
