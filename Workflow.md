# Workflow

The best way to contribute to this project is with a pull request (PR).
You need to fork the main repository on GitHub and clone it to your local system.
Then you edit on a branch that you create locally. It is best practice to edit
your own branch, as opposed to the main branch. These are the steps to do it:

- You need to have git [installed](<https://docs.github.com/en/get-started/quickstart/set-up-git>)
on your system and an account on github.com.

- Fork the project repository to create a copy on your own GitHub account. For this you need to go to the original project <https://github.com/natnew/Awesome-Prompt-Engineering> and click on the “fork” button.

- Open a new terminal and clone your fork. With this step, you will have a copy of the repository on your system:

  ```text
  git clone https://github.com/YourAccount/Awesome-Prompt-Engineering.git
  ```

- The last step should have created a subdirectory “Awesome-Prompt-Engineering”.
Create an `upstream` remote alias in order for you to have the latest version of the project:

  ```text
  git remote add upstream  https://github.com/natnew/Awesome-Prompt-Engineering.git
  ```

- Check your `upstream` and `origin` remote aliases with the command `git remote -v`. You should have:

  ```text
  origin   https://github.com/YourAccount/Awesome-Prompt-Engineering.git (fetch)
  origin   https://github.com/YourAccount/Awesome-Prompt-Engineering.git (push)
  upstream https://github.com/natnew/Awesome-Prompt-Engineering.git (fetch)
  upstream https://github.com/natnew/Awesome-Prompt-Engineering.git (push)
  ```

- In order to synchronize your `main` branch with the `upstream/main` branch:

  ```text
  git checkout main
  git fetch upstream
  git merge upstream/main
  ```

- Now you are ready to create and checkout a new branch were you can work with this command:

  ```text
  git checkout -b my_awsomebranch
  ```

- You edit the files as you need, and when you are ready, add the changed files, commit and push to your fork on GitHub. You should synchronize with the main project in order to have the latest changes and resolve conflicts if necessary:

  ```text
  git add modified_files
  git commit -m “add a message to your commit here”
  git fetch upstream
  git merge upstream/main
  git push origin my_awsomebranch
  ```

- Create a pull request from your fork on GitHub. If you need help with this, please see [here.](<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork>)
