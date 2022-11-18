# Checks used in the files

## Valid statements

1. First line in module.
2. Blank line before statement.
3. Constant expression before statement.
4. Lorem ipsum dolor sit amet as long as there is a blank line above the comment.
5. First and last statement with an if/elif/else statement.
6. First and last statement with a for/else statement.
7. First and last statement with a while/else statement.
8. First and last statement within a try/except statement.

## Invalid statements

1. No blank line between 2 statements of a different type.
2. No blank line between 2 statements of the same type.
3. Lorem ipsum dolor sit amet with no blank line above the comment.
4. Constant expression before statement with no blank line above the comment.
5. Multiline assignment before statement.
6. No blank line between 2 statements of a different type within a compound statement.
7. No blank line between 2 statements of the same type within a compound statement.
8. Statement following a non-constant expression.

NOTES:

* Not all checks are applicable for each statement type, e.g. `yield` should theoretically never be the first line of code.
* The code doesn't need to make sense or be executable, as long as it doesn't contain syntax errors.
