import time
from app.enrollment import Course

def run_load_test():
    print("Starting CampusConnect Load Test...")
    # Set a massive capacity so the course doesn't fill up during the test
    course = Course(capacity=50000)
    latencies = []
    total_requests = 10000

    # 1. Start the Load Test
    start_test_time = time.time()
    
    for i in range(total_requests):
        req_start = time.time()
        course.enroll_student(f"student_{i}")
        req_end = time.time()
        
        # Calculate latency for this specific request in milliseconds
        latencies.append((req_end - req_start) * 1000)

    end_test_time = time.time()

    # 2. Calculate Metrics
    total_time_seconds = end_test_time - start_test_time
    throughput_rps = total_requests / total_time_seconds
    
    # Calculate p95 latency (sort the list and find the 95th percentile value)
    latencies.sort()
    p95_index = int(len(latencies) * 0.95)
    p95_latency = latencies[p95_index]

    # 3. Print Results
    print("\n--- PERFORMANCE TEST RESULTS ---")
    print(f"Total Requests Processed: {total_requests}")
    print(f"Total Execution Time: {total_time_seconds:.4f} seconds")
    print(f"Throughput: {throughput_rps:.2f} Requests Per Second (RPS)")
    print(f"p95 Latency: {p95_latency:.6f} ms")

if __name__ == "__main__":
    run_load_test()