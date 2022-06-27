# 0x06-regular_expressions

Regular expressions – known as regexes – are a specialized syntax
that let you search and replace text using match criteria. When you were using * and ? on the
terminal to match filenames, you can think of them as very simple regexes: * means “match
anything” and ? means “match any one thing.”

There are some downsides to regex. First, they are designed to solve the problem of parsing
text that follows a specific pattern. If you’re trying to parse something extremely complicated
– raw HTML being the usual offender –then regexes are the wrong solution. Second, even
moderately difficult regexes can start to look like line noise rather than something meaningful,
so you really need to learn them in a graded way to avoid being overwhelmed.