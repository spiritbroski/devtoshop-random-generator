# RANDOM DEV.TO SHOP ITEM GENERATOR

### this action get you a random item that you can buy on a budget from dev.to shop

### You can see the explanation here

https://dev.to/spiritbro1/pick-random-item-from-dev-to-shop-based-on-how-much-money-you-got-29a

## Required argument

- ```budget``` your budget in us dollar
- ```personal_token``` to create a branch and pull request
- ```github_repo``` your repo name 

## Example Yaml

```yaml
# This is a basic workflow to help you get started with Actions

name: Get Random Item from dev.to

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the master branch
on:
  push:
    branches: [ master ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - name: generate and pull request
        uses: spiritbro1/devtoshop-random-generator@v7
        with:
          budget: 50
          personal_token: ${{ secrets.PERSONAL_TOKEN }}
          github_repo: ${{ secrets.GH_REPO }} 


```


