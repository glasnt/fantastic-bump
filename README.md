A test of the release system. 

Setup: 
 
 * Install versioneer into the repo
 * Install git-version-bump
 * Install github-release
 * Add workflows/python-publish.yml

Release process, e.g. for a patch:

 * `git version-bump patch`
 * `git release`

What should happen: 

 * git-version-bump handles updating the git tag and semver
 * versioneer listens to tags
 * github-release pushes the tag to GitHub as a release
 * the workflow publishes the package to pypi

TODO: 

 * confirm github actions environment knows what tags are.
