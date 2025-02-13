Approach 1: Sequential Scan (Brute Force)

✅ Simple to implement.
❌ Inefficient for large files (~1TB) as it scans everything.
Approach 2: Binary Search on Sorted Logs

✅ Efficient log retrieval for time-based searches.
✅ Reduces read operations significantly.
❌ Assumes logs are sorted.
Approach 3: Indexing with a Log Database (e.g., Elasticsearch)

✅ Fast queries using indexing.
❌ Requires additional storage & setup.
2. Final Solution Summary
Explain why you chose the final approach over others.

Example:
We chose binary search + streaming read because:

It efficiently locates the starting position for retrieval.
It avoids loading the entire file into memory.
It works well for large log files (~1TB).

3. Steps to Run the Solution
Provide step-by-step instructions on how to execute the program.


The filtered logs will be displayed in the terminal.
