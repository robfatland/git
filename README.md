# git

This POC project intends to try out the `manim` engine for building educational content.
Our first notion is a modular video documenting `git` in relation to `github`.

> Note: Rob's [nexus manim entry](https://github.com/robfatland/nexus/blob/gh-pages/manim/index.md)
> has manim community / resource links.

Rob's original thesis is "I get 98% of my safe backup value by knowing the 5-command recipe: 
`get clone / pull / add / commit / push`. Once I have these memorized and I've created a
couple GitHub repos: I'm back to the topic of interest and I never need to think about
`git` ever again, hurray."

...but there are directions to expand and further enhance one's workflow, broadly:

- What else can `git` do?
    - branches, pull requests, `stash`, `stash pop`, reconciling content, ...
- What else can `GitHub` do?
    - actions, pages, `hugo`, associated data volumes > 100MB, ...
- How about programmatic access to `GitHub`?
    - ...see below...
 

Python has a `requests` library available; so the following example code uses that
to start tapping into the `GitHub` API.


```
import requests
response = requests.get("https://api.github.com")

print('\nThe basic response:')
print(response)
print('\nstatus code:')
print(response.status_code)
print('\nsome of the response text:')
print(response.text[:300])
response_dictionary = response.json()
print('\nA response dictionary entry:')
print(response_dictionary['gists_url'])
```


