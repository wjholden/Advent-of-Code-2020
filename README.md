# Advent of Code 2020

This year: Python!

# Daily Themes and Stars

1. `**` Basic loops and conditions, Cartesian product, quadratic and cubic time algorithms.
2. `**` String parsing, regular expressions, Boolean operations (`xor`), one-indexed arrays
3. `**` 2D arrays (matrices), modulus operator (`%`), functions
4. `**` Parsing, regular expressions, input validation, strings, key/value pairs, dictionaries
5. `**` Binary, sorting and searching, edge cases
6. `  `
7. `  `
8. `  `
9. `  `
10. `  `
11. `  `
12. `  `
13. `  `
14. `  `
15. `  `
16. `  `
17. `  `
18. `  `
19. `  `
20. `  `
21. `  `
22. `  `
23. `  `
24. `  `
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