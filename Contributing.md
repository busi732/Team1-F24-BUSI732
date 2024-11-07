# Project Contribution Guide

This guide provides a detailed overview of the branching and naming conventions, contributing workflow, and review process for this project. Please follow these guidelines to ensure consistency and collaboration efficiency.

## Table of Contents
1. [Branching Convention](#branching-convention)
2. [Naming Convention](#naming-convention)
3. [Contributing Workflow](#scontributing-workflow)
4. [Additional Resources](#additional-resources)
---

## Branching Convention

1. **Main Branches**
   - Main: This branch contains stable, production-ready code. All changes should ultimately be merged into this branch. Every commit on `main` should represt a complete, stable version.

2. **Supporting Branches**
   - Feature Branches (`feature/*`): Created for developing new features.
   - Bug Fix Branches (`bug/*`): Created for fixing bugs in the code.
   - Hotfix Branches (`hotfix/*`): Created for urgent fixes that need immediate deployment.

## Naming Convention

Each branch name should follow a standardized format to clearly indicate its purpose. The general format is:

1. **General Format**

   `<type>/<description>`
      - Type: A prefix to specify the branch type (e.g., `feature`, `bug`, `hotfix`).
      - Description: A short, descriptive name for the work being done, using hyphens instead of spaces.

2. **Examples**
   - `feature/eda`
   - `bug/fix-model-setup`
   - `hotfix/correct-envir`

## Contributing Workflow

Follow these steps to contribute to the project effectively:

1. **Step 1: Update Local Main Branch**
   - After you clone the repo for the first time, keep updating the local main branch before starting work.
      ```bash
      git checkout main
      git pull origin main
      ```

2. **Step 2: Create New Branch or Update Your Branch**
   - Create a new branch based on the naming convention:
      ```bash
      git checkout -b <branch-name>
      ```
      Replace `<branch-name>` with a descriptive branch name following the conventions, e.g., `feature/eda`, `bug/fix-model-setup`.
   - If working on an existing branch, make sure to pull the latest changes from the main branch into your branch:
      ```bash
      git checkout <branch-name>
      git pull origin main
      ```

3. **Step 3: Making Changes and Committing**
   - Make your changes in the new branch.
   - Add files to the staging area:
      ```bash
      git add <file-name>
      ```
      > **Note**: Using `git add .` to add all modified files.
   - Commit your changes with a descriptive message:
      ```bash
      git commit -m "Descriptive message about the changes"
      ```

4. **Step 4: Pushing the Branch and Creating a Pull Request (PR)**
   - Push your branch to the remote repository:
      ```bash
      git push origin <branch-name>
      ```
   - Go to GitHub and create a Pull Request
      - Click on Compare & pull request.
      - Add a detailed description of the changes made in the PR.

5. **Step 5: Review Process**
   - The review process ensures that all changes are thoroughly reviewed and discussed before merging
   - Code Review: Other contributors or maintainers will review your PR. Be prepared to receive feedback or suggestions.
      - Take turns; each turn has 2 reviewers.
   - Address Feedback: Make any necessary adjustments based on feedback by committing changes to the same branch.
   - Approval and Merge: Once approved, the PR will be merged into the main branch by a reviewer.

6. **Step 6: Deleting the Branch**
   - After your PR is merged, delete the branch locally
   ```bash
   git branch -d <branch-name>
   ```
   - Delete the branch on GitHub
   ```bash
   git push origin --delete <branch-name>
   ```

## Additional Resources

This are also in Lecture 2 Materials.

   - [Git Flow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
   - [Using Git Branches](https://www.atlassian.com/git/tutorials/using-branches)
   - [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)

