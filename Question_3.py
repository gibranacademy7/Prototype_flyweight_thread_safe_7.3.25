"""
QUESTION 3a:
What is the meaning of the term "safe thread"?

Answer:
A "safe thread" (or "thread-safe") refers to a piece of code, function,
or program that can be safely executed in a multi-threaded environment without causing unintended behavior,
such as race conditions or data corruption.

In other words, thread safety ensures that multiple threads can access shared resources
without leading to inconsistencies or unexpected errors.
This is typically achieved using synchronization mechanisms such as:

Locks (Mutexes, Semaphores) – Prevent multiple threads from modifying shared data simultaneously.
Atomic operations – Ensure that certain operations are performed indivisibly.
Thread-local storage – Keeps separate copies of variables for each thread.
Immutable objects – Data structures that do not change, preventing race conditions.


*** Thread-Safe Example Using threading.Lock:

import threading

# Shared resource
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Ensures only one thread modifies 'counter' at a time
            counter += 1

# Creating two threads that modify the same variable
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final counter value:", counter)  # Expected: 200000


Explanation:
Two threads (t1 and t2) increment a shared counter variable.
Without a lock, both threads might read the same value before updating it,
leading to incorrect results due to race conditions.
With lock, only one thread at a time can modify counter, ensuring the correct final result.
==================================================================================================
"""

"""
QUESTION 3b:
"Are the add and remove functions here thread-safe?"
----------------------------------------------------
The code intended in the question:

import threading
import time
import random

# Shared list - NOT thread safe
shared_list = []

def add_items(thread_id, count):
    """Add items to the shared list"""
    for i in range(count):
        # Get current length
        current_length = len(shared_list)
        # Simulate some processing time to increase chances of race condition
        time.sleep(0.001)
        # Append a new item
        shared_list.append(f"Thread {thread_id} - Item {i}")
        # Print progress occasionally
        if i % 10 == 0:
            print(f"Thread {thread_id} added item {i}")

def remove_items(thread_id, count):
    """Remove items from the shared list"""
    for i in range(count):
        if shared_list:  # Check if list is not empty
            # Simulate some processing time
            time.sleep(0.002)
            try:
                # Try to remove the last item
                item = shared_list.pop()
                # Print progress occasionally
                if i % 10 == 0:
                    print(f"Thread {thread_id} removed item: {item}")
            except IndexError:
                # This can happen if the list becomes empty between the check and pop
                print(f"Thread {thread_id} - List was empty!")

# Create and start threads
threads = []

# Add two threads that add items
for i in range(2):
    t = threading.Thread(target=add_items, args=(i, 50))
    threads.append(t)
    t.start()

# Add two threads that remove items
for i in range(2):
    t = threading.Thread(target=remove_items, args=(i+2, 40))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Final list length: {len(shared_list)}")
print(f"Expected length: {2*50 - 2*40} = 20")
------------------------------------------------------------------
Answer:
No, the add_items and remove_items functions are not thread-safe. Both functions modify the shared list 
(shared_list) without synchronization mechanisms like locks, 
meaning that multiple threads could be accessing and modifying the list concurrently, 
leading to a race condition. For example, one thread might check the length of the list and append an item, 
while another thread might pop an item at the same time, leading to unpredictable behavior and possible errors. 
To make them thread-safe, you would need to use synchronization techniques like threading.
Lock or other concurrency mechanisms to ensure only one thread can modify the shared list at a time.
==============================================================================================================
"""

"""
QUESTION 3c:
"Are the add and remove functions here thread-safe?"
----------------------------------------------------
The code intended in the question:

import threading
import time
import random
from multiprocessing import Manager, freeze_support

# Main function that contains all the code
def main():
    # Create a Manager
    manager = Manager()
    # Create a thread-safe shared list
    shared_list = manager.list()

    def add_items(thread_id, count):
        """Add items to the shared list"""
        for i in range(count):
            # Append a new item (this operation is atomic/thread-safe)
            shared_list.append(f"Thread {thread_id} - Item {i}")
            # Simulate some processing time
            time.sleep(0.001)
            # Print progress occasionally
            if i % 10 == 0:
                print(f"Thread {thread_id} added item {i}")

    def remove_items(thread_id, count):
        """Remove items from the shared list"""
        for i in range(count):
            # We still need to handle potential emptiness
            if len(shared_list) > 0:  # This check is now thread-safe
                try:
                    # Pop is now thread-safe
                    item = shared_list.pop()
                    # Simulate some processing time
                    time.sleep(0.002)
                    # Print progress occasionally
                    if i % 10 == 0:
                        print(f"Thread {thread_id} removed item: {item}")
                except IndexError:
                    # This should be much less likely now
                    print(f"Thread {thread_id} - List was empty!")

    # Create and start threads
    threads = []

    # Add two threads that add items
    for i in range(2):
        t = threading.Thread(target=add_items, args=(i, 50))
        threads.append(t)
        t.start()

    # Add two threads that remove items
    for i in range(2):
        t = threading.Thread(target=remove_items, args=(i+2, 40))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print(f"Final list length: {len(shared_list)}")
    print(f"Expected length: {2*50 - 2*40} = 20")

if __name__ == "__main__":
    # This line is critical for Windows multiprocessing
    freeze_support()
    main()
---------------------------------------------------------

Answer:
Yes, the functions add_items and remove_items in your code are thread-safe. 
The reason is that you are using a Manager from the multiprocessing module, 
which provides a thread-safe shared list (shared_list). 
Operations like append and pop on this list are atomic and safe across multiple threads.

The Manager ensures that only one thread can access the shared list at a time when modifying it. 
However, there is still some potential risk when doing complex operations, 
like checking the list's length and modifying it in one step. In the case of remove_items, 
you are correctly checking if the list has items before trying to pop, 
which is a good practice to avoid errors like IndexError.

"""

