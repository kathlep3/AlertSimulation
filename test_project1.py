import unittest
from simulation import Simulation
from project1 import simulation_input


class TestDevice(unittest.TestCase):
    def test_length_simulation_input(self):
        input = "/Users/kathleenpham/PycharmProjects/Project1/samples/sample_input.txt"
        with open(input, 'r') as file:
            simulation = simulation_input(input)
        self.assertIsInstance(simulation, Simulation)
        self.assertEqual(simulation.length, 9999)


class TestSimulation(unittest.TestCase):
    def test_alert_cancel_simulation(self):
        input = "/Users/kathleenpham/PycharmProjects/Project1/samples/sample_input.txt"
        with open(input, 'r') as file:
            simulation = simulation_input(input)
        expected = [(0, 'ALERT', 1, 'Trouble'), (2200, 'CANCEL', 1, 'Trouble')]
        self.assertIsInstance(simulation, Simulation)
        self.assertEqual(simulation.notifs, expected)

    def test_sent_alert_output(self):
        simulation = Simulation(10)
        simulation.sent_alert_output(0, 1, 2, "Trouble")
        expected = "@0: #1 SENT ALERT TO #2: Trouble"
        self.assertIn(expected, simulation.outputs)

    def test_received_alert_output(self):
        simulation = Simulation(10)
        simulation.received_alert_output(1, 2, 1, "Trouble")
        expected = "@1: #1 RECEIVED ALERT FROM #2: Trouble"
        self.assertIn(expected, simulation.outputs)

    def test_sent_cancel_output(self):
        simulation = Simulation(10)
        simulation.sent_cancel_output(2, 1, 2, "Trouble")
        expected = "@2: #1 SENT CANCELLATION TO #2: Trouble"
        self.assertIn(expected, simulation.outputs)

    def test_received_cancel_output(self):
        simulation = Simulation(10)
        simulation.received_cancel_output(3, 2, 1, "Trouble")
        expected = "@3: #1 RECEIVED CANCELLATION FROM #2: Trouble"
        self.assertIn(expected, simulation.outputs)

    def test_run_alert(self):
        self.simulation = Simulation(10)
        self.simulation.add_sim_device(1)
        self.simulation.add_sim_device(2)
        self.simulation.add_propagation_rule(1, 2, 1)
        self.simulation.notifs.append((0, 'ALERT', 1, "Trouble"))
        self.simulation.run_alert(1, 0, "Trouble")
        self.assertIn((1, 'ALERT', 2, "Trouble"), self.simulation.notifs)

    def test_run_cancel(self):
        self.simulation = Simulation(10)
        self.simulation.add_sim_device(1)
        self.simulation.add_sim_device(2)
        self.simulation.add_propagation_rule(1, 2, 1)
        self.simulation.notifs.append((0, 'CANCEL', 1, "Cancel Trouble"))
        self.simulation.run_cancel(1, 0, "Cancel Trouble")
        self.assertIn((1, 'CANCEL', 2, "Cancel Trouble"), self.simulation.notifs)

    def test_simulate(self):
        self.simulation = Simulation(10)
        self.simulation.add_sim_device(1)
        self.simulation.add_sim_device(2)
        self.simulation.add_propagation_rule(1, 2, 1)
        self.simulation.notifs.append((0, 'ALERT', 1, "Trouble"))
        self.simulation.notifs.append((1, 'CANCEL', 2, "Cancel Trouble"))
        self.simulation.simulate()
        expected_outputs = [
            "@0: #1 SENT ALERT TO #2: Trouble",
            "@1: #2 RECEIVED ALERT FROM #1: Trouble"]
        self.assertEqual(self.simulation.outputs, expected_outputs)


if __name__ == "__main__":
    unittest.main()