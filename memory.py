"""
Project: Kenya Fleet Memory Sentinel
Description: Demonstrates Python's object model, reference cycles, 
             generational GC monitoring, and weakref optimization 
             for high-throughput Matatu Sacco background workers.
"""

import gc
import sys
import tracemalloc
import weakref
import time

# --- 1. THE FLAWED MODEL (CREATES REFERENCE CYCLES) ---
class LeakyTripSession:
    def __init__(self, vehicle_plate: str, driver_name: str):
        self.vehicle_plate = vehicle_plate
        self.driver_name = driver_name
        self.dispatcher = None  # Will hold a strong reference back to the dispatcher

    def __del__(self):
        print(f"[CLEANED] Trip session for {self.vehicle_plate} dropped from RAM.")

class LeakyDispatcher:
    def __init__(self, route_code: str):
        self.route_code = route_code
        self.active_sessions = []

    def register_session(self, session: LeakyTripSession):
        self.active_sessions.append(session)
        # Creating the circular reference: Dispatcher -> Session -> Dispatcher
        session.dispatcher = self

    def clear_sessions(self):
        self.active_sessions.clear()


# --- 2. THE OPTIMIZED MODEL (USING WEAKREF) ---
class SafeTripSession:
    def __init__(self, vehicle_plate: str, driver_name: str):
        self.vehicle_plate = vehicle_plate
        self.driver_name = driver_name
        self._dispatcher = None # Will hold a weak reference

    @property
    def dispatcher(self):
        return self._dispatcher() if self._dispatcher else None

    @dispatcher.setter
    def dispatcher(self, disp):
        # Prevent strong reference cycle
        self._dispatcher = weakref.ref(disp)

    def __del__(self):
        print(f"[OPTIMIZED CLEAN] Safe session for {self.vehicle_plate} wiped cleanly!")

class SafeDispatcher:
    def __init__(self, route_code: str):
        self.route_code = route_code
        self.active_sessions = []

    def register_session(self, session: SafeTripSession):
        self.active_sessions.append(session)
        session.dispatcher = self

    def clear_sessions(self):
        self.active_sessions.clear()


def run_memory_audit():
    print("=== STARTING KENYA FLEET MEMORY AUDIT ===")
    
    # Start tracking memory allocations
    tracemalloc.start()

    print("\n[Phase 1] Simulating Leaky Sessions (Circular Reference Trap)...")
    dispatcher = LeakyDispatcher("Route 23 (Town - Kahawa West)")
    
    # Simulate high volume trip initialization
    for i in range(5000):
        session = LeakyTripSession(f"KBC {100+i}A", f"Driver_{i}")
        dispatcher.register_session(session)

    # Clear dispatcher records
    dispatcher.clear_sessions()
    del dispatcher # We deleted the dispatcher, but sessions still point to it via cycles!

    # Force garbage collection scan
    uncollected = gc.collect()
    print(f"Leaky Mode: Garbage collector found {uncollected} trapped objects due to cycles.")
    
    snapshot1 = tracemalloc.take_snapshot()

    print("\n[Phase 2] Simulating Optimized Sessions (WeakRef Protected)...")
    safe_dispatcher = SafeDispatcher("Route 23 (Town - Kahawa West)")
    
    for i in range(5000):
        safe_session = SafeTripSession(f"KDG {500+i}B", f"SafeDriver_{i}")
        safe_dispatcher.register_session(safe_session)

    # Clear safe dispatcher records
    safe_dispatcher.clear_sessions()
    del safe_dispatcher # Everything unbinds cleanly because of weakref!

    collected_safe = gc.collect()
    print(f"Optimized Mode: Cleaned up {collected_safe} objects immediately.")

    # Stop tracking
    tracemalloc.stop()
    print("\n=== AUDIT COMPLETE: READY FOR GITHUB ===")

if __name__ == "__main__":
    run_memory_audit()