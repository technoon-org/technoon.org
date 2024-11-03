---
title: GitNoon Lesson 4
---

In this tutorial, you will learn how to:

1. Make a pull request
2. Rebase a pull request
3. Perform an interactive rebase


## Making sure our `main` branch is clean

```
git switch main
```

```
git fetch
git reset --hard origin/main
```


## Setting up a branch for a pull request

```
git branch contributing-guide
git switch contributing-guide
```

```
nano CONTRIBUTING.md
```

```
* Pull requests are welcome!
```

Save and exit `nano` (`Ctrl + x`, `y`, `Enter`), then add and commit
`CONTRIBUTING.md`:

```
git status
git add CONTRIBUTING.md
git status
# We'll use a shortcut to write the message inline
git commit -m "Add contributing guide"
git status
```

```
git graph
```


## Making a pull request

* Many teams will use a **pull request** (also know as a **merge
  request**) to manage the merging of a feature branch back into the
  `main` branch.
* We'll do that ourselves now.

First, let's push the `contributing-guide` branch to the `origin`
remote:

```
git push -u origin contributing-guide
```

* `-u` is only needed the first time you push a particular branch


Now open your repo's page on GitHub, you'll see various shortcuts to
create a pull request, but let's do it the standard way:

1. Open the `Pull requests` tab
2. Select `New pull request`
3. Make sure the **base** branch is `main`
4. Choose `contributing-guide` for the **compare** branch
   * You'll see a summary showing the commit to be merged in from
     `contributing-guide`, along with a diff of the changes
5. Select `Create pull request`
6. You can fill in some details for the pull request:
   * Change the title and description if more context is needed
   * If you were in a team, you could add a reviewer
7. Finally, click `Create pull request`

* Because there are no merge conflicts, GitHub will say the branch is
  ready to merge.
* Normally, this would be the point for someone else to review and
  merge your pull request.


## Creating a merge conflict with your pull request

Now what happens if someone updates `main` and causes a merge conflict
between your pull request branch and `main`?

```
git switch main
```

```
nano CONTRIBUTING.md
```

```
* Please rebase conflicting pull requests
```

Save and exit `nano` (`Ctrl + x`, `y`, `Enter`), then add and commit
`CONTRIBUTING.md`:

```
git status
git add CONTRIBUTING.md
git status
# We'll use a shortcut to write the message inline
git commit -m "Remind contributors to rebase"
git status
```

```
git push origin main
```

```
git graph
```


## Rebasing the pull request

```
git switch
```

```
git fetch
```

```
git rebase origin/main
```

CONFLICT RESOLUTION

```
git graph
```

```
git push origin contributing-guide
```


## Completing the pull request

* Select `Merge pull request` and then `Confirm merge`

Now let's fetch the results of that merge from the `origin` remote to
our local repo:

```
git fetch
git graph
```

* We can see `origin/main` contains a new merge commit
* Even though a fast-forward merge was possible, a pull request will
  always create a merge commit by default
  * This keeps a log of significant merges into `main`

You'll now need to switch back to your main branch and "fast-forward"
merge it to the latest state of `origin/main` - just like we did last
week:

```
git switch main
git merge --ff-only origin/main
```

* Note why we use the "fast-forward only" option:
  * If there were local commits that weren't in the remote branch,
    then we'd want to stop and think about what to do next
  * We may want to merge, or as we'll see next week, we may want to
    rebase

Finally, now that our branch is merged, we should tidy-up by deleting
our feature branch on the remote and locally:

```
# Delete the remote branch
git push -d origin readme-additions
# Delete the local branch
git branch -d readme-additions
```


## Performing an interactive rebase

Example: Accidentally committed a password, need to edit the commit
