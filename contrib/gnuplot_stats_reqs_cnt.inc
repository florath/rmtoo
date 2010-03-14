set timefmt "%Y-%m-%d_%H:%M:%S"
set xdata time
set title "Requirements Count Statistics"
set ylabel "Count"
set xlabel "Time"
set output "stats_reqs_cnt.eps"
set terminal postscript eps
plot 'stats_reqs_cnt.csv' using 1:2 title 'requirement count' with lines
