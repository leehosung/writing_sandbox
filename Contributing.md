#Contributing to Writing sandbox

## Found an Issue?

If you find a bug in the source code or a mistake in the documentation, you can help us improve by submitting an issue to our
[GitHub Repository](https://github.com/leehosung/writing_sandbox/issues/new). Even better you can submit a
**Pull Request** with a fix. Your custom changes can be crafted in a repository fork and submitted
to the [GitHub Repository](https://github.com/leehosung/writing_sandbox/compare)

## Want a Feature?

You can request a new feature by
[submitting an issue](https://github.com/leehosung/writing_sandbox/issues/new)). If you would like to
implement a new feature then consider what kind of change it is:

* **Major Changes** that you wish to contribute to the project should be discussed first on our [Chatiing rooms](https://gitter.im/leehosung/writing_sandbox), so that we can better coordinate our efforts, prevent duplication of work, and help you to craft the change so that it is successfully accepted into the project.
* **Small Changes** can be crafted and submitted to the [GitHub Repository](https://github.com/leehosung/writing_sandbox/compare) as a Pull Request.

## Coding Rules

To ensure consistency throughout the source code, keep these rules in mind as you are working:

* All features or bug fixes must be tested by one more functional or unit tests.
* We follow [PEP8](https://www.python.org/dev/peps/pep-0008/)

## Required libraries and tools

* python3
* pyflake8
* git-flow

## Install and run the test server

1. [Fork](http://help.github.com/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

    ```bash
    git clone https://github.com/leehosung/writing_sandbox.git
    cd writing_sandbox
    ```

2. I recommend using a Python virtualenv to isolate your environment. To set up a new virtualenv, do:

    ```bash
    mkdir ~/.pyvnev
    pyvenv ~/.pyvenv/writing-sandbox
    source ~/.pyvenv/writing-sandbox/bin/activate
    ```

3. Install dependency using requirements.txt

    ```bash
    pip install -r requirements.txt
    ```

4. Set up database and insert sample data. run the server.
    
    ```bash
    python manage.py migrate
    python manage.py loaddata quiz/fixtures/test.json
    python manage.py runserver
    ```

## Branching

The Writing sandbox project uses the [gitflow](http://nvie.com/posts/a-successful-git-branching-model) model for branching.

1. Configure the remotes

    ```bash
    git remote add upstream https://github.com/leehosung/writing_sandbox.git
    ```

2. Create a new feature branch (off the main project development branch) to
   contain your feature, change, or fix:

   ```bash
   git checkout -b feature/<feature-name>
   ```

3. Commit your changes in logical chunks. Please adhere to these [git commit
   message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   or your code is unlikely be merged into the main project. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.

4. Locally merge (or rebase) the upstream development branch into your feature branch:

   ```bash
   git pull [--rebase] upstream development
   ```

5. Push your feature branch up to your fork:

   ```bash
   git push origin feature/<feature-name>
   ```

6. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description against the `develop` branch.

### Checking coding style

Run `flake8 --exclude=migrations .` before committing to ensure your changes follow our coding standards.
