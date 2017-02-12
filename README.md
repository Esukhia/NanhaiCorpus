# NanhaiCorpus

The Nanhai Corpus is a collection of word-segmented Tibetan totalling some 1.2 million words. The corpus contains 3 main sections: 

(1) Natural Speech -- Labeled "Speech_Natural_XXXX", where XXXX is a topic/genre category, of natural speech (full days were recorded with a clip-on mic). 

(2) Scripted & Prompted Speech -- Labeled "Speech_Dialogs_XXXX", which are transcripts of dialogs created for educational purposes; and "Speech_Studio_XXXX", which are transcripts of prompted speech, usually on topics of monastic life. 
  -- All speech data was collected in the Himalaya Diaspora (India/Nepal). ("Speech_UNDEFINED" means the tracking system between the audio and transcript has been misplaced; we are working to resolve these missing data tags). 
  
(3) Modern Writing -- Labeled "Writing_Modern_Children'sLit..." or "Writing_Modern_News_XXXX_YYYY", where XXXX is the dialect/region represented by the data source (being AMDO, KHAM, LHASA, or CENTRAL) and YYYY is the topic/genre of the excerpt. 

A 4th section is under construction, representing Middle Tibetan texts (aka "Classical" Tibetan—we prefer the more accurate, modern linguistic term "Middle Tibetan" to describe this register and era: Old Tibetan, Middle Tibetan, Modern Tibetan just as Old English, Middle English, Modern English. 

The Nanhai Corpus Folder contains 3 subfolders: 

(1) CORPUS_TEXT -- contains the raw, word-segmented data (to be analyzed by corpus tools like AntConc [instructions below] or WordSmith, etc.) 

(2) FREQ_LISTS -- some rudimentary frequency lists, by level. The best-made thus far is "GSL_LevelA1.txt", which is the 300 most frequent headwords from a balanced subsection of the full corpus, representing 50% speech, 50% writing. 

(3) LEMMA -- some rudimentary Python scripts useful for "cleaning" the data for headword analysis (a basic stemmer, a tsheg-stripper). POS (part of speech) and true Lemma tagging are under construction... 

The corpus texts are currently available in 3 Unicode encodings: 1) utf-16 (sometimes simpy called "Unicode", as in NotePad), 2) utf-8, and 3) utf-8-sig. Which one you use will depend on your software and OS (see below for some options). I've also included the Python script used to convert between encodings. 

Enjoy! Send feedback to the repo developer: thedirk[AT]gmail.com 

INSTRUCTIONS for USING the CORPUS
------------------------------------
Instructions for using WordSmith in analysis: See the update UTF16 files. WordSmith can't analyze UTF8 or UTF8-SIG encodings. There are still some kinks to work out, and I'll be updating this repo with any strides we make in that area. A better, FREE option, for analyzing Tibetan corpora is AntConc... 

Instructions for using AntConc in analysis: 

FIRST, the bad news: You will need MAC or LINUX for AntConc. While there is a Windows version (that works for Latin-based alphabets), the Tibetan font encodings are an insurmountable issue for AntConc in Windows. We've spent days and days trying to come up with a solution to get AntConc working in Windows with Tibetan, to no avail; if you have a solution, please share it! 

NOW, the good news: Fortunately, those of you with Windows machines CAN still use AntConc... in a round-about way. What you'll need to do is install a Virtual Machine with an Ubuntu OS (or your other preferred Linux distro). For that, follow the instructions here: https://www.lifewire.com/install-ubuntu-linux-windows-10-steps-2202108 

If you're on a 64-bit machine, you'll also need to add the i386 architechture & libraries. From a terminal, enter:

(1) sudo apt-get install libc6-i386
(2) sudo dpkg --add-architecture i386
(3) sudo apt-get install libx11-6:i386 libxss1:i386 libxft2:i386

That's it! 

Download AntConc from http://www.laurenceanthony.net/software.html 
To make it useful for Tibetan, there's a few things you NEED to do: 

(1) enter "Global Settings". 

(2) Go to "Token Definition Setup" ('Token' here basically means 'character'--what characters will AntConc recognize?) 

(3) At the bottom, select "User-Defined Token Class" -- "Use Following Definition" 

(4) In the space available, copy & paste the following (the entire unicode set of Tibetan characters): 
ༀ༁༂༃༸༹ཀཁགགྷངཅཆཇ཈ཉཊཋཌཌྷཎཏཐདདྷནཔཕབབྷམཙཚཛཛྷཝཞཟའཡརལཤཥསཧཨཀྵཪཫཬ཭཮཯཰ཱཱཱིིུུྲྀཷླྀཹེཻོཽཾཿ྄ཱྀྀྂྃ྅ྌྍྎྏྐྑྒྒྷྔྕྖྗ྘ྙྚྛྜྜྷྞྟྠྡྡྷྣྤྥྦྦྷྨྩྪྫྫྷྭྮྯྰྱྲླྴྵྶྷྸྐྵྺྻྼ

(5) In "Append Definition", add the 'tsheg' (་)

(6) Be sure to check the boxes! And hit "apply"... 

Note: In Linux OS, like Ubuntu, you should be good to go. In Windows, there is a problem: While AntConc can internally read the Tibetan, it doesn't recognize file names in Tibetan... I'll post a version of the corpus that uses only ASCII characters in the following weeks. 
