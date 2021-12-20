from pathingSim.simulator import Simulator
import sys

def main():
    try:
        JSON_file = sys.argv[1]
    except IndexError:
        raise ValueError("Please provide a valid config file path.")
    sim = Simulator(JSON_file)

    if sim.run():
        sim.animate()
    else:
        print("Simulation failed to converge.")

if __name__ == "__main__":
    print("Fuck me")
    main()
