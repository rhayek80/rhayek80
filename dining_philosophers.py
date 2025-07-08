import threading
import time
import random

class Philosopher(threading.Thread):
    """A philosopher who alternates between thinking and eating."""
    def __init__(self, index, left_fork, right_fork, butler):
        super().__init__(name=f"Philosopher-{index}")
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.butler = butler

    def run(self):
        while True:
            # Philosopher is thinking
            time.sleep(random.uniform(0.1, 0.5))
            print(f"{self.name} is hungry.")
            # Request permission from the butler to pick up forks
            self.butler.acquire()
            with self.left_fork:
                with self.right_fork:
                    # Philosopher is eating
                    print(f"{self.name} starts eating.")
                    time.sleep(random.uniform(0.1, 0.5))
                    print(f"{self.name} finished eating.")
            # Release the butler so another philosopher may eat
            self.butler.release()


def main():
    """Run the dining philosophers simulation."""
    num_philosophers = 5
    forks = [threading.Lock() for _ in range(num_philosophers)]
    butler = threading.Semaphore(num_philosophers - 1)

    philosophers = []
    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]
        philosopher = Philosopher(i, left_fork, right_fork, butler)
        philosophers.append(philosopher)
        philosopher.start()

    # Let philosophers run for a while
    time.sleep(5)

    # Since threads run forever, we can exit after the sleep period
    print("Simulation finished.")


if __name__ == "__main__":
    main()
