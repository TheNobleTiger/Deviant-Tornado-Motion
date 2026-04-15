cm1runs is the directory of cm1 runs. currently inside you will find the following:
 - Default Runs (This is based purely on the standard cm1 runs with no changes made after compiling)
 - elreno (This is simulating using a sounding sourced from the May 31 2013 El Reno tornadic event)

.gitattributes:
 - This is to filter out .nc files, our runs are too large to do a standard push. I have to utilize git lfs.

cm1visualizer.py:
 - This python script is being developed to simulate various different products from the CM1 model, the goal is for variables at the top to be enabled true or false. Using if statements the program then will plot the specefied items (or save the outputs as pngs in a folder you name). The program has been well commented, my goal is that someone who has never read code could take a look at the file at any line and understand what is going on (the what and why).

radarscope-br.pal/radarscopeBR_raw.pal:
 - Rather than use a standard color map I wanted to incorporate the visuals of radarscopes expert color palette, this was something I worked on previously with my mentor as a fun coding challenge. I wanted to utilize this again but I also provided the raw file if you wanted to reverse engineer what I have done.
