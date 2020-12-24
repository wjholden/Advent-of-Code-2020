# Advent of Code 2020

This year: Python!

# Daily Themes and Stars

1. `**` Basic loops and conditions, Cartesian product, quadratic and cubic time algorithms.
2. `**` String parsing, regular expressions, Boolean operations (`xor`), one-indexed arrays
3. `**` 2D arrays (matrices), modulus operator (`%`), functions
4. `**` Parsing, regular expressions, input validation, strings, key/value pairs, dictionaries
5. `**` Binary, sorting and searching, edge cases
6. `**` Set union and intersection, lambda expressions/function pointers for reusability
7. `**` How to invert a binary tree, directed acyclic graphs
8. `**` Assembly languages, pure functions, infinite loops
9. `**` Nested loops, array slices, two-index scanning, greedy algorithms
10. `**` Dynamic programming, overlapping subproblems, combinatorics
11. `* ` Procedural programming, immutability, annoyingly large problems
12. `**` Affine transforms, matrix multiplication
13. `**` Modular arithmetic, Chinese Remainder Theorem, big integers
14. `  `
15. `**` Optimization, 1-indexed arrays, `#theremustbeabetterway`, profiling
16. `  `
17. `**` 4-dimensional geometry, code reuse, generalized solutions vs. performance (`O(1) != O(2)`)
18. `  `
19. `  `
20. `* ` Strings, rotations (**hard** problem)
21. `  `
22. `* ` Procedural programming, lists and iterators
23. `  `
24. `**` Automata, `set` intersection/difference
25. `  `

# Lessons Learned
* Python has no logical `xor` operator.
* You must explicitly cast a string to integer with the `int` function.
* After `filter` you need to convert back to `list` before you can get the length with `len`.
* Regular expression strings start with `r`.
* RE matches does does not return a boolean type unless you wrap it with `bool`, such as `bool(re.match(r"^\d{16}$", "1"))`.
* Python syntax allows line breaks with an open `(`.
* `all` and `any` are built-in functions that perform logical tests over an iterable.
* `str.isdigit` can validate that a string represents a numeric value.
* `str.zfill` is an easy way to zero-pad a string.
* `open` is a built-in function. You do not need to `import os` to use it.
* You should use `with` before `open`. It is syntatically similar to the SQL `WITH` and semantically analagous to Java's try-with-resources.
* `with` can declare multiple items by separating them with commas, such as `with A() as a, B() as b`.
* The `yield` keyword allows for pipelines. This is cool. You can use it to pass values through nested iterators to avoid buffering a large transaction.
* `re` does not expand nested groups. The `regex` has some more features in the `regex.search` function.
* You can name a group in a regular expression with the syntax `(?P<name of group>)`.
* `set.update` serves as an `addAll`/union.
* The unpacking operator (`*`) can spread a list or tuple for functions that require positional arguments.
* Generators and list comprehensions can use `if` as a `WHERE` clause, such as `[i for i in range(10) if i % 3 > 0]`.
* `@lru_cache` cannot has a `set()` object passed as a parameter.
* Python 3.9 adds a `@cache` decorator to automatically memoize a function, similar to `@lru_cache` in `functools`.
* Numpy does not use the `*` operator the same way as Julia. To multiply matrices, you usually want to use the `@` operator.
* Creating matrices with Numpy is a lot more painful than it would be in Julia.
* You can fake a `switch` statement by creating an anoymous `dict` and calling its index. However, this is not free: the interpreter will have to compute all values in this dictionary. If those value computations have side effects then you might have a bad time.
* Apparently Python has very little support for immutable objects. Python lacks the `final` and `freeze` features from Java and JavaScript.
* `cProfile` is awesome. Just wrap any function you want in `cProfile.run(...)` and get an easy table of profiling data.
* `input` is a built-in function that I have been shadowing this whole time. Whoops.
* The syntax `x not in a` is equivalent to `not x in a`.
* Python trivializes a value swap: `x, y = y, x`.
* A `dict` gives you an extremely general solution to `xRy` with many constant time operations, but if `x` is an integer then an array might actually be faster. Sometimes the constants of `O(1)` operations actually matter. (See days 15 and 17).
* Python probably has no [`Nest`](https://stackoverflow.com/questions/65345098/does-python-have-a-nest-function-like-mathematica) equivalent.
* (Hey look, Julia has [`@code_warntype`](https://docs.julialang.org/en/v1/manual/performance-tips/#man-code-warntype)).
* Parsing an expression from left to right means that the base case is on the left.
* List comprehension gives you an easy way to filter keys in a `dict` by value: `[key for (key, value) in my_dict if some_condition(key)]`.
* Python's format strings are inferior to JavaScript.
* Python's official documentation on [docs.python.org](https://docs.python.org) is often not the top search result on Google. This is unlike most other languages, where you easily find websites like [TechNet](https://docs.microsoft.com), [MDN](https://developer.mozilla.org/en-US/), and [JavaDoc](https://docs.oracle.com/javase/8/docs/api/overview-summary.html) very easily.
* You can use the syntax `{1, 2}` to create a `set`.
* Tally the elements of a list with `Counter` in `collections`.