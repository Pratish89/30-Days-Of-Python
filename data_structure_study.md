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

