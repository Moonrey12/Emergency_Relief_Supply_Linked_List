# Emergency_Relief_Supply_Linked_List

# Emergency Relief Supply Management System

## Project Description
A command-line Python program that helps relief workers track emergency
supplies (like rice, water, blankets, and medicine) during disasters such
as typhoons, floods, and earthquakes. Supplies can be added as they arrive
and removed as they're distributed.

## Features
- Add a new supply
- Delete a supply after distribution
- Search for a supply by name
- Display all currently available supplies
- Exit the program

## Data Structure Used
A manually implemented **Singly Linked List** — no built-in Python `list`
or `collections.deque` is used to store supply records.

## How the Linked List Works
Each supply is stored in a `Node` containing its name, quantity, and a
reference to the next node. The `LinkedList` class keeps a `head` pointer
to the first node, and all operations (insert, search, delete, display)
walk the chain of `next` references starting from `head`.

## How to Run
```bash
python main.py
```

## Example Usage


## Complexity
| Operation | Time Complexity |
|-----------|------------------|
| Insert    | O(n)             |
| Search    | O(n)             |
| Delete    | O(n)             |
| Traversal | O(n)             |
| Space     | O(n)             |

## Challenges
Handling all deletion cases correctly (first node, middle node, last node,
missing item, empty list) required carefully tracking a `previous` pointer
alongside `current` while traversing.

## Key Learnings
Built a real understanding of how pointer-based data structures work
under the hood — how nodes connect, how `head` anchors the whole
structure, and why operations that seem "free" in a Python list (like
random access) require full traversal in a linked list.