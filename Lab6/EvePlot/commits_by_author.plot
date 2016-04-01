set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'commits_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Commits"
set xtics rotate
set bmargin 6
plot 'commits_by_author.dat' using 1:2 title "Blake Lingenau" w lines, 'commits_by_author.dat' using 1:3 title "funnymanpatrick" w lines, 'commits_by_author.dat' using 1:4 title "chrisNvalmas" w lines, 'commits_by_author.dat' using 1:5 title "Patrick Hesselbach" w lines, 'commits_by_author.dat' using 1:6 title "MikeMacelletti" w lines, 'commits_by_author.dat' using 1:7 title "Mike Macelletti" w lines, 'commits_by_author.dat' using 1:8 title "Barry Hu" w lines, 'commits_by_author.dat' using 1:9 title "dlingenau" w lines, 'commits_by_author.dat' using 1:10 title "Josh Goldberg" w lines, 'commits_by_author.dat' using 1:11 title "Barry" w lines
