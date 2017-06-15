class HashMap(object):
  def __init__(self):
    self.hash_map = [[] for i in range(256)]
  
  def insert(self, key, value):
    hash_key = hash(key) % len(self.hash_map)
    bucket = self.hash_map[hash_key]
    key_exists = False
    
    for i, key_value in enumerate(bucket):
      k, value = key_value
      if key == k:
        key_exists = True
        break
    
    if key_exists:
      # Replace value
      bucket[i] = ((key, value))
    else:
      # Add to bucket
      bucket.append((key, value))
      
  def get(self, key):
    hash_key = hash(key) % len(self.hash_map)
    bucket = self.hash_map[hash_key]
    key_exists = False
    
    for i, kv in enumerate(bucket):
      k, value = kv
      if key == k:
        key_exists = True
        break
    
    if key_exists:
      return bucket[i][1]
    else:
      return "Not found"
      
  def print_hash_map(self):
    print(self.hash_map)
      
dct = HashMap()
dct.insert('fruit', 'apple')
dct.insert('electronics', 'iPad')
import pdb; pdb.set_trace()
dct.insert('fruit', 'jackfruit')
dct.insert('electronics', 'iPhone')
print(dct.print_hash_map())
