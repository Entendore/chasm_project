# ChASM Core ISA
## Data Movement
- LOAD_MOL [Reg], [Formula]: Loads a molecule into a register.
- MIX [RegA], [RegB]: Combines registers into the main vessel.
- EXTRACT [Product], [Reg]: Isolates a molecule.

## Environment Control
- HEAT [Temp] / COOL [Temp]: Modifies vessel temperature.
- SET_PH [Value]: Adjusts acidity.
- STIR [RPM]: Agitates vessel.

## Control Flow
- WAIT [Time]: Pauses execution.
- CMP_EQUIL [Threshold]: Checks reaction equilibrium.
- JNE [Label]: Jump if Not Equilibrium.
- HALT: Ends program.
