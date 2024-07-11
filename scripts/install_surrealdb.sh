if [[ ! -d $(pwd)/.surrealdb ]]; then
  curl -sSf https://install.surrealdb.com | sh &&
    mkdir $(pwd)/.surrealdb &&
    mv $HOME/.surrealdb/surreal $(pwd)/.surrealdb/surreal &&
    rm -rf $HOME/.surrealdb
    
  echo "SurrealDB installed successfully"
fi

export PATH=$(pwd)/.surrealdb/:$PATH
