###[EveOnlineMarketAnalysisTool](https://github.com/funnymanpatrick/EveOnlineMarketAnalysisTool)  
* 7 contributors
* 62396 total lines of code
* Earliest commit: Feb 10, 2015
* Latest commit: Dec 3, 2015
* Current branches:
	* Merge
	* Web
	* develop
	* dygraphs
	* master

![GitStats](http://puu.sh/nCWl1/9cd2ba7a6f.png)

The only difference between the above and gitstats is that gitstats shows 10 contributors instead of 7, one of which was repeated.  

####[Youtube gource link](https://youtu.be/fVkju6Wuvr4)  

#Part 2  
The goal of this part of lab was to implement markdown translations for headers and blockquotes such that:  
  - `#` => `<h1>` and `</h1>` 
  - `##` => `<h2>` and `</h2>` 
  - `###` => `<h3>` and `</h3>` 
  - `>` => `<blockquote>` with `</blockquote>` at the end of the last line with a `>`  
  
The biggest challenge with these implementations was ensuring that all text within blockquotes are properly wraped in their respective tags as well. This was done by first handling all blockquotes, then filling in any tags that should appear inside them. Another challenge was handling the `</blockquote>` tag, as it required some form of read ahead or modification of the previous line which could not be done with the given implementation. In order to circumvent this I stored each input line in a list so that I could modify lines other than the one currently being parsed. 

Below is sample input/output and a unittest run:
![sample output](http://puu.sh/o2cBQ/396ff2c219.png)
  
  

