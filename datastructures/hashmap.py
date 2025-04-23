import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib
#from sympy import nextprime

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets = Array(starting_sequence = \
        [LinkedList(data_type=tuple) for _ in range(number_of_buckets)], \
        data_type = LinkedList)
        self._count = 0
        self._load_factor_threshold = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_number(self, key: KT) -> int:
        return self._hash_function(key) % len(self._buckets)

    def _get_next_size(self) -> int:
        #return nextprime(len(self._buckets), 1) # codegrade doesn't like using sympy
        # rudimentary next prime finding function:
        size = len(self._buckets) * 2 + 1
        found = False
        while True:
            size += 2 # starts on odd, only need to check odds
            divisors = 0
            for i in range(2, size):
                if size % i == 0:
                    divisors += 1
                    break
            if divisors == 0:
                return size
    
    def _rehash_and_resize(self, new_size) -> None:
        new_array = Array(starting_sequence = \
        [LinkedList(data_type=tuple) for _ in range(new_size)], \
        data_type = LinkedList)
        for bucket in self._buckets:
            for (k, v) in bucket:
                bucketnumber = self._hash_function(k) % new_size
                new_array[bucketnumber].append((k, v))
        self._buckets = new_array

    def __getitem__(self, key: KT) -> VT:
        bucketnumber = self._get_bucket_number(key)
        for (k, v) in self._buckets[bucketnumber]:
            if k == key:
                return v
        raise KeyError("No such key can be found in this plane of existence.")

    def __setitem__(self, key: KT, value: VT) -> None:        
        bucketnumber = self._get_bucket_number(key)
        for pair in self._buckets[bucketnumber]:
            if pair[0] == key:
                self._buckets[bucketnumber].remove(pair)
                self._count -= 1
                break
        self._buckets[bucketnumber].append((key, value))
        self._count += 1
        if self._count > len(self._buckets) * self._load_factor_threshold:
            self._rehash_and_resize(self._get_next_size())

    def keys(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield k
    
    def values(self) -> Iterator[VT]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield v

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield (k, v)
            
    def __delitem__(self, key: KT) -> None:
        bucketnumber = self._get_bucket_number(key)
        for pair in self._buckets[bucketnumber]:
            if pair[0] == key:
                self._buckets[bucketnumber].remove(pair)
                self._count -= 1
                return None
        raise KeyError("No such key can be found in this plane of existence.")

    
    def __contains__(self, key: KT) -> bool:
        bucketnumber = self._get_bucket_number(key)
        for (k, v) in self._buckets[bucketnumber]:
            if k == key:
                return True
        return False
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        return self.keys()
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        if len(other) != len(self):
            return False
        for item in self.items():
            if item not in other.items():
                return False
        return True

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)