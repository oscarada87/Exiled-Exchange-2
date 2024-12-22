# DataStore

Current process to run stuff:

1. Run `parserRunner.py`
2. Run `npm run copy-py-ndjson`
3. Run `add-to-new.py` (pseudo mods)
4. Copy data from `updated_stats.ndjson` to `stats.ndjson` if it worked correctly
5. Run `npm run temp-images`
6. Delete `updated_stats.ndjson` from folders
7. Run `npm run push-ndjson`
8. In `renderer` run `npm run make-index-files`