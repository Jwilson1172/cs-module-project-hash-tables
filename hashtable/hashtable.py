import operator


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next = None
        return

    def has_next(self) -> bool:
        """returns true if there is another element in the chain

        Returns:
            bool: [description]
        """
        if self.next == None:
            return False
        else:
            return True

    def add(self, node) -> None:
        """adds a Node to the Hashtable collion chain

        Args:
            node (HashTableEntry): the item to add to the head of the chain

        Returns:
            None
        """
        self.next = node
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity
        self.occupied = 0
        return

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.data)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        if self.occupied != 0:
            return self.capacity / self.occupied
        else:
            # logically if there are no elements then the load is %0
            return 0

# [hashing algos]

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # the FNV-1 hash from
        # https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#FNV-1_hash

        # factors used to calculate FNV-1 Hash
        FNV_offset = 0xcbf29ce484222325
        FNV_prime = 0x100000001b3
        # init a var to hold the hashed value for the key
        hash_hex = None
        # wrap in a try/catch to handle brokenness
        try:
            h = FNV_offset
            h = h * FNV_prime
            for b in self.data[key]:
                hash_hex = operator.xor(h, b)
            return hash_hex & 0xffffffff
        except Exception as e:
            breakpoint()
            print(e)
            return None

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        try:
            hash = 5381
            for byte in key:
                hash = ((hash << 5) + hash) + ord(byte)
            return hash & 0xFFFFFFFF
        except Exception as e:
            print(e)
            breakpoint()
            return None


# [end hashing]

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
            A function that takes the key and stores the value at the hashed
            index for that key
        """
        # going to need the hash of the key
        k = self.fnv1(key)

        # if there is already an entire then tack on another entry on the chain
        # otherwise start a new chain
        if self.data[k] is not None:
            # add the kv pair to the head of the root node in the linked list
            self.data[k].next = HashTableEntry(key, value)
        else:
            # create a new linked list at the index in the hashtable, this will
            # cache collisions
            self.data[k] = HashTableEntry(key, value)
        self.occupied += 1
        return self.data[k]

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        k = self.fnv1(key)

        # use the list function to remove the entry at the key hash
        self.data.remove(self.data[k])
        self.occupied -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        return self.data[self.fnv1(key)]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # not %100 what this is going to look like so let me wireframe it
        # reinit that object with a new size
        # take all of the data entries and recompute the key's hash
        # iterate through the data list's and copy them to the new
        # object using new hashed indexes
        canvas = HashTable(new_capacity)
        assert self.capacity > canvas.capacity

        # iterate through the hashtable and for each entry see if there is a
        # linked list if there is not then put the hashtable entry into the
        # new table this process is going to be O(n + k) runtime because:
        #           n
        #   [0]     |
        #   [0]     V
        #   [0,1,2] --> k
        for i in self.data:
            # rt + O(n) of the list object backbone
            if i.next == None:
                canvas.put(i.key, i.value)
            else:
                # if there is another object then we want to transverse the
                # linked list and transfer the items to the new hashtable
                # rt + O(n) of the length of the linked list
                k = i
                while k.next is not None:
                    canvas.put(k.key, k.value)
                    k = k.next
        return canvas

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
