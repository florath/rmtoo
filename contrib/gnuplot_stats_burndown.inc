set timefmt "%Y-%m-%d"
set xdata time
set title "Burndown diagram"
set ylabel "EfE units"
set xlabel "Time"
set output "stats_burndown.eps"
set terminal postscript eps
plot 'stats_burndown.csv' using 1:5 title 'Open (not done + assigned)' with lines, 'stats_burndown.csv' using 1:2 title 'Not done' with lines, 'stats_burndown.csv' using 1:3 title 'Assigned' with lines, 'stats_burndown.csv' using 1:4 title 'Finished' with lines, 'stats_burndown.csv.est' using 1:2 title 'Estimation' with lines

