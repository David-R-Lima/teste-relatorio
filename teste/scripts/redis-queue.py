import asyncio
from bullmq import Worker

async def process(job, job_token):
    # Example implementation for process function
    print(f"Processing job: {job.id}")
    await asyncio.sleep(1)  # Simulate some async work
    return "Job completed"

async def main():
    worker = Worker("myQueue", process, {"connection": "rediss://localhost:6379"})

    try:
        await worker.wait_until_ready()
        await asyncio.Event().wait()  # Keep the script running
    except KeyboardInterrupt:
        print("Shutting down worker...")
    finally:
        await worker.close()

if __name__ == "__main__":
    asyncio.run(main())