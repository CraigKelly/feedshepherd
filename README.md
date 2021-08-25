# feedshepherd

Help for aggregating and annotating RSS feeds

## Hacking

Deps and all managed with poetry

## Testing

* Run `poetry run devtest` on your own
* Run `poetry run ci` for CI
* Currently `poetry run test` is an alias for `devtest`

## Sample Files

To gather sample files, you can use `poetry run samples`.

All files will be placed in the `./samples` dir. The feeds are sourced from
`DoggCatcherExport.opml` in that directory. No old files are deleted.
