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
14. `**` Binary, bitwise operations, wide integers (>32 bits), computer architecture
15. `**` Optimization, 1-indexed arrays, `#theremustbeabetterway`, profiling
16. `  `
17. `**` 4-dimensional geometry, code reuse, generalized solutions vs. performance (`O(1) != O(2)`)
18. `* ` Grammars, parsers, operator precedence
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
* A way to format a fixed-width binary string: `format(value, '#036b')`.
* Python automatically supports big integers. See [PEP237](https://www.python.org/dev/peps/pep-0237/).
* You cannot customize Python's operator precedence.
* Ignore values in loops or tuple unpacking with `_`. Examples: `a, _, c = (1, 2, 3)` and `for _ in range(10)`.

# Thoughts on Python

Python is pretty nice.
I can see the appeal.
The syntax is expressive, compact, and easy to read.
Some people dislike the use of tabs, but this was never a problem for me.
I liked the separation of bitwise operators (`&`, `|`, `^`, `~`) from logical operators (`and`, `or`, `not`).
I also like the `in` operator.
Python does not have labeled statements, so you cannot specify which nested loop to `break` or `continue` from.

Python arrays use the same square brackets as C with many rich features, such as negative indices.
I believe subarrays are views into the original array, not copies.
Arrays are zero-indexed (first element is position 0).

Most programmers will reach for arrays-of-arrays to represent matrices in row-major.
This will be familiar to Java and JavaScript programmers.
This feels strange to those used to matrix operations in scientific languages, such as R and Julia. 

To my knowledge, Python has no pointers and no support for low-level memory tricks that you might see in C and C++.

I don't think Python has a vanilla solution for vectorized operations.
This was something I liked in R and Julia.
Python was designed as a general-purpose programming language and not for scientific computing.
I think [Numpy](https://numpy.org) can vectorize a function, but I only used Numpy for one problem this year.

I **really** wish Python used Emacs-style keyboard shortcuts in its REPL.
IDLE makes things even worse by moving the cursor with the up and down keys instead of scrolling through previous commands entered.
No other terminal interface that I know of does this.
I read that the reason for this behavior is that the developers consider it more beginner-friendly.
This is a bad reason in my opinion and makes Python feel like a language with training wheels.
The REPL is missing tab completion and context-sensitive help.

List comprehension is really good.
`filter`, `map`, and `reduce` are not quite as compact as they would be in Java and JavaScript.
Worse, these operations would not compose left-to-right.

Generator expressions are really interesting.
This concept of a eager/lazy (possibly asynchronous) generator queuing a result that can be retrieved by another function is compelling.
I think now appreciate why Java has an [`Iterator`](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html) interface.
You could do all kinds of expensive queries eagerly in the `Iterator` for immediate consumption when needed.
I have never noticed a `yield` keyword in any other language.

Performance was generally not a problem for me in Advent of Code.
It probably helps to have a general awareness of data structures to use.

Python's support for immutability is pretty poor.
I love setting `final` and `const` wherever possible in Java and JavaScript.
I also like to seal an object with `freeze` or equivalent when debugging, as this helps enforce assumptions.
There is also no support to annotate pure functions.

I never reached for an object-oriented solution to a problem this year, so I have no opinion of Python's support for OOP.
Many of my solutions use tuples as an anonymous record type.
Python's support for tuples is superior.
Tests for equality "just work".
Tuple unpacking is expressive and pleasant to use.

`@cache` trivializes memoization of pure functions.

In general, string operations are quite intuitive in Python.
It is a joy to use the same square-bracket syntax as arrays for substrings.
Python's format strings are not quite as friendly as those in JavaScript.
Python partly makes up for this with `bin` and `hex`.
`bin` and `hex` are very convenient and ought to be included in every language.

Python's official documentation is adequate but not quite as easy to navigate as JavaDoc, MDN, and TechNet.
It was annoying that [docs.python.org](https://docs.python.org) is usually *not* the top Google search result for Python-related queries
(examples: [Python array](https://www.google.com/search?q=python%20array),
[Python bitwise](https://www.google.com/search?q=python%20bitwise),
[Python string](https://www.google.com/search?q=python%20string),
[Python repl](https://www.google.com/search?q=python%20repl),
[Python reserved keywords](https://www.google.com/search?q=python%20reserved%20keywords))
It is probably a little more usable than Mathematica's documentation.
Python has a built-in `help` command, but I did not find it anywhere near as useful as Julia's built-in `?` help.

Overall, Python's rich features, clear syntax, and flexibility make it a pleasant and easy high-level language.
