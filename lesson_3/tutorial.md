---
title: GitNoon Lesson 3
---

In this tutorial, you will learn how to:

1. Work on a separate branch
2. Merge your branch into `main`
3. Resolve a merge conflict


## Viewing a repo as a graph

Before we get started, we're going to create a git *alias* to
conveniently run `git log` with options that will display a succinct
graphical view of all branches in our repo:

```
git config --global alias.graph "log --all --graph --oneline --decorate"
```

Open your terminal to your `blog` repo (`cd blog`), and try running
it:

```
git graph
```

### Understanding the graph

* You should see a commit on each line
* You should see labels for your `main` branch and the `origin/main`
  remote branch.
  * **The key idea** to understand branches in Git is that **a branch
    is effectively a pointer to a specific commit**.
* You should also see a `HEAD` label pointing to your `main` branch.
  * `HEAD` indicates the branch that our repo has *checked-out*, which
    has two key implications:
    1. `HEAD` represents the current version of the files in our
       directory - any file changes will be compared to `HEAD`
    2. When you run `git commit`, the new commit will have the current
       `HEAD` commit as its *parent*, and the `HEAD` branch will be
       updated to point to the new commit
       * You can already see these parent/child links between commits
         by the chain/history of commits in the log.
  * Think of `HEAD` like the head on a spinning hard disk - it points
    to the data that is currently being read or written.
* You may also see `origin/HEAD`, which just indicates the *default
  branch* for new clones of the `origin` remote.


## Working on a separate branch

We can keep our work isolated from the `main` branch while it is still
a work-in-progress by committing to a separate branch.

To do so, let's create a new branch for some additions to the README:

```
git branch readme-additions
```

We can see our newly created branch in the graph; it points to the
same commit as whatever branch `HEAD` was pointing to:

```
git graph
```

Now let's *check-out* our new branch:

```
git switch readme-additions
```

We can confirm our current branch by again checking the graph and also
by checking `git status`:

```
git graph
git status
```

Now let's make some changes on our new branch, open up the README:

```
nano README.md
```

And add more information at **the bottom of the file**:

```
## Built with

* Markdown
```

Save and exit `nano` (`Ctrl + x`, `y`, `Enter`), then add and commit
the README:

```
git status
git add README.md
git status
# We'll use a shortcut to write the message inline
git commit -m "Add tool info to README"
git status
```

Now let's see what that's done to the graph:

```
git graph
```

Success! The new commit has been added to the `readme-additions`
branch, but not `main`.

Now let's switch back to the `main` branch, again confirming the
change to `HEAD` in the graph and status:

```
git switch main
git graph
git status
```

When we look at the log from `main`, we don't see that commit:

```
git log
```

And when we look at the README, we don't see our latest additions:

```
cat README.md
```


## Merge your branch into `main`

Now that we've finished the work on our *feature branch* let's merge
it back into `main`.

This is as simple as running:

```
git merge readme-additions
```

* **TIP: To remember which branch will be updated by a merge, always
  remember that almost all git commands will only change the branch
  you are checked-out on.**
  * In this case, we are checked-out on `main`, so we will be updating
    the `main` by *merging in* `readme-additions`

Now let's see what that's done to the graph:

```
git graph
```

We can see that `main` has been updated to the same commit as
`readme-additions`, and the README on `main` now has the additions:

```
cat README.md
```


## Fast-forward merges

Notice that Git told us this was a **fast-forward** merge:

* A fast-forward merge is only possible when the current branch has no
  commits that aren't already in the branch we are merging in
  * i.e. Our current branch is linearly/directly behind the branch
    being merged in.
* A fast-forward merge just updates the current branch to point to the
  same commit as the named branch.
* We also saw a fast-forward merge in the last lesson when updating
  our local `main` branch with the latest commits fetched from
  `origin/main`.


## Non-fast-forward merges

Let's see what happens when a fast-forward merge is not possible.

First off, let's undo that previous merge by *resetting* the `main`
branch to point to the same commit as `origin/main` again:

```
git reset --hard origin/main
git graph
```

**IMPORANT:** `git reset` is a dangerous command because it can delete
both commits and uncommitted changes. We'll learn more about how to
use it responsibly in the next lesson.

Now let's add a commit directly to the `main` branch, as if someone
else had merged in some changes while we were still working on
`readme-additions`:

```
nano README.md
```

Change the README's title to something else:

```
# My Awesome Blog
```

Save and exit `nano` (`Ctrl + x`, `y`, `Enter`), then add and commit
the README:

```
git status
git add README.md
git status
# We'll use a shortcut to write the message inline
git commit -m "Update README title"
git status
```

