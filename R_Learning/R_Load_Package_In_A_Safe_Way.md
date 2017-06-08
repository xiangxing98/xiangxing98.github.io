# Load package in a safe way

## Load data.table package

```
# Load data.table package
if(!suppressWarnings(require(data.table)))
{
    install.packages('data.table')
    require(data.table)
}
```