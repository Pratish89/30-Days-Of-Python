# Data Structure Study Guide (Python)

This guide is a quick study companion for Python's core built-in data structures.

## 1) List

**What it is:** Ordered, mutable collection. Allows duplicates.

```python
numbers = [10, 20, 30]
numbers.append(40)       # [10, 20, 30, 40]
numbers[1] = 25          # [10, 25, 30, 40]
```

**Use list when:**
- Order matters
- You need to update/add/remove items frequently

**Common operations:**
- `append(x)`, `extend(iterable)`, `insert(i, x)`
- `remove(x)`, `pop()`, `pop(i)`, `clear()`
- slicing: `items[start:stop:step]`

**Operation examples:**
```python
fruits = ["apple", "banana"]
fruits.append("mango")               # ['apple', 'banana', 'mango']
fruits.extend(["orange", "kiwi"])   # ['apple', 'banana', 'mango', 'orange', 'kiwi']
fruits.insert(1, "grape")            # ['apple', 'grape', 'banana', 'mango', 'orange', 'kiwi']

fruits.remove("banana")              # removes first matching value
last_item = fruits.pop()              # pops 'kiwi'
first_two = fruits[:2]                # slicing -> ['apple', 'grape']
```

---

## 2) Tuple

**What it is:** Ordered, immutable collection. Allows duplicates.

```python
point = (3, 5)
x, y = point             # unpacking
```

**Use tuple when:**
- Data should not change
- You want a fixed record-like structure

**Common operations:**
- Indexing/slicing: `t[0]`, `t[1:]`
- `count(x)`, `index(x)`

**Operation examples:**
```python
colors = ("red", "blue", "red", "green")
first = colors[0]                     # 'red'
tail = colors[1:]                     # ('blue', 'red', 'green')

red_count = colors.count("red")      # 2
blue_index = colors.index("blue")    # 1
```

---

## 3) Set

**What it is:** Unordered collection of unique items.

```python
ids = {1, 2, 2, 3}       # becomes {1, 2, 3}
ids.add(4)
```

**Use set when:**
- You need uniqueness
- Fast membership checks are important

**Common operations:**
- `add(x)`, `remove(x)`, `discard(x)`
- `union(|)`, `intersection(&)`, `difference(-)`, `symmetric_difference(^)`

**Operation examples:**
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.add(7)                              # {1, 2, 3, 4, 7}
a.discard(2)                          # {1, 3, 4, 7}

all_items = a | b                     # union -> {1, 3, 4, 5, 6, 7}
common = a & b                        # intersection -> {3, 4}
only_a = a - b                        # difference -> {1, 7}
sym_diff = a ^ b                      # symmetric difference -> {1, 5, 6, 7}
```

---

## 4) Dictionary

**What it is:** Key-value mapping. Keys are unique.

```python
student = {"name": "Sara", "score": 95}
student["grade"] = "A"
score = student.get("score")
```

**Use dictionary when:**
- You need to map keys to values
- Fast lookup by key is needed

**Common operations:**
- `get(key, default)`, `keys()`, `values()`, `items()`
- `update({...})`, `pop(key)`, `del dict[key]`

**Operation examples:**
```python
student = {"name": "Sara", "score": 95}

student["grade"] = "A"               # add a key
student.update({"score": 98})         # update existing key

name = student.get("name")            # 'Sara'
country = student.get("country", "N/A")

pairs = list(student.items())          # [('name', 'Sara'), ('score', 98), ('grade', 'A')]
removed = student.pop("grade")        # removes 'grade', returns 'A'
```

---

## Quick Comparison

| Structure   | Ordered | Mutable | Duplicates | Typical Use |
|-------------|---------|---------|------------|-------------|
| List        | Yes     | Yes     | Yes        | Sequences you modify |
| Tuple       | Yes     | No      | Yes        | Fixed records |
| Set         | No      | Yes     | No         | Uniqueness + membership checks |
| Dictionary  | Yes*    | Yes     | Keys: No   | Key-value lookup |

\*Dictionary preserves insertion order in modern Python (3.7+ language guarantee).

---

## Study Checklist

- [ ] Can I explain when to use list vs tuple?
- [ ] Can I remove duplicates from a list using a set?
- [ ] Can I merge two dictionaries?
- [ ] Can I iterate over dictionary keys and values?
- [ ] Can I perform union/intersection on sets?

---

## Practice Questions

1. Convert `['a', 'b', 'a', 'c']` into a unique collection.
2. Store a 2D point and unpack it into `x` and `y`.
3. Count word frequency in a sentence using a dictionary.
4. Find common items between two lists using sets.
5. Build a list of squares from 1 to 10.
