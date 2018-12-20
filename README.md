# town-sim-py
Town growth simulator that creates road networks.

Outputs a text file which contains lists of roads, and if the road is curved, a list of its turning points. 

## Commandline Options
---
```
usage: graph.py [-h] [--noui] [-o OUTPUT] [-s SIZE] [-c CYCLES] [-p2 PHASE2]
                [-p3 PHASE3] [-ma MAJOR] [-mi MINOR] [-by BYPASS]
                [-br BRIDGES]

optional arguments:
  -h, --help            show this help message and exit
  --noui                Suppresses UI if set.
  -o OUTPUT, --output OUTPUT
                        Output file name. Default: output.txt.
  -s SIZE, --size SIZE  n for nxn grid. Default: 200.
  -c CYCLES, --cycles CYCLES
                        The number of full cycles to run before ending
                        simulation in commandline. The simulation does not
                        self-terminate when running in UI. Default: 15.
  -p2 PHASE2, --phase2 PHASE2
                        Minimum total prosperity to allow calculation for
                        bypass roads. Default: 200000.
  -p3 PHASE3, --phase3 PHASE3
                        Minimum total prosperity to allow calculation for
                        minor roads. Default: 80000.
  -ma MAJOR, --major MAJOR
                        Minimum local prosperity for a new major road.
                        Default: 10.
  -mi MINOR, --minor MINOR
                        Minimum local prosperity for a new minor road.
                        Default: 400.
  -by BYPASS, --bypass BYPASS
                        Minimum local traffic for a new bypass segment.
                        Default: 2000.
  -br BRIDGES, --bridges BRIDGES
                        Minimum local prosperity for a new bridge. Default:
                        5000.
```
## Piping into SUMO format
---
We mirror-forked SUMO here allowing the town-sim output to be piped into the SUMO format (.net.xml): https://github.com/julinas/sumo-mirror making some minor changes to SUMO's netgenerate program. Edited files are netgen/NGEdge.* , netgen/NGNet.* , and netgen/NGFrame.* 

The added usage is: --town-sim --town-sim.file=[filename1] --output-file=[filename2] where filename1 should be the location of the file generated by town-sim-py and filename2 is the output location of the resulting .net.xml file.

Ex. netgenerate --town-sim --town-sim.file="output.txt" --output-file="NewSUMOFile.net.xml"

