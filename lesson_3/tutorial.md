---
title: GitNoon Lesson 3
---

In this lesson, you will learn how to:

1. Work on a separate branch
2. Merge your branch into `main`
3. Resolve a merge conflict
4. Make and merge a pull request




```
git branch my-feature
```

```
git commit
```

```
git switch my-feature
```

```
git commit
```

```
git switch main
```

```
git merge my-feature
```

Then do it again, but this time with a conflict.


## TODO

**Add an alias to conveniently view a graphical history with `git graph`:**

```
git config --global alias.graph "log --graph --oneline --all"
```

* git log a..b
* git log a...b
