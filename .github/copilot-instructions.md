
# Copilot Instructions

These rules tell GitHub Copilot how to behave in this repository.

## 🧠 Python Style Rule (Custom)

1. **Rule: Avoid List Comprehensions**  
   In this repository, developers **should NOT use list comprehensions**.  
   Always use regular `for` loops instead for better readability.

2. **Violation Handling**  
   Copilot should avoid generating code that uses list comprehensions.  
   If it detects or suggests one, replace it with a traditional `for` loop.

3. **Example Replacement**

   ❌ Bad:
   ```python
   squares = [x * x for x in numbers]
   ```

## PR review: flag list comprehensions

When reviewing PRs, detect Python list comprehensions, suggest a `for`-loop replacement with a short example or patch, and mark it as a non-blocking suggestion.
