# Novel Fetcher

A simple collection (a single script for now) of scripts to download novel chapters from various sites.

Currently supported sites:

- bronovel.com (formerly boxnovel.com)

## Example Usage

Download all chapters of "Legendary Mechanic" from `bronovel.com`:

```shell
poetry run python3 bronovel.com -n the-legendary-mechanic-boxnovel -f 1 -l 1462 -e 1463-end
```