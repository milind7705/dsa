import hashlib
import bisect

class ConsistentHashing:
    def __init__(self, nodes=None, replicas=3):
        """
        Initialize consistent hash ring
        :param nodes: physical nodes
        :param replicas: number of replicas for virtual nodes per physical nodes
        """
        self.replicas = replicas
        self.ring = {} # Mapping: hash -> node
        self.sorted_keys = [] # Sorted list of hashes (positions on the ring)
        self.nodes = set()
        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        # Create hash for a given key(data) using MD5
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        # Add physical node in the hashring along with the virtual node
        self.nodes.add(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#{i}" # Create a unique virtual node
            hash_val = self._hash(vnode_key)
            self.ring[hash_val] = node
            bisect.insort(self.sorted_keys, hash_val)

    def display_ring(self):
        print("HASH RING")
        for hash_val in self.sorted_keys:
            print(f"Hash: {hash_val}, Node: {self.ring[hash_val]}")
        print("-" * 40)

    def get_node(self, key):
        """
        Get the closest node for the given data item(key)
        :param key: key to lookup (userID, file name)
        :return: physical node of the key maps to
        """
        if not self.ring:
            return

        hash_val = self._hash(key)
        # Find the first hash greater than or equal to the key's hash
        index = bisect.bisect(self.sorted_keys, hash_val)
        if index == len(self.sorted_keys):
            return 0 # Wrap around to the first node
        closest_hash = self.sorted_keys[index]
        return self.ring[closest_hash]

    def remove_node(self, node):
        """
        Remove a physical node and its virtual nodes from the hash ring.
        :param node: The name/IP of the physical node
        :return:
        """
        if node not in self.nodes:
            return
        self.nodes.remove(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#{i}"
            hash_val = self._hash(vnode_key)
            if hash_val in self.ring:
                del self.ring[hash_val]
                self.sorted_keys.remove(hash_val)

    def redistribute_keys_after_node_removal(self, node, keys):
        """
        Redistribute keys after removing a physical node.
        :param node:
        :param keys: A dictionary {key: node} mapping keys to their nodes.
        :return:Updated key-to-node mapping.
        """
        print(f"\nRemoving node '{node}' and redistributing its keys...\n")
        self.remove_node(node)

        updated_keys = {}
        for key, current_node in keys.items():
            if current_node == node: # Only remap keys that were on the removed node
                new_node = self.get_node(key)
                updated_keys[key] = new_node
                print(f"Key '{key}' moved from '{node}' to '{new_node}'")
            else:
                updated_keys[key] = current_node  # Keep other keys unchanged

        return updated_keys


if __name__ == "__main__":
    # Initialize consistent hashing with 3 physical nodes and 3 replicas each
    ch = ConsistentHashing(nodes=["server1", "server2", "server3"], replicas=3)
    ch.display_ring()

    keys = ["user123", "item567", "file890", "session456", "user1001"]
    for key in keys:
        print(f"Key {key} maps to node: {ch.get_node(key)}")

    print("Adding another server")
    ch.add_node("server4")
    ch.display_ring()

    for key in keys:
        print(f"Key '{key}' is now mapped to node: {ch.get_node(key)}")

    # Remove a server
    print("\nRemoving 'server2' from the ring...")
    ch.remove_node("server2")
    ch.display_ring()

    for key in keys:
        print(f"Key '{key}' is now mapped to node: {ch.get_node(key)}")


    # Simulate initial key distribution
    keys = ["user123", "item567", "file890", "session456", "user1001"]
    key_to_node = {key: ch.get_node(key) for key in keys}
    print("\nInitial Key Distribution:")
    for key, node in key_to_node.items():
        print(f"Key '{key}' is mapped to node: {node}")

    updated_keys = ch.redistribute_keys_after_node_removal("server4", key_to_node)

    for key, node in updated_keys.items():
        print(f"Key {key} now mapping to {node}")

    # Applications:
    # Distributed Cache (e.g., Redis, Memcached): Keys can be mapped to cache nodes using consistent hashing.
    # Database Sharding: Map keys (e.g., user IDs) to database shards.
    # Load Balancing: Route user requests or API requests to backend servers using consistent hashing.
    # CDN (Content Delivery Network): Distribute content efficiently across CDN servers


    # Distributed Cache
    # Problem Without Consistent Hashing
    # In a distributed caching system like Redis or Memcached, data (key-value pairs) is stored across multiple cache servers.
    # f a naive hashing approach (e.g., hash(key) % N) is used to assign keys to servers,
    # adding or removing a cache server changes the value of N.
    # This results in most of the keys being remapped, which causes:
    # * Cache misses (reloading data from the database).
    # * Increased load on the database and system degradation
    # How Consistent Hashing Solves This
    # Consistent hashing ensures that when a server is added or removed:
    # * Only a small subset of keys are remapped to new servers.
    # * Most of the keys remain on the same servers, preserving cache hits.

    #  Database Sharding
    # Problem Without Consistent Hashing
    # Database sharding divides a database into smaller shards to improve performance and scalability.
    # A naive approach like hash(key) % N ties the hash to the number of shards (N)
    # How Consistent Hashing Solves This
    # With consistent hashing:
    #
    # Shards are placed on a hash ring.
    # Data (keys) is mapped to shards based on the first shard found clockwise on the ring.
    # When a shard is added or removed:
    # Only data belonging to that shard's range is moved.
    # The rest of the data stays on its original shards

    # Distributed Message Queues:
    # Message queues like Kafka or RabbitMQ can use consistent hashing to balance partitions across brokers.
