import sys
import os

# Ensure we can import the package even if not installed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from uuidify import UuidifyClient, UuidifyError

def main():
    client = UuidifyClient()
    
    print("--- UUIDify Python Client Demo ---")
    
    try:
        # 1. UUIDv4
        print("\nGenerating UUIDv4...")
        uuid_val = client.uuid_v4()
        print(f"Result: {uuid_val}")
        
        # 2. UUIDv7 (Batch)
        print("\nGenerating 3 UUIDv7s...")
        uuids = client.uuid_v7(count=3)
        for i, uid in enumerate(uuids):
            print(f"  {i+1}: {uid}")
            
        # 3. ULID
        print("\nGenerating ULID...")
        ulid_val = client.ulid()
        print(f"Result: {ulid_val}")
        
    except UuidifyError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
