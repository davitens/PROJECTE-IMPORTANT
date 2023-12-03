from pyboy import PyBoy, WindowEvent
from accions import Accions
import random
import multiprocessing

n=0

def generate_random(exclude_number):
    result = random.randint(1, 9)  # Generate a random number between 1 and 9
    while result == exclude_number:
        result = random.randint(1, 9)  # Regenerate if the result matches the excluded number
    return result

def run_code():
    pyboy = PyBoy('pokered.gb')
    global n
    pyboy.set_emulation_speed(4)
    comandaments = Accions(pyboy)
    constant = 1
    while constant == 1:
        n = generate_random(n)
        if n == 1 or n == 7:
            comandaments.boto_A()
        if n == 3 or n == 9:
            comandaments.boto_B()
        #if n == 0 or n == 5:
        #    comandaments.boto_START()
        if n == 2:
            comandaments.boto_DOWN()
        if n == 6:
            comandaments.boto_RIGHT()
        if n == 8:
            comandaments.boto_UP()
        if n == 4:
            comandaments.boto_LEFT()
        pyboy.tick()
    
    pyboy.stop()

if __name__ == '__main__':
    # Create multiple processes to run the function in parallel
    processes = []
    for _ in range(8):  # Adjust the number of processes as needed
        process = multiprocessing.Process(target=run_code)
        process.start()
        processes.append(process)

    # Ensure all processes have completed
    for process in processes:
        process.join()
