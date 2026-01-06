---
author: glenzac
categories:
  - "open-source"
  - "tinkering"
date: "2021-06-21T16:21:30+00:00"

tags:
  - eda
  - opensource
  - tools
  - vlsi

title: List of Open Source VLSI EDA tools
---
## SPICE Simulators

1. [Ngspice](http://ngspice.sourceforge.net/) \- Does not have schematic view. Input is command line / netlist based.
1. [XSchem](https://sourceforge.net/projects/xschem/) \- SPICE schematic capture and simulation software. It can also generate HDL netlist from the schematic.
1. [Xyce](https://xyce.sandia.gov/) \- SPICE-compatible, high-performance analog circuit simulator
1. [eSim](https://esim.fossee.in/home) \- EDA tool for circuit design, simulation, analysis and PCB design
1. [IRSIM](http://opencircuitdesign.com/irsim/index.html) \- Switch level simulator for digital circuits
1. [Cppsim](https://cppsim.com/) \- CppSim automatically generates, compiles, and runs C++ code corresponding to the schematic design that you create

## HDL Simulation/Synthesis

1. [Verilator](https://www.veripool.org/verilator/) \- Compiles Verilog or System Verilog into C++ for faster simulations
1. [Icarus Verilog](http://iverilog.icarus.com/) \- Verilog simulation and synthesis tool
1. Veriwell Verilog simulator - Verilog simulator - supports only IEEE1364-1995 standard
1. [Yosys](http://www.clifford.at/yosys/) \- HDL synthesis tool chain
1. [Qflow](http://opencircuitdesign.com/qflow/index.html) \- HDL synthesis tool chain

## Logic Simulation

1. [Logisim](http://www.cburch.com/logisim/) \- Digital Logic designer and circuit simulator
1. [Digital](https://github.com/hneemann/Digital) \- Digital Logic designer and circuit simulator and much more advanced features than logisim
1. [Logic Circuit](https://www.logiccircuit.org/) \- Logic circuit simulator with an intiutive lab like GUI

## Layout Tools

1. [Klayout](https://klayout.de/) \- GDS and OASIS Layout viewing and editing
1. [Magic](http://opencircuitdesign.com/magic/) \- Layout viewing and editing tool
1. [Electric](https://www.staticfreesoft.com/index.html) \- Comprehensive tool for integrated-circuit layout, DRC, simulation, routing
1. [Qrouter](http://opencircuitdesign.com/qrouter/index.html) \- Layout Routing tool that can be used with the Qflow tool
1. [Toped](http://www.toped.org.uk/) \- IC layout editor supporting GDS, OASIS and CIF formats
1. [Fairly Good Router](http://vlsicad.eecs.umich.edu/BK/FGR/) \- software for global routing, based on Lagrange Multipliers - an approach similar to what industry routers use

## STA Tools

1. [OpenTimer](https://github.com/OpenTimer/OpenTimer) \- A High-Performance Timing Analysis Tool for VLSI Systems
1. [HiTas](https://www-soc.lip6.fr/equipe-cian/logiciels/tasyagle/) \- STA tool with the ability to perform analysis at the transistor-level, cell-level or a mixture of the two.

## LVS tool

1. [Netgen](http://opencircuitdesign.com/netgen/index.html) \- LVS

## Standard Cell Placement

1. [Dragon](http://vlsicad.eecs.umich.edu/BK/Slots/cache/er.cs.ucla.edu/Dragon/) \- standard-cell placement tool for both variable-die and fixed-die ASIC design

## Miscellaneous

1. [GTK Wave](https://sourceforge.net/projects/gtkwave/) \- GTK+ based wave viewer
1. Alliance/Coriolis VLSI CAD Tools - a complete toolchain for vlsi design. It provides a vhdl compiler and simulator, logic synthetiser, automatic place & route and portable cmos library.
1. [ChipVault](http://chipvault.sourceforge.net/) \- a VHDL and Verilog Chip Design Organization tool
