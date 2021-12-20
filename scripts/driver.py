from pathingSim.simulator import Simulator
import sys

def main():
    print("Test")
    try:
        JSON_file = sys.argv[1]
        print("got config")
    except IndexError:
        raise ValueError("Please provide a valid config file path.")
    print("tried to get config")
    sim = Simulator(JSON_file)
    print("Built sim")

    if sim.run():
        sim.animate()
    else:
        print("Simulation failed to converge.")

if __name__ == "__main__":
    print("Fuck me")
    main()
