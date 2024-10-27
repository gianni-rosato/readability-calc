# Methodology

In order to get a baseline "Privacy Understanding" value, we will divide grade level by 16 and cap our value at 7. This will give us a value between 0 and 7, with 7 being the most literate value we'll consider for privacy understanding.

So, a third grader would have a privacy understanding of 3 / 16 = 0.1875, while a college graduate would have a privacy understanding of 16 / 16 = 10.0 clamped to 7.0.

## Filename Formatting

The formatting is as follows:

```
[policyname]-[age]-[grade]-[privacyunderstanding]_[modelspeed].txt
```

LLM outputs are scrubbed of emojis and stylistic formatting (HTML, Markdown).
