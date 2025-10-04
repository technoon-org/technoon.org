---
title: GitNoon Lesson 3
---

### Get Ready for Lesson 3!

<div style="font-size: 0.85em;">

1. Make sure your blog has no uncommitted changes and that you are up
   to date with `origin/main` by checking the output of `git status`
2. If you missed the previous lesson, ask for help with the
   quick-setup on the next slide
   * [technoon-org.github.io/gitnoon/lesson_3/slides.html](https://technoon-org.github.io/gitnoon/lesson_3/slides.html#/quick-setup)

</div>

### Quick Setup

<div style="font-size: 0.55em;">

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

</div>

### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi

### Lunch Talk: Collaboration Workflows

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

You may like to add *annotated* tags to mark specific commits as
released versions:

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

<div style="font-size: 0.85em;">

1. Make a feature branch off the latest `main`
2. Make commits to your feature branch
3. Push your feature branch to the remote
   * If you don't have permission, you'll need to push to your own
     [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)
     of the repo
4. Open a *Pull Request* / *Merge Request*
5. Respond to reviewer feedback and suggestions by pushing more commits
6. Once the reviewer is happy, they will merge your branch into `main`
   * If your branch conflicts with `main`, you will need to *rebase*
     your branch (we'll cover that next lesson)

</div>

:::

### Workflow 3: Release Branches

<div class="mermaid" style="transform: scale(1); margin: 1em 0;">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': false} } }%%
gitGraph
  commit tag: "v1.0.0"
  branch 1234-add-birthday-notifications
  branch v1.0
  checkout 1234-add-birthday-notifications
  commit
  commit
  commit
  checkout v1.0
  commit
  commit tag: "v1.0.1"
  checkout main
  merge v1.0
  checkout 1234-add-birthday-notifications
  checkout main
  merge 1234-add-birthday-notifications tag: "v1.1.0"
</pre>
</div>

<div style="font-size: 0.9em;">

* Useful if you need to support `v1.0` while working on new features for `v1.1`
* A *hotfix* on release branch `v1.0` is tagged as *point release*
  `v1.0.1` and merged forward into `main`.

</div>

### Environment Branches

<div style="font-size: 0.95em;">

Instead of release tags, you might use branches to track which commit
is deployed in each environment:

<div class="mermaid" style="transform: scale(1.5); margin-top: 1.8em;">
<pre>
%%{init: { 'gitGraph': {'showCommitLabel': true, 'mainBranchName': 'origin/main'} } }%%
gitGraph
  commit id: " "
  commit id: "  "
  commit id: "prod"
  commit id: "   "
  commit id: "    "
  commit id: "test"
  commit id: "     "
  commit id: "dev"
  commit id: "      "
</pre>
</div>

(continuous deployments could even be triggered by updates to those
branches)

</div>


### Other Workflows

::: incremental

<div class="top-fragment-only" style="font-size: 0.74em;">

* [**GitLab Flow**](https://about.gitlab.com/blog/2020/03/05/what-is-gitlab-flow/)
  * Extends the Feature Branches workflow (i.e. GitHub Flow) with
    environment branches and process recommendations
* [**Git Flow**](https://nvie.com/posts/a-successful-git-branching-model/)
  * Extends the Release Branches workflow with more branch types
  * Increases complexity, but allows for more process control
* **Octopus Merges**
  * Instead of merging into `main` one-by-one, many feature branches
    are "octopus merged" to create a release on-demand
  * Allows you to delay deciding which features to include in a
    release, but risks octopus conflicts!

</div>

:::

### Other considerations

::: incremental

<div class="top-fragment-only" style="font-size: 0.7em;">

* **Versioning non-files**
  * Database schemas → database migrations
  * Datasets → [dvc](https://dvc.org/), [dagster](https://docs.dagster.io/getting-started/what-why-dagster)
* **Conventions**
  * Branch naming, commit messages
  * Versioning, e.g. date-based versions, [Semantic Versioning](https://semver.org/)
* **What belongs in the same repo?**
  * Usually: different team or project = different repo
  * Some organisations use [monorepos](https://monorepo.tools/)
  * Keep docs close to code so they change together
* **Processes**
  * Configure branch protection rules
  * Pull request code review checklists
  * Automate checks (e.g. linting, tests) for Continous Integration (CI)
  * Automate deployments for Continous Deployment (CD)

</div>

:::

### Choosing your Workflow

Adapt your workflow to fit **how your team works** and **the
requirements of your project**

<div class="fragment" style="font-size: 0.85em;">

> **Document your workflow and reasons** for decisions so that
> everyone understands how the team uses Git!

</div>


### Tutorial Objectives

1. Work on a separate branch
2. Merge your branch into `main`
3. Resolve a merge conflict


### Homework

<div style="font-size: 0.8em;">

1. **Continue your daily blog entries**
   * Instead of working directly on `main`, make each entry in a new
     branch that you then merge into `main`

</div>