Now let's look at the graph:

```
git graph
```

* The branches have diverged!
* There is now a commit in `main` that doesn't exist in `readme-additions`
* This means that `main` cannot be fast-forwarded to `readme-additions`
* Aside: `git log` can be used to check which commits exist in one
  branch but not another with the "two dots" syntax:

```
# Commits in readme-additions but not main
git log main..readme-additions
# Commits in main but not readme-additions
git log readme-additions..main
```

Now what happens when we merge :

```
git merge readme-additions
```

* Git opens a text editor for us to edit a commit message for a
  *merge commit*
  * Just save and exit to confirm the message (`Ctrl + x`, `y`, `Enter`)

Now check the graph:

```
git graph
```

* Git has added a *merge commit* that combines the commits from both
  branches.
* The `main` branch has been updated to point to the new merge commit.

So what does the README look like now on the `main` branch?

```
cat README.md
```

Because each branch had made changes to different parts of the same
file, Git was able to combine both sets of changes into a single file
without us having to do anything!


## Resolve a merge conflict

But what if both branches had changed the same part of the same file?

Let's find out!

Again, let's undo the previous merge and the commit we made on `main`
by *resetting* the `main` branch to point to the same commit as
`origin/main` again:

```
git reset --hard origin/main
git graph
```

Now let's make a commit directly on `main` again, but this time
editing the same part of the file as our commit on `readme-additions`:

```
nano README.md
```

Add some different content to **the bottom of the file**:

```
## Thanks

* Git
```

Save and exit `nano` (`Ctrl + x`, `y`, `Enter`), then add and commit
the README:

```
git status
git add README.md
git status
# We'll use a shortcut to write the message inline
git commit -m "Add thanks to README"
git status
```

Look at the graph, and you should see the branches diverging again:

```
git graph
```

Now let's see what happens when we try to merge `readme-additions`
into `main`:

```
git merge readme-additions
```

* Aha! Git tells us that there is a merge conflict in the README
* A merge conflict is not a cause for panic!
* Let's see more about the conflict by checking the status:

```
git status
```

* We can see `README.md` is an *unmerged path* where both branches
  made modifications
* Let's see what's going on in the README:

```
git diff README.md
```

* We see two alternative hunks at the bottom of the file
  * One from our current branch (i.e. `HEAD`, which is `main`)
  * One from the branch we are merging in (i.e. `readme-additions`)
* We need to manually edit the file to have the correct content that
  resolves this conflict
  * **This should often involve a conversation with whomever wrote the
    other code**
  * **Don't just blindly choose to keep one or the other**
  * **If you don't want to resolve it now**, you could run `git merge --abort`
* (press `q` to exit `git diff`)

```
nano README.md
```

To resolve this conflict, let's remove the conflict markers and
combine the two changes into one:

```
## Thanks

* Git
* Markdown
```

* Save and exit `nano` (`Ctrl + x`, `y`, `Enter`)
* Check `git status`:

```
git status
```

The README is still unmerged, let's check `git diff` again:

```
git diff README.md
```

* The two columns of pluses and minuses can see the results of our
  manual conflict resolution:
  * The changes from `readme-additions` will effectively lose `Built
    with` but gain `Thanks` and `Git`
  * The changes from `main` will effectively gain `Markdown`

We can now add our resolution:

```
git add README.md
git status
```

The resolution is now staged and ready to be committed, so let's
complete the merge with a merge commit:

```
git commit
```

* Git opens a text editor for us to edit a commit message for a
  *merge commit*
  * Just save and exit to confirm the message (`Ctrl + x`, `y`, `Enter`)
* The merge is now complete!
* Let's check what that's done to the repo:

```
git status
git graph
```

* We see a merge commit just like we did for the previous merge
* This was a relatively straightforward conflict
* Sometimes Git is able to automatically merge changes that may still
  be incompatible with each other
  * For example, maybe one branch renamed a variable, while the other
    branch added a new reference to the old variable name.
  * So you should validate and test after any merge!

To wrap-up, let's undo the last merge and commit on `master` by
resetting again:

```
git reset --hard origin/main
git graph
```


## Conclusion

* You've learned a lot about branching and merging in this lesson,
  including four different kinds of merging:
  * Fast-forward merges
  * Non-fast-forward merges with merge commits
  * Merges with conflicts
* In the next lesson, you'll learn some more powerful (and potentially
  dangerous!) tools for manipulating commits and branches.
  * In particular, we'll learn how to rebase a feature branch that is
    conflicting with `main` in order to avoid unnecessary merge
    commits.
