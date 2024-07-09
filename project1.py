from pathlib import Path
from simulation import Simulation


def simulation_input(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        simulation = None
        for line in lines:
            input_list = line.split()
            if 'LENGTH' in line:
                length = int(input_list[1])
                simulation = Simulation(length)

            elif 'DEVICE' in line:
                device_id = int(input_list[1])
                simulation.add_sim_device(device_id)

            elif 'PROPAGATE' in line:
                from_device = int(input_list[1])
                to_device = int(input_list[2])
                delay = int(input_list[3])
                simulation.add_propagation_rule(from_device, to_device, delay)

            elif 'ALERT' in line:
                device_id = int(input_list[1])
                description = input_list[2]
                time_raised = int(input_list[3])
                simulation.notifs.append((time_raised, 'ALERT', device_id, description))

            elif 'CANCEL' in line:
                device_id = int(input_list[1])
                description = input_list[2]
                time_raised = int(input_list[3])
                simulation.notifs.append((time_raised, 'CANCEL', device_id, description))

    return simulation


#Cannot create a test for this without using mock because it asks for input
#Also cannot test this because the function is too simple,
#taking no arguments. Tried to test for a Path type, but
#program won't terminate because it wants an input.
def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())


#Cannot create a test for this without using mock because it asks for input
#same issues as _read_input_file_path()
def main() -> None:
    """Runs the simulation program in its entirety"""
    input_file_path = _read_input_file_path()

    try:
        simulation = simulation_input(input_file_path)
        if simulation:
            simulation.simulate()

    except FileNotFoundError:
        print("FILE NOT FOUND")


if __name__ == '__main__':
    main()
