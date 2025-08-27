# 🐍 Python Coding Practice Problems 🚀

Welcome to my journey of solving **3000 Python problems**!  
Currently: **200+ problems solved** 🎉 and counting daily.  

This repo is organized to help anyone learning Python, preparing for coding interviews, or practicing problem-solving skills.

![Progress](https://img.shields.io/badge/Problems_Solved-200%2B-brightgreen)
![Goal](https://img.shields.io/badge/Goal-3000-blue)
![Python](https://img.shields.io/badge/Made%20with-Python-yellow)
![GitHub last commit](https://img.shields.io/github/last-commit/Dev0psKing/Python-Code-Challenges)
![GitHub repo size](https://img.shields.io/github/repo-size/Dev0psKing/Python-Code-Challenges)

---

## 📑 Table of Contents
- [📂 Structure](#-structure)
- [📌 Progress Tracker](#-progress-tracker)
- [🎯 Goal](#-goal)
- [🔥 Features](#-features)
- [📊 Goals Updates](#-goals-updates)
- [💻 Sample Problem](#-sample-problem)
- [🤝 Contributing](#-contributing)
- [⭐ Support](#-support)

---

## 📂 Structure
- **Simple** → Basic syntax, logic, loops, functions, OOP  
- **Topic-specific** → Strings, Lists, Control Flow, etc.  

Each folder contains:
- `Questions.md` → problem list  
- `Solutions.md` → Python solutions with explanations  

---

## 📌 Progress Tracker  

Here’s my current progress (click links to view):  

- ✅ [Simple Part → 100+ done](https://github.com/Dev0psKing/Python-Code-Challenges/tree/master/01_Simple%20Part%20(100%2B%20Questions))  
- ✅ [Control Flow → 20+ done](https://github.com/Dev0psKing/Python-Code-Challenges/tree/master/Control%20Flow%20Questions)  
- ✅ [Lists → 20+ done](https://github.com/Dev0psKing/Python-Code-Challenges/tree/master/Lists%20Questions)  

---

## 🎯 Goal
To build a **public learning resource** for programmers to practice Python and prepare for:  
- 💡 Coding interviews  
- 📘 Problem-solving skill building  
- 🏆 Competitive programming  

---

## 🔥 Features
- 200+ Python problems (growing daily)  
- Well-structured by topics  
- Detailed explanations for each solution  
- Beginner → Advanced difficulty  

---

## 📊 Goals Updates  

<div align="center">
  <!-- Progress bar -->
  <img alt="Progress bar" src="https://progress-bar.dev/200/?scale=3000&title=Problems%20Solved&width=500&color=2ea44f" />
  <br/>
  <a href="https://github.com/Dev0psKing/Python-Code-Challenges">
    <img alt="Progress badge" src="https://img.shields.io/badge/Progress-6.67%25-2ea44f" />
  </a>
</div>

---

## 💻 Sample Problem  

Here’s a taste of what you’ll find inside 👇

**Problem:** Reverse a string in Python.  

```python
# Solution: Reverse a string
def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("Python"))  # Output: nohtyP
```

**Problem:** Find all prime numbers up to n using the Sieve of Eratosthenes.

```python
def sieve_of_eratosthenes(n: int) -> list[int]:
    """Return a list of prime numbers up to n."""
    if n < 2:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False

    return [i for i, prime in enumerate(primes) if prime]

# Example usage
print(sieve_of_eratosthenes(50))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```