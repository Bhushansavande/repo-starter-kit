# Repo Starter Kit

A GitHub **template repository** with everything a small open-source project needs on day one, learned while shipping [File Rescue](https://github.com/Bhushansavande/file-rescue): working tests, CI on several Python versions, one-tag releases, a GitHub Pages site, Dependabot, issue and pull request templates, and a security policy. Python is used for the example, but every other file works for any language.

## Use it

1. Click **Use this template** > *Create a new repository*.
2. Replace `your-project` / `your_project` / `OWNER/REPO` (search the repository for them) and rewrite this README.
3. Edit the code in `src/` and the tests in `tests/`. CI runs on every push.
4. **Website:** Settings > Pages > Source: *GitHub Actions*, then re-run the *Website* workflow once.
5. **Release:** `git tag v0.1.0 && git push origin v0.1.0` builds the package and publishes a release with notes.

## What is included

| File | Purpose |
|---|---|
| `.github/workflows/ci.yml` | Tests on Python 3.10, 3.12 and 3.13 for every push and pull request |
| `.github/workflows/release.yml` | Tag -> build -> GitHub release with generated notes |
| `.github/workflows/pages.yml` | Publishes `docs/` as a website |
| `.github/dependabot.yml` | Monthly updates for actions and pip packages |
| `.github/ISSUE_TEMPLATE/`, `pull_request_template.md` | Better bug reports and pull requests |
| `SECURITY.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE` | The files visitors look for (MIT, change the name) |

## Lessons baked in

- Pin to current action versions and let Dependabot move them; the `ubuntu-latest` image changes, so old Python versions can disappear (this template tests 3.10+).
- Give every repository a one-line description and topics (the gear next to *About*), and tick *Use your GitHub Pages website*; those matter more for discovery than the README.
- Never put real user data in issues or tests. Use synthetic fixtures.
- Keep commit history readable and honest; document known limits in the README rather than hiding them.

## License

MIT
