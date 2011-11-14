set terminal pdf
set grid
set output "graph.pdf"              
set datafile separator ","          
set xlabel "Garmin distance (km)"
set ylabel "Delta to Haversine distance (%)"
plot "data.txt" using 7:9 with lines notitle
set xlabel "Trackpoint"
set ylabel "Distance (km)"
plot "data.txt" using 5 with lines title "Haversine", "data.txt" using 7 with lines title "Garmin"
set xrange [0:20]
plot "data.txt" using 5 with lines title "Haversine", "data.txt" using 7 with lines title "Garmin"
