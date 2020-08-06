# magicnumber

## Running with Docker

Build the image.

```bash
docker build -t yoshiodeveloper/magicnumber .
```

Now you can run it passing the array:

```bash
docker run -t --rm yoshiodeveloper/magicnumber -s "[[1,3], [50, 10982]]"
```

A file:

```bash
docker run -t --rm yoshiodeveloper/magicnumber -f dataset.json
```

Or using stdin:

```bash
cat dataset.json | docker run -i --rm yoshiodeveloper/magicnumber
```


## Project directories

**/bin**: Scripts/programs to be executed on shell.

**/datasets**: Datasets file used on tests.
 
**/magicnumber**: The module/source of application.
 
**/tests**: Pytest test scripts.
 