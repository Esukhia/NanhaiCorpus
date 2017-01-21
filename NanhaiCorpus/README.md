# NanhaiCorpus

# TibetanCorpus

Resources for using the Tibetan Corpus. Access to the raw data and regex rules that help you analyze the corpus. 

First, familiarize yourself with AntConc for analysis. 

Download AntConc from http://www.laurenceanthony.net/software.html 
To make it useful for Tibetan, there's a few things you NEED to do: 

(1) enter "Global Settings". 

(2) Go to "Token Definition Setup" ('Token' here basically means 'character'--what characters will AntConc recognize?) 

(3) At the bottom, select "User-Defined Token Class" -- "Use Following Definition" 

(4) In the space available, copy & paste the following (the entire unicode set of Tibetan characters): 
ༀ༁༂༃༸༹ཀཁགགྷངཅཆཇ཈ཉཊཋཌཌྷཎཏཐདདྷནཔཕབབྷམཙཚཛཛྷཝཞཟའཡརལཤཥསཧཨཀྵཪཫཬ཭཮཯཰ཱཱཱིིུུྲྀཷླྀཹེཻོཽཾཿ྄ཱྀྀྂྃ྅ྌྍྎྏྐྑྒྒྷྔྕྖྗ྘ྙྚྛྜྜྷྞྟྠྡྡྷྣྤྥྦྦྷྨྩྪྫྫྷྭྮྯྰྱྲླྴྵྶྷྸྐྵྺྻྼ

(5) Will you be using a space-segmented Tibetan corpus? If yes, select "Append Following Definition" and add: 
་
The "tsheg". If not, AntConc will treat the "tsheg" as a non-character (a space) and you can analyze by syllable. 

(6) Be sure to hit "apply". 

If you have a space-segmented corpus, you may need to use the TshegRegex code to remove unwanted tshegs.
(For example, we want AntConc to see ཡོད་ and ཡོད as the same word, not different words; TshegRegex, included in this GitHub, will remove the final tshegs from word-separated text). 

Further normalization options to come... 
