# AlertSimulation

Kathleen Pham

This Python program simulates a distributed system where devices communicate alerts and cancellations among each other. The simulation is driven by an input file containing instructions that define device behaviors, alert propagation rules, and simulation duration.

Program Execution-
The program reads input from the Python shell specifying the path to an input file. If the file doesn't exist, it prints "FILE NOT FOUND" and terminates. Otherwise, it processes the input file to simulate the described scenarios.

Input File Structure-
The input file consists of several types of lines:

LENGTH: Specifies the duration of the simulation in milliseconds.
DEVICE: Defines a device by its unique ID.
PROPAGATE: Establishes rules for propagating alerts or cancellations between devices.
ALERT: Indicates when and from which device an alert is raised.
CANCEL: Indicates when and from which device an alert is cancelled.
Blank lines and comments (lines starting with #) are ignored for readability.
Output Format
During the simulation, the program outputs events such as:

Device receiving an alert.
Device sending or propagating an alert.
Device receiving a cancellation.
Device sending or propagating a cancellation.
Simulation end.

Each event is timestamped and formatted as specified in the output section of the input description.

