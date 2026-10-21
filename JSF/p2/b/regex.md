
### Name Regex

```regex
[a-zA-Z ]+
```

> One or more occurrences of a small letter, capital letter or space.
Use \\s to match any whitespace character. Including \t, \n, \r.

### Email Regex

```regex
[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}
```

| Regex Part | Meaning |
| --- | --- |
| `\w` | A word character: letters, digits, or underscore |
| `.` inside `[ ]` | A literal dot |
| `-` inside `[ ]` | A hyphen |
| `[\w.-]` | One word character, dot, or hyphen |
| `+` | One or more occurrences |
| `@` | A literal `@` symbol |
| `\.` | A literal dot outside a character class |
| `[a-zA-Z]` | Any English letter, uppercase or lowercase |
| `{2,}` | At least two occurrences |

---

### Java String Escaping Note

In Java source code, a double backslash (`\\`) represents one actual backslash passed to the regex engine:

* **Java code:** `\\. `
* **Regex engine receives:** `\.`
* **Regex meaning:** A literal dot (`.`)


---
