import ApolloClient from "apollo-boost";
import { ApolloProvider, Query } from "react-apollo";
import gql from "graphql-tag";
import React, { Component } from "react";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      searchTerm: ""
    };
  }

  render() {
    const query = gql`
      query RecipeSearchResults($searchTerm: String, $ingredients: [Int]) {
        recipeSearchResults(
          searchTerm: $searchTerm
          ingredients: $ingredients
        ) {
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
    `;

    const client = new ApolloClient({
      uri: "http://127.0.0.1:5000/graphql"
    });

    const ingredients = [];

    const { searchTerm } = this.state;

    return (
      <ApolloProvider client={client}>
        <header className="App-header" />
        <input
          onChange={evt => this.setState({ searchTerm: evt.target.value })}
        />
        <Query query={query} variables={{ searchTerm, ingredients }}>
          {({ loading, error, data }) => {
            if (loading) return <p>Loading...</p>;
            if (error) return <p>Error :(</p>;

            return data.recipeSearchResults.results.map(
              ({ name, ingredients }) => {
                return (
                  <div key={name}>
                    {name}
                    <div>
                      <ul>
                        {ingredients.map(({ name, amount }) => {
                          return <li key={name}>{`${amount} of ${name}`}</li>;
                        })}
                      </ul>
                    </div>
                  </div>
                );
              }
            );
          }}
        </Query>
      </ApolloProvider>
    );
  }
}

export default App;
