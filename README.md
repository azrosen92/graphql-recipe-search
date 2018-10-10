# GraphQL Recipe Search API

## Getting started
1. Install dependencies `pip install -r requirements.txt`
1. Run seed script to get some sample data `python seed.py`
1. Run Server `python app.py`
1. Visit `localhost:7000/graphql`

Try a query like
```gql
query {
  recipeSearchResults(searchTerm: "oil", ingredients: [44]) {
    results {
      id
      name
      ingredients {
        id
        name
        amount
      }
    }
  }
}
```

## How graphql works
https://graphql.org/learn/
