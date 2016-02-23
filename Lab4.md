###Sam Deslandes - Lab 4  

A total of 3 changes were made by our table: 
#Bug 1  
This [bug](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=207340) involed a case of 
mismatched quotation marks, in which the opening quotation mark was an apostrophe instead 
of a quotation mark. The generated diff can be viewed [here](http://puu.sh/ndVi9/f235b91825.png).  

#Bug 2
This [bug](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=207345) had an unnecessary 
apostrophe, making a word that should've been plural posessive. Our fix involed simply
 removing the apostrophe. The diff can be viewed [here](http://puu.sh/ndVB6/2b878ebf3e.png).  
 
#Bug 3
This [bug](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=207353) was also a grammatical
 error involing the improper use of the conjunction "or", preceeded by the adverb "not". The 
 fix was simply to change the "or" to "nor". The [diff](http://puu.sh/niHtS/c00ad4bfe9.png) can be viewed here.  
 
Maintaing good documentation is important because it is mutually beneficial for both prospetive contributors and the project itself.
With descriptive and clear documentation, contributors should have no problems getting acclimated with how the project works and at the same time
 have all of the resourses needed for them to get started. Similarly, if any road blocks arise, the documentation serves as a way of overcoming said 
 obstacle. As said in the lab description, "Good documentation enables good code. Good code enables good documentation."
 

