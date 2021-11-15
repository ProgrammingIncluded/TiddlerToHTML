# DEPRECATED PROJECT

This project has now been deprecated in favor of actual `export Tiddler` > `static HTML` functionality.
The scripts have been outdated and has been a while since I last used them, please use with caution.

# Tiddler to HTML
Python to converts eachtiddler files (.tid) in a folder into
the corresponding HTML file in another folder.

## Usage

```
python tparse <foldername> <outputfolder>
```

## Remarks
Currently the project does not have very thorough error
message or prevention. Works well if you verify .tid thru
tiddly wiki interface first.

The project was designed for easy, quick, and dirty solution
for an internal project. Mass majority .tid files are markdown.
So you can use pre-existing markdown converters if you require
a more thorough and error proof solution.

The metadata on each .tid file is appended at the beginning
of each HTML file. You can use it to parse metadata or
remove them entirely.
