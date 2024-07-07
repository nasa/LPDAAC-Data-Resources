# Contributing to this Repository

> Please submit a pull request early in the development phase, outlining the changes you intend to make or features you intend to add. This allows us to offer feedback early on, ensuring your contribution can be added to the repository before you invest a significant amount of time.

We want your help! Even if you're not a coder! There are several ways you can contribute to this repository:

- Report an [Issue](https://github.com/nasa/VITALS/issues) or make a recommendation
- Update code, documentation, notebooks, or other files (even fixing typos)
- Propose a new notebook

In the sections below we outline how to approach each of these types of contributions. If you're new to GitHub, you can [sign up here](https://github.com/). There are a bunch of great resources on the [GitHub Quickstart page](https://docs.github.com/en/get-started/quickstart). The [GitHub Cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet/) is also quite helpful, even for experienced users. Please reach out to [lpdaac@usgs.gov](lpdaac@usgs.gov) with questions or concerns.  

## Report an Issue or Make a Recommendation

If you've found a problem with the repository, we want to know about it! Please submit an [Issue](https://github.com/nasa/VITALS/issues). Before submitting, we would appreciate if you check to see if a similar issue already exists. If not, create a new issue, providing as much detail as possible. Things like screenshots and code excerpts demonstrating the problem are very helpful!

## Updating Code, Documentation, Notebooks, or Other Files

To contribute a solution to an issue or make a change to files within the repository we've created a typical outline of how to do that below. If you want to make a simple change, like correcting a typo within a markdown document or other documentation, there's a great video explaining how to do that without leaving the GitHub website [here](https://www.youtube.com/watch?v=PHoScPeMWHI). To make a more complex change to a notebook, code, or other file follow the instructions below.  

1. Please create an [Issue](https://github.com/nasa/LPDAAC-Data-Resources) or comment on an existing issue describing the changes you intend to make.  
2. Create a [fork](https://docs.github.com/en/get-started/quickstart/contributing-to-projects#about-forking) of this repository. This will create your own copy of the repository. When working from your fork, you can do whatever you want, you won't mess up anyone else's work so you're safe to try things out. Worst case scenario you can delete your fork and recreate it.  
3. Clone your fork to your local computer or cloud workspace using your preferred command line interface after navigating to the directory you want to place the repository in:

    ```
    git clone your-fork-repository-url
    ```

    - Change directories to the one you cloned

    ```
    cd repository-name
    ```

    - Add the upstream repository, this is the original repository that you want to contribute to.

    ```
    git remote add upstream original-repository-url
    ```

    - You can use the following to view the remote repositories:

    ```
    git remote -v
    ```

    - `upstream`, which refers to the original repository  
    - `origin`, which refers to your personal fork  

4. Develop your contribution:
    - Create a new branch named appropriately for the feature you want to work on:

    ```
    git checkout -b new-branch-name
    ```

    - Often, updates to an `upstream` repository will occur while you are developing changes on your personal fork. You can pull the latest changes from `upstream`

    ```
    git pull upstream dev
    ```

    - You can check the status of your local copy of the repository to see what changes have been made using:

    ```
    git status
    ```

    - Commit locally as you progress using `git add` and `git commit`. For example, updating a readme.md file:

    ```
    git add readme.md
    git commit -m "updated readme file"
    ```

    - You can check the status of your local copy of the repository again to see what pending changes have not been added or committed using:

    ```
    git status
    ```

    - After making some changes, push your changes back to your fork on GitHub:

    ```git
    git push origin branch-name
    ```

    - Enter username and password, depending on your settings, you may need to use a [Personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

5. To submit your contribution, navigate to your forked repository GitHub page and make a pull request using the `Compare &pull request` green button. Make sure to select the `base repository` and its `dev` branch. Also select your forked repository as `head repository` and make sure `compare` shows your branch name. You can add your comments and press `Create pull request` green button. Our team will be notified and will review your suggested revisions.

    - **Please submit a pull request early in the development phase, outlining the changes you intend to make or features you intend to add. This allows us to offer feedback early on, ensuring your contribution can be added to the repository before you invest a significant amount of time.**

## Adding New Notebooks or Example Workflows

In the spirit of open science, we want to minimize barriers to sharing code and examples. We have added `user_contributed` directories to our repositories for users to share examples of their work in notebook or code form. Documentation and descriptions do not need to be as thorough as the examples we've created, but we ask that you provide as much as possible. Follow the [instructions](#updating-code-documentation-notebooks-or-other-files) above, placing your new notebook or module in a suitably named directory within the `user_contributed` directory. Be sure to remove any large datasets and indicate where users can retrieve them.

## Attribution

These contributing guidelines are adapted from the NASA Transform to Open Science GitHub, available at <https://github.com/nasa/Transform-to-Open-Science/blob/main/CONTRIBUTING.md>.
