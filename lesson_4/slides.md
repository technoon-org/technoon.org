---
title: GitNoon Lesson 4
---

### Get Ready for Lesson 4

<div style="font-size: 0.75em;">

1. Login to your account on [github.com](https://github.com/)
2. Make sure you have no uncommitted changes and that you are up to
   date with `origin/main` by checking `git status`
3. If you missed the previous lesson, ask for help with the
   quick-setup on the next slide
   * [technoon-org.github.io/gitnoon/lesson_4/slides.html](https://technoon-org.github.io/gitnoon/lesson_4/slides.html#/quick-setup)

</div>

### Quick Setup

<div style="font-size: 0.45em;">

1. Configuring Git:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global core.editor nano
git config --global init.defaultBranch main
# For Linux or macOS:
git config --global core.autocrlf input
# For Windows:
git config --global core.autocrlf true
# If you're behind a corporate proxy on Windows
git config --global http.sslBackend schannel
```
2. Setting up a `blog` repository:
```bash
mkdir blog
cd blog
git init
echo "# Entry 1" > entry_1.md
git add entry_1.md
git commit -m "Add first blog entry"
git status
```
3. Creating a new public `blog` repository on GitHub, and pushing your local repo to it:
```bash
git remote add origin ssh://git@ssh.github.com:443/<username>/blog.git
git push -u origin main
```
4. Add the `git graph` alias for visualising branches:
```bash
git config --global alias.graph "log --all --graph --oneline --decorate"
```

</div>

### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi


### Lunch Talk: Rewriting History

* Git has features for **rewriting commit history**
* These can be **dangerous** if used incorrectly
* But, they can be **very useful** for:
  * Keeping a tidy, readable commit history
  * Fixing "Git messes"

### Merging vs Rebasing

<div class="mermaid" style="transform: scale(1.5); margin: 2em 0;">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': true} } }%%
gitGraph
  commit id: "A"
  commit id: "B"
  branch feature
  checkout feature
  commit id: "X"
  commit id: "Y"
  checkout main
  commit id: "C"
  commit id: "D"
</pre>
</div>

<div style="font-size: 0.9em;">

**Problem:** `feature` conflicts with `main`, how do I update `feature` so
that it will merge cleanly back into `main`?

</div>


### Merging vs Rebasing

<div style="font-size: 0.75em;">

<div style="display: flex; align-items: center;">

<div style="width: 65%;">

**Option 1:** `git merge main`

<div class="mermaid" style="transform: scale(1);">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': true} } }%%
gitGraph
  commit id: "A"
  commit id: "B"
  branch feature
  checkout feature
  commit id: "X"
  commit id: "Y"
  checkout main
  commit id: "C"
  commit id: "D"
  checkout feature
  merge main
</pre>
</div>

</div>

<div style="width: 35%; font-size: 0.8em;">

* Clutters history with merge commits
* Especially if you update `feature` multiple times

</div>

</div>

<div class="fragment" style="display: flex; align-items: center;">

<div style="width: 65%;">

**Option 2:** `git rebase main`

<div class="mermaid" style="transform: scale(1);">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': true} } }%%
gitGraph
  commit id: "A"
  commit id: "B"
  branch "feature (old)"
  checkout "feature (old)"
  commit id: "X"
  commit id: "Y"
  checkout main
  commit id: "C"
  commit id: "D"
  branch "feature (rebased)"
  checkout "feature (rebased)"
  commit id: "X*"
  commit id: "Y*"
</pre>
</div>

</div>

<div style="width: 35%; font-size: 0.8em;">

* `X` and `Y` are "replayed" on top of `main`
* Keeps a linear history

</div>

</div>

</div>

### Implications of Rebasing

<div class="mermaid" style="transform: scale(1.25); margin: 1em 0;">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': true} } }%%
gitGraph
  commit id: "A"
  commit id: "B"
  branch "feature (old)"
  checkout "feature (old)"
  commit id: "X"
  commit id: "Y"
  checkout main
  commit id: "C"
  commit id: "D"
  branch "feature (rebased)"
  checkout "feature (rebased)"
  commit id: "X*"
  commit id: "Y*"
</pre>
</div>

<div style="font-size: 0.75em;">

* Every commit's identifying SHA is determined by its *content*,
  *message*, *author*, *date*, and **_parent_**
* Changing the parent commit changes the SHA, so Git will see the
  rebased commits as **different commits!**
* If you already pushed `feature`, Git will stop you from overwriting
  the "old commits" unless you use `git push --force`

</div>

### When to Rebase?

::: incremental

<div class="top-fragment-only" style="font-size: 0.8em;">

* **Avoid rebasing if others are using the branch**
  * Otherwise they must rebase or reset to get the new history
  * Personal feature branches are usually safe
* Some teams avoid rewriting history to treat commits like an
  **unchanging audit log**
  * This can come at the cost of a *clean, readable history*
* Rebasing replays commits one-by-one, so conflicts can **require
  multiple resolutions**
  * If in doubt, `git rebase --abort` and merge instead

</div>

:::

### Fixing "Git Messes"

<div style="font-size: 0.9em;">

A bad rebase or merge might leave users feeling confused and like
they've "messed up" their repo

**Here's a general process for sorting out a mess:**

::: incremental

<div class="top-fragment-only" style="font-size: 0.75em;">

1. **Understand the current state of the repo**
   * Use `git log --graph --all --oneline`<br>and `git status`
   * Draw a Git graph on a piece of paper
2. **Determine the desired state**
   * Draw a graph of what you'd like the repo to look like
   * (if it's not your repo, confirm it with the owner)
3. **Draft a series of commands** to get from the current to the
   desired state
4. **Make backups:** copy the repo, make a new branch, etc.
5. **Execute the steps, checking the repo state as you go**

</div>

:::

</div>

### Your Git Tool Belt

<div style="font-size: 0.65em;">

Here's a quick cheat sheet of useful (but potentially dangerous)
commands that can learn more about to help you sort out Git messes:

* `git cherry-pick`: Replay a single commit on top of the current
  branch
* `commit --amend`: Instead of making a new commit, rewrite the last
  one
* `git rebase --interactive`: Rewrite a branch by deleting, editing,
  or re-ordering commits
* `git reset`: Force a branch to point to a different commit
* `git restore`: Update files in the working directory with content
  from a specific commit
* [`git filter-repo`](https://github.com/newren/git-filter-repo):
  Power tool for rewriting history
  * E.g. removing a file from every commit in the history
* `git reflog`: Get a list of commit SHAs `HEAD` has pointed to
  recently
  * In case you accidentally remove important commits from the
    history

</div>

### Further Learning

<div style="font-size: 0.85em;">

* [Git for Ages 4 and Up](https://www.youtube.com/watch?v=1ffBJ4sVUb4)
  * Great visual explanation of Git branching, merging, rebasing, etc.
  * Uses `git checkout`, while we've used the modern `git switch` and `git restore`
* Free e-book: [Pro Git](https://git-scm.com/book/en/v2)
  * To learn more about Git commands for your "tool belt"
* Try a [graphical client](https://git-scm.com/downloads/guis), a text
  editor extension, or a graphical diff tool like
  [meld](https://meldmerge.org/)
* Checkout more TechNoon courses: [technoon.org](https://technoon.org)

</div>


### Tutorial Objectives

1. Make a pull request
2. Rebase a pull request
3. Complete a pull request


### Homework

<div style="font-size: 0.8em;">

1. **Make a pull request to a neighbour's repo**
   1. Visit the repo's GitHub page, and select `Fork`
   2. Clone your fork, make a branch with some changes
   3. Push your local branch up to your fork
   4. [Make a pull request from your fork to your neighbour's repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
   5. Good practice for contributing to open-source projects!
2. **Continue your daily blog entries**
   * Instead of working directly on `main`, make each entry in a new
     branch, and merge them into `main` with pull requests

</div>
