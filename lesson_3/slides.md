---
title: GitNoon Lesson 3
---

### Get Ready for Lesson 3

* Clone this repo: TODO


### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi

### Lunch Talk: Collaboration Strategies

* Git is a very **flexible** tool - there are many ways you can
  collaborate with Git
* How your team uses Git will be a **trade-off** between
  **simplicity** and **requirements**
* We're going to look at some of the key workflows and concepts

### Workflow 1: Single Branch

The simplest option; what we've been using so far:

<div class="mermaid" style="transform: scale(1.5);">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': false} } }%%
gitGraph
  commit
  commit
  commit tag: "v1.0.0"
  commit tag: "v1.0.1"
  commit
  commit
  commit
  commit tag: "v1.1.0"
</pre>
</div>

You can add *annotated* tags to mark specific commits as released versions:

```bash
git tag -a v1.0.0 -m "Release of version 1.0.0"
# Push tags to the remote
git push origin --tags
# Any command that accepts a commit SHA will accept a tag:
git diff v1.0.0
```

### Collaboration on a Single Branch

<style>
.single-branch-diagram .mermaid {
    transform: scale(1.4);
}
</style>
<div class="r-stack" style="margin: 2em 0; height: 100px;">
<div class="fragment fade-out single-branch-diagram" data-fragment-index="0">

<div class="mermaid">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': false, 'mainBranchName': 'origin/main'} } }%%
gitGraph
  commit
  commit
  commit
  branch main
  checkout main
  commit
  commit
</pre>
</div>

</div>
<div class="fragment fade-in-then-out single-branch-diagram" data-fragment-index="0">

<div class="mermaid">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': false, 'mainBranchName': 'origin/main'} } }%%
gitGraph
  commit
  commit
  commit
  branch main
  checkout main
  commit
  commit
  checkout origin/main
  commit
  commit
</pre>
</div>

</div>
<div class="fragment fade-in single-branch-diagram" data-fragment-index="1">

<div class="mermaid">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': false, 'mainBranchName': 'origin/main'} } }%%
gitGraph
  commit
  commit
  commit
  branch main
  checkout main
  commit
  commit
  checkout origin/main
  commit
  commit
  checkout main
  merge origin/main
</pre>
</div>

</div>
</div>

<div class="r-stack">

<div class="fragment fade-out" data-fragment-index="0">

* Clone the remote repo (`origin/main`)
* Make commits on your local `main` branch

</div>

<div class="fragment fade-in-then-out" data-fragment-index="0">

* But what if someone pushes to the remote branch before you?
* Git won't let you push your state of the branch, because the latest
  commits on the remote would be lost

</div>

<div class="fragment fade-in-then-out" data-fragment-index="1">

* First, fetch the latest commits: `git fetch`
* Then merge `origin/main` into your local `main`: `git merge origin/main`
* If both branches changed the same part of the same file, there will be a
  **merge conflict**
  * We'll learn how to resolve these in the tutorial

</div>

<div class="fragment fade-in" data-fragment-index="2">

* Finally, push the merged branch to the remote: `git push origin main`
* This flow might work for a couple of contributors, but it can get
  messy with bigger teams

</div>

</div>

### Workflow 2: Feature Branches

<div class="mermaid" style="transform: scale(1);">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': false} } }%%
gitGraph
  commit tag: "v1.0.0"
  branch 1234-add-birthday-notifications
  branch 5678-fix-mobile-layout
  checkout 1234-add-birthday-notifications
  commit
  commit
  commit
  checkout 5678-fix-mobile-layout
  commit
  checkout main
  merge 5678-fix-mobile-layout tag: "v1.0.1"
  checkout 1234-add-birthday-notifications
  commit
  commit
  checkout main
  merge 1234-add-birthday-notifications tag: "v1.1.0"
</pre>
</div>

* A new **feature branch** is made for every task
* Makes it easy for contributors to **work in parallel**
  * (or for one person to **switch between tasks**)
* Formalised in [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)

### A Typical Pull/Merge Request

::: incremental

<div style="font-size: 0.9em;">

1. Make a feature branch of the latest `main`
2. Make commits to your feature branch
3. Push your feature branch to the remote
   * If you don't have permission, you'll need to push to your own
     [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)
     of the repo
4. Respond to reviewer feedback and suggestions by pushing more commits
5. Once the reviewer is happy, they will merge your branch into `main`
   * If your branch conflicts with `main`, you will need to *rebase*
     your branch (we'll cover that next lesson)

</div>

:::

### Workflow 3: Feature & Release Branches

### Advanced Workflows

* GitLab Flow
* Git Flow
* Octo-merges

### Other considerations

* Database Migrations
* Branches to track environments
* Set up branch protection
* Create review checklists
* Set up CI pipelines to automatically check pull requests
* Document your team's process


### Tutorial Objectives


### Homework
